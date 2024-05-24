import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

class VideoCapture:
    def __init__(self, label):
        self.label = label
        ip = 'http://192.168.0.2:8080/video'
        self.cap = cv2.VideoCapture(ip)  # 0 for the default camera

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30 ms

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(q_img))