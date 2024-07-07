import socket
import numpy as np
from PIL import Image, ImageTk
import io
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import traceback
# from blurwindow import GlobalBlur

import time
COMMAND_DELIMITER = ";;"  # Define a command delimiter

class RemoteDesktopClient:
    def __init__(self, master):
        self.master = master
        master.title("Remote Desktop Client")
        # master.geometry("1024x768")  # Set initial size 

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', background='#2a2a2a', foreground='white')
        self.style.configure('TCheckbutton', background='#1e1e1e', foreground='white')
        self.style.configure('TEntry', fieldbackground='#2a2a2a', foreground='white')
        self.style.configure('TScale', background='#1e1e1e', troughcolor='#2a2a2a')

        self.frame = ttk.Frame(master, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        control_frame = ttk.Frame(self.frame)
        control_frame.pack(fill=tk.X, pady=10)

        self.ip_entry = ttk.Entry(control_frame, width=20)
        self.ip_entry.pack(side=tk.LEFT, padx=5)
        self.ip_entry.insert(0, "Enter host IP")

        self.connect_button = ttk.Button(control_frame, text="Connect", command=self.connect)
        self.connect_button.pack(side=tk.LEFT, padx=5)

        self.disconnect_button = ttk.Button(control_frame, text="Disconnect", command=self.disconnect, state=tk.DISABLED)
        self.disconnect_button.pack(side=tk.LEFT, padx=5)

        self.control_var = tk.BooleanVar()
        self.control_checkbox = ttk.Checkbutton(control_frame, text="Enable Control", variable=self.control_var, command=self.toggle_control)
        self.control_checkbox.pack(side=tk.LEFT, padx=5)

        self.overwrite_var = tk.BooleanVar()
        self.overwrite_checkbox = ttk.Checkbutton(control_frame, text="Enable Overwrite", variable=self.overwrite_var, command=self.toggle_overwrite)
        self.overwrite_checkbox.pack(side=tk.LEFT, padx=5)

        self.scale_var = tk.DoubleVar(value=1.0)
        self.scale_slider = ttk.Scale(control_frame, from_=0.1, to=2.0, orient=tk.HORIZONTAL, variable=self.scale_var, command=self.update_scale)
        self.scale_slider.pack(side=tk.LEFT, padx=5)

        self.scale_label = ttk.Label(control_frame, text="Scale: 1.0x")
        self.scale_label.pack(side=tk.LEFT, padx=5)

        self.socket = None
        self.connected = False
        self.host_screen_size = (0, 0)
        self.scale_factor = 1.0
        self.current_image = None

        self.master.bind("<Configure>", self.on_resize)
        self.last_mouse_position = (0, 0)
        self.mouse_update_interval = 0.05  # 50ms
        self.last_mouse_update_time = 0

    def connect(self):
        host = self.ip_entry.get()
        port = 12345

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((host, port))
            response = self.socket.recv(1024).decode()
            if response == "Request accepted":
                self.connected = True
                self.connect_button.config(state=tk.DISABLED)
                self.disconnect_button.config(state=tk.NORMAL)
                
                size_data = self.socket.recv(1024).decode().split(',')
                self.host_screen_size = (int(size_data[0]), int(size_data[1]))
                self.update_scale()
                
                threading.Thread(target=self.receive_screen, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))

    def disconnect(self):
        if self.connected:
            try:
                self.socket.send(b"DISCONNECT")
                self.socket.close()
            except:
                pass
            finally:
                self.connected = False
                self.connect_button.config(state=tk.NORMAL)
                self.disconnect_button.config(state=tk.DISABLED)

    def toggle_control(self):
        if self.connected:
            if self.control_var.get():
                self.socket.send(b"ENABLE_CONTROL")
            else:
                self.socket.send(b"DISABLE_CONTROL")

    def toggle_overwrite(self):
        if self.connected:
            if self.overwrite_var.get():
                self.socket.send(b"ENABLE_OVERWRITE")
            else:
                self.socket.send(b"DISABLE_OVERWRITE")

    def update_scale(self, *args):
        self.scale_factor = self.scale_var.get()
        self.scale_label.config(text=f"Scale: {self.scale_factor:.1f}x")
        self.resize_image()

    def resize_image(self):
        if self.current_image:
            scaled_size = (int(self.host_screen_size[0] * self.scale_factor),
                           int(self.host_screen_size[1] * self.scale_factor))
            resized_image = self.current_image.resize(scaled_size, Image.LANCZOS)
            self.display_image(resized_image)

    def on_resize(self, event=None): 
        if self.current_image:
            self.resize_image()
            self.master.geometry("")  # Auto-resize window

  

    def receive_screen(self):
        while self.connected:
            try:
                is_full_image = self.socket.recv(1) == b'1'
                size = int.from_bytes(self.socket.recv(4), byteorder='big')
                img_data = b''
                while len(img_data) < size:
                    chunk = self.socket.recv(size - len(img_data))
                    if not chunk:
                        raise RuntimeError("socket connection broken")
                    img_data += chunk
                image = Image.open(io.BytesIO(img_data))
                
                self.current_image = image
                self.resize_image()
            except Exception as e:
                print(f"Error receiving screen: {e}")
                traceback.print_exc()
                self.disconnect()
                break

    def display_image(self, image):
        photo = ImageTk.PhotoImage(image)
        self.canvas.delete("all")
        self.canvas.config(width=image.width, height=image.height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def send_mouse_event(self, event):
        if self.connected and self.control_var.get():
            current_time = time.time()
            if current_time - self.last_mouse_update_time >= self.mouse_update_interval:
                x = int(event.x / self.scale_factor)
                y = int(event.y / self.scale_factor)
                self.socket.send(f"MOUSE,{x},{y}{COMMAND_DELIMITER}".encode()) # Add delimiter
                self.last_mouse_update_time = current_time
                self.last_mouse_position = (x, y)

    def send_click_event(self, event):
        if self.connected and self.control_var.get():
            x, y = self.last_mouse_position
            button = "left"
            if event.num == 2:
                button = "middle"
            elif event.num == 3:
                button = "right"
            self.socket.send(f"CLICK,{button},down,{x},{y}{COMMAND_DELIMITER}".encode()) # Add delimiter

    def send_release_event(self, event):
        if self.connected and self.control_var.get():
            x, y = self.last_mouse_position
            button = "left"
            if event.num == 2:
                button = "middle"
            elif event.num == 3:
                button = "right"
            self.socket.send(f"CLICK,{button},up,{x},{y}{COMMAND_DELIMITER}".encode()) # Add delimiter

    def send_key_event(self, event):
        if self.connected and self.control_var.get():
            key = event.char
            if not key:
                key = event.keysym  
            print(f"Sending key: {key}")
            self.socket.send(f"KEY,{key}{COMMAND_DELIMITER}".encode())  # Add delimiter

def main():
    root = tk.Tk()
    client = RemoteDesktopClient(root)
    root.bind("<Motion>", client.send_mouse_event)
    root.bind("<Button-1>", client.send_click_event)
    root.bind("<Button-2>", client.send_click_event)
    root.bind("<Button-3>", client.send_click_event)
    root.bind("<ButtonRelease-1>", client.send_release_event)
    root.bind("<ButtonRelease-2>", client.send_release_event)
    root.bind("<ButtonRelease-3>", client.send_release_event)
    root.bind("<Key>", client.send_key_event)
    root.mainloop()

if __name__ == "__main__":
    main()