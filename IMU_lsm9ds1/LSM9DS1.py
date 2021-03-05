# Date: 04.03.2021
# Author: Maciej Biskup

import smbus
import time

# Accelerometr default slave address
AccelerometerSlaveAddr = 0x1E
# Accelerometer ID
AccelerometerID = 0x68

# Magnetometer default slave address
MagnetometerSlaveAddr = 0x6B
MagnetometerID = 0x3D

# Accelerometr Register Mapping

WHO_AM_I = 0x0F

# Magnetometer Register Mapping

WHO_AM_I_M = 0x0F

bus = smbus.SMBus(1)

class lsm9ds1:

        def searchDevice(self):
                who_am_i = bus.read_byte_data(self.address, WHO_AM_I)
                if(who_am_i == AccelerometerID):
                        return true
                else:
                        return false

