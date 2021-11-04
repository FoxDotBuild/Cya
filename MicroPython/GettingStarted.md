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

## Install and test the start_i2c.py library

The start_i2c.py library configures the I2C bus on Cya so you can use the accelerometer. Once you have installed it following the procedure above you can test it from _rshell_.

	Cya> repl
	Entering REPL. Use Control-X to exit.
	
	>>> from start_i2c import *
	>>> i2c
	I2C(0, scl=22, sda=21, freq=400000)
	>>> i2c.scan()
	[104]
	
This shows that the I2C bus is initialized and a device was found at address 104. This is the accelerometer. 104 is decimal, which is equivalent to 0x68. If you had more devices on the I2C bus they would also show up when you ran the i2c.scan() command.




