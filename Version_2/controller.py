from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QApplication, QWidget,QVBoxLayout,QHBoxLayout,QPushButton, QComboBox, QTextEdit
from Position_Widget import position_widget
from serial_connection import serial_connection
import math
import time


class controller(QWidget):
    def __init__(self):
        super().__init__()
        self.init_layouts()
    
    def init_layouts(self):
        self.main_hbox = QHBoxLayout()

        #create button layout
        left_vbox = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.join_selector = QComboBox()
        self.join_selector.addItem("J0")
        self.join_selector.addItem("J1")
        self.join_selector.addItem("J2")
        self.join_selector.setCurrentIndex(1)
        self.join_selector.currentIndexChanged.connect(self.update_locked_joint)

        go_to_position = QPushButton("Go to location")
        add_position = QPushButton("Add Position")
        add_position.pressed.connect(self.add_pos)
        button_layout.addStretch()
        button_layout.addWidget(self.join_selector)
        button_layout.addWidget(go_to_position)
        button_layout.addWidget(add_position)
        button_layout.addStretch()
        left_vbox.addLayout(button_layout)
        
        #position_widget:
        self.pos_widget = position_widget()
        left_vbox.addWidget(self.pos_widget)

        self.main_hbox.addLayout(left_vbox)
        #create right_widget
        self.terminal = program_terminal()
        self.main_hbox.addWidget(self.terminal)
        self.setLayout(self.main_hbox)
    
    def update_locked_joint(self,index):
        self.pos_widget.set_joint(index)
    
    def add_pos(self):
        J1, base, J2 = self.pos_widget.get_position()

        self.terminal.insert_instruction(J1, base, J2)




class program_terminal(QWidget):
    def __init__(self):
        super().__init__()
        self.connection = serial_connection()
        self.program = []
        self.setup_layout()

    def setup_layout(self):
        main_vbox = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.wait_time = QComboBox()
        for i in range(10):
            self.wait_time.addItem(str(i+1) + " Seconds")

        insert_wait = QPushButton("Insert Wait")
        insert_wait.pressed.connect(self.insert_wait)

        run = QPushButton("Run Program")
        run.pressed.connect(self.run_program)

        self.button_layout.addStretch()
        self.button_layout.addWidget(self.wait_time)
        self.button_layout.addWidget(insert_wait)
        self.button_layout.addWidget(run)
        self.button_layout.addStretch()
        main_vbox.addLayout(self.button_layout)

        #text edit
        self.text_edit = QTextEdit()
        for line in self.program:
            self.text_edit.insertPlainText(str(line) + "\n")
        
        main_vbox.addWidget(self.text_edit)
        self.setLayout(main_vbox)

    def insert_wait(self):
        time = self.wait_time.currentIndex() + 1
        self.program.append(time)
        self.text_edit.insertPlainText(f"Wait for {time} seonds \n")
    
    def run_program(self):
        for command in self.program:
            if type(command) == int:
                print(f"Waiting for {command} seconds")
                time.sleep(command)

            else:
                print(f"Sending: {command}")
                self.connection.send_value(command)


    def insert_instruction(self, J1, base, J2):
        text = f"base = {round(base)}, J1 = {round(J1)}, J2 = {round(J2)}"
        self.text_edit.insertPlainText(text + "\n")
        #adjust for gear ratio of J1:
        J1 = (J1 * 2.5)
        J1_Step = J1/1.8

        #Adjust for base gear ratio
        base = base * 4.5
        base_step = base/1.8

        #adjust for wrist:
        J2 = J2
        command = f"{round(J1_Step)}B{round(base_step)}W{round(J2)}"
        self.program.append(command)
        

        


