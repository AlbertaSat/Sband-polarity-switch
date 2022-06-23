# Sband-polarity-switch
Polarity switch for sband groundstation arduino board

The structure of this code is to use a custom sketch for serial communication on the arduino and then use a Python script to command the Arduino pins on or off.

## PythonControl Sketch
The Arduino will have pythoncontrol.ino sketch uploaded.
June 23 - First implementation
Using an Arduino Mega. Pin 36 is assigned to Relay 1. Pin 38 is assigned to Relay 2. The Arduino monitors for incoming serial data.
'L' sets Pin 36 HIGH, activating Relay 1. Relay 1 is connected to the polarity switch. The polarity switch has the RHCP port of the S-band septum polarizer on NC and the LHCP port on NO, so activating Relay 1 sets the polarity to LHCP.
'R' sets Pin 36 LOW, deactivating Relay 1. This sets the polarity to RHCP.
'U' sets Pin 38 HIGH, activating Relay 2. Relay 2 is connected to the TX/RX switch. The TX/RX switch has RX on NC for Downlink and TX on NO for Uplink, so activating Relay 2 sets the switch to TX for Uplink.
'D' sets Pin 38 LOW, deactivating Relay 2. This sets the switch to RX for Downlink.
'Q' sets both pins 36 and 38 to LOW, deactivating both relays. This sets the default configuration to RHCP and Downlink.

## sband_ps_control.py
This program uses the pyserial package for serial comms in python and the tkinter package for creating a python gui.

The serial port of the Arduino is defined. Then the five commands associated with the five states defined in the PythonControl Sketch are defined. Each program prints a message to the terminal and writes a letter to the serial port of the Arduino ('L', 'R', 'U', 'D', or 'Q')

The rest of the program defines the colour, size, and location of the command buttons in the gui.

TO DO:
- Improve the colours of the buttons in the GUI
- Implement user defined inputs: ask user for the serial port, baud rate, pins of the Arduino
- Figure out how to make this program and gui available on the ground station software website
