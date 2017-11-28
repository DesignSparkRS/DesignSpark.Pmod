# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Manages Pmod HAT port resources, enforcing correct usage and 
avoiding conflicts.
"""

from __future__ import absolute_import
from DesignSpark.Pmod import TC1
from DesignSpark.Pmod import AD1
from DesignSpark.Pmod import MIC3
from DesignSpark.Pmod import HB3
from DesignSpark.Pmod import ISNS20
from DesignSpark.Pmod import OLEDrgb
from DesignSpark.Pmod import Error

# Physical pin map of Pmod to BCM I/O

JA1 = 8  #SPI_CE0
JA2 = 10 #SPI0_MOSI
JA3 = 9  #SPI0_MISO
JA4 = 11 #SPI0_CLK
# Gnd JA5
# Vcc JA6 
JA7 = 19  #PCM_FS/PWM1
JA8 = 21  #PCM_DOUT/GPCLK1
JA9 = 20  #PCM_DIN/GPCLK0
JA10 = 18 #PCM_CLK/PWM0
# Gnd JA11
# Vcc JA12

JB1 = 7  #SPI_CE1
JB2 = 10 #SPI0_MOSI
JB3 = 9  #SPI0_MISO
JB4 = 11 #SPI_CLK
# Gnd JB5
# Vcc JB6 
JB7 = 26
JB8 = 13 #PWM1
JB9 = 3  #SCL1
JB10 = 2 #SDA1
# Gnd JB11
# Vcc JB12

JC1 = 16  #CTS0
JC2 = 14 #TXD0
JC3 = 15  #RXD0
JC4 = 17 #RTS0
# Gnd  JB5
# Vcc JB6 
JC7 = 4  #GPCLK0
JC8 = 12 #PWM0
JC9 = 5  #GPCLK1
JC10 = 6 #GPCLK2
# Gnd JB11
# Vcc JB12

moduleDict = {
    'TC1': TC1,
    'AD1': AD1,
    'MIC3': MIC3,
    'HB3': HB3,
    'ISNS20': ISNS20,
    'OLEDrgb': OLEDrgb
    }

capabilityDict = {
    'JAA': [JA1,JA2,JA3,JA4,True,False,False],
    'JAB': [JA7,JA8,JA9,JA10,False,False,False],
    'JBA': [JB1,JB2,JB3,JB4,True,False,False],
    'JBB': [JB7,JB8,JB9,JB10,False,True,False],
    'JCA': [JC1,JC2,JC3,JC4,False,False,True], # UART pins are active by default 
    'JCB': [JC7,JC8,JC9,JC10,False,False,False]
    }

portUseDict = {}

def __checkPhysical(module, port):
    return module.PHY == port.phy

def __checkCapability(module, port):
    if module.CAP == 'SPI' and port._spi == True:
        return True
    if module.CAP == 'I2C' and port._i2c == True:
        return True
    if module.CAP == 'UART' and port._uart == True:
        return True
    if module.CAP == 'GPIO':
        return True
    # No capability match found
    return False

def createPmod(moduleName, portName):
        if moduleName in moduleDict:
            module = moduleDict[moduleName]
        else:
            erma = moduleName+' is not a recognised module identifier'
            raise Error.incorrectModuleName(erma) 
    
        if portName == 'JA' or portName == 'JB' or portName == 'JC':
            port = DSPMod12(portName)
        else:
            if portName in capabilityDict:
                port = DSPMod6(portName)
            else:
                erma = portName+' is not a recognised port identifier'
                raise Error.incorrectPortName(erma)
        
        if __checkPhysical(module,port) == False:
            erma = 'chosen port '+portName+' is the wrong size'+moduleName+' is a Pmod'+module.PHY+' module' 
            raise Error.portCapabilitySupport(erma)
        
        if __checkCapability(module,port) == False:
            erma = 'chosen port '+portName+' does not support '+module.CAP
            raise Error.portCapabilitySupport(erma)

        if port.inUse():
            erma = 'chosen port '+portName+' is already in use with '+portUseDict[portName]
            raise Error.portInUse(erma)
        
        ## Usage conflicts
        """
        If SPI is used on JAA or JBB allow only other SPI modules to init
        If a non-SPI module is used on JAA or JBB do not allow any other module 
        """
        
        if 'JAA' in portUseDict:
            cap = moduleDict[portUseDict['JAA']].CAP
            if cap == 'SPI':
                if portName == 'JBA' or portName == 'JB':
                    if moduleDict[moduleName].CAP != 'SPI':
                        erma = 'when port JAA is using an SPI module, port '+portName+' must also only use SPI'
                        raise Error.portCapabilityConflict(erma)
            else:       
                if portName == 'JBA' or portName == 'JB':
                    erma = 'when port JAA is not using an SPI module, port JBA is unavailable'
                    raise Error.portCapabilityConflict(erma) 


        if 'JBA' in portUseDict:
            cap = moduleDict[portUseDict['JBA']].CAP
            if cap == 'SPI':
                if portName == 'JAA' or portName == 'JA':
                    if moduleDict[moduleName].CAP != 'SPI':
                        erma = 'when port JBA is using an SPI module port '+portName+' must also only use SPI'
                        raise Error.portCapabilityConflict(erma)
            else:       
                if portName == 'JAA' or portName == 'JA':
                    erma = 'when port JBA is not using an SPI module, port JAA is unavailable'
                    raise Error.portCapabilityConflict(erma) 
                    
        
        ## All qualifiers passed
        port.setUseModule(moduleName)

        if moduleName == 'HB3':
            return HB3.PmodHB3(port)
        
        if moduleName == 'AD1':
            return AD1.PmodAD1(port)   
        
        if moduleName == 'ISNS20':
            return ISNS20.PmodISNS20(port)
        
        if moduleName == 'MIC3':
            return MIC3.PmodMIC3(port)
        
        if moduleName == 'TC1':
            return TC1.PmodTC1(port)
        
        if moduleName == 'OLEDrgb':
            return OLEDrgb.PmodOLEDrgb(port)
        
    
class DSPMod6:
    
    def __init__(self, _portName):
        self.portName = _portName
        cap = capabilityDict[self.portName]
        self.pin1 = cap[0]
        self.pin2 = cap[1]
        self.pin3 = cap[2]
        self.pin4 = cap[3]
        self._spi = cap[4] 
        self._i2c = cap[5]
        self._uart = cap[6]
        self.phy = '1x6'
         
    def setUseModule(self,moduleName):
        portUseDict[self.portName] = moduleName
        
    def inUse(self):
        return self.portName in portUseDict
    
class DSPMod12:
     
    def __init__ (self, _portName):
        
        self.dspMod6A = DSPMod6(_portName + 'A')
        self.dspMod6B = DSPMod6(_portName + 'B')
        
        self.pin1 = self.dspMod6A.pin1
        self.pin2 = self.dspMod6A.pin2
        self.pin3 = self.dspMod6A.pin3
        self.pin4 = self.dspMod6A.pin4
        self.pin7 = self.dspMod6B.pin1
        self.pin8 = self.dspMod6B.pin2
        self.pin9 = self.dspMod6B.pin3
        self.pin10 = self.dspMod6B.pin4
        
        self._spi = self.dspMod6A._spi # All SPI is on the upper 'a' Pmod port
        self._i2c = self.dspMod6B._i2c # Only I2C is on the lower 'b' Pmod port
        self._uart = self.dspMod6A._uart # Only UART is on the upper 'a' Pmod port
        self.phy = '2x6'
        
    def setUseModule(self, moduleName):
        self.dspMod6A.setUseModule(moduleName)
        self.dspMod6B.setUseModule(moduleName)
         
    def inUse(self):
        return self.dspMod6A.inUse() and self.dspMod6B.inUse()
        
