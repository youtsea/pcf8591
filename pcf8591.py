# must use Python 2.7
import smbus
bus = smbus.SMBus(1)
# This is the address we setup in the PCF8591
address = 0x48
# 0x00 - 0x03 is AIN0 - AIN3
# bus.write_byte(address,0x00)


class Module8591:

        def read_AIN0(self):
            bus.write_byte(address,0x40)
            bus.read_byte(address) # dummy read to start conversion
            return bus.read_byte(address)
            
            
        def read_AIN1(self):
            bus.write_byte(address,0x41)
            bus.read_byte(address) # dummy read to start conversion
            return bus.read_byte(address)


        def read_AIN2(self):
            bus.write_byte(address,0x42)
            bus.read_byte(address) # dummy read to start conversion
            return bus.read_byte(address)
            

        def read_AIN3(self):
            bus.write_byte(address,0x43)
            bus.read_byte(address) # dummy read to start conversion
            return bus.read_byte(address)


        def writeAOUT(self):
            temp = self.aout_var.get() # move string value to temp
            temp = int(temp) # change string to integer
            # print temp to see on terminal else comment out
            bus.write_byte_data(address, 0x40, temp)
            
      

