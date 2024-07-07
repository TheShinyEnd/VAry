# pyinstaller --onefile --console  --noconfirm C:\Users\thesh\Documents\Main\Development\VAry\Other\ss_hostv2.py 


import socket
import pyautogui
import numpy as np
from PIL import Image, ImageDraw
import io
import time
import cv2
import traceback
import select

pyautogui.FAILSAFE = False

COMMAND_DELIMITER = ";;"

def capture_screen():
    try:
        screenshot = pyautogui.screenshot()
        return np.array(screenshot)
    except Exception as e:
        return create_error_image(str(e))

def create_error_image(error_message):
    img = Image.new('RGB', (800, 600), color='black')
    d = ImageDraw.Draw(img)
    d.text((10, 10), f"Screen grab failed: {error_message}", fill=(255, 255, 255))
    return np.array(img)

def compare_images(img1, img2):
    diff = cv2.absdiff(img1, img2)
    return diff, np.any(diff != 0)

def send_screen_diff(conn, diff, full_image):
    try:
        img = Image.fromarray(diff)
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        is_full_image = b'1' if np.array_equal(diff, full_image) else b'0'
        conn.send(is_full_image)
        conn.send(len(img_byte_arr).to_bytes(4, byteorder='big'))
        conn.send(img_byte_arr)
    except Exception as e:
        print(f"Error sending screen diff: {e}")

def process_command(conn, command):
    print(f'Processing: {command}')
    global control_enabled, overwrite_enabled
    try:
        if command == "DISCONNECT":
            raise ConnectionResetError("Client disconnected")
        elif command == "ENABLE_CONTROL":
            control_enabled = True
            print("Control enabled")
        elif command == "DISABLE_CONTROL":
            control_enabled = False
            print("Control disabled")
        elif command == "ENABLE_OVERWRITE":
            overwrite_enabled = True
            print("Overwrite enabled")
        elif command == "DISABLE_OVERWRITE":
            overwrite_enabled = False
            print("Overwrite disabled")
        elif command.startswith("MOUSE"):
            if control_enabled and not (overwrite_enabled and pyautogui.onScreen(*pyautogui.position())):
                parts = command.split(',')
                if len(parts) == 3:
                    _, x, y = parts
                    pyautogui.moveTo(int(x), int(y))
        elif command.startswith("CLICK"):
            if control_enabled and not (overwrite_enabled and pyautogui.onScreen(*pyautogui.position())):
                parts = command.split(',')
                if len(parts) >= 3:
                    _, button, state = parts[:3]
                    if state == "down":
                        pyautogui.mouseDown(button=button)
                    elif state == "up":
                        pyautogui.mouseUp(button=button)
                    else:
                        pyautogui.click(button=button)
        elif command.startswith("KEY"):
            if control_enabled and not overwrite_enabled:
                parts = command.split(',')
                if len(parts) > 1: 
                    keys = parts[1:] 
                    for key in keys:
                        pyautogui.keyDown(key)
                    for key in keys:
                        pyautogui.keyUp(key)
                else:
                    print("No key provided with KEY command")
                    
        elif command == "Disable keyboard":
            # disable_keyboard()
            print(f"Keyboard disabled (not implemented)")
        elif command == "Disable mouse":
            # disable_mouse()
            print(f"Mouse disabled (not implemented)")
        elif command == "Enable keyboard":
            # enable_keyboard()
            print(f"Keyboard enabled (not implemented)")
        elif command == "Enable mouse":
            # enable_mouse()
            print(f"Mouse enabled (not implemented)")
        elif command == "PING":
            conn.send(b"PONG")
    except ConnectionResetError as e:
        print(f"Connection closed: {e}")
        raise  # Re-raise the exception to be caught in the main loop
    except Exception as e:
        print(f"Error processing command: {e}")

def main():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Listening on {host}:{port}")

    global control_enabled
    control_enabled = False
    global overwrite_enabled
    overwrite_enabled = False

    while True:
        try:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            conn.send(b"Request accepted")

            screen_size = pyautogui.size()
            conn.send(f"{screen_size.width},{screen_size.height}".encode())

            previous_screen = None

            while True:
                try:
                    ready_to_read, _, _ = select.select([conn], [], [], 0.05)
                    if ready_to_read:
                        data = conn.recv(1024).decode()
                        if not data:
                            raise ConnectionResetError("Client disconnected") 
                        commands = data.split(COMMAND_DELIMITER)
                        for command in commands:
                            if command: 
                                process_command(conn, command)

                    current_screen = capture_screen()
                    if previous_screen is None:
                        send_screen_diff(conn, current_screen, current_screen)
                    else:
                        diff, has_changes = compare_images(previous_screen, current_screen)
                        if has_changes:
                            send_screen_diff(conn, current_screen, current_screen)
                    
                    previous_screen = current_screen

                except ConnectionResetError as e:
                    print(f"Connection closed: {e}")
                    break
                except Exception as e:
                    print(f"Error in main loop: {e}")
                    traceback.print_exc()
                    if isinstance(e, socket.error):
                        break  # Exit the inner loop if there's a socket error

        except Exception as e:
            print(f"Error in connection handling: {e}")
            traceback.print_exc()

        finally:
            if 'conn' in locals():
                conn.close()

    server_socket.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Fatal error: {e}")
        traceback.print_exc()