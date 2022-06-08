import random
from PyQt5 import QtWidgets, uic
import centralofGAMES 
import jogo_joken_po
from velha import jogo_velha
import jogo_da_forca
from random import randint

class Menu(centralofGAMES.Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.velha = uic.loadUi('qt_designer/velha.ui')
        self.btnHangman_2.clicked.connect(self.btn_joken_po)   
        self.btnTictactoe.clicked.connect(self.chamar_jogo_velha)   
        self.btnHangman.clicked.connect(self.btn_jogo_forca)  
        
    def btn_joken_po(self):
        self.Form = QtWidgets.QWidget()
        self.joken = JokenPo(self.Form)
        self.Form.show()
        
    def chamar_jogo_velha(self):
        self.velha = jogo_velha()
        
    def btn_jogo_forca(self):
        self.forca = Forca()
        
class Forca(jogo_da_forca.Ui_FormForca):
    def __init__(self):
        self.FormForca = QtWidgets.QWidget()
        self.jogo_da_forca = uic.loadUi('qt_designer/jogo_da_forca.ui')
        self.jogo_da_forca.show()
        self.jogo_da_forca.chute.setHidden(True)
        print('aaaaSAA')
        self.jogo_da_forca.btn_chutar.clicked.connect(self.game)

    tempo = True
    word = {}
    keys = []
    escolher = ''
    text = ''
    error = 0
    empty = []

    def game(self):
        if self.tempo:
            self.jogo_da_forca.b_esquerdo.setHidden(True)
            self.jogo_da_forca.b_direito.setHidden(True)
            self.jogo_da_forca.p_direita.setHidden(True)
            self.jogo_da_forca.p_esquerda.setHidden(True)
            self.jogo_da_forca.cabeca.setHidden(True)
            self.jogo_da_forca.tronco.setHidden(True)

            self.jogo_da_forca.btn_chutar.setHidden(False)
            self.jogo_da_forca.btn_chutar.setText("chutar")
            self.jogo_da_forca.chute.setHidden(False)
            self.word = self.palavras()

            self.keys = list(self.word.keys())
            self.escolher = self.keys[0]
            self.jogo_da_forca.dicas.setText(self.word[self.keys[0]])
            self.tempo = False
            
            for i in range(len(self.keys[0])):
                self.empty.append("_")
            self.jogo_da_forca.letras_underlines.setText(" ".join(self.empty))
        else:
            letter = self.jogo_da_forca.chute.text()
            self.jogo_da_forca.chute.setText("")
            result = self.verify(letter)
            
            if not result:
                self.error += 1
            self.lost(self.error)

    def palavras(self):
        words = [{"colar": "acessorio"}, {"chuva": "gotas"}, {"computador": "eletronico"}, {"medico": "profissão"},
                 {"javascript": "linguagem de programacao"}, {"tibia": "jogo"},{"tenis": "calçado"},{"pizza": "massa"}, {"alemanha": "bosch"}]
        return words[randint(0, len(words))]
    
    def verify(self, letter):
        count = 0
        
        for i in self.escolher:
            if letter == i:
                for x in range(len(self.keys[0])):
                    if self.keys[0][x] == letter:
                        self.empty[x] = letter
                self.escolher = self.escolher.replace(letter, "")
                count -= 1
                break
            else:
                count += 1
                
        if count == len(self.escolher):
            return False
        
        elif len(self.escolher) == 0:
            self.jogo_da_forca.letras_underlines.setText(" ".join(self.empty))
            self.jogo_da_forca.dicas.setText("voce ganhou!")

            self.jogo_da_forca.btn_chutar.setEnabled(False)
            return True
        
        else:
            self.jogo_da_forca.letras_underlines.setText(" ".join(self.empty))
            return True

    def lost(self, value):
        if value == 1:
            self.jogo_da_forca.cabeca.setHidden(False)
        elif value == 2:
            self.jogo_da_forca.tronco.setHidden(False)
        elif value == 3:
            self.jogo_da_forca.b_direito.setHidden(False)
        elif value == 4:
            self.jogo_da_forca.b_esquerdo.setHidden(False)
        elif value == 5:
            self.jogo_da_forca.p_direita.setHidden(False)
        elif value == 6:
            self.jogo_da_forca.p_esquerda.setHidden(False)
            self.jogo_da_forca.letras_underlines.setText(" ".join(self.empty))
            self.jogo_da_forca.dicas.setText("perdeu. . .")
            self.jogo_da_forca.letras_underlines.setText("A palavra é:\n" + self.keys[0])
            self.jogo_da_forca.chute.setEnabled(False)
        
class JokenPo(jogo_joken_po.Ui_Form):
    escolhas = ['pedra', 'papel', 'tesoura']
    escolha = ''
    def __init__(self, Form):
        self.setupUi(Form)
        self.btn_papel.clicked.connect(self.btnPapel)
        self.btn_pedra.clicked.connect(self.btnPedra)
        self.btn_tesoura.clicked.connect(self.btnTesoura)
        self.btn_reset.clicked.connect(self.btnReset)
        
        JokenPo.__sortear()
    
    def verificar_vitoria(self):
        if self.escolha_usuario == 'papel' and JokenPo.escolha == 'pedra':
            self.resposta.setText(" VOCÊ VENCEU O COMPUTADOR")
        if JokenPo.escolha == 'papel' and self.escolha_usuario == 'pedra':
            self.resposta.setText(" O COMPUTADOR TE VENCEU . .")
            
        if self.escolha_usuario == 'pedra' and JokenPo.escolha == 'tesoura':
            self.resposta.setText("\t VOCÊ VENCEU O COMPUTADOR")
        if JokenPo.escolha == 'pedra' and self.escolha_usuario == 'tesoura':
            self.resposta.setText("\t O COMPUTADOR TE VENCEU . .")
            
        if self.escolha_usuario == 'tesoura' and JokenPo.escolha == 'pedra':
            self.resposta.setText("\t O COMPUTADOR TE VENCEU . .")
        if JokenPo.escolha == 'tesoura' and self.escolha_usuario == 'pedra':
            self.resposta.setText("\t VOCÊ VENCEU O COMPUTADOR")
            
        if self.escolha_usuario == 'papel' and JokenPo.escolha == 'tesoura':
            self.resposta.setText("\t O COMPUTADOR TE VENCEU . .")
        if JokenPo.escolha == 'papel' and self.escolha_usuario == 'tesoura':
            self.resposta.setText("\t VOCÊ VENCEU O COMPUTADOR")
            
        if self.escolha_usuario == 'papel' and JokenPo.escolha == 'papel':
            self.resposta.setText(" *** Aconteceu um empate ***")
        if self.escolha_usuario == 'pedra' and JokenPo.escolha == 'pedra':
            self.resposta.setText(" *** Aconteceu um empate ***")
        if self.escolha_usuario == 'tesoura' and JokenPo.escolha == 'tesoura':
            self.resposta.setText(" *** Aconteceu um empate ***")
        
        # desabilitar botoes para nao clicar
        self.btn_pedra.setEnabled(False)
        self.btn_papel.setEnabled(False)
        self.btn_tesoura.setEnabled(False)
        self.btn_pedra.setStyleSheet('QPushButton {background: gray; color: white; border-radius:3px;}')
        self.btn_papel.setStyleSheet('QPushButton {background: gray; color: white; border-radius:3px;}')
        self.btn_tesoura.setStyleSheet('QPushButton {background: gray; color: white; border-radius:3px;}')
    
    def btnPedra(self):
        self.escolha_usuario = 'pedra'
        self.verificar_vitoria()
        
    def btnPapel(self):
        self.escolha_usuario = 'papel'
        self.verificar_vitoria()
        
    def btnTesoura(self):
        self.escolha_usuario = 'tesoura'
        self.verificar_vitoria()
    
    def btnReset(self):
        JokenPo.__sortear()
        self.btn_pedra.setEnabled(True)
        self.btn_papel.setEnabled(True)
        self.btn_tesoura.setEnabled(True)
        self.btn_pedra.setStyleSheet('QPushButton {background-color:rgb(138,43,226); color: white;}')
        self.btn_papel.setStyleSheet('QPushButton {background-color:rgb(238,130,238); color: white;}')
        self.btn_tesoura.setStyleSheet('QPushButton {background-color:rgb(147,112,219); color: white;}')
        self.resposta.setText("")
        
    @staticmethod    
    def __sortear():
        JokenPo.escolha = random.choice(JokenPo.escolhas)
        print(JokenPo.escolha)

if __name__ == "__main__":    
    import sys
    app = QtWidgets.QApplication(sys.argv)  # main loop
    MainWindow = QtWidgets.QMainWindow() # janela que usa pra conf botoes pyqt
    ui = Menu(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_())