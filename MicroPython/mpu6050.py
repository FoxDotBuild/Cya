# Copyright (c) 2018-2020 Mika Tuupola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of  this software and associated documentation files (the "Software"), to
# deal in  the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copied of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# https://github.com/tuupola/micropython-mpu9250

# Modifications made for Cya by Doug Kimber

"""
MicroPython I2C driver for MPU6050 6-axis motion tracking device
"""

__version__ = "0.9.0"

# pylint: disable=import-error
import ustruct
import utime
# from machine import I2C, Pin
from micropython import const
# pylint: enable=import-error

# Self test register addresses
_SELF_TEST_X = const(0x0d)
_SELF_TEST_Y = const(0x0e)
_SELF_TEST_Z = const(0x0f)
_SELF_TEST_A = const(0x10)

# Sampling rate divider address
_SMPLRT_DIV = const(0x19)

# Configuration register addresses
_CONFIG = const(0x1a)
_GYRO_CONFIG = const(0x1b)
_ACCEL_CONFIG = const(0x1c)

# FIFO Enable register address
_FIFO_EN = const(0x23)

# Auxiliary I2C bus register addresses
_I2C_MST_CTRL = const(0x24)
_I2C_SLV0_ADDR = const(0x25)
_I2C_SLV0_REG = const(0x26)
_I2C_SLV0_CTRL = const(0x27)
_I2C_SLV1_ADDR = const(0x28)
_I2C_SLV1_REG = const(0x29)
_I2C_SLV1_CTRL = const(0x2a)
_I2C_SLV2_ADDR = const(0x2b)
_I2C_SLV2_REG = const(0x2c)
_I2C_SLV2_CTRL = const(0x2d)
_I2C_SLV3_ADDR = const(0x2e)
_I2C_SLV3_REG = const(0x2f)
_I2C_SLV3_CTRL = const(0x30)
_I2C_SLV4_ADDR = const(0x31)
_I2C_SLV4_REG = const(0x32)
_I2C_SLV4_DO = const(0x33)
_I2C_SLV4_CTRL = const(0x34)
_I2C_SLV4_DI = const(0x35)
_I2C_MST_STATUS = const(0x36)

# Interrupt configuration register addresses
_INT_PIN_CFG = const(0x37)
_INT_ENABLE = const(0x38)
_INT_STATUS = const(0x3a)

# Accelerometer measurement register addresses
_ACCEL_XOUT_H = const(0x3b)
_ACCEL_XOUT_L = const(0x3c)
_ACCEL_YOUT_H = const(0x3d)
_ACCEL_YOUT_L = const(0x3e)
_ACCEL_ZOUT_H = const(0x3f)
_ACCEL_ZOUT_L = const(0x40)

# Temperature measurement register addresses
_TEMP_OUT_H = const(0x41)
_TEMP_OUT_L = const(0x42)

# Gyroscope measurement register addresses
_GYRO_XOUT_H = const(0x43)
_GYRO_XOUT_L = const(0x44)
_GYRO_YOUT_H = const(0x45)
_GYRO_YOUT_L = const(0x46)
_GYRO_ZOUT_H = const(0x47)
_GYRO_ZOUT_L = const(0x48)

# External sensor data register addresses
# These store data from sensors on the auxiliary I2C bus
_EXT_SENS_DATA_00 = const(0x49)
_EXT_SENS_DATA_01 = const(0x4a)
_EXT_SENS_DATA_02 = const(0x4b)
_EXT_SENS_DATA_03 = const(0x4c)
_EXT_SENS_DATA_04 = const(0x4d)
_EXT_SENS_DATA_05 = const(0x4e)
_EXT_SENS_DATA_06 = const(0x4f)
_EXT_SENS_DATA_07 = const(0x50)
_EXT_SENS_DATA_08 = const(0x51)
_EXT_SENS_DATA_09 = const(0x52)
_EXT_SENS_DATA_10 = const(0x53)
_EXT_SENS_DATA_11 = const(0x54)
_EXT_SENS_DATA_12 = const(0x55)
_EXT_SENS_DATA_13 = const(0x56)
_EXT_SENS_DATA_14 = const(0x57)
_EXT_SENS_DATA_15 = const(0x58)
_EXT_SENS_DATA_16 = const(0x59)
_EXT_SENS_DATA_17 = const(0x5a)
_EXT_SENS_DATA_18 = const(0x5b)
_EXT_SENS_DATA_19 = const(0x5c)
_EXT_SENS_DATA_20 = const(0x5d)
_EXT_SENS_DATA_21 = const(0x5e)
_EXT_SENS_DATA_22 = const(0x5f)
_EXT_SENS_DATA_23 = const(0x60)

