# light.py

import serial
from serial.tools import list_ports
import time

import serial.tools.list_ports


class serial_connection():

    def __init__(self):

        # Initialize the serial connection
        self.ser = None  # Initialize to None for now
        try:
            #Check which com port arduino is plugged into:
            ports = list(serial.tools.list_ports.comports())
            for p in ports:
                if "VID:PID=2341:0043" in p.hwid:
                    port = (p[0])
                    break
            else:
                port = "COM4"

            print(f"The port found was {port}")
            # Try to open the serial connection
            self.ser = serial.Serial(port, 9600, timeout=1)

            self.pluggedIn = True
        except serial.SerialException as e:
            # Handle the exception (COM4 not available)
            print(f"Error: {e}")
            self.pluggedIn = False

    def send_value(self,value:str):
        try:
            self.ser.write(value.encode('utf_8'))
            self.ser.flush()
            print(f"{value} was sent via serial connection")
        except serial.SerialException as e:
            # Handle the exception (COM4 not available)
            print(f"Error in sending R: {e}")

            
            
