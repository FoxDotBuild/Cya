import utime
import mpu6050
from machine import Pin, I2C
scl_pin = Pin( 22 )
sda_pin = Pin( 21 )
i2c = I2C( 0, scl=scl_pin, sda=sda_pin )
mpu = mpu6050.MPU6050( i2c )
mpu.wake
for x in range(1, 10):
  print( mpu.acceleration )
  utime.sleep_ms(1000) # Wait 1 second
