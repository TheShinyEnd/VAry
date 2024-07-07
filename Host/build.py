import os
import sys
from Crypto.Cipher import AES
import time
import gevent

# run in the server directory. cd server.


# Define the file to be encrypted
file_to_encrypt = 'dvrfy.py'

# Generate a 256-bit AES key
key = os.urandom(32)
print(repr(key))



# Get the path of the Python executable
python_path = f'"{sys.executable}"'

# Build the PyInstaller command to encrypt the file 

# encryption is off at the moment

# for some reason encrypting cdwn.py doesn't work properly, --key {key} & "--hidden-import Crypto.Cipher.AES" is removed, for rb you can keep it - i think.
pyinstaller_cmd = (
    f'pyinstaller --onefile --console --noconfirm --icon "C:/Users/thesh/Documents/Main/Development/VAry/Items/application icon.ico" '
    rf'--add-data "C:\Users\thesh\Documents\Main\Development\VAry\Host\templates\index.html;templates" '
    f'--hidden-import gevent '
    f'--hidden-import geventwebsocket '
    f'--hidden-import engineio.async_gevent '
    f'{file_to_encrypt}'
)
# change from console to windowed, console = with a console, windowed = hidden
# Encrypt the file by running the PyInstaller command
starting_time = time.time()

os.system(pyinstaller_cmd)
print(f'Build time took: {time.time()-starting_time} seconds.')