# Auxiliary I2C Data out register addresses
_I2C_SLV0_D0 = const(0x63)
_I2C_SLV1_D0 = const(0x64)
_I2C_SLV2_D0 = const(0x65)
_I2C_SLV3_D0 = const(0x66)

# Auxiliary I2C control register address
_I2C_MST_DELAY_CTRL = const(0x67)

# Signal path reset register address
_I2C_SIGNAL_PATH_RESET = const(0x68)

# FIFO and auxiliary I2C control register address
_USER_CTRL = const(0x6a)

# Power Management Register addresses
_PWR_MGMT_1 = const(0x6b)       # Power Management 1 register address
_PWR_MGMT_2 = const(0x6c)       # Power Management 2 register address

# Power management register field values
_CLKSEL_INT_8MHZ = const(0x00)  # Select Internal 8 Mhz clock
_CLKSEL_XPLL = const(0x01)      # Use X-axis PLL gyro as clock reference
_CLKSEL_YPLL = const(0x02)      # Use Y-axis PLL gyro as clock reference
_CLKSEL_ZPLL = const(0x03)      # Use Z-axis PLL gyro as clock reference
_CLKSEL_32KPLL = const(0x04)    # Use external 32.768 Khz reference with PLL
_CLKSEL_19MPLL = const(0x05)    # Use external 19.2 Mhz reference with PLL
_CLKSEL_STOP = const(0x07)      # Stop the clock, reset the timing generator
_TEMP_DIS = const(0x08)         # Disable the temperature sensor when set
_CYCLE = const(0x20)            # Sleep, wake and sample, sleep again
_SLEEP = const(0x40)            # Put device to sleep when set
_RESET = const(0x80)            # Reset the device when set

# FIFO Control register addresses
_FIFO_COUNTH = const(0x72)      # High byte of number of bytes in FIFO
_FIFO_COUNTL = const(0x73)      # Low byte of number of bytes in FIFO
_FIFO_R_W = const(0x74)         # Address to Read/Write data from/to FIFO

# I2C bus address register. Should contain 0x68. Does not reflect the AD0 pin.
_WHO_AM_I = const(0x75)

#_ACCEL_FS_MASK = const(0b00011000)
ACCEL_FS_SEL_2G = const(0b00000000)
ACCEL_FS_SEL_4G = const(0b00001000)
ACCEL_FS_SEL_8G = const(0b00010000)
ACCEL_FS_SEL_16G = const(0b00011000)

_ACCEL_SO_2G = 16384 # 1 / 16384 ie. 0.061 mg / digit
_ACCEL_SO_4G = 8192 # 1 / 8192 ie. 0.122 mg / digit
_ACCEL_SO_8G = 4096 # 1 / 4096 ie. 0.244 mg / digit
_ACCEL_SO_16G = 2048 # 1 / 2048 ie. 0.488 mg / digit

#_GYRO_FS_MASK = const(0b00011000)
GYRO_FS_SEL_250DPS = const(0b00000000)
GYRO_FS_SEL_500DPS = const(0b00001000)
GYRO_FS_SEL_1000DPS = const(0b00010000)
GYRO_FS_SEL_2000DPS = const(0b00011000)

_GYRO_SO_250DPS = 131
_GYRO_SO_500DPS = 62.5
_GYRO_SO_1000DPS = 32.8
_GYRO_SO_2000DPS = 16.4

SF_G = 1
SF_M_S2 = 9.80665 # 1 g = 9.80665 m/s2 ie. standard gravity
SF_DEG_S = 1
SF_RAD_S = 0.017453292519943 # 1 deg/s is 0.017453292519943 rad/s

