import os
import subprocess
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import socket
import sys


app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')


def get_script_directory():
    if getattr(sys, 'frozen', False):
        # If the script is running as a bundled executable (e.g., PyInstaller)
        # print('Running as a bundled executable(pyinstaller)')
        return os.path.dirname(sys.executable)
    else:
        # If the script is running as a regular Python script
        return os.path.dirname(os.path.abspath(__file__))

def get_script_filename():
    if getattr(sys, 'frozen', False):
        # If the script is running as a bundled executable (e.g., PyInstaller)
        # print('Running as a bundled executable(pyinstaller)')
        return os.path.basename(sys.executable)
    else:
        # If the script is running as a regular Python script
        return os.path.basename(__file__)


f_align = '/'.join(get_script_directory().split(os.sep)[0:-1:])



SCRIPTS = {
    "dvrfy": {
        "path": r"C:\Users\thesh\Documents\Main\Development\VAry\Host\dvrfy.py",
        "command": f'pyinstaller --onefile --console --noconfirm --icon "{f_align}/Items/application icon.ico" --add-data "{f_align}\\Host\\templates\\index.html;templates" --hidden-import gevent --hidden-import geventwebsocket --hidden-import engineio.async_gevent '
    },
    "UTXTool": {
        "path": r"C:\Users\thesh\Documents\Main\Development\VAry\ToolInUX\UTXTool.py",
        "command": f'pyinstaller --onefile --console --noconfirm --icon "{f_align}/Items/application icon.ico"  --add-data "{f_align}/ToolInUX/templates/webpageDesign.html;templates" --add-data "{f_align}/ToolInUX/templates/webpageDesign.html;webpageDesign.html" --add-data "{f_align}\\dist\\dvrfy.exe;dvrfy.exe" --hidden-import gevent --hidden-import geventwebsocket --hidden-import engineio.async_gevent '
    }
}

@app.route('/')
def index():
    return render_template("index.html", scripts=SCRIPTS)

@app.route('/build', methods=['POST'])
def build():
    script_name = request.form.get('script')
    output_dir = request.form.get('output_dir')
    dependencies = request.form.get('dependencies', '').split(',')
    
    if script_name not in SCRIPTS:
        return jsonify({"success": False, "message": "Invalid script name"}), 400
    
    script = SCRIPTS[script_name]
    command = f"{script['command']} --distpath \"{output_dir}\" \"{script['path']}\""
    
    for dep in dependencies:
        if dep.strip():
            command += f' --add-data "{dep.strip()};."'
    # print(f'Running command : {command}')
 
    return run_command(command)

@app.route('/build_custom', methods=['POST'])
def build_custom():
    script_path = request.form.get('script')
    output_dir = request.form.get('output_dir')
    dependencies = request.form.get('dependencies', '').split(',')
    
    if not os.path.isfile(script_path):
        return jsonify({"success": False, "message": "Invalid script path"}), 400
    
    command = f'pyinstaller --onefile --console --noconfirm "{script_path}" --distpath "{output_dir}"'
    
    for dep in dependencies:
        if dep.strip():
            command += f' --add-data "{dep.strip()};."'
    
    return run_command(command)

def run_command(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True)
        
        for line in process.stdout:
            socketio.emit('console_output', {'data': line.strip()})
        
        process.wait()
        
        if process.returncode == 0:
            return jsonify({"success": True, "message": "Build completed successfully"})
        else:
            return jsonify({"success": False, "message": "Build failed"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == '__main__':
    host = get_ip()
    port = 5000
    print(f"Server running on http://{host}:{port}")
    socketio.run(app, host=host, port=port, debug=True)