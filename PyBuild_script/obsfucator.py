
# cheap ass obsfucator found online. no it does not do the job, and thus isn't being used anymore.


import zlib
import base64
import subprocess
import random
import os
import string
import logging
import sys
import time
import re
from cryptography.fernet import Fernet

# Constants and configurations
BUILD_PATH = r"C:\Users\thesh\Documents\Main\Development\VAry\Host\\"
TEMP_FILE_PATH = "C:\\Users\\thesh\\Documents\\Main\\Development\\VAry\\Host\\dvrfy.py"
ENCRYPTED_FILE_PATH = "C:\\Users\\thesh\\Documents\\Main\\Development\\VAry\\Host\\en_dvrfy.py"


# Configure logging
logging.basicConfig(level=logging.INFO)
def generate_random_string(length=19, chars=string.ascii_letters + string.digits):
    while True:
        result = ''.join(random.choice(chars) for _ in range(length))
        if result[0].isalpha():  # Ensure the first character is a letter
            return result

def generate_fake_code(num_vars=10, num_funcs=15, num_classes=10):
    fake_code = [f"{generate_random_string()} = {repr(random.randint(1000000, 100000000))}" for _ in range(num_vars)]

    def get_user_info():
        return {'username': generate_random_string(7), 'age': random.randint(18, 99)}

    def get_channel_name():
        return repr(generate_random_string())

    def get_repos():
        return [repr(generate_random_string()) for _ in range(random.randint(1, 5))]

    fake_functions = [get_user_info, get_channel_name, get_repos]

    fake_classes = [f"class {generate_random_string()}:\n    def __init__(self):\n        self.data = {repr(random.choice([True, False]))}\n    def get_data(self):\n        return self.data" for _ in range(num_classes)]

    all_code = fake_code + fake_functions + fake_classes
    all_code = [str(item()) if callable(item) else str(item) for item in all_code]
    random.shuffle(all_code)
    return "\n".join(all_code)

def encrypt_code(code, key):
    cipher_suite = Fernet(key)
    encrypted_code = cipher_suite.encrypt(zlib.compress(code.encode()))
    return base64.b64encode(encrypted_code).decode()

def get_pyinstaller_dependencies(script_path):
    try:
        result = subprocess.run(['pyinstaller', '--onefile', '--collect-all', script_path], capture_output=True, text=True, check=True)
        output = result.stdout
        dependencies = []
        for line in output.splitlines():
            match = re.search(r"found package (.*?) ", line)
            if match:
                dependencies.append(match.group(1))
        return dependencies
    except subprocess.CalledProcessError as e:
        logging.error(f"Error getting PyInstaller dependencies: {e}")
        return []

def obfuscate(input_file, output_file):
    key = Fernet.generate_key()

    with open(input_file, "r") as f:
        code = f.read()

    encoded_code = encrypt_code(code, key)
    dependencies = get_pyinstaller_dependencies(input_file)
    fake_code = generate_fake_code()
    decrypt_func_name = generate_random_string()
    exec_func_name = generate_random_string()

    obfuscated_code = f"""
import zlib, base64, subprocess, time
from sys import executable
from importlib import import_module
{fake_code}
{' '.join([f'import {dep}' for dep in dependencies])}
try: from cryptography.fernet import Fernet as {decrypt_func_name}
except: subprocess.run('python -m pip install cryptography', shell=True); from cryptography.fernet import Fernet as {decrypt_func_name}
{fake_code}
requirements = [["requests", "requests"], ["Cryptodome.Cipher", "pycryptodomex" if not 'PythonSoftwareFoundation' in executable else 'pycryptodome']]
for modl in requirements:
    try: import_module(modl[0])
    except: subprocess.Popen(executable + " -m pip install " + modl[1], shell=True); time.sleep(3)
{fake_code}
encoded_code = "{encoded_code}"
{exec_func_name} = exec
key = "{key.decode()}"
{fake_code}
decrypted_code = {decrypt_func_name}(key).decrypt(base64.b64decode(encoded_code))
decompressed_code = zlib.decompress(decrypted_code).decode()
{exec_func_name}(decompressed_code)
{fake_code}
    """

    with open(output_file, "w") as f:
        f.write(obfuscated_code)

if __name__ == "__main__":
    obfuscate(TEMP_FILE_PATH, ENCRYPTED_FILE_PATH)
    logging.info(f"Obfuscated script saved to: {ENCRYPTED_FILE_PATH}")
exit()
import argparse
import zlib
import base64
import subprocess
import random
import os
import string
import logging
import sys
import time
try:
    import cryptography
