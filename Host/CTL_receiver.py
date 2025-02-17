# when you receive you delete the file in temp of the host, and when it finishes sending all the files it'll delete all of the downloda folder items

# this is the function that you add to utxtool where it can scan the ports across ALL subnets with the optimized scanner you create(you need to test it first), and it asks if you want to take the items from there and it'll
# bring you it to the same folder as utxtool just in a Restore folder. unencrypted.


# import tools
import os
import os
import shutil
import time
import hashlib
import sys
import socket
 
print("Starting CTL recv...")

key_for_encryption_of_backup = b'}\x8fLg\xa2#\xda7\xda\xb5\x18\xfb\xbew2\xd4\xb5\x899\xa6\xdb\xc4\xca|<\x8b\xd7KV\xb2\xb9\x16'

HOST_IP = '192.168.1.89'
HOST_PORT = 58963  # Same port as server
# CLIENT_BACKUP_DIR = os.path.join(tools.get_script_directory(), "RestoredFiles") 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST_IP, HOST_PORT))
    s.sendall("ZpH7wM2k9LnB5".encode())  # Send close signal - new connection for close signal
exit()

# exit()
#  netifaces

# def get_subnet_base():
#     interfaces = netifaces.interfaces()
#     for interface in interfaces:
#         addresses = netifaces.ifaddresses(interface)
#         if netifaces.AF_INET in addresses:
#             ip_address = addresses[netifaces.AF_INET][0]['addr']
#             if ip_address != '127.0.0.1':
#                 octets = ip_address.split('.')
#                 subnet_base = '.'.join(octets[:2])  # Get first two octets
#                 return subnet_base + '.' # include the first period for clarity

#     return None


# # import threading
# # import socket
# # from scapy.all import *

# # def scan_port(ip, port):
# #     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #     sock.settimeout(0.1)  # Adjust timeout as needed
# #     result = sock.connect_ex((ip, port))
# #     if result == 0:
# #         print(f"Port {port} is open on {ip}")
# #     sock.close()

# # def scan_subnet(subnet, port):
# #     threads = []
# #     for i in range(256):
# #         for j in range(256):
# #             ip = f"{subnet}{i}.{j}"
# #             # print(ip)
# #             # continue
# #             thread = threading.Thread(target=scan_port, args=(ip, port))
# #             threads.append(thread)
# #             thread.start()

# #     for thread in threads:
# #         thread.join()


# # if __name__ == "__main__":
# #     subnet = get_subnet_base()
# #     # print(subnet)
# #     # temp hardcode for subnet
# #     subnet = '172.31.'
# #     scan_subnet(subnet, HOST_PORT)
# #     print('Scan complete')


# # exit()

# def receive_file(conn, filename):
#     """Receives a file, handles errors, and sends confirmation."""
#     try:
#         file_size_bytes = conn.recv(4)
#         if not file_size_bytes: # Handle potential disconnect
#             return False

#         file_size = int.from_bytes(file_size_bytes, 'big')
#         received_data = b""
#         while len(received_data) < file_size:
#             chunk = conn.recv(4096)
#             if not chunk:
#                 return False # Socket closed prematurely
#             received_data += chunk
    
#         with open(filename, "wb") as f:
#             f.write(received_data)

#         conn.sendall("OK".encode())  # Send confirmation to server
#         return True # file successfully received


#     except Exception as e:
#         print(f"Error receiving file {filename}: {e}")
#         return False



# def decrypt_file(src, dst):
#     """Decrypts a file, handling decryption errors."""
#     with open(src, 'rb') as f_in:
#         encrypted_data = f_in.read()

#     decrypted_data = tools.decrypt_msg(encrypted_data, key_for_encryption_of_backup)
#     if decrypted_data is None:  # Check if decryption failed
#         print(f"Decryption of {src} failed. Deleting the encrypted file.")
#         os.remove(src) # deletes the encrypted file
#         return False  # Indicate failure

#     with open(dst, 'wb') as f_out:
#         f_out.write(decrypted_data)
#     print(f"Decrypted {src} to {dst}")
#     return True


# def request_file(host, port, filename):
#     """Requests and receives a single file."""
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((host, port))
#         s.sendall(filename.encode())
#         filepath = os.path.join(CLIENT_BACKUP_DIR, filename)
#         if receive_file(s, filepath):
#             if decrypt_file(filepath, filepath.replace(".encrypted", "")):
#                 os.remove(filepath)
#                 print(f"Received and decrypted: {filename}")
#                 return True # signal success
#             else:
#                 print(f"Error decrypting {filename}. File deleted.")
#         return False  # signal failure



# def get_backup_files(host, port):  # Takes host and port to make its own connection
#     """Retrieves the list of backup files."""

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((host, port))
#         s.sendall("LIST_FILES".encode())
#         files_bytes = s.recv(4096)  # Receive file list
#         files_str = files_bytes.decode()
#         if files_str:
#             return files_str.split(',')
#         else:
#             return []
 
# """ 
 
# def request_files(host, port):
#     """Requests and receives all files, establishing a new connection for each."""
#     # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

#     #     s.connect((host, port))
#     #     s.sendall("ZpH7wM2k9LnB5".encode())  # Send close signal - new connection for close signal
#     # exit()
#     if not os.path.exists(CLIENT_BACKUP_DIR):
#         os.makedirs(CLIENT_BACKUP_DIR)
        
#     filenames = get_backup_files(host, port)
#     if filenames:
#         for filename in filenames:
#             request_file(host, port, filename) # request files 1 by 1
#             time.sleep(1) # wait 1 second to prevent issues

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((host, port))
#         s.sendall("CLOSE".encode())  # Send close signal - new connection for close signal

#         s.sendall("CLOSE".encode()) # Signal server client is done.

# if __name__ == "__main__":
#     request_files(HOST_IP, HOST_PORT)"""
    
    
#     not up to date.. up to date version is in utxtool