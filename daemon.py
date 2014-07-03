#!/usr/bin/python
import struct
import serial
import time

#ser = serial.Serial(0)


class NeoPixel(object):
    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(self.port, 9600, timeout=60)
        self.command_count = 0
        ready = None
        while not ready:
            print("Not ready")
            ready = self.ser.readline()
            print("Ready")
            print(ready)

    def setPixelColor(self, pixel, red, green, blue):
        message = struct.pack('>BBBHBBB', ord(':'), self.command_count, ord('c'), pixel, red, green, blue)
        self.command_count += 1
        if self.command_count >=255:
            self.command_count = 0
        print(message)
        self.ser.write(message)
        response = self.ser.readline()
        print(response)

    def show(self):
        message = struct.pack('BBB', ord(':'), self.command_count, ord('s'))
        self.command_count += 1
        print(message)
        self.ser.write(message)
        response = self.ser.readline()
        print(response)


import random

if __name__ == "__main__":
    strand = NeoPixel('/dev/ttyUSB0')
        
    strand.setPixelColor(x, 0, 0, 0)
    strand.show()

