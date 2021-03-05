# Date: 04.03.2021
# Author: Maciej Biskup

import smbus
import time

## Register mapping
# Accelerometer and gyroscope register address map
ACT_THS			=0x04
ACT_DUR 		=0x05
INT_GEN_CFG_XL		=0x06
INT_GEN_THS_X_XL	=0x07
INT_GEN_THS_Y_XL	=0x08
INT_GEN_THS_Z_XL	=0x09
INT_GEN_DUR_XL  	=0x0A
REFERENCE_G		=0x0B
INT1_CTRL		=0x0C
INT2_CTRL		=0x0D


WHO_AM_I		=0x0F


# Magnetic sensor register address map
OFFSET_X_REG_L_M	=0x05
OFFSET_X_REG_H_M	=0x06


WHO_AM_I_M		=0x0F

# Accelerometr and gyroscope i2c (default) slave address
AccelerometerGyroSlaveAddr	=0x1E
# Magnetometer i2c (default) slave address
MagnetometerSlaveAddr 		=0x6B

# Accelerometer and gyroscope ID
AccelerometerGyroID 		=0x68
# Magnetometer ID
MagnetometerID 			=0x3D

print("hello")

bus = smbus.SMBus(1)

class LSM9DS1:

        def searchDevice(self):
                who_am_i = bus.read_byte_data(self.address, WHO_AM_I)
                if(who_am_i == AccelerometerGyroID):
                        return true
                else:
                        return false
