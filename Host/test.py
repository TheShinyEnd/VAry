import win32gui
import win32con
import win32process
import win32com.client
import psutil
import time

def force_show_hidden_windows(name):  # e.g. chrome.exe
    def enum_windows_callback(hwnd, result):
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        try:
            process = psutil.Process(pid)
            if process.name().lower() == name.lower():
                # Include the window even if it's not currently visible
                title = win32gui.GetWindowText(hwnd)
                if title:  # Only include windows with a title
                    result.append((hwnd, title))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        return True

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
            
            # Force the taskbar button to flash
            win32gui.FlashWindow(hwnd, True)
            
            # Use the shell to force the window to the foreground
            shell.MinimizeAll()
            time.sleep(0.5)  # Give some time for minimization
            win32gui.SetForegroundWindow(hwnd)
            
            print(f"Successfully showed window: '{title}' (handle: {hwnd})")
        except Exception as e:
            print(f"Error showing window '{title}' (handle: {hwnd}): {str(e)}")

    print("Finished attempting to show hidden windows.")

# Usage
force_show_hidden_windows("notepad.exe")  # Replace with your process name