class MPU6050:
    """Class which provides interface to MPU6050 6-axis motion tracking device."""
    def __init__(
        self, i2c, address=0x68,
        accel_fs=ACCEL_FS_SEL_2G, gyro_fs=GYRO_FS_SEL_250DPS,
        accel_sf=SF_M_S2, gyro_sf=SF_RAD_S,
        gyro_offset=(0, 0, 0)
    ):
        self.i2c = i2c
        self.address = address

        # MPU6050 I2C address from this register must be 0x68
        # This register does not reflect the value of the AD0 pin
        if self.whoami not in [0x68]:
            raise RuntimeError("MPU6500 not found in I2C bus.")

        self._accel_so = self._accel_fs(accel_fs)
        self._gyro_so = self._gyro_fs(gyro_fs)
        self._accel_sf = accel_sf
        self._gyro_sf = gyro_sf
        self._gyro_offset = gyro_offset

        # Use the x axis gyro for clock, but don't wake the chip up
        self._register_char( _PWR_MGMT_1, value=_SLEEP | _CLKSEL_XPLL )
        
    @property
    def wake(self):
        """ The mpu6050 comes up in sleep mode. Take it out of sleep mode
        and start gathering data. """
        pwr_mgmt_1 = self._register_char(_PWR_MGMT_1)
        pwr_mgmt_1 &= ~_SLEEP
        print(pwr_mgmt_1)
        self._register_char(_PWR_MGMT_1, value=pwr_mgmt_1 )
        
    @property
    def sleep(self):
        """ Put the mpu6050 back into sleep mode. This conserves power."""
        pwr_mgmt_1 = self._register_char(_PWR_MGMT_1)
        pwr_mgmt_1 |= _SLEEP
        print(pwr_mgmt_1)
        self._register_char(_PWR_MGMT_1, value=pwr_mgmt_1 )
        
    def clock_sel( self, clk=_CLKSEL_XPLL ):
        """ Select the clock source. Default to X-axis gyro PLL. """
        pwr_mgmt_1 = self._register_char(_PWR_MGMT_1)
        pwr_mgmt_1 &= 0xf8
        pwr_mgmt_1 |= clk
        print(pwr_mgmt_1)
        self._register_char( _PWR_MGMT_1, value=pwr_mgmt_1 )
       
    @property
    def acceleration(self):
        """
        Acceleration measured by the sensor. By default will return a
        3-tuple of X, Y, Z axis acceleration values in m/s^2 as floats. Will
        return values in g if constructor was provided `accel_sf=SF_M_S2`
        parameter.
        """
        so = self._accel_so
        sf = self._accel_sf

        xyz = self._register_three_shorts(_ACCEL_XOUT_H)
        return tuple([value / so * sf for value in xyz])

    @property
    def gyro(self):
        """
        X, Y, Z radians per second as floats.
        """
        so = self._gyro_so
        sf = self._gyro_sf
        ox, oy, oz = self._gyro_offset

        xyz = self._register_three_shorts(_GYRO_XOUT_H)
        xyz = [value / so * sf for value in xyz]

        xyz[0] -= ox
        xyz[1] -= oy
        xyz[2] -= oz

        return tuple(xyz)

    @property
    def temperature(self):
        """ Temperature of the chip (not ambient) in celsius. """
        temp = self._register_short( _TEMP_OUT_H )
        # MPU6050 datasheet specifies this formula
        return ((temp / 340.0 ) + 36.53 )

    @property
    def temp_f(self):
        """ Temperature of the chip (not ambient) in farenheight. """
        temp = self.temperature
        return (((temp * 9.0) / 5.0 ) + 32.0)
    
    @property
    def whoami(self):
        """ Value of the whoami register. SHOULD be 0x68 """
        return self._register_char(_WHO_AM_I)

    def calibrate(self, count=256, delay=0):
        ox, oy, oz = (0.0, 0.0, 0.0)
        self._gyro_offset = (0.0, 0.0, 0.0)
        n = float(count)

        while count:
            utime.sleep_ms(delay)
            gx, gy, gz = self.gyro
            ox += gx
            oy += gy
            oz += gz
            count -= 1

        self._gyro_offset = (ox / n, oy / n, oz / n)
        return self._gyro_offset

    def _register_short(self, register, value=None, buf=bytearray(2)):
        if value is None:
            self.i2c.readfrom_mem_into(self.address, register, buf)
            return ustruct.unpack(">h", buf)[0]

        ustruct.pack_into(">h", buf, 0, value)
        return self.i2c.writeto_mem(self.address, register, buf)

    def _register_three_shorts(self, register, buf=bytearray(6)):
        self.i2c.readfrom_mem_into(self.address, register, buf)
        return ustruct.unpack(">hhh", buf)

    def _register_char(self, register, value=None, buf=bytearray(1)):
        if value is None:
            self.i2c.readfrom_mem_into(self.address, register, buf)
            return buf[0]

        ustruct.pack_into("<b", buf, 0, value)
        return self.i2c.writeto_mem(self.address, register, buf)

    def _accel_fs(self, value):
        self._register_char(_ACCEL_CONFIG, value)

        # Return the sensitivity divider
        if ACCEL_FS_SEL_2G == value:
            return _ACCEL_SO_2G
        elif ACCEL_FS_SEL_4G == value:
            return _ACCEL_SO_4G
        elif ACCEL_FS_SEL_8G == value:
            return _ACCEL_SO_8G
        elif ACCEL_FS_SEL_16G == value:
            return _ACCEL_SO_16G

    def _gyro_fs(self, value):
        self._register_char(_GYRO_CONFIG, value)

        # Return the sensitivity divider
        if GYRO_FS_SEL_250DPS == value:
            return _GYRO_SO_250DPS
        elif GYRO_FS_SEL_500DPS == value:
            return _GYRO_SO_500DPS
        elif GYRO_FS_SEL_1000DPS == value:
            return _GYRO_SO_1000DPS
        elif GYRO_FS_SEL_2000DPS == value:
            return _GYRO_SO_2000DPS

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass
