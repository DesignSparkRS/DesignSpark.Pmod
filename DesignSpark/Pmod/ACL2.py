"""
Interface for Pmod ACL2 module.
"""

# TODO
# FIFO setting
# Active and inactive detection


import spidev
import RPi.GPIO as GPIO
import time
CAP = 'SPI'
PHY = '2x6'


class PmodACL2:
    
    def __init__(self, DSPMod12):
        self.selectedRange = 1
        self.port = DSPMod12
        self.cs = self.port.pin1
        self.nc = self.port.pin2
        self.miso = self.port.pin3
        self.sclk = self.port.pin4
        
        self.int2 = self.port.pin7
        self.int1 = self.port.pin8
        GPIO.setmode(GPIO.BCM)  #
        GPIO.setup(self.int1,GPIO.IN)   #
        GPIO.setup(self.int2,GPIO.IN)   #

        # Register setting
        # ADXL362 range options
        self.SENSOR_RANGE_2G = 0 # +/-2 g
        self.SENSOR_RANGE_4G = 1 # +/-4 g
        self.SENSOR_RANGE_8G = 2 # +/-8 g
        # ADXL362 range options
        self.SENSOR_ODR_12_5_HZ= 0 # 12.5 Hz
        self.SENSOR_ODR_25_HZ  = 1 # 25 Hz
        self.SENSOR_ODR_50_HZ  = 2 # 50 Hz
        self.SENSOR_ODR_100_HZ = 3 # 100 Hz
        self.SENSOR_ODR_200_HZ = 4 # 200 Hz
        self.SENSOR_ODR_400_HZ = 5 # 400 Hz
        
        self.spi = spidev.SpiDev()
        self.__startSPI()

        self.softwareReset()
        # self.__spiWrite( 0x1F, 0x52)         # Software Reset
        time.sleep(0.01)
        self.setRange(1)                     # 4g
        self.setOutputRate(3)                # 100Hz
        self.setPowerMode(0x02)              # Measurement mode
       
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

    def __spiRead(self, Address):
        response = self.spi.xfer2([0x0B, Address, 0x00])
        return response[-1]

    def __spiRead16(self, Address):
        resp = self.spi.xfer2([0x0B, Address, 0x00, 0x00])
        # w = resp[3] 
        # w <<= 8
        # w |= resp[2]
        val_l = resp[2]
        val_h = resp[3] << 8
        w = (val_l + val_h) 

        return w

    def __spiWrite(self,address,value):
        self.spi.xfer2([0x0A, address, value])

    def __spiWrite16(self, address, value):
        highValue = value >> 8
        lowValue  = value & 0xFF
        self.spi.xfer2([0x0A, address, lowValue, highValue])
    
    def __unsigned2int(self, val):
        if val&(1<<15) != 0:
            val = val - (1<<16)
        return val

    def cleanup(self):
        self.__stopSPI()
        GPIO.cleanup()

    def setRange(self,newRange):
        # Range options: +/- 2,4,8 [unit: g]
        # 0: 2g
        # 1: 4g
        # 2: 8g
        if (newRange == self.SENSOR_RANGE_2G) or (newRange == self.SENSOR_RANGE_4G) or (newRange == self.SENSOR_RANGE_8G):
            oldFilterCtl = self.__spiRead(0x2C)
            time.sleep(0.01)
            newFilterCtl = oldFilterCtl & ~((0x3) << 6)
            newFilterCtl = newFilterCtl | (((newRange) & 0x03) << 6)
            self.__spiWrite(0x2C, newFilterCtl)
            time.sleep(0.01)
            self.selectedRange = (1 << newRange) * 2
            # print(self.selectedRange)
            return True
        else:
            return False

    def setOutputRate(self,outRate):
        # Rate Options:
        # 0: 12.5Hz,
        # 1: 25Hz,
        # 2: 50Hz,
        # 3: 100Hz,
        # 4: 200Hz,
        # 5: 400Hz
        if(outRate >=0)and(outRate <= 5):
            oldFilterCtl = self.__spiRead(0x2C) # ADXL362_REG_FILTER_CTL = 0x2C
            time.sleep(0.01)
            newFilterCtl = oldFilterCtl & ~0x7
            newFilterCtl = newFilterCtl | (0x7 & outRate)
            self.__spiWrite(0x2C, newFilterCtl)
            time.sleep(0.01)
            return True
        else:
            return False

    def setPowerMode(self,PowerMode):
        # Power Mode:
        # 0x0: standby
        # 0x2: measurement
        # self.spi.cshigh = True
        if (PowerMode == 0x00) or (PowerMode == 0x02):
            oldPowerCtl = self.__spiRead(0x2D) # ADXL362_REG_POWER_CTL = 0x2D
            time.sleep(0.01)
            newPowerCtl = oldPowerCtl & 0xFC
            newPowerCtl = newPowerCtl | (PowerMode & 0x03)
            self.__spiWrite(0x2D, newPowerCtl)
            # print(hex(newPowerCtl))
            # self.spi.cshigh = False
            time.sleep(0.01)
            return True
        else:
            return False

    def softwareReset(self):
        self.__spiWrite(0x1F, 0x52)         # Software Reset

    def getX(self):
        x = self.__spiRead16(0x0E)
        x = self.__unsigned2int(x)
        return x

    def getY(self):
        y = self.__spiRead16(0x10)
        y = self.__unsigned2int(y)
        return y

    def getZ(self):
        z = self.__spiRead16(0x12)
        z = self.__unsigned2int(z)
        return z

    def getTemperature(self):
        temp = self.__spiRead16(0x14)
        temp = self.__unsigned2int(temp)
        return temp

    def getRawXYZT(self):
        # return raw data
        x = self.getX()
        y = self.getY()
        z = self.getZ()
        t = self.getTemperature()
        return x, y, z, t

    def getXYZT(self):
        # return data in phisical unit
        x = self.getX()/(1000.0/(self.selectedRange/2.0))
        y = self.getY()/(1000.0/(self.selectedRange/2.0))
        z = self.getZ()/(1000.0/(self.selectedRange/2.0))
        t = self.getTemperature()*0.065
        return x, y, z, t

    def getDeviceID(self):
        # Get device ID. If device is connected properly, 0xAD will be returnd.
        DEVID_AD = self.__spiRead(0x00)
        return DEVID_AD

    def getPowerMode(self):
        # Get Power Mode.
        PowerMode = self.__spiRead(0x2d)
        return PowerMode
    
    def getSensorStatus(self):
        # Get status register (0x0B)
        StatusReg = self.__spiRead(0x0B)
        return StatusReg
