# Getting Started with MicroPython on Cya

This tutorial assumes you have assembled your Cya and installed MicroPython as described in the README.md file.

The next step is to install the library files and test that each peripheral device is accessible. There are multiple options for communicating between your PC and MicroPython to install the libraries. The two most popular are _ampy_ and _rshell_.

Instructions for using _ampy_ are available [here](https://pypi.org/project/adafruit-ampy/).

Instructions for using _rshell_ are available [here](https://pypi.org/project/rshell/). Note that rshell requires python3.

For the rest of this duscussion we will provide _rshell_ examples, but _ampy_ is equally capable and has similar commands.

To install a library using _rshell_ type the following (assumes Cya is connected to COM10 - use the COM port your Cya is connected to):

  Cya> rshell -p COM10

You will see output something like:

  Using buffer-size of 32
  Connecting to com10 (buffer-size 32)...
  Trying to connect to REPL  connected
  Retrieving sysname ... esp32
  Testing if ubinascii.unhexlify exists ... Y
  Retrieving root directories ... /CyaMech.bmp/ /Nose.bmp/ /boot.py/ /lib/ /mic_left_channel_16bits.wav/
  Setting time ... Nov 03, 2021 20:51:28
  Evaluating board_name ... pyboard
  Retrieving time epoch ... Jan 01, 2000
  Welcome to rshell. Use the exit command to exit rshell.
  Cya>

## Install the start_i2c.py library
The start_i2c.py library configures the I2C bus on Cya


