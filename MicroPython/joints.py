
# Setup and control for Cya leg joints
# Provides control for the motor of each joint
# Reads sensors to determine joint position


import pca9685
import utime
from machine import Pin, ADC

#_DC_MOTORS = ((8, 9, 10), (13, 12, 11), (2, 3, 4), (7, 6, 5))
_JOINT_PINS = ((0 ,1), (4, 5), (2, 3), (6, 7), (10, 11), (8, 9))
_SENSOR_SEL = ((0, 0, 0), (0, 0, 4095), (0, 4095, 0), (0, 4095, 4095), (4095, 0, 0), (4095, 0, 4095), (4095, 4095, 0), (4095, 4095, 4095))


FORWARD = const(0x00)
REVERSE = const(0x01)
COAST   = const(0x02)
BRAKE   = const(0x03)


class JOINTS:
    def __init__(self, i2c, address=0x40, freq=1600):
        self.pca9685 = pca9685.PCA9685(i2c, address)
        self.pca9685.freq(freq)
        self._analog_in = ADC(Pin(36))         # Use pin 36 to read sensors
        self._analog_in.atten(ADC.ATTN_11DB)   # Full range 0 to 3.3V
        
    def _pin(self, pin, value=None):
        if value is None:
            return bool(self.pca9685.pwm(pin)[0])
        if value:
            self.pca9685.pwm(pin, 4096, 0)
        else:
            self.pca9685.pwm(pin, 0, 0)

    def speed( self, joint, value, direction ):
        in2, in1 = _JOINT_PINS[ joint ]
        if joint >= 6 or joint < 0 :
            print("Joint out of range")
            return
        if direction == FORWARD:
            val1 = value
            val2 = 0
        elif direction == REVERSE:
            val1 = 0
            val2 = value        
        elif direction == COAST:
            val1 = 0
            val2 = 0        
        elif direction == BRAKE:
            val1 = 4095
            val2 = 4095        
        else:
            print("Invalid Direction")
            return
        self.pca9685.duty( in1, val1 )
        self.pca9685.duty( in2, val2 )
        
    def step( self, joint, value, time, direction ):
        in2, in1 = _JOINT_PINS[ joint ]
        if joint >= 6 or joint < 0 :
            print("Joint out of range")
            return
        if direction == FORWARD:
            val1 = value
            val2 = 0
        elif direction == REVERSE:
            val1 = 0
            val2 = value        
        self.pca9685.duty( in1, val1 )
        self.pca9685.duty( in2, val2 )
        utime.sleep_ms( time )          # Move for the fixed amount of milliseconds
        self.pca9685.duty( in1, 0 )     # and then coast
        self.pca9685.duty( in2, 0 )
        
    def sensor( self, joint ):
        sel1, sel2, sel3 = _SENSOR_SEL[ joint ]
        self.pca9685.duty( 12, sel1 )   # Select the joint sensor
        self.pca9685.duty( 13, sel2 )
        self.pca9685.duty( 14, sel3 )
        sensor_val = self._analog_in.read()
        return sensor_val

        
    
    
    
    
