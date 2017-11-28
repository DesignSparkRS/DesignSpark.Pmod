# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Interface for PmodTC1 module (MAX31855).
"""

import spidev
CAP = 'SPI'
PHY = '1x6'

class PmodTC1:
    
    def __init__(self, DSPMod6):
        
        self.port = DSPMod6
        
        self.cs = self.port.pin1
        self.nc = self.port.pin2
        self.miso = self.port.pin3
        self.sclk = self.port.pin4
        
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
        self.spi.max_speed_hz = 400000
        self.spi.mode = 0b00
        
    def __stopSPI(self):
        self.spi.close()   
    
    def __spiRead32(self):
            resp = self.spi.xfer2([0x00, 0x00, 0x00, 0x00])
            w = 0
            for i in range(3): 
                w |= resp[i]
                if i < 3:
                    w <<= 8
            return w
              
    def readCelcius(self):
            w = self.__spiRead32()
            #is error?
            if w & 0x7:
                return float('nan')
            #is negative ?
            if w & 0x80000000:
                w = 0xFFFFC000 | (( w >> 18) & 0x00003FFFF)
            else:
            #its standard    
                w >>= 18

            cent = float(w)
            cent *= 0.25
            return cent
                                  
    def readFarenheit(self):
            f = self.readCelcius()
            f *= 9.0
            f /= 5.0                      
            f += 32
            return f
    
    def readInternal(self):
            w = self.__spiRead32()
            w >> 4
            w &= 0x7FF
             
            if w & 0x800:
            # is negative    
                w = 0x0F800 | (w & 0x7FF)
            internal = float(w)    
            internal  *= 0.0625  
            
            return internal
        
    def readError():
        w = self.__spiRead32()
        return w & 0x7
    
    def cleanup(self):
        self.__stopSPI()
        
    
