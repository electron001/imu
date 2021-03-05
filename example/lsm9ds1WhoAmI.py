import IMU_LSM9DS1
import time
import sys

lsm9ds1 = IMU_LSM9DS1.LSM9DS1()

try:

        while True:
                print("hello_world")
                time.sleep(0.5)

except KeyboardInterrupt:
        sys.exit()
