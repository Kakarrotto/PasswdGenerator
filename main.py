#!/usr/bin/python3

# Password Generator

# Easy to use password generator. List of things to implement:
# - System to generate password                                 # done // it can be better
# - How long is password                                        # done
# - Weak - strong password                                      # not implemented yet
# - Button to copy generated password                           # done
# - Place with password                                         # done
# - Buttons: Generate, copy, exit                               # done

# -----------------------------------------------
# First it shows generated password
# Second it shows slider with length of password
# Third it shows button: Generate, Copy, Exit
# -----------------------------------------------

import sys
import random
import pyperclip
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class App(QWidget):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        # Width and Height Window

        self.left = 860
        self.top = 440
        self.width = 320
        self.height = 120

        self.initUI()

    def initUI(self):
        
        # Window
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Layouts
        layoutv = QVBoxLayout()
        layouth = QHBoxLayout()
        mainLayout = QGridLayout()
        mainLayout.addLayout(layoutv , 0, 1)
        mainLayout.addLayout(layouth , 1, 1)
        
        # Password view
        self.password_label = QLabel("Password: " + str())
        layoutv.addWidget(self.password_label)
     
        # Slider
        self.howlong = QLabel("Choose size of password: (min 1 - max 26)")
        layoutv.addWidget(self.howlong)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(5)
        self.slider.setMinimum(1)
        self.slider.setMaximum(26)
        layoutv.addWidget(self.slider)
        self.slider.valueChanged.connect(self.slidervalue)

        # Button to generate new password
        self.button_gen = QPushButton("Generate")
        self.button_gen.clicked.connect(self.generatepasswd)

        # Button to copy new password
        self.button_copy = QPushButton("Copy")
        self.button_copy.clicked.connect(self.copypasswd)

        # Button to quit
        self.button_quit = QPushButton("Quit")
        self.button_quit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        
        # Adding buttons horizontal to layout
        layouth.addWidget(self.button_gen)
        layouth.addWidget(self.button_copy)
        layouth.addWidget(self.button_quit)
        self.setLayout(mainLayout)
        self.setWindowTitle("Passwd Generator")

        # Function to ctr+c password
    def copypasswd(self):
        pyperclip.copy(self.copy_passwd)      

        # Function to generate password
        # It uses value from slider and creating password from this string
    def generatepasswd(self):
        password = []
        for i in range(int(svalue)):
            addpass = password.append(random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwwerttyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+;'))
        self.passwd = "".join(password)
        password_string = str("Password: " + str(self.passwd))
        global copy_passwd
        self.copy_passwd = self.passwd
        self.password_label.setText(password_string)
    
        #Function slider value
    def slidervalue(self):
        global svalue
        svalue = self.slider.value()
        slider_string = "Choose length of password: " + str(svalue) + " (min 1 - max 26)"
        self.howlong.setText(slider_string)

    
        # Main program
def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()