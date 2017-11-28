# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Interface for PmodAD1 module (AD7476A).

.. note::
   Only a single channel (A1) is supported at present due to the way that SPI is configured.
"""

import spidev
CAP = 'SPI'
PHY = '1x6'

class PmodAD1:
    
    def __init__(self, DSPMod6):
        
        self.port = DSPMod6
        self.cs = self.port.pin1
        self.d0 = self.port.pin2
        self.d1 = self.port.pin3 #miso
        self.clk = self.port.pin4
        
        self.spi = spidev.SpiDev()
        self.__startSPI()
       
    def __startSPI(self):
        if self.cs == 7: #CE1
            self.spi.open(0,1)
        elif self.cs == 8: #CE0
            self.spi.open(0,0)
        else:
            #throw exception here
            return
        self.spi.max_speed_hz = 100000
        self.spi.mode = 0b00
        
    def __stopSPI(self):
        self.spi.close()   
    
    def __spiRead16(self):
            resp = self.spi.xfer2([0x00, 0x00])
            w = resp[0] 
            w <<= 8
            w |= resp[1]
            return w
    
    def readA1(self):
            return self.__spiRead16()
    
    def readA1Volts(self):
            w = self.__spiRead16()
            
            refV = 3.3
            lsb =  refV/4096
            volts= w*lsb
            
            return volts
 
    def cleanup(self):
            self.__stopSPI()

