from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 350)
        MainWindow.setMaximumSize(QtCore.QSize(350, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(350, 350))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(400, 400))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnHangman = QtWidgets.QPushButton(self.frame)
        self.btnHangman.setGeometry(QtCore.QRect(110, 150, 101, 25))
        self.btnHangman.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnHangman.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHangman.setStyleSheet("background-color: rgb(255, 196, 254);\n"
"border-radius:5px;")
        self.btnHangman.setObjectName("btnHangman")
        self.btnTictactoe = QtWidgets.QPushButton(self.frame)
        self.btnTictactoe.setGeometry(QtCore.QRect(10, 150, 81, 23))
        self.btnTictactoe.setMaximumSize(QtCore.QSize(100, 25))
        self.btnTictactoe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTictactoe.setStyleSheet("background-color: rgb(255, 196, 254);\n"
"border-radius:5px;")
        self.btnTictactoe.setObjectName("btnTictactoe")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 50, 203, 24))
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Century Gothic\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 300, 121, 21))
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";")
        self.label_2.setObjectName("label_2")
        self.btnHangman_2 = QtWidgets.QPushButton(self.frame)
        self.btnHangman_2.setGeometry(QtCore.QRect(230, 150, 91, 25))
        self.btnHangman_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnHangman_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHangman_2.setStyleSheet("background-color: rgb(255, 196, 254);\n"
"border-radius:5px;")
        self.btnHangman_2.setObjectName("btnHangman_2")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Games"))
        self.btnHangman.setText(_translate("MainWindow", "HANGMAN GAME(off)"))
        self.btnTictactoe.setText(_translate("MainWindow", "TIC TAC TOE"))
        self.label.setText(_translate("MainWindow", "CENTRAL GAMES"))
        self.label_2.setText(_translate("MainWindow", "Dsgn.menu: Igu "))
        self.btnHangman_2.setText(_translate("MainWindow", "Joken Po"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