except: 
    subprocess.run(f'python -m pip install cryptography', shell=True, check=True)


from cryptography.fernet import Fernet

# Constants and configurations
BUILD_PATH = r"C:\Users\thesh\Documents\Main\Development\VAry\Host\\" # in this directory, the code to become obsfucated should be located
TEMP_FILE_PATH = "C:\\Users\\thesh\\Documents\\Main\\Development\\VAry\\Host\\dvrfy.py" 
ENCRYPTION_KEY_FILE = "encryption_key.txt" # unneeded

# Configure logging
logging.basicConfig(level=logging.INFO)


# Function Definitions
def generate_random_string(length=19, chars=string.ascii_letters + string.digits):
    """
    Generate a random string of given length.
    """
    return ''.join(random.choice(chars) for _ in range(length))

def generate_random_string(length=10):
    """
    Generate a random string of the given length with the first character as a letter.
    """
    first_char = random.choice(string.ascii_letters)
    rest_of_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=length - 1))
    return first_char + rest_of_chars

def generate_fake_code(num_vars=10, num_funcs=15, num_classes=10):
    """
    Generate fake variables, functions, and classes for obfuscation.
    """
    fake_code = [f"{generate_random_string()} = {repr(random.randint(1000000, 100000000))}" for _ in range(num_vars)]

    # List of real function names with meaningful implementations
    def get_user_info():
        return {'username': generate_random_string(7), 'age': random.randint(18, 99)}

    def get_channel_name():
        return repr(generate_random_string())

    def get_repos():
        return [repr(generate_random_string()) for _ in range(random.randint(1, 5))]

    fake_functions = [get_user_info, get_channel_name, get_repos]

    fake_classes = [f"class {generate_random_string()}:\n    def __init__(self):\n        self.data = {repr(random.choice([True, False]))}\n    def get_data(self):\n        return self.data" for _ in range(num_classes)]

    # Combine functions and classes into a single list
    all_code = fake_code + fake_functions + fake_classes
    
    # Convert functions to strings
    all_code = [str(item()) if callable(item) else str(item) for item in all_code]
    all_code = random.sample(all_code, len(all_code))
    return "\n".join(all_code)

def encrypt_code(code, key):
    """
    Encrypt and encode the code.
    """
    cipher_suite = Fernet(key)
    encrypted_code = cipher_suite.encrypt(zlib.compress(code))
    return base64.b64encode(encrypted_code).decode('utf-8')

def random_class_name():
    return ''.join(random.choice(string.ascii_letters) + random.choice(string.ascii_letters + string.digits) for _ in range(19))

