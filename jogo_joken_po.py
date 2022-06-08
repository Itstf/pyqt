from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 530)
        Form.setMinimumSize(QtCore.QSize(450, 530))
        Form.setMaximumSize(QtCore.QSize(450, 530))
        Form.setStyleSheet("background-color:rgb(0,0,0);")
        self.titulo = QtWidgets.QLabel(Form)
        self.titulo.setGeometry(QtCore.QRect(140, 30, 201, 61))
        self.titulo.setStyleSheet("color: white; font: 75 12pt \"Century Gothic\";")
        self.titulo.setObjectName("titulo")
        self.btn_pedra = QtWidgets.QPushButton(Form)
        self.btn_pedra.setGeometry(QtCore.QRect(50, 170, 101, 71))
        self.btn_pedra.setStyleSheet("color: white; background-color:rgb(138,43,226);")
        self.btn_pedra.setObjectName("btn_pedra")
        self.btn_papel = QtWidgets.QPushButton(Form)
        self.btn_papel.setGeometry(QtCore.QRect(170, 170, 101, 71))
        self.btn_papel.setStyleSheet("color: white; background-color:rgb(238,130,238);")
        self.btn_papel.setObjectName("btn_papel")
        self.btn_tesoura = QtWidgets.QPushButton(Form)
        self.btn_tesoura.setGeometry(QtCore.QRect(300, 170, 101, 71))
        self.btn_tesoura.setStyleSheet("color: white; background-color:rgb(147,112,219);")
        self.btn_tesoura.setObjectName("btn_tesoura")
        self.resposta = QtWidgets.QLabel(Form)
        self.resposta.setGeometry(QtCore.QRect(60, 280, 331, 111))
        self.resposta.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.resposta.setText("")
        self.resposta.setObjectName("resposta")
        self.btn_reset = QtWidgets.QPushButton(Form)
        self.btn_reset.setGeometry(QtCore.QRect(160, 420, 111, 61))
        self.btn_reset.setStyleSheet("color: white; background-color:rgb(255,0,0);")
        self.btn_reset.setObjectName("btn_reset")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pedra-Papel-Tesoura"))
        self.titulo.setText(_translate("Form", "qUe comece os jogos c:"))
        self.btn_pedra.setText(_translate("Form", "Pedra"))
        self.btn_papel.setText(_translate("Form", "Papel"))
        self.btn_tesoura.setText(_translate("Form", "Tesoura"))
        self.btn_reset.setText(_translate("Form", "Resetar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())