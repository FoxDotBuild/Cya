# Getting Started with MicroPython on Cya

This tutorial assumes you have assembled your Cya and installed MicroPython as described in the README.md file.

The next step is to install the library files and test that each peripheral device is accessible. There are multiple options for communication with MicroPython for installing the libraries. The two most popular are _ampy_ and _rshell_.

Instructions for using _ampy_ are available [here](https://pypi.org/project/adafruit-ampy/).

Instructions for using _rshell_ are available [here](https://pypi.org/project/rshell/). Note that rshell requires python3.

For the rest of this duscussion we will provide _rshell_ examples, but _ampy_ is equally capable and has similar commands.


## Install the start_i2c.py library
The start_i2c.py library configures the I2C bus on Cya


