import socket
import pyautogui
import numpy as np
import cv2
import struct
import threading

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

def send_img(client_socket):
    while True:
        img = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        img_data = cv2.imencode('.jpg', img)[1].tobytes()
        length = struct.pack('!I', len(img_data))
        client_socket.sendall(length)
        client_socket.sendall(img_data)

def receive_events(client_socket):
    while True:
        event_type = struct.unpack("!I", client_socket.recv(4))[0]
        print(f'event_type: %s' % event_type)
        if event_type == 0: # Mouse press event
            data = b''
            while len(data) < 12:
                data += client_socket.recv(12 - len(data))
            x, y, button = struct.unpack("!III", data)
            if button == 0:
                pyautogui.mouseDown(x, y, button='left')
            elif button == 1:
                pyautogui.mouseDown(x, y, button='right')
            elif button == 2:
                pyautogui.mouseDown(x, y, button='middle')
        elif event_type == 1: # Mouse release event
            data = b''
            while len(data) < 12:
                data += client_socket.recv(12 - len(data))
            x, y, button = struct.unpack("!III", data)
            if button == 0:
                pyautogui.mouseUp(x, y, button='left')
            elif button == 1:
                pyautogui.mouseUp(x, y, button='right')
            elif button == 2:
                pyautogui.mouseUp(x, y, button='middle')
        elif event_type == 2: # Mouse move event
            data = b''
            while len(data) < 8:
                data += client_socket.recv(8 - len(data))
            x, y = struct.unpack("!II", data)
            pyautogui.moveTo(x, y)
        elif event_type == 3: # Scroll up event
            pyautogui.scroll(1)
        elif event_type == 4: # Scroll down event
            pyautogui.scroll(-1)
        elif event_type == 5: # Key press event
            key = struct.unpack("!I", client_socket.recv(4))[0]
            pyautogui.keyDown(chr(key))
            print('pressing key %s' % chr(key))
        elif event_type == 6: # Key release event
            key = struct.unpack("!I", client_socket.recv(4))[0]
            pyautogui.keyUp(chr(key))



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5000))
server_socket.listen()

while True:
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)
    threading.Thread(target=send_img, args=(client_socket,)).start()
    threading.Thread(target=receive_events, args=(client_socket,)).start()
