# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Interface for PmodOLEDrgb module (ssd1331).

.. note::
   Depends on luma.oled and luma.core.
"""

import RPi.GPIO as gpio
from luma.core.render import canvas
from luma.core.sprite_system import framerate_regulator

from luma.core.interface.serial import spi
from luma.oled.device import ssd1331

CAP = 'SPI'
PHY = '2x6'

class PmodOLEDrgb:

    def __init__(self, DSPMod12):
        self.port = DSPMod12
        
        self.cs = self.port.pin1
        self.mosi = self.port.pin2
        self.nc = self.port.pin3
        self.sclk = self.port.pin4
        
        self.dc = self.port.pin7
        self.rst = self.port.pin8
        self.vccen = self.port.pin9
        self.pmoden = self.port.pin10
        self.powerf = True
        
        #
        if self.cs == 7: #CE1
            self.serial = spi(device=1, port=0, gpio_DC=self.dc, gpio_RST=self.rst)
        elif self.cs == 8: #CE0
            self.serial = spi(device=0, port=0, gpio_DC=self.dc, gpio_RST=self.rst)
        else:
            #throw exception
            pass

        # Setup GPIO.
        gpio.setmode(gpio.BCM)
        gpio.setup(self.vccen, gpio.OUT)
        gpio.output(self.vccen, gpio.HIGH)
        gpio.setup(self.pmoden, gpio.OUT)
        gpio.output(self.pmoden, gpio.HIGH)
        
        self.device = ssd1331(self.serial)
    
    def powerOff(self):
        gpio.output(self.vccen, gpio.LOW)
        gpio.output(self.pmoden, gpio.LOW)
        self.powerf = True
        
    def powerOn(self):
        gpio.output(self.vccen, gpio.HIGH)
        gpio.output(self.pmoden, gpio.HIGH)
        self.powerf = False
    
    def cleanup(self):
        self.powerOff
        #gpio.cleanup()
        self.device.cleanup()
    
    def getDevice(self):
        return self.device
