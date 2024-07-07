import socket
import pyautogui
import numpy as np
import cv2
import sys
import threading

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


running_ss = True
def send_img(client_socket):
    try:
        while True:
            img = pyautogui.screenshot()
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            img_data = cv2.imencode('.jpg', img)[1].tobytes()
            length = len(img_data).to_bytes(4, byteorder='big')
            client_socket.sendall(length)
            client_socket.sendall(img_data)
    except ConnectionResetError as e:
        print(f'Error at send image:', e)
    finally:
        client_socket.close()
        
        
        
def receive_kbd(server_socket_kbd):
    while True:
        client_socket, addr = server_socket_kbd.accept()
        print('Got connection from', addr)
        threading.Thread(target=receive_kbd_events, args=(client_socket,)).start()

def receive_kbd_events(client_socket):
    try:
        while True:
            kbd_event = client_socket.recv(1024).decode()
            
            if ':' in kbd_event:
                event_type, key = kbd_event.split(':')
                print(f'Received keyboard event: {event_type}, Key: {key}')
                if event_type == 'keyDOWN':
                    # Simulate pressing the key
                    pyautogui.keyDown(key)
                elif event_type == 'keyUP':
                    # Simulate releasing the key
                    pyautogui.keyUp(key)
            else:
                print(f'Invalid keyboard event: {kbd_event}')
    except Exception as e:
        print(f'Error at receive keyboard events:', e)



def receive_events(client_socket_mouse):
    """emphasis on mouse receive events as keyboard has a separate handler"""
    try:
        while True:
            event_type = int.from_bytes(client_socket_mouse.recv(4), byteorder='big')
            print(f'event_type: %s' % event_type)
            if event_type == 0:  # Mouse press event
                data = b''
                while len(data) < 12:
                    data += client_socket_mouse.recv(12 - len(data))
                x, y, button = (
                    int.from_bytes(data[:4], byteorder='big'),
                    int.from_bytes(data[4:8], byteorder='big'),
                    int.from_bytes(data[8:], byteorder='big')
                )
                if button == 0:
                    pyautogui.mouseDown(x, y, button='left')
                elif button == 1:
                    pyautogui.mouseDown(x, y, button='right')
                elif button == 2:
                    pyautogui.mouseDown(x, y, button='middle')
            elif event_type == 1:  # Mouse release event
                data = b''
                while len(data) < 12:
                    data += client_socket_mouse.recv(12 - len(data))
                x, y, button = (
                    int.from_bytes(data[:4], byteorder='big'),
                    int.from_bytes(data[4:8], byteorder='big'),
                    int.from_bytes(data[8:], byteorder='big')
                )
                if button == 0:
                    pyautogui.mouseUp(x, y, button='left')
                elif button == 1:
                    pyautogui.mouseUp(x, y, button='right')
                elif button == 2:
                    pyautogui.mouseUp(x, y, button='middle')
            elif event_type == 2:  # Mouse move event
                data = b''
                while len(data) < 8:
                    data += client_socket_mouse.recv(8 - len(data))
                x, y = (
                    int.from_bytes(data[:4], byteorder='big'),
                    int.from_bytes(data[4:], byteorder='big')
                )
                pyautogui.moveTo(x, y)
            elif event_type == 3:  # Scroll up event
                pyautogui.scroll(1)
            elif event_type == 4:  # Scroll down event
                pyautogui.scroll(-1)
    except Exception as e:
        print(f'Error at receive events:', e)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5000))
server_socket.listen()

server_socket_cntrls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket_cntrls.bind(('0.0.0.0', 5001))
server_socket_cntrls.listen()

client_socket_mouse = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket_mouse.bind(('0.0.0.0', 5002))
client_socket_mouse.listen()

threading.Thread(target=receive_kbd, args=(server_socket_cntrls,)).start()

while True:
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)
    threading.Thread(target=send_img, args=(client_socket,)).start()
    threading.Thread(target=receive_events, args=(client_socket_mouse,)).start()

