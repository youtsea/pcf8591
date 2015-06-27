# must use Python 2.7
from pcf8591 import Module8591
import time

model = Module8591()
while True:    
    val = model.read_AIN0()
    print val
    time.sleep(0.5)


