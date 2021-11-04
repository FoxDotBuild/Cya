# Getting Started with MicroPython on Cya

This tutorial assumes you have assembled your Cya and installed MicroPython as described in the README.md file.

The next step is to install the library files and test that each peripheral device is accessible. There are multiple options for communicating between your PC and MicroPython to install the libraries. The two most popular are _ampy_ and _rshell_.

Instructions for using _ampy_ are available [here](https://pypi.org/project/adafruit-ampy/).

Instructions for using _rshell_ are available [here](https://pypi.org/project/rshell/). Note that rshell requires python3.

For the rest of this discussion we will provide _rshell_ examples, but _ampy_ is equally capable and has similar commands.

Download all the libraries you plan to use (See the README.md file to determine which libraries you will need and where to get them). Then go to the directory/folder where you  downloaded the libraries (The examples assume the directory /Cya, hence the 'Cya>' prompt). Type the following (assumes Cya is connected to COM10 - use the COM port your Cya is connected to):

 	Cya> rshell -p COM10

You will see output something like:

	Using buffer-size of 32
	Connecting to com10 (buffer-size 32)...
	Trying to connect to REPL  connected
	Retrieving sysname ... esp32
	Testing if ubinascii.unhexlify exists ... Y
	Retrieving root directories ... /boot.py/
	Setting time ... Nov 03, 2021 20:51:28
	Evaluating board_name ... pyboard
  	Retrieving time epoch ... Jan 01, 2000
	Welcome to rshell. Use the exit command to exit rshell.
	Cya>

FIrst, we need to create the lib directory:

	Cya> mkdir /pyboard/lib
	
Then, to install a library called _my_lib.py_ enter the following:

	cp my_lib.py /pyboard/lib/my_lib.py
	
That's all there is to it! The next step is to test the peripherals that each library supports.

## Install and Test the start_i2c.py Library for I2C Communications

The start_i2c.py library configures the I2C bus on Cya so you can use the accelerometer. Once you have installed it following the procedure above you can test it from _rshell_.

	Cya> repl
	Entering REPL. Use Control-X to exit.
	
	>>> from start_i2c import *
	>>> i2c
	I2C(0, scl=22, sda=21, freq=400000)
	>>> i2c.scan()
	[104]
	
This shows that the I2C bus is initialized with clock on pin 22, data on pin 21, and a bus frequency of 400000 Hz. It also shows a device was found at address 104. This is the accelerometer. 104 is decimal, which is equivalent to hex 0x68. If you had more devices on the I2C bus they would also show up when you ran the i2c.scan() command. If you did not see the 104 after scanning the I2C bus then check your connections and solder joints for the accelerometer.

## Install and Test the mpu6050.py Library for the Accelerometer

The mpu6050.py library provides a variety of methods for accessing the mpu6050 accelerometer. Install it as directed above and then test it with:

	Cya> repl
	Entering REPL. Use Control-X to exit.
	
	>>> import mpu6050
	>>> From machine import Pin, I2C
	>>> scl_pin = Pin( 22 )
	>>> sda_pin = Pin( 21 )
	>>> i2c = I2C( 0, scl=scl_pin, sda=sda_pin )
	>>> mpu = mpu6050.MPU6050( i2c )
	>>> mpu.wake
	1
	>>> mpu.acceleration   # Display the X, Y, and Z acceleration values
	(0.8690952, -0.06464344, -10.24)
	
Put Cya in a different position and re-type the _mpu.acceleration_ command. You will see different X,Y, and Z acceleration values. This shows your accelerometer is working!

## Install and Test the st7735.py Library for the Display

## Install and Test the hcsr04.py Library for the Ultrasonic Distance Sensor

The hcsr04.py library provides a variety of methods for accessing the HC-SR04 Ultrasonic distance sensor. Install it as directed above and then test it with:

	>>> import hcsr04
	>>> dist = hcsr04.HCSR04( 32, 27 )
	>>> dist.distance_cm()     # Get the distance in centimeters
	3.505155
	
Repeat the _dist.distance_cm()_ command with your hand at varying distances from the sensor. You will be able to see the distance change.

## Install and Test the kt403A.py Library for the DFPlayer Mini MP3 Player

The kt403A.py library provides a number of methods for controlling the DFPlayer Mini MP3 player. Before using it you will need to install some .mp3 files onto a uSD card and insert the uSD card into the DF Player Mini (Be sure Cya's power is off while inserting the uSD card!). The order you copy files to the uSD card determines the index number used to play them. For instance, the first file copied to the uSD is index 1, the second index 2, etc. Once you have installed the uSD card then power Cya up, connect to Cya, and in REPL enter the following:

	>>> import kt403A
	>>> mp3 = kt403A.KT403A( 1, 9, 10 )
	>>> mp3.SetVolume( 99 )  # Set the volume to 99% of maximum
	>>> mp3.PlaySpecific( 1 )    # Play .mp3 file #1

You should hear the first .mp3 file you put on the uSD card.

## Install and Test the pca9685.py Library for the PWM Controller

The pca9685.py library provides methods to control the motors and read the position sensors in the joints. It is used by the joints.py library to do the low-level functions of joint and motor control. Install it the same way as the other libraries then test it via:

	>>> From machine import Pin, I2C
	>>> import pca9685
	>>> scl_pin = Pin( 22 )
	>>> sda_pin = Pin( 21 )
	>>> i2c = I2C( 0, scl=scl_pin, sda=sda_pin )
	>>> pwm = pca9685.PCA9685( i2c )
	
*** Need a way to test communication

## install and Test the joints.py Library to control Cya's Motors and Joints


## Install and Test the INMP441.py Library for the Microphone





