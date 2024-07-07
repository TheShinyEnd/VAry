from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QSizePolicy, QCheckBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import PyQt5.QtCore as QtCore
import pyautogui
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QSizePolicy, QCheckBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import PyQt5.QtCore as QtCore
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QWidget
import cv2
import numpy as np
import socket
import sys
import numpy as np
import sys
import socket
import threading

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


class ImageThread(QThread):
    changePixmap = pyqtSignal(QImage)
    def __init__(self, ip, parent=None):
        super().__init__(parent)
        self.ip = ip
        self.client_socket_cntrls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket_cntrls.connect((self.ip, 5001))
        self.client_socket_mouse = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket_mouse.connect((self.ip, 5002))
    def run(self):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.ip, 5000))
            while True:
                length_data = client_socket.recv(4)
                if not length_data:
                    break
                length = int.from_bytes(length_data, byteorder='big')
                img_data = b""
                while len(img_data) < length:
                    chunk = client_socket.recv(min(4096, length - len(img_data)))
                    if not chunk:
                        break
                    img_data += chunk
                img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, ch = img.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(w, h, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            client_socket.close()
    def send_mouse_event(self, event_type, x, y, button):
        try:
            if button == -1:
                message = event_type.to_bytes(4, byteorder='big') + \
                          x.to_bytes(4, byteorder='big') + \
                          y.to_bytes(4, byteorder='big') + \
                          0xFFFFFFFF.to_bytes(4, byteorder='big')
            else:
                message = event_type.to_bytes(4, byteorder='big') + \
                          x.to_bytes(4, byteorder='big') + \
                          y.to_bytes(4, byteorder='big') + \
                          button.to_bytes(4, byteorder='big')
            
            self.client_socket_mouse.sendall(message)

        except Exception as e:
            print(f'Error at send mouse event:', e)
            

    def send_key_event(self, event_type, key):
        try:
            message = f'{event_type}:{key}'.encode('utf-8')
            self.client_socket_cntrls.sendall(message)
        except Exception as e:
            print(f'Error at send key event:', e)
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
        
    def focusInEvent(self, event):
        # Start listening for keyboard events
        self.control_checkbox.setChecked(True)
        print('focused')

    def focusOutEvent(self, event):
        # Stop listening for keyboard events
        self.control_checkbox.setChecked(False)
        print('unfocusewd')
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
                tlss.send_mouse_event(0, x, y, 0)
            elif event.button() == Qt.RightButton:
                tlss.send_mouse_event(0, x, y, 1)
            elif event.button() == Qt.MiddleButton:
                tlss.send_mouse_event(0, x, y, 2)
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
                tlss.send_mouse_event(1, x, y, 0)
            elif event.button() == Qt.RightButton:
                tlss.send_mouse_event(1, x, y, 1)
            elif event.button() == Qt.MiddleButton:
                tlss.send_mouse_event(0, x, y, 2)
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
          
            tlss.send_mouse_event(2, x, y, -1)
          
    def wheelEvent(self, event):
        if self.isActiveWindow() and self.control_checkbox.isChecked():
            delta = event.angleDelta().y()
            print('scroll thing')
            # Send a scroll up or scroll down event
            if delta > 0:
                tlss.send_mouse_event(3, 0, 0, 0)
            else:
                tlss.send_mouse_event(4, 0, 0, 0)
    def keyPressEvent(self, event):
        if self.isActiveWindow():
            if event.key() == Qt.Key_Alt:
                tlss.send_key_event('keyDOWN', 'ALT')
            elif event.key() == Qt.Key_Shift:
                tlss.send_key_event('keyDOWN', 'SHIFT')
            elif event.key() == Qt.Key_Enter:
                tlss.send_key_event('keyDOWN', 'ENTER')
            elif event.key() == Qt.Key_Super_L:
                tlss.send_key_event('keyDOWN', 'WINDOWS')
            else:
                try:
                    key = chr(event.key())
                    tlss.send_key_event('keyDOWN', key)
                except Exception as e:
                    print(f'Exception keypress evcent: {e}')

    def keyReleaseEvent(self, event):
        if self.isActiveWindow():
            if event.key() == Qt.Key_Alt:
                tlss.send_key_event('keyUP', 'ALT')
            elif event.key() == Qt.Key_Shift:
                tlss.send_key_event('keyUP', 'SHIFT')
            elif event.key() == Qt.Key_Enter:
                tlss.send_key_event('keyUP', 'ENTER')
            elif event.key() == Qt.Key_Super_L:
                tlss.send_key_event('keyUP', 'WINDOWS')
            else:
                try:
                    key = chr(event.key())
                    tlss.send_key_event('keyUP', key)
                except Exception as e:
                    print(f'Exception keyrelease evcent: {e}')
                    
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            try:
                print(f'KeyPress: {event.text()}')
            except Exception as e:
                # print(f'KeyPress: {event.key().toUtf8()}')
                print(f'Exception: {e}')
        return super().eventFilter(source, event)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ip = socket.gethostbyname(socket.gethostname())#'192.168.1.11'  # Update with your server's IP address
    tlss = ImageThread(ip)
    tlss.changePixmap.connect(ex.set_image)
    tlss.start()
    sys.exit(app.exec_())