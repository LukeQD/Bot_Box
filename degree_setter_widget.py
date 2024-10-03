import sys
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
        send.pressed.connect(self.send_data)
        send_hbox.addWidget(send)
        #send_hbox.addStretch()
        

        main_vbox.addLayout(terminal_hbox)
        main_vbox.addLayout(send_hbox)
        #main_vbox.addStretch()

        self.setLayout(main_vbox)

    def send_data(self):
        self.connection.send_value(self.terminal.text())

