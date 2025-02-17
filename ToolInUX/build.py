import os
import sys
from Crypto.Cipher import AES
import time
# import pyinstaller
# run in the server directory. cd server.


# Define the file to be encrypted
file_to_encrypt = 'UTXTool.py'

# Generate a 256-bit AES key
key = os.urandom(32)
print(repr(key))





# Get the path of the Python executable
python_path = f'"{sys.executable}"'

# Build the PyInstaller command to encrypt the file 

# encryption is off at the moment

# for some reason encrypting cdwn.py doesn't work properly, --key {key} & "--hidden-import Crypto.Cipher.AES" is removed, for rb you can keep it - i think.
pyinstaller_cmd = f'pyinstaller --onefile --console --noconfirm --icon "C:/Users/thesh/Documents/Main/Development/VAry/server/application icon.ico" --add-data "webpageDesign.html;templates" --add-data "webpageDesign.html;webpageDesign.html" --add-data "dvrfy.exe;dvrfy.exe" --hidden-import gevent --hidden-import gevent-websocket --hidden-import engineio.async_geevent {file_to_encrypt}'# change from console to windowed, console = with a console, windowed = hidden
# Encrypt the file by running the PyInstaller command

#prompt to copy dvrfy from the dist to here.
auto_copy = False # idk why not working
if not auto_copy:
    tocopy = 'n'
    # tocopy = input('Do you want to copy dvrfy.exe to here?(y/n)')
if auto_copy or tocopy == 'y':
        os.system(rf'robocopy "C:\Users\thesh\Documents\Main\Development\VAry\dist\" "C:\Users\thesh\Documents\Main\Development\VAry\ToolInUX\" "dvrfy.exe" /Z'.replace('\\', '\\\\'))

starting_time = time.time()
os.system(pyinstaller_cmd)
print(f'Build time took: {time.time()-starting_time} seconds.')


if (time.time()-starting_time) < 30:
    os.system('msg * wrong dir, rebuilding in a diff cmd, pay attention')
    os.system(r'C:\Users\thesh\Documents\Main\Development\VAry\wrongdirstartbuild.bat')
    os.system('pause')
    
    
# i think it was panicking becasue if the build is already done/same it'll just not build again and skip as it's already build