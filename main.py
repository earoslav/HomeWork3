from PyQt5.QtWidgets import (QLabel,QVBoxLayout,QHBoxLayout,QWidget,QRadioButton,QApplication,QMessageBox)
from PyQt5.QtCore import Qt

title = "Питання"
qW = "-> Як звали першого ютуб-блогера, який набрав 100000000 підписників?"
answ = ["PewDiePie (правильна відповідь),", "Рет і Лінк,", "SlivkiShow,","TheBrianMaps,","Mister Max,","EeOneGuy."]

app = QApplication([])
win = QWidget()
win.resize(400,600)
win.move(400,300)
win.setWindowTitle(title)

qw = QLabel(qW)
rbnList = list()
for i in range(6):
    rbn = QRadioButton(answ[i])
    rbnList.append(rbn)

lineH1 = QHBoxLayout()
lineH2 = QHBoxLayout()
lineH3 = QHBoxLayout()
lineH4 = QHBoxLayout()
lineH5 = QHBoxLayout()
lineH6 = QHBoxLayout()
lineH7 = QHBoxLayout()
mainLine = QVBoxLayout()

lineH1.addWidget(qw, alignment=Qt.AlignLeft)
lineH2.addWidget(rbnList[0], alignment=Qt.AlignLeft)
lineH3.addWidget(rbnList[1], alignment=Qt.AlignLeft)
lineH4.addWidget(rbnList[2], alignment=Qt.AlignLeft)
lineH5.addWidget(rbnList[3], alignment=Qt.AlignLeft)
lineH6.addWidget(rbnList[4], alignment=Qt.AlignLeft)
lineH7.addWidget(rbnList[5], alignment=Qt.AlignLeft)
mainLine.addLayout(lineH1)
mainLine.addLayout(lineH2)
mainLine.addLayout(lineH3)
mainLine.addLayout(lineH4)
mainLine.addLayout(lineH5)
mainLine.addLayout(lineH6)
mainLine.addLayout(lineH7)

win.setLayout(mainLine)

def winner():
    mess = QMessageBox()
    mess.setWindowTitle("Winner")
    mess.setText("You won")
    mess.show()
    mess.exec()

def looser():
    mess = QMessageBox()
    mess.setWindowTitle("Loser")
    mess.setText("You lost")
    mess.show()
    mess.exec()

rbnList[0].clicked.connect(winner)    
rbnList[1].clicked.connect(looser)    
rbnList[2].clicked.connect(looser)    
rbnList[3].clicked.connect(looser)    
rbnList[4].clicked.connect(looser)    
rbnList[5].clicked.connect(looser)    

win.show()
app.exec()