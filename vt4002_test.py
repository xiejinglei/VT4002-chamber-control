# -*- coding: utf-8 -*-

import serial
import time

ser = serial.Serial('COM7', 9600, timeout=2)
print(ser.name)


# 询问试验箱的状态
ser.write(b'$01I\r\n')
time.sleep(0.1)
line = ser.readline().decode("utf-8")
value = str.split(line, ' ')
print(value)

time.sleep(0.1)

# 更改温度
ser.write(b"$01E " + "-10".encode() + b"\r\n")
ser.write(b'$01I\r\n')
time.sleep(0.1)
line = ser.readline().decode("utf-8")
value = str.split(line, ' ')
print("Temperature has been set to " + value[0])

ser.close()