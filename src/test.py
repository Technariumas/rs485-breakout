#!/usr/bin/python

"""Waits for the sensor to appear on /dev/ttyUSB5, then reads moisture and temperature from it continuously"""

import minimalmodbus as mm
from time import sleep
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('serialport', metavar='SERIAL', type=str, help='Serial port')
parser.add_argument('--address', metavar='ADDR', type=int, default=1, choices=range(1, 248), help='An address to set')
parser.add_argument('--baudrate', metavar='BAUD', type=int, default=4, choices=range(0, 7), help='Current baudrate index - [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]')
args = parser.parse_args()

baudrates=[1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]

ADDRESS = args.address
SERIAL_PORT = args.serialport
BAUDRATE = baudrates[args.baudrate]

while True:
	try:
		instrument = mm.Instrument(SERIAL_PORT, ADDRESS)
		adc7 = instrument.read_register(0, functioncode=4);
		fw = instrument.read_register(2, functioncode=4);
		print(
			  " FW=" + str(hex(fw)) +
			  " ADC7=" + str(adc7)
		) 
		print("Setting 00")
		instrument.write_register(5, 0b00000000, functioncode=6);
		sleep(0.1)

		print("Setting 01")
		instrument.write_register(5, 0b00000001, functioncode=6);
		sleep(0.1)

		print("Setting 10")
		instrument.write_register(5, 0b00000010, functioncode=6);
		sleep(0.1)

		print("Setting 11")
		instrument.write_register(5, 0b00000011, functioncode=6);

		sleep(0.1)
	except ValueError as e:
		print e
		print("Waiting...")
		sleep(0.1)
	except IOError as e:
		print e
		print("Waiting...")
		sleep(0.1)
