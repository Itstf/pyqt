from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5 import uic

class jogo_velha(QMainWindow):
    def __init__(self):
        super(jogo_velha, self).__init__()
        uic.loadUi('qt_designer/velha.ui', self)
        
        self.cont = 0
        
        # botões | findChild -> encontrar botão
        self.b1 = self.findChild(QPushButton, 'btn1')
        self.b2 = self.findChild(QPushButton, 'btn2')
        self.b3 = self.findChild(QPushButton, 'btn3')
        self.b4 = self.findChild(QPushButton, 'btn4')
        self.b5 = self.findChild(QPushButton, 'btn5')
        self.b6 = self.findChild(QPushButton, 'btn6')
        self.b7 = self.findChild(QPushButton, 'btn7')
        self.b8 = self.findChild(QPushButton, 'btn8')
        self.b9 = self.findChild(QPushButton, 'btn9')
        self.label = self.findChild(QLabel, 'win')
        # lambda -> escrever em "anonimo"
        self.b1.clicked.connect(lambda:self.vez_user(self.b1))
        self.b2.clicked.connect(lambda:self.vez_user(self.b2))
        self.b3.clicked.connect(lambda:self.vez_user(self.b3))
        self.b4.clicked.connect(lambda:self.vez_user(self.b4))
        self.b5.clicked.connect(lambda:self.vez_user(self.b5))
        self.b6.clicked.connect(lambda:self.vez_user(self.b6))
        self.b7.clicked.connect(lambda:self.vez_user(self.b7))
        self.b8.clicked.connect(lambda:self.vez_user(self.b8))
        self.b9.clicked.connect(lambda:self.vez_user(self.b9))
        
        self.show()
    
    def verif(self):
        # verificar todas as posicoes possiveis de ganhar
        if self.b1.text() != '' and self.b1.text() == self.b4.text() and self.b1.text() == self.b7.text():
            self.vencer(self.b1, self.b4, self.b7)
        
        if self.b2.text() != '' and self.b2.text() == self.b5.text() and self.b2.text() == self.b8.text():
            self.vencer(self.b2, self.b5, self.b8)  
            
        if self.b3.text() != '' and self.b3.text() == self.b6.text() and self.b3.text() == self.b9.text():
            self.vencer(self.b3, self.b6, self.b9)
        # -------------------------------------------------
        if self.b1.text() != '' and self.b1.text() == self.b2.text() and self.b1.text() == self.b3.text():
            self.vencer(self.b1, self.b2, self.b3)
            
        if self.b4.text() != '' and self.b4.text() == self.b4.text() and self.b4.text() == self.b6.text():
            self.vencer(self.b4, self.b5, self.b6)
            
        if self.b7.text() != '' and self.b7.text() == self.b8.text() and self.b7.text() == self.b9.text():
            self.vencer(self.b7, self.b8, self.b9)
        # -------------------------------------------------
        if self.b1.text() != '' and self.b1.text() == self.b5.text() and self.b1.text() == self.b9.text():
            self.vencer(self.b1, self.b5, self.b9)
            
        if self.b3.text() != '' and self.b3.text() == self.b5.text() and self.b3.text() == self.b7.text():
            self.vencer(self.b3, self.b5, self.b7)
                    
    def vencer(self, btnum, btndois, btntres):
        btnum.setStyleSheet('QPushButton {background: black; color: white; border:none; border-radius:10px;}')
        btndois.setStyleSheet('QPushButton {background: black; color: white; border:none; border-radius:10px;}')
        btntres.setStyleSheet('QPushButton {background: black; color: white; border:none; border-radius:10px;}')
        #Adicionar label de vencedor
        self.label.setText(f'jogador {btnum.text()} ganhou ')
        self.reset()
                
    def vez_user(self, btn):
        if self.cont % 2 == 0:
            vez = 'x'
            # escrever na label o próximo jogador
            self.label.setText('Jogador O')
        else:
            vez = 'o'
            self.label.setText('Jogador X')
        btn.setText(vez)
        # depois que botao já selecionado, não conseguir clicar novamente
        btn.setEnabled(False)
        self.cont += 1
        self.verif()
        
    def reset(self):
        lista = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        for btn in lista:
            btn.setEnabled(False)