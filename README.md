<h1 align="center">Choose Your own Adventure Robot</h1>
<p align="center">
  <img src="https://user-images.githubusercontent.com/34964678/138538713-a7e72414-160c-42ff-8357-d56fdd33e000.jpg" />
</p>

There are many different aspects to robotics and Cya lets you explore the ones you find most interesting. You can explore electronics, mechanical design, programming, CAD design, sensors, 3D printing, create your own anthropomorphic behaviors, or just have fun building Cya. Cya was originally created as part of a Hackaday competition; additional info can be found [here](https://hackaday.io/project/181010-choose-your-own-adventure-bot).

## Electronics
There are three circuit boards in the basic Cya, the _head_, the _hip_, and the _femur-tibula_. The schematics and circuit board designs for each of these are in the Electronics folder. This allows you to examine the schematics, modify them to create your own custom version of Cya or to learn how to do electronics CAD, and even create your own circuit boards.

### Head Circuit Board
The head circuit board is where the Cya's brains are - the microprocessor and most of the sensors reside on the head board. It is designed in [KiCad](https://www.kicad.org/), a free and open source circuit board design tool.

### Hip Circuit Board
The hip circuit board controls the motors of the hip and provides feedback about the current angle of the hip. This circuit board is designed in [EasyEDA](https://easyeda.com/), another circuit board design CAD program. The Hip directory contains all the files necessary to view and modify the hip circuit board. You can also use the files as an example to help learn EasyEDA.

### Femur-Tibula Circuit Board
The Femur-Tubula circuit board is used in two places, the knee and the ankle joints. This board controls the motion of the knee or ankle joint and reports back the current position of the joint. This circuit board is also designed in EasyEDA. The Femur-Tibula directory contains all the files necessary to view and modify the Femur-Tibula circuit board.

## Mechanical Design
The mechanical design was done in OnShape. The entire design is available [here](https://cad.onshape.com/documents/090e28431662267442a38c78/w/26598236b7b4ff63fa80c892/e/632ca0c0b54aa3744d249046). (Note: A free login to OnShape is required). In addition to the CAD files in OnShape the .stl files are included in the Mechanical folder so they may be 3D printed. Alternatively, OnShape allows users to download .stl files directly, so you can modify the files in OnShape (you will have to create a copy of Cya in OnShape in order to modify it) and 3D print your modified version. If you want to learn to use a CAD program this is a good option.

## Programming
Cya can run using either python code or C++ Arduino style code, or actually any code that can be run on an ESP-32 processor. The two most popular programming languages for the ESP-32 are Arduino style C++ and python.

### Arduino Style C/C++
The Arduino microcontroller family has introduced millions of people to the joy of programming in C/C++. Arduino supports an Integrated Development Environment (IDE) that makes it easy to write programs and download them to Cya. This is a good way to learn C/C++ in an embedded scenario - you can modify your program and see exactly how Cya responds. The Arduino directory contains examples and instructions for programming Cya using the Arduino IDE.

### Python
Cya is capable of running the [MicroPython](https://micropython.org/) version of the python programming language. MicroPython must first be installed on Cya's ESP-32 in order to run programs that control Cya. The MicroPython directory contains instructions for installing MicroPython on Cya in addition to a number of MicroPython examples and libraries for controlling Cya.

## Documentation
Topic specific documentation is included in the directories where it applies. More general documentation is in the Docs directory. Additionally, be sure to look in the images directory for help in assembling Cya.


