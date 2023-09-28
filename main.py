import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('Hesap Makinesi')
        self.setGeometry(560,190,310,585)
        self.setStyleSheet('background-color: black;')
        self.veri = ''

        self.label = QLabel('',self)
        self.label.setGeometry(0,120,335,60)

        buttonac = QPushButton("AC", self)
        buttonac.setFont(QFont('Bold', 20))
        buttonac.setGeometry(10, 200, 64,64)
        buttonac.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #9E9E9E;color:black')
        buttonac.clicked.connect(lambda:self.clickme('AC'))

        buttonsilme = QPushButton("⌫", self)
        buttonsilme.setFont(QFont('Bold', 20))
        buttonsilme.setGeometry(85, 200, 64,64)
        buttonsilme.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #9E9E9E;color:black')
        buttonsilme.clicked.connect(lambda:self.clickme('silme'))

        buttonyuzde = QPushButton("%", self)
        buttonyuzde.setFont(QFont('Bold', 20))
        buttonyuzde.setGeometry(160, 200, 64,64)
        buttonyuzde.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #9E9E9E;color:black')
        buttonyuzde.clicked.connect(lambda:self.clickme('%'))

        buttonbolme = QPushButton("÷", self)
        buttonbolme.setFont(QFont('Bold', 30))
        buttonbolme.setGeometry(235, 200, 64,64)
        buttonbolme.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #F59906;')
        buttonbolme.clicked.connect(lambda:self.clickme('/'))
        
        button7 = QPushButton("7", self)
        button7.setFont(QFont('Bold', 30))
        button7.setGeometry(10, 278, 64,64)
        button7.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #313131;')
        button7.clicked.connect(lambda:self.clickme('7'))

        button8 = QPushButton("8", self)
        button8.setFont(QFont('Bold', 30))
        button8.setGeometry(85, 278, 64,64)
        button8.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #313131;')
        button8.clicked.connect(lambda:self.clickme('8'))

        button9 = QPushButton("9", self)
        button9.setFont(QFont('Bold', 30))
        button9.setGeometry(160, 278, 64,64)
        button9.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #313131;')
        button9.clicked.connect(lambda:self.clickme('9'))

        buttoncarpi = QPushButton("x", self)
        buttoncarpi.setFont(QFont('Bold', 30))
        buttoncarpi.setGeometry(235, 278, 64,64)
        buttoncarpi.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #F59906;')
        buttoncarpi.clicked.connect(lambda:self.clickme('*'))

        button4 = QPushButton("4", self)
        button4.setFont(QFont('Bold', 30))
        button4.setGeometry(10, 356, 64,64)
        button4.setStyleSheet('border-radius : 32;border : 0px solid black;background-color:#313131;')
        button4.clicked.connect(lambda:self.clickme('4'))

        button5 = QPushButton("5", self)
        button5.setFont(QFont('Bold', 30))
        button5.setGeometry(85, 356, 64,64)
        button5.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #313131;')
        button5.clicked.connect(lambda:self.clickme('5'))

        button6 = QPushButton("6", self)
        button6.setFont(QFont('Bold', 30))
        button6.setGeometry(160, 356, 64,64)
        button6.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #313131;')
        button6.clicked.connect(lambda:self.clickme('6'))

        buttoneksi = QPushButton("-", self)
        buttoneksi.setFont(QFont('Bold', 30))
        buttoneksi.setGeometry(235, 356, 64,64)
        buttoneksi.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #F59906;')
        buttoneksi.clicked.connect(lambda:self.clickme('-'))

        button1 = QPushButton("1", self)
        button1.setFont(QFont('Bold', 30))
        button1.setGeometry(10, 434, 64,64)
        button1.setStyleSheet('border-radius : 32;border : 0px solid black;background-color:#313131;')
        button1.clicked.connect(lambda:self.clickme('1'))

        button2 = QPushButton("2", self)
        button2.setFont(QFont('Bold', 30))
        button2.setGeometry(85, 434, 64,64)
        button2.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #313131;')
        button2.clicked.connect(lambda:self.clickme('2'))

        button3= QPushButton("3", self)
        button3.setFont(QFont('Bold', 30))
        button3.setGeometry(160, 434, 64,64)
        button3.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #313131;')
        button3.clicked.connect(lambda:self.clickme('3'))

        buttonarti = QPushButton("+", self)
        buttonarti.setFont(QFont('Bold', 30))
        buttonarti.setGeometry(235, 434, 64,64)
        buttonarti.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #F59906;')
        buttonarti.clicked.connect(lambda:self.clickme('+'))

        button0 = QPushButton("0", self)
        button0.setFont(QFont('Bold', 30))
        button0.setGeometry(10, 512,128,64)
        button0.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #313131;')
        button0.clicked.connect(lambda:self.clickme('0'))

        buttonvirgul = QPushButton(",", self)
        buttonvirgul.setFont(QFont('Bold', 30))
        buttonvirgul.setGeometry(160, 512, 64,64)
        buttonvirgul.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #313131;')
        buttonvirgul.clicked.connect(lambda:self.clickme('.'))

        buttonesittir = QPushButton("=", self)
        buttonesittir.setFont(QFont('Bold', 30))
        buttonesittir.setGeometry(235, 512, 64,64)
        buttonesittir.setStyleSheet('border-radius : 32;border : 0px solid black;background-color: #F59906;')
        buttonesittir.clicked.connect(lambda:self.clickme('='))
    def keyPressEvent(self,event):
        a=event.key()
        if a ==49 or a ==50 or a ==52 or a ==51 or a ==54 or a ==53 or a ==55 or a ==56 or a ==57 or a ==48:
            sayi = a-48
            self.clickme(str(sayi))
        if a == 43:
            self.clickme('+')
        if a == 45:
            self.clickme('-')
        if a == 47:
            self.clickme('/')
        if a == 42:
            self.clickme('*')
        if a == 46:
            self.clickme('.')
        if a == 61 or a==16777220:
            self.clickme('=')
        if a == 16777219:
            self.clickme('silme') 
        if a == 65:
            self.clickme('AC') 
        if a == 37:
            self.clickme('%') 
    def clickme(self,mesaj):
        if mesaj == 'AC':
            self.veri=''
        elif mesaj == 'silme':
            self.veri = self.veri[:-1]
        elif mesaj != '=' :
            self.veri += mesaj
        elif mesaj == '=':
            sonuc = eval(self.veri)
            print(sonuc)
            self.veri = str(sonuc)
        self.label.setText(self.veri)
        self.label.setFont(QFont('Bold', 40))
        
        
App = QApplication(sys.argv)
 
window = Window()
window.show()

sys.exit(App.exec())