# Set up the I2C bus

from machine import Pin, I2C
scl_pin = Pin(22)
sda_pin = Pin(21)
i2c=I2C(0, scl=scl_pin, sda=sda_pin )
