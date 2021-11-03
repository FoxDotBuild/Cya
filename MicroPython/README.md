# Running MicroPython on Cya.
## Installing MicroPython on Cya
If you don't have it, install Python on your PC. I chose version 3.9.6.
Note: Wherever the following commands use pip or python you may need to use pip3 or python3 if you have python2.7 and python 3.x installed and want to use python 3.x.
Install "pip" if you don't already have it (It is installed automatically with newer versions of python):

	Download get-pip.py from https://bootstrap.pypa.io/get-pip.py
  
	$python get-pip.py

https://docs.micropython.org/en/latest/esp32/tutorial/intro.html provides details on installing MicroPython on an ESP32 based board.

Install "esptool.py" from https://github.com/espressif/esptool using:

	$pip install esptool
  
Download the latest MicroPython .bin file from

https://micropython.org/download/#esp32 

Select the "Generic ESP32 module" version. Note: I2S support, required for the microphone, is only available in builds after July 5, 2021.
The downloaded file will be something like: esp32-20210623-v1.16.bin

Note: Whenever you encounter COMx in the following commands substitute the actual port number your MH-ET is connected to (e.g., COM5. You can find the port using Windows Device Manager and looking under Ports.

If this is the first time you've installed MicroPython on this board then erase the Flash:

	$esptool.py --chip esp32 --port COMx erase_flash
  
Now program MicroPython into the flash (Substitute the name of the .bin file you downloaded):

	$esptool.py --chip esp32 --port COMx --baud 460800 write_flash -z 0x1000 esp32-20210811-unstable-v1.16-198-g42d1a1635.bin
  
Check Your Work

Now see if MicroPython is running on the MH-ET Live. Do this using REPL (Read, Evaluate, Print, and Loop). Be sure the MH-ET is connected to your PC and start a serial console (You can use your favorite serial console, for example PuTTY, a free serial console program available here:

	https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
  
Connect to the COM port of the MH-ET at 115200 baud. If you hit your enter key you should see a “>>>” prompt. You might also see some additional information preceding the “>>>” prompt. When you get the prompt congratulate yourself – you now have MicroPython installed on your Cya! 

## Cya Specific Micropython Library Files:

MicroPython looks for library files in the /lib directory. Any file you place in the /lib directory can then be imported using the python import command. You may need some or all of the following libraries, depending on which features of Cya you plan to use.

- start_i2c.py Configure the I2C bus. Saves some typing during inital setup.
- setup.py Initializes all the Cya peripherals
- st7735.py  library for 1.44” TFT Display
- kt403A.py library for the DFPlayer Mini: https://github.com/jczic/KT403A-MP3
- mpu6050.py library for the accelerometer
- INMP-441 microphone driver
- hcsr04.py HC-SR04 Ultrasonic driver: https://github.com/rsc1975/micropython-hcsr04
- Driver for voice recognition? Can the C/C++ from Edge Impulse be converted for Python use?
- pca9685.py library for the pca9685 PWM board: https://github.com/adafruit/micropython-adafruit-pca9685
- joints.py - maps pca9685 pins to joints for controlling the motors and reading the sensors.

