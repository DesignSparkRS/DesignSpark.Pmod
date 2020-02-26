"""
Interface for Pmod_KYPD
"""

import RPi.GPIO as GPIO

CAP = 'GPIO'
PHY = '2x6'

ROWNUM = 4; # 4 lines
COLNUM = 4; # 4 columms

# Declaration of the key of the keypad
DefaultKeyMap=[['1','2','3','A'],['4','5','6','B'],['7','8','9','C'],['0','F','E','D']]
keyMap=[['0','0','0','0'],['0','0','0','0'],['0','0','0','0'],['0','0','0','0']]


class PmodKYPD:
    def __init__(self,DSPmod12):
        # Assignement of pin for the keypad
        self.port = DSPmod12
        self.rowPins=[0,0,0,0]
        self.colPins=[0,0,0,0]
        self.colPins[0] = self.port.pin4
        self.colPins[1] = self.port.pin3
        self.colPins[2] = self.port.pin2
        self.colPins[3] = self.port.pin1
        self.rowPins[0] = self.port.pin10
        self.rowPins[1] = self.port.pin9
        self.rowPins[2] = self.port.pin8
        self.rowPins[3] = self.port.pin7
        GPIO.setmode(GPIO.BCM)  #
        for i in range(COLNUM):
            GPIO.setup(self.colPins[i],GPIO.OUT) #
        for i in range(ROWNUM):
            GPIO.setup(self.rowPins[i],GPIO.IN)  #
        self.setKeyMapDefault() # Default key map

    def cleanup(self):
        GPIO.cleanup()

    def setKeyMapDefault(self):
        for i in range(COLNUM):
            for j in range(ROWNUM):
                keyMap[i][j] = DefaultKeyMap[i][j]

    def setKeyMap(self,UsrKeyMap):
        # Set User KeyMap
        for i in range(COLNUM):
            for j in range(ROWNUM):
                keyMap[i][j] = UsrKeyMap[i][j]

    def getKey(self):
        # initialize col to be high
        for i in range(COLNUM):
            GPIO.output(self.colPins[i], GPIO.HIGH)
        for i in range(COLNUM):
            # start to scan colPins[i]
            GPIO.output(self.colPins[i],GPIO.LOW)
            for j in range(ROWNUM):
                # row[j]
                # print(i,j)
                if(GPIO.input(self.rowPins[j])== 0):
                    return keyMap[j][i]
                # stop scanning colPins[i]
            GPIO.output(self.colPins[i],GPIO.HIGH)

    def getColRow(self):
        # initialize col to be high
        for i in range(COLNUM):
            GPIO.output(self.colPins[i], GPIO.HIGH)
        for i in range(COLNUM):
            # start to scan colPins[i]
            GPIO.output(self.colPins[i],GPIO.LOW)
            for j in range(ROWNUM):
                # row[j]
                if GPIO.input(self.rowPins[j])== 0:
                    return j<<2|i
                # stop scanning colPins[i]
            GPIO.output(self.colPins[i],GPIO.HIGH)
            
    def getKeyMap(self):
        return keyMap
