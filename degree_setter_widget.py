import random
import time
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QPushButton, QRadioButton, QLineEdit, QHBoxLayout
from serial_connection import serial_connection

class degree_setter_widget(QWidget):
    """
    A widget that allows you to send degree or step values to the stepper motor(s) via serial connection.
    """
    def __init__(self):
        super().__init__()
        self.connection = serial_connection()
        main_vbox = QVBoxLayout()

        # Create radio buttons to toggle degrees/steps
        self.degree_button = QRadioButton("Degrees")
        self.steps_button = QRadioButton("Steps")
        self.degree_button.setChecked(True)  # Select degrees by default
        toggle_hbox = QHBoxLayout()
        toggle_hbox.addWidget(self.degree_button)
        toggle_hbox.addWidget(self.steps_button)

        # Create line edit and label for arm pos
        arm_terminal_hbox = QHBoxLayout()
        arm_terminal_hbox.addWidget(QLabel("Arm Pos"))
        self.arm_terminal = QLineEdit()
        arm_terminal_hbox.addWidget(self.arm_terminal)

        # Create line edit and label for base pos
        base_terminal_hbox = QHBoxLayout()
        base_terminal_hbox.addWidget(QLabel("Base"))
        self.base_terminal = QLineEdit()
        base_terminal_hbox.addWidget(self.base_terminal)

        # Create line edit and label for wrist pos
        wrist_terminal_hbox = QHBoxLayout()
        wrist_terminal_hbox.addWidget(QLabel("wrist"))
        self.wrist_terminal = QLineEdit()
        wrist_terminal_hbox.addWidget(self.wrist_terminal)

        # Create "send" button and connect it to send_data
        send_hbox = QHBoxLayout()
        send = QPushButton("Send")
        send.pressed.connect(self.send_data)
        send_hbox.addWidget(send)
        
        #create fire button:
        fire_hbox = QHBoxLayout()
        fire = QPushButton("Fire")
        fire.pressed.connect(self.fire)
        fire_hbox.addWidget(fire)

        # Add all layouts to main vertical layout
        main_vbox.addLayout(toggle_hbox)
        main_vbox.addLayout(arm_terminal_hbox)
        main_vbox.addLayout(base_terminal_hbox)
        main_vbox.addLayout(wrist_terminal_hbox)
        main_vbox.addLayout(send_hbox)
        main_vbox.addLayout(fire_hbox)

        self.setLayout(main_vbox)

    def fire(self):
        self.connection.send_value("fire")
        print("fire")


    def send_data(self):
        """
        Sends the specified value in steps to the serial connection, and updates the line edit to show the true sent value.
        """
        #get arm and base pos from terminal
        arm_pos = float(self.arm_terminal.text())*2.5
        if self.degree_button.isChecked():
            arm_pos /= 1.8  # Convert degrees to steps before sending
        arm_pos = round(arm_pos)

        base_pos = float(self.base_terminal.text())*4.5
        if self.degree_button.isChecked():
            base_pos /= 1.8
        base_pos = round(base_pos)

        wrist_pos = round(float(self.wrist_terminal.text()))


        #create pos string and send it
        pos_string = str(arm_pos) + "B" + str(base_pos) +"W" + str(wrist_pos)
        print(pos_string)
        self.connection.send_value(pos_string)  # Send number of steps to serial connection

        # Update the lineedit to show the true value
        arm_display_value = (arm_pos * 1.8)/2.5 if self.degree_button.isChecked() else arm_pos
        self.arm_terminal.setText(str(arm_display_value))
        base_display_value = (base_pos * 1.8)/4.5 if self.degree_button.isChecked() else base_pos
        self.base_terminal.setText(str(base_display_value))
        



    def send_cycle(self):
        """
        Sends a series of random positions to the serial connection in cycles.
        """
        cycles = int(self.terminal.text())
        for i in range(cycles):
            pos_multiply = int(random.randint(0, 36)) #5 X Pos = step
            pos = pos_multiply*5
            print(f"going to position {pos} degrees")
            self.connection.send_value(str(round(pos/1.8)))
            time.sleep(3)
            print(f"going to position 0 degrees")
            self.connection.send_value(str(0))
            time.sleep(5)

        #self.connection.send_value(self.terminal.text())
