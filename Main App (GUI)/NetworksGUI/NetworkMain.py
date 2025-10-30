import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QSizeGrip, QPushButton, 
                             QHeaderView, QTableWidgetItem, QMessageBox, QFileDialog,QLineEdit)

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSettings, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QImage

from UI_MainWindow import Ui_MainWindow

import os
import time
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore
from datetime import datetime
from PyQt5.QtCore import QTimer

import resources_rc
import cv2

from bridge1 import InteractiveDoorMonitor

class CameraThread(QThread):
    update_frame = pyqtSignal(QImage)
    
    def __init__(self):
        super().__init__()
        self.running = True
        self.recording = False
        self.video_writer = None
        self.output_path = None
        
    def start_recording(self, output_path):
        self.output_path = output_path
        self.recording = True
        
    def stop_recording(self):
        self.recording = False
        if self.video_writer:
            self.video_writer.release()
            self.video_writer = None
        

    def run(self):
        cap = cv2.VideoCapture(0)
        
        fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        while self.running:
            ret, frame = cap.read()
            if ret:
                if self.recording and self.video_writer is None and self.output_path:
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                    self.video_writer = cv2.VideoWriter(
                        self.output_path, fourcc, fps, (width, height)
                    )
                
                if self.recording and self.video_writer:
                    self.video_writer.write(frame)
                
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_frame.shape

                qt_image = QImage(rgb_frame.data, w, h, ch * w, QImage.Format_RGB888)
                self.update_frame.emit(qt_image)
            time.sleep(0.03)  # ~30 fps
        
        cap.release()
        if self.video_writer:
            self.video_writer.release()
        
    def stop(self):
        self.recording = False
        self.running = False
        self.wait()


class NetworksMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Door = InteractiveDoorMonitor()
        self.LoginData=  {"mohamed.elsayedt10@gmail.com":1234, "test":123 }

        # Set application font
        app = QApplication.instance()
        app.setFont(QFont("Segoe UI", 10))

        self.setWindowFlags(Qt.FramelessWindowHint) 

        self.stackedWidget.setCurrentWidget(self.Login)
        self.clickPosition = None

        self.is_recording = False
        self.current_recording_path = None

        self.door_manually_closed = False  # Track if door was closed using the close button
        self.expected_door_state = "unknown"  # Track what the door state should be
        self.last_known_door_state = "unknown"  # Track the last known actual door state


        self.IS_WINDOW_MAXIMIZED = False
        self.exitButton.clicked.connect(lambda: self.close())
        self.minimizeButton.clicked.connect(lambda: self.showMinimized())
        self.maximizeButton.clicked.connect(lambda: self.maximizeButtonLogic())


        self.exitButton_2.clicked.connect(lambda: self.close())
        self.minimizeButton_2.clicked.connect(lambda: self.showMinimized())
        self.maximizeButton_2.clicked.connect(lambda: self.maximizeButtonLogic())


        self.emailPlainText.setPlaceholderText("Email Address")
        self.passwordPlainText.setPlaceholderText("Password")


        self.loginButton.clicked.connect(lambda: self.validation())
        self.logoutButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Login))


        self.openDoorButton.clicked.connect(lambda: self.openDoor() )
        self.closeDoorButton.clicked.connect(lambda: self.closeDoor() )


        QSizeGrip(self.sizeGripFrame)
        QSizeGrip(self.sizeGripFrame_3)

        self.navigationButton.clicked.connect(lambda: self.navigationButtonLogic())


        self.homeButton.clicked.connect(lambda: self.mainBodyStackedWidget.setCurrentWidget(self.homePage)) 

        self.stackedWidget.setCurrentWidget(self.homePage)



        self.headerFrame.mouseMoveEvent = self.moveWindow
        self.headerFrame.mousePressEvent = self.mousePressEvent
        self.homeButton.click()


        self.camera_thread = CameraThread()
        self.camera_thread.update_frame.connect(self.update_camera_frame)
        self.camera_thread.start()
        
        self.startRecordButton.clicked.connect(self.start_recording)
        self.stopRecordButton.clicked.connect(self.stop_recording)
        

        self.stopRecordButton.setEnabled(False)
        
        self.destroyed.connect(self.cleanup_camera)

 
        self.door_status_timer = QTimer()
        self.door_status_timer.timeout.connect(self.check_door_status)
        self.door_status_timer.start(2000)  # Check every 2 seconds

        self.initialize_door_state()


                        
    def initialize_door_state(self):

        try:

            self.Door.send_door_command("open")
            

            self.statusLabel.setText("Initializing - Opening Door")
            self.statusLabel.setStyleSheet("color: blue;")
            

            self.door_manually_opened = True
            self.expected_door_state = "open"
            self.door_manually_closed = False
            
            QTimer.singleShot(2000, self.initialization_complete)
            
        except Exception as e:
            print(f"Error initializing door state: {e}")
            self.statusLabel.setText("Door Initialization Failed")
            self.statusLabel.setStyleSheet("color: red;")
    
    def initialization_complete(self):
        self.statusLabel.setText("Door Open - System Ready")
        self.statusLabel.setStyleSheet("color: green;")


    def check_door_status(self):
        try:
            current_door_status = self.Door.get_door_status()
            
            if current_door_status and current_door_status != self.last_known_door_state:
                self.last_known_door_state = current_door_status
                
                if (current_door_status == "0" and 
                    self.expected_door_state != "closed" and 
                    not self.door_manually_closed):

                    self.statusLabel.setText("Intruder Detected - Door Closed")
                    self.statusLabel.setStyleSheet("color: red; font-weight: bold;")
                    self.expected_door_state = "closed"
                    
                        
        except Exception as e:
            print(f"Door status check error: {e}")


    def openDoor(self):
        self.statusLabel.setText("Opening Door")
        self.Door.send_door_command("open")
        self.statusLabel.setStyleSheet("color: green; font-weight: bold;")
        

        self.door_manually_opened = True
        self.expected_door_state = "open"

        self.door_manually_closed = False

        QTimer.singleShot(1000, self.door_opened_status)


    def door_opened_status(self):
        self.statusLabel.setText("Door Open")
        self.statusLabel.setStyleSheet("color: green;font-weight: bold;")

    def door_closed_status(self):
        self.statusLabel.setText("Door Closed")
        self.statusLabel.setStyleSheet("color: Red;font-weight: bold;")


    def closeDoor(self):
        self.statusLabel.setText("Closing Door")
        self.Door.send_door_command("close")
        self.statusLabel.setStyleSheet("color: Red;font-weight: bold;")
        

        self.door_manually_closed = True
        self.expected_door_state = "closed"


        QTimer.singleShot(1000, self.door_closed_status)


            
    def validation(self):
        
        inputEmail = self.emailPlainText.toPlainText()
        inputPassword = self.passwordPlainText.toPlainText()
        if inputEmail in self.LoginData and self.LoginData[inputEmail] == int(inputPassword):
            self.stackedWidget.setCurrentWidget(self.homepage)
            self.emailPlainText.setPlainText("")
            self.passwordPlainText.setPlainText("")
            self.loginSatus.setText("")
        else:
            self.loginSatus.setText("Incorrect Credentials")
            self.emailPlainText.setPlainText("")
            self.passwordPlainText.setPlainText("")
            self.loginSatus.setStyleSheet("color: red;")
            



    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.clickPosition = event.globalPos()


    def moveWindow(self, event):

        if not self.isMaximized() and self.clickPosition is not None: 
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition) 
                self.clickPosition = event.globalPos()


    def start_recording(self):

        if not self.is_recording:

            save_dir = os.path.join(os.getcwd(), "recordings")
            os.makedirs(save_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"recording_{timestamp}.mp4"
            file_path = os.path.join(save_dir, filename)


            self.current_recording_path = file_path
            self.camera_thread.start_recording(file_path)
            self.is_recording = True


            self.startRecordButton.setEnabled(False)
            self.stopRecordButton.setEnabled(True)
            self.startRecordButton.setText("Recording...")

            QMessageBox.information(self, "Recording", f"Recording started!\nSaving to: {file_path}")
        

    def stop_recording(self):

        if self.is_recording:
            self.camera_thread.stop_recording()
            self.is_recording = False
            
            self.startRecordButton.setEnabled(True)
            self.stopRecordButton.setEnabled(False)
            

            self.startRecordButton.setText("Start Record")
            

            if self.current_recording_path:
                QMessageBox.information(
                    self, 
                    "Recording Complete", 
                    f"Recording saved successfully!\nLocation: {self.current_recording_path}"
                )
            

            self.current_recording_path = None



    def update_camera_frame(self, image):

        scaled_image = image.scaled(self.cameraLabel.width(), self.cameraLabel.height(), 
                       Qt.KeepAspectRatio)
        self.cameraLabel.setPixmap(QPixmap.fromImage(scaled_image))

        
    def cleanup_camera(self):

        if hasattr(self, 'camera_thread'):
            self.camera_thread.stop()
        

        if hasattr(self, 'door_status_timer'):
            self.door_status_timer.stop()



    def navigationButtonLogic(self):

        width = self.mainBodyLeftButtonsFrame.width() 
        
        if width == 30: 
            newWidth = 100 
        else: 
            newWidth = 30
    
        self.animation = QPropertyAnimation(self.mainBodyLeftButtonsFrame, b"minimumWidth") 
        self.animation.setDuration(100) 
        self.animation.setStartValue(width) 
        self.animation.setEndValue(newWidth) 
        self.animation.setEasingCurve(QEasingCurve.InOutQuart) 
        self.animation.start() 
    
    def maximizeButtonLogic(self):

        if (self.IS_WINDOW_MAXIMIZED):
            self.IS_WINDOW_MAXIMIZED = False
            self.showNormal()
            self.maximizeButton.setIcon(QIcon("./feather/maximize-2.svg")) 
            self.maximizeButton_2.setIcon(QIcon("./feather/maximize-2.svg")) 
        else:
            self.IS_WINDOW_MAXIMIZED = True
            self.showMaximized()
            self.maximizeButton.setIcon(QIcon("./feather/maximize.svg")) 
            self.maximizeButton_2.setIcon(QIcon("./feather/maximize.svg")) 



    def closeEvent(self, event):

        # Stop recording if it's active
        if self.is_recording:
            self.stop_recording()
        
        # Stop door monitoring
        if hasattr(self, 'door_status_timer'):
            self.door_status_timer.stop()
            
        self.cleanup_camera()
        event.accept()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create and show the main window
    window = NetworksMainWindow()
    window.show()
    
    # Execute the application
    sys.exit(app.exec_())