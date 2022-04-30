from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)

morse_code = {
    "a":[1,1,3],
    "b":[3,1,1,1,1,1,1],
    "c":[3,1,1,1,3,1,1],
    "d":[3,1,1,1,1],
    "e":[1],
    "f":[1,1,1,1,3,1,1],
    "g":[3,1,3,1,1],
    "h":[1,1,1,1,1,1,1],
    "i":[1,1,1],
    "j":[1,1,3,1,3,1,3],
    "k":[3,1,1,1,3],
    "l":[1,1,3,1,1,1,1],
    "m":[3,1,3],
    "n":[3,1,1],
    "o":[3,1,3,1,3],
    "p":[1,1,3,1,3,1,1],
    "q":[3,1,3,1,1,1,3],
    "r":[1,1,3,1,1],
    "s":[1,1,1,1,1],
    "t":[3],
    "u":[1,1,1,1,3],
    "v":[1,1,1,1,1,1,3],
    "w":[1,1,3,1,3],
    "x":[3,1,1,1,1,1,3],
    "y":[3,1,1,1,3,1,3],
    "z":[3,1,3,1,1,1,1]
    }

def clicked(t1):
    
    morse = []
    text = t1.text()
    i = 0
    for char in text:
        
        morse += morse_code[char]
        if i != len(text) - 1:
            morse.append(3)
        i+=1
    i=0
    for num in morse:
        if i%2 == 0:
            GPIO.output(19, GPIO.HIGH)
            time.sleep(num*0.1)
        else:
            GPIO.output(19, GPIO.LOW)
            time.sleep(num*0.1)
            
        i+=1 
    GPIO.output(19, GPIO.LOW)


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("Morse Code GUI")
    
    label = QtWidgets.QLabel(win)
    label.setText("Morse Code GUI")
    label.move(100,25)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("enter")
    b1.clicked.connect(lambda: clicked(t1))
    b1.move(100,200)
    
    t1 = QtWidgets.QLineEdit(win)
    t1.move(100,150)
    t1.setMaxLength(12)
    
    win.show()
    sys.exit(app.exec_())

window()

