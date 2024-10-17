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

        # Create line edit and label for input
        terminal_hbox = QHBoxLayout()
        terminal_hbox.addWidget(QLabel("Pos"))
        self.terminal = QLineEdit()
        terminal_hbox.addWidget(self.terminal)

        # Create "send" button and connect it to send_data
        send_hbox = QHBoxLayout()
        send = QPushButton("Send")
        send.pressed.connect(self.send_data)
        send_hbox.addWidget(send)
        
        # Add all layouts to main vertical layout
        main_vbox.addLayout(toggle_hbox)
        main_vbox.addLayout(terminal_hbox)
        main_vbox.addLayout(send_hbox)

        self.setLayout(main_vbox)

    def send_data(self):
        """
        Sends the specified value in steps to the serial connection, and updates the line edit to show the true sent value.
        """
        value = float(self.terminal.text())
        if self.degree_button.isChecked():
            value /= 1.8  # Convert degrees to steps before sending

        value = round(value)  # Round steps to nearest int
        self.connection.send_value(str(value))  # Send number of steps to serial connection

        # Update the lineedit to show the true value
        display_value = value * 1.8 if self.degree_button.isChecked() else value
        self.terminal.setText(str(display_value))

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
