import serial
import time


class vt4002:

    def __init__(self, com, baud, bus_addr='01'):
        self.bus_addr = bus_addr
        self.ser = serial.Serial('COM7', 9600, timeout=2)
        time.sleep(0.1)
        if not self.ser.is_open:
            assert False, "Fail to open port " + com

    # Print all parameters
    def status(self):
        command = '$' + str(self.bus_addr) + 'I\r\n'
        self.ser.write(command.encode())
        time.sleep(0.1)
        line = self.ser.readline().decode("utf-8")
        value = str.split(line, ' ')
        print(value)

    # Set temperature
    def set_temp(self, temp):
        command = "$" + str(self.bus_addr) + "E " + str(temp) + "\r\n"
        self.ser.write(command.encode())
        command = '$' + str(self.bus_addr) + 'I\r\n'
        self.ser.write(command.encode())
        time.sleep(0.1)
        line = self.ser.readline().decode("utf-8")
        value = str.split(line, ' ')
        if value[0] != "" and float(value[0]) == float(temp):
            print("Temperature has been set to " + value[0])
    
    # Get actual temperature
    def get_actual_temp(self):
        command = '$' + str(self.bus_addr) + 'I\r\n'
        self.ser.write(command.encode())
        time.sleep(0.1)
        line = self.ser.readline().decode("utf-8")
        value = str.split(line, ' ')
        return value[0]

    # Get set temperature
    def get_set_temp(self):
        command = '$' + str(self.bus_addr) + 'I\r\n'
        self.ser.write(command.encode())
        time.sleep(0.1)
        line = self.ser.readline().decode("utf-8")
        value = str.split(line, ' ')
        return value[1]

    # Start running the chamber
    def start_program(self, program=1):
        command = "$" + self.bus_addr + "P" + str(program).zfill(4) + "\r\n"
        self.ser.write(command.encode())
        if not program==0:
            print("Running program.")
        else:
            print("Stopped.")

    # Stop running the chamber
    def stop_program(self):
        self.start_program(0)

    def __del__(self):
        self.ser.close()
        print("Port closed.")