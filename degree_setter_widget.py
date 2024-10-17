import sys
import random
import time
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QLineEdit,QHBoxLayout
from serial_connection import serial_connection

class degree_setter_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.connection = serial_connection()
        main_vbox = QVBoxLayout()

        terminal_hbox = QHBoxLayout()
        terminal_hbox.addWidget(QLabel("Enter Position"))
        self.terminal = QLineEdit()
        terminal_hbox.addWidget(self.terminal)
        #terminal_hbox.addStretch()

        send_hbox = QHBoxLayout()
        send = QPushButton("Send")
        send.pressed.connect(self.send_cycle)
        send_hbox.addWidget(send)
        #send_hbox.addStretch()
        

        main_vbox.addLayout(terminal_hbox)
        main_vbox.addLayout(send_hbox)
        #main_vbox.addStretch()

        self.setLayout(main_vbox)

    def send_data(self):
        self.connection.send_value(self.terminal.text())


    def send_cycle(self):
        cycles = int(self.terminal.text())
        for i in range (cycles):
            pos_multiply = int(random.randint(0, 36)) #5 X Pos = step
            pos = pos_multiply*5
            print(f"going to position {pos} degrees")
            self.connection.send_value(str(round(pos/1.8)))
            time.sleep(3)
            print(f"going to position 0 degrees")
            self.connection.send_value(str(0))
            time.sleep(5)


        #self.connection.send_value(self.terminal.text())


