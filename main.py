import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication
import Ui_MainWindow
import VideoCapture


class MainWindow(QMainWindow, Ui_MainWindow.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.video_capture = VideoCapture.VideoCapture(self.videoFeed)

    def closeEvent(self, event):
        self.video_capture.release()
        event.accept()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())