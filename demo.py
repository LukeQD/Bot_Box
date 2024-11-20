from serial_connection import serial_connection
import time


connection = serial_connection()

start_string = "167B112W"
fire = "fire"
end_string = "0B0W20"


connection.send_value(end_string)
time.sleep(3)
connection.send_value(start_string)
print("firsts string sent")
time.sleep(5)
connection.send_value(fire)
time.sleep(3)
connection.send_value(end_string)
print("second string sent")


