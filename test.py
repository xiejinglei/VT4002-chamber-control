from vt4002 import vt4002
import time

inst = vt4002('COM7', 9600)
inst.status()
inst.set_temp(20)
inst.start_program(1)
time.sleep(10)
inst.stop_program()