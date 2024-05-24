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

    def release(self):
        self.cap.release()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 891, 561))
        self.tabWidget.setStyleSheet("background-color: rgb(80, 80, 80);\n"
"color: rgb(0,0,0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.liveFeed = QtWidgets.QWidget()
        self.liveFeed.setObjectName("liveFeed")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.liveFeed)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 421, 521))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.videoFeed = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoFeed.sizePolicy().hasHeightForWidth())
        self.videoFeed.setSizePolicy(sizePolicy)
        self.videoFeed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.videoFeed.setObjectName("videoFeed")
        self.horizontalLayout.addWidget(self.videoFeed)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.liveFeed)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 10, 431, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vehicleTypeBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vehicleTypeBox.sizePolicy().hasHeightForWidth())
        self.vehicleTypeBox.setSizePolicy(sizePolicy)
        self.vehicleTypeBox.setStyleSheet("color: rgb(240, 240, 240);")
        self.vehicleTypeBox.setObjectName("vehicleTypeBox")
        self.vehicleTypeBox.addItem("")
        self.vehicleTypeBox.addItem("")
        self.verticalLayout.addWidget(self.vehicleTypeBox)
        self.plateType = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plateType.sizePolicy().hasHeightForWidth())
        self.plateType.setSizePolicy(sizePolicy)
        self.plateType.setStyleSheet("color: rgb(248, 248, 248);")
        self.plateType.setObjectName("plateType")
        self.plateType.addItem("")
        self.plateType.addItem("")
        self.plateType.addItem("")
        self.verticalLayout.addWidget(self.plateType)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("color: rgb(241, 241, 241);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.liveFeed)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(590, 320, 171, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.date = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.date.setStyleSheet("color: rgb(255, 255, 255);")
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setObjectName("date")
        self.verticalLayout_2.addWidget(self.date)
        self.time = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.time.setStyleSheet("color: rgb(255, 255, 255);")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.verticalLayout_2.addWidget(self.time)
        self.tabWidget.addTab(self.liveFeed, "")
        self.database = QtWidgets.QWidget()
        self.database.setObjectName("database")
        self.tabWidget.addTab(self.database, "")
        self.availableSpaces = QtWidgets.QWidget()
        self.availableSpaces.setObjectName("availableSpaces")
        self.tabWidget.addTab(self.availableSpaces, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.videoFeed.setText(_translate("MainWindow", "VideoFeed"))
        self.vehicleTypeBox.setPlaceholderText(_translate("MainWindow", "Vehicle Type"))
        self.vehicleTypeBox.setItemText(0, _translate("MainWindow", "Two Wheeler"))
        self.vehicleTypeBox.setItemText(1, _translate("MainWindow", "Four Wheeler"))
        self.plateType.setPlaceholderText(_translate("MainWindow", "Liscence Plate Type"))
        self.plateType.setItemText(0, _translate("MainWindow", "Embossed"))
        self.plateType.setItemText(1, _translate("MainWindow", "Regional"))
        self.plateType.setItemText(2, _translate("MainWindow", "Provincial"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Liscence Plate Number"))
        self.date.setText(_translate("MainWindow", datetime.now().date().strftime('%Y-%m-%d')))
        self.time.setText(_translate("MainWindow", datetime.now().strftime('%H:%M:%S')))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.liveFeed), _translate("MainWindow", "LiveFeed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.database), _translate("MainWindow", "Database"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.availableSpaces), _translate("MainWindow", "Available Spaces"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.video_capture = VideoCapture(self.videoFeed)

    def closeEvent(self, event):
        self.video_capture.release()
        event.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