def main():
    # parser = argparse.ArgumentParser(description='Obfuscate and create an executable.')
    # parser.add_argument('name', help='Name for the obfuscated file (Do not include the extension)')
    # args = parser.parse_args()

    # Key generation and encryption
    key = Fernet.generate_key()
    with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
        key_file.write(key)

    with open(TEMP_FILE_PATH, "rb") as code_file:
        code = code_file.read()

    encoded_code = encrypt_code(code, key)

    # Obfuscation
    all_fake_code = generate_fake_code()

    a = random_class_name()
    e = random_class_name()
    def generate_random_keys(num_keys):
        keys = [Fernet.generate_key() for _ in range(num_keys)]
        return keys
    
    key_list = []
    key_list.extend(generate_random_keys(random.randint(10,25)))
    keyssss = random.randint(0, len(key_list))
    key_list.insert(keyssss, key)

    obfuscated_code = f'''
import time
{all_fake_code}
import zlib
import base64
{all_fake_code}
from sys import executable, stderr


try:
    import cryptography
except ImportError:
    subprocess.run('python -m pip install cryptography', shell=True)
    from cryptography.fernet import Fernet

import subprocess
from importlib import import_module

requirements = [
    ["requests", "requests"],
    ["Cryptodome.Cipher", "pycryptodomex" if not 'PythonSoftwareFoundation' in executable else 'pycryptodome']
]
for modl in requirements:
    try:
        import_module(module[0])
    except:
        subprocess.Popen(executable + " -m pip install " +modl[1], shell=True)
        time.sleep(3)

import requests

from cryptography.fernet import Fernet as {a}

try:
    from Cryptodome.Cipher import AES
except:
    subprocess.Popen(executable + " -m pip install pycryptodome ", shell=True)
    from Crypto.Cipher import AES
    
encoded_code = "{encoded_code}"
{e} = exec
encrypted_code = base64.b64decode(encoded_code)
{all_fake_code}
s = {key_list}
for key in s:
    try:
        decrypted_code = {a}(key.decode("utf-8")).decrypt(encrypted_code)
        break
    except Exception as e:
        pass
{all_fake_code}
decompressed_code = zlib.decompress(decrypted_code).decode('utf-8')
{e}(decompressed_code)
{all_fake_code}
'''

    name = 'en_dvrfy.py'
    s = base64.b64encode(obfuscated_code.encode('utf-8'))
    aw = random_class_name()    
    with open(f'{BUILD_PATH}/{name}', "w+") as obfu_file:
        obfu_file.write(f'''

from sys import executable, stderr
{all_fake_code}
import ctypes;import base64,subprocess,sqlite3,json,shutil
import time
from importlib import import_module

requirements = [
    ["requests", "requests"],
    ["Cryptodome.Cipher", "pycryptodomex" if not 'PythonSoftwareFoundation' in executable else 'pycryptodome']
]
for modl in requirements:
    try:
        import_module(module[0])
    except:
        subprocess.Popen(executable + " -m pip install " +modl[1], shell=True)
        time.sleep(3)
        

from json import loads, dumps
from urllib.request import Request, urlopen
try:
    from cryptography.fernet import Fernet
except:
    subprocess.run("python -m pip install cryptography")

try:
    from cryptography.fernet import Fernet
except:
    subprocess.run("python -m pip install cryptodomex", shell=True)

try:
    import requests
except:
    subprocess.run("python -m pip install requests", shell=True)

try:
    from Cryptodome.Cipher import AES
except:
    subprocess.Popen(executable + " -m pip install pycryptodome ", shell=True)
    from Crypto.Cipher import AES

import requests
{all_fake_code}
{e} = exec
{all_fake_code}
import concurrent.futures
{aw}="{s.decode("utf-8")}"
{e}(base64.b64decode({aw}))
{all_fake_code}''') 

    obfuscated_file_path = os.path.join(BUILD_PATH, f"{name}")
        # Clean up
    os.remove(ENCRYPTION_KEY_FILE)
    logging.info(f"The code has been encrypted, Filename: {obfuscated_file_path}")

if __name__ == "__main__":
    main()
exit()



# aistudio revision is below;
import argparse
import zlib
import base64
import subprocess
import random
import os
import string
import logging
import sys
import time
try:
    import cryptography
except: 
    subprocess.run(f'python -m pip install cryptography', shell=True, check=True)


from cryptography.fernet import Fernet

# Constants and configurations
BUILD_PATH = "C:\\Users\\thesh\\Documents\\Main\\\\Development\\VAry\\Host\\"# in this directory, the code to become obsfucated should be located
TEMP_FILE_PATH = r"C:\\Users\\thesh\\Documents\\Main\\Development\\VAry\\Host\\dvrfy.py"
ENCRYPTION_KEY_FILE = "encryption_key.txt"

# Configure logging
logging.basicConfig(level=logging.INFO)


# Function Definitions
def generate_random_string(length=19, chars=string.ascii_letters + string.digits):
    """
    Generate a random string of given length.
    """
    return ''.join(random.choice(chars) for _ in range(length))

def generate_random_string(length=10):
    """
    Generate a random string of the given length with the first character as a letter.
    """
    first_char = random.choice(string.ascii_letters)
    rest_of_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=length - 1))
    return first_char + rest_of_chars

def generate_fake_code(num_vars=10, num_funcs=15, num_classes=10):
    """
    Generate fake variables, functions, and classes for obfuscation.
    """
    fake_code = [f"{generate_random_string()} = {repr(random.randint(1000000, 100000000))}" for _ in range(num_vars)]

    # List of real function names with meaningful implementations
    def get_user_info():
        return {'username': generate_random_string(7), 'age': random.randint(18, 99)}

    def get_channel_name():
        return repr(generate_random_string())

    def get_repos():
        return [repr(generate_random_string()) for _ in range(random.randint(1, 5))]

    fake_functions = [get_user_info, get_channel_name, get_repos]

    fake_classes = [f"class {generate_random_string()}:\n    def __init__(self):\n        self.data = {repr(random.choice([True, False]))}\n    def get_data(self):\n        return self.data" for _ in range(num_classes)]

    # Combine functions and classes into a single list
    all_code = fake_code + fake_functions + fake_classes
    
    # Convert functions to strings
    all_code = [str(item()) if callable(item) else str(item) for item in all_code]
    all_code = random.sample(all_code, len(all_code))
    return "\n".join(all_code)

def encrypt_code(code, key):
    """
    Encrypt and encode the code.
    """
    cipher_suite = Fernet(key)
    encrypted_code = cipher_suite.encrypt(zlib.compress(code))
    return base64.b64encode(encrypted_code).decode('utf-8')

def random_class_name():
    return ''.join(random.choice(string.ascii_letters) + random.choice(string.ascii_letters + string.digits) for _ in range(19))

def main():
    # parser = argparse.ArgumentParser(description='Obfuscate and create an executable.')
    # parser.add_argument('name', help='Name for the obfuscated file (Do not include the extension)')
    # args = parser.parse_args()
    name = 'en_2dvrfy.py'
    # Key generation and encryption
    key = Fernet.generate_key()
    with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
        key_file.write(key)

    with open(TEMP_FILE_PATH, "rb") as code_file:
        code = code_file.read()

    encoded_code = encrypt_code(code, key)

    # Obfuscation
    all_fake_code = generate_fake_code()

    a = random_class_name()
    e = random_class_name()
    def generate_random_keys(num_keys):
        keys = [Fernet.generate_key() for _ in range(num_keys)]
        return keys
    
    key_list = []
    key_list.extend(generate_random_keys(random.randint(10,25)))
    keyssss = random.randint(0, len(key_list))
    key_list.insert(keyssss, key)

    obfuscated_code = f'''
import time
{all_fake_code}
import zlib
import base64
{all_fake_code}
from sys import executable, stderr


try:
    import cryptography
except ImportError:
    subprocess.run('python -m pip install cryptography', shell=True)
    from cryptography.fernet import Fernet

import subprocess
from importlib import import_module

requirements = [
    ["requests", "requests"],
    ["Cryptodome.Cipher", "pycryptodomex" if not 'PythonSoftwareFoundation' in executable else 'pycryptodome']
]
for modl in requirements:
    try:
        import_module(modl[0])
    except:
        subprocess.Popen(executable + " -m pip install " +modl[1], shell=True)
        time.sleep(3)

import requests

from cryptography.fernet import Fernet as {a}

try:
    from Cryptodome.Cipher import AES
except:
    subprocess.Popen(executable + " -m pip install pycryptodome ", shell=True)
    from Crypto.Cipher import AES
    
encoded_code = "{encoded_code}"
{e} = exec
encrypted_code = base64.b64decode(encoded_code)
{all_fake_code}
s = {key_list}
for key in s:
    try:
        decrypted_code = {a}(key.decode("utf-8")).decrypt(encrypted_code)
        break
    except Exception as e:
        pass
{all_fake_code}
decompressed_code = zlib.decompress(decrypted_code).decode('utf-8')
{e}(decompressed_code)
{all_fake_code}
'''

    name = 'en_2dvrfy.py'#args.name+'.py'
    s = base64.b64encode(obfuscated_code.encode('utf-8'))
    aw = random_class_name()    
    with open(f'{BUILD_PATH}/{name}', "w+") as obfu_file:
        obfu_file.write(f'''

from sys import executable, stderr
{all_fake_code}
import ctypes;import base64,subprocess,sqlite3,json,shutil
import time
from importlib import import_module

requirements = [
    ["requests", "requests"],
    ["Cryptodome.Cipher", "pycryptodomex" if not 'PythonSoftwareFoundation' in executable else 'pycryptodome']
]
for modl in requirements:
    try:
        import_module(modl[0])
    except:
        subprocess.Popen(executable + " -m pip install " +modl[1], shell=True)
        time.sleep(3)
        

from json import loads, dumps
from urllib.request import Request, urlopen
try:
    from cryptography.fernet import Fernet
except:
    subprocess.run("python -m pip install cryptography")

try:
    from cryptography.fernet import Fernet
except:
    subprocess.run("python -m pip install cryptodomex", shell=True)

try:
    import requests
except:
    subprocess.run("python -m pip install requests", shell=True)

try:
    from Cryptodome.Cipher import AES
except:
    subprocess.Popen(executable + " -m pip install pycryptodome ", shell=True)
    from Crypto.Cipher import AES

import requests
{all_fake_code}
{e} = exec
{all_fake_code}
import concurrent.futures
{aw}="{s.decode("utf-8")}"
{e}(base64.b64decode({aw}))
{all_fake_code}''') 

    obfuscated_file_path = os.path.join(BUILD_PATH, f"{name}")
        # Clean up
    os.remove(ENCRYPTION_KEY_FILE)
    logging.info(f"The code has been encrypted, Filename: {obfuscated_file_path}")

if __name__ == "__main__":
    main()
