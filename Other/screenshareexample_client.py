from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QSizePolicy, QCheckBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import PyQt5.QtCore as QtCore
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QWidget
import cv2
import numpy as np
import socket
import struct
import sys
# from threading import thread
class ImageThread(QThread):
    changePixmap = pyqtSignal(QImage)

    sys._excepthook = sys.excepthook 
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback) 
        sys.exit(1) 
    sys.excepthook = exception_hook 

    def run(self):
        try:
            # print("Starting run method")
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # print("Created client_socket")
            ip = '192.168.1.13'#str(input("Server ip: "))
            # print(f"Got server ip: {ip}")
            client_socket.connect((ip, 5000))
            self.client_socket = client_socket
            print("Connected to server")
            while True:
                # print("Starting loop")
                length = struct.unpack("!I", client_socket.recv(4))[0]
                # print(f"Got length: {length}")
                img_data = b""
                while len(img_data) < length:
                    img_data += client_socket.recv(4096)
                # print(f"Got img_data: {len(img_data)} bytes")
                img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
                # print("Decoded image")
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # print("Converted image to RGB")
                h, w, ch = img.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(w, h, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p)
                # print("Emitted changePixmap signal")
        except Exception as e:
            print(f"An error occurred: {e}")

    def send_mouse_event(self,event_type ,x ,y ,button ):
        try:
            if button==-1:
                message=struct.pack("!I",event_type )+struct.pack("!I",x )+struct.pack("!I",y )+struct.pack("!I",0xFFFFFFFF )
            else:
                message=struct.pack("!I",event_type )+struct.pack("!I",x )+struct.pack("!I",y )+struct.pack("!I",button )
            self.client_socket.sendall(message )
        except struct.error as e:
            print(f'Erorr at send mouse event, ', e)
    def send_key_event(self,event_type ,key ):
        message=struct.pack("!I",event_type )+struct.pack("!I",key )
        self.client_socket.sendall(message )

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="Screenshare test application"
        self.left=100
        self.top=100
        self.width=640
        self.height=480
        self.imgis = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title )
        self.setGeometry(self.left ,self.top ,self.width ,self.height )
        layout=QVBoxLayout()
        self.label=QLabel(self )
        self.label.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        self.btn=QPushButton("Stop Streaming",self )
        self.btn.clicked.connect(self.stop_streaming )
        
        # Add a QCheckBox to the layout
        self.control_checkbox=QCheckBox("Control",self )
        
        layout.addWidget(self.label )
        layout.addWidget(self.btn )
        
        layout.addWidget(self.control_checkbox)
        
        self.setLayout(layout )
        
        # Set the label to accept mouse events
        self.label.setMouseTracking(True)

        QApplication.instance().installEventFilter(self)

        self.show()

    sys._excepthook=sys.excepthook 
    def exception_hook(exctype,value ,traceback ):
        print(exctype,value ,traceback )
        sys._excepthook(exctype,value ,traceback ) 
        sys.exit(1) 
    sys.excepthook=exception_hook 

    def stop_streaming(self):
         QApplication.instance().quit()

    def set_image(self, image):
        self.imgis = image
        image = image.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio)
        self.label.setPixmap(QPixmap.fromImage(image))


    def mousePressEvent(self, event):
        if self.isActiveWindow() and self.control_checkbox.isChecked():
            x_scale = self.imgis.width() / self.label.width()
            y_scale = self.imgis.height() / self.label.height()
            width = self.imgis.width()
            height = self.imgis.height()

            # Scale the mouse coordinates
            x = int(event.x() * x_scale)
            y = int(event.y() * y_scale)

            if event.button() == Qt.LeftButton:
                ImageThread.send_mouse_event(0, x, y, 0)
            elif event.button() == Qt.RightButton:
                ImageThread.send_mouse_event(0, x, y, 1)
            elif event.button() == Qt.MiddleButton:
                ImageThread.send_mouse_event(0, x, y, 2)

    def mouseReleaseEvent(self, event):
        if self.isActiveWindow() and self.control_checkbox.isChecked():
            x_scale = self.imgis.width() / self.label.width()
            y_scale = self.imgis.height() / self.label.height()
            width = self.imgis.width()
            height = self.imgis.height()

            # Scale the mouse coordinates
            x = int(event.x() * x_scale)
            y = int(event.y() * y_scale)

            if event.button() == Qt.LeftButton:
                ImageThread.send_mouse_event(1, x, y, 0)
            elif event.button() == Qt.RightButton:
                ImageThread.send_mouse_event(1, x, y, 1)
            elif event.button() == Qt.MiddleButton:
                ImageThread.send_mouse_event(0, x, y, 2)

    def mouseMoveEvent(self, event):
        if self.isActiveWindow() and self.control_checkbox.isChecked():
            # Calculate the scaling factor for the x and y coordinates
            x_scale = self.imgis.width() / self.label.width()
            y_scale = self.imgis.height() / self.label.height()
            print(self.label.pixmap().height(), self.label.height(), ' y')
            width = self.imgis.width()
            height = self.imgis.height()
            print(f'Image resolution: {width}x{height}')
            
            # Scale the mouse coordinates
            x = int(event.x() * x_scale)
            y = int(event.y() * y_scale)
            
            ImageThread.send_mouse_event(2, x, y, -1)
            
    def wheelEvent(self, event):
        if self.isActiveWindow() and self.control_checkbox.isChecked():
            delta = event.angleDelta().y()
            print('scroll thing')
            # Send a scroll up or scroll down event
            if delta > 0:
                ImageThread.send_mouse_event(3, 0, 0, 0)
            else:
                ImageThread.send_mouse_event(4, 0, 0, 0)


    def keyPressEvent(self,event ):
        if self.isActiveWindow() and self.control_checkbox.isChecked():
            key = QKeySequence(event.key()).toString().lower()
            if key == r'\udc22':
                key = 'win'
                return
                # cannot handle this due to limitations of the amount of letters can be sent/used in ord and cannot sent plain characters, only numbers
            ImageThread.send_key_event(5,ord(key))

    def keyReleaseEvent(self,event ):
        if self.isActiveWindow() and self.control_checkbox.isChecked():
            print('released, ', QKeySequence(event.key()).toString())
            ImageThread.send_key_event(6,ord(QKeySequence(event.key()).toString()))

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            print('KeyPress: %s [%r]' % (event.key(), source))
        return super().eventFilter(source, event)

if __name__=="__main__":
    app=QApplication(sys.argv )
    ex=App()
    thread=ImageThread()
    thread.changePixmap.connect(ex.set_image)
    thread.start()
    sys.exit(app.exec_())


# from pynput import keyboard

# def on_press(key):
#     try:
#         print(f'Key pressed: {key.char}')
#     except AttributeError:
#         print(f'Special key pressed: {key}')

# # Create a listener
# listener = keyboard.Listener(on_press=on_press)

# # Start the listener
# listener.start()

# # Keep the listener running
# listener.join()