# -*- coding: utf-8 -*-
# Copyright (c) 2019 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Interface for Pmod_LS1
"""

import RPi.GPIO as GPIO
CAP = 'GPIO'
PHY = '1x6'

class PmodLS1:
    def __init__(self,DSPmod6):
        # GPIO setup
        self.port = DSPmod6
        self.SNS1 = self.port.pin1
        self.SNS2 = self.port.pin2
        self.SNS3 = self.port.pin3
        self.SNS4 = self.port.pin4
        GPIO.setmode(GPIO.BCM)  #
        GPIO.setup(self.SNS1,GPIO.IN)   #
        GPIO.setup(self.SNS2,GPIO.IN)   #
        GPIO.setup(self.SNS3,GPIO.IN)   #
        GPIO.setup(self.SNS4,GPIO.IN)   #

    def cleanup(self):
        GPIO.cleanup()

    def GetSensorPin(self,Sensor):
        # returns phisical GPIO Pin assignment
        if Sensor == 1:
            return self.SNS1
        elif Sensor == 2:
            return self.SNS2
        elif Sensor == 3:
            return self.SNS3
        elif Sensor == 4:
            return self.SNS4
        else:
            return None
    def GetStatus(self,SNS):
        # return sensor status
        sensorPin = self.GetSensorPin(SNS)
        return GPIO.input(sensorPin)
    def GetAllStatus(self):
        # return all sensor status
        return self.GetStatus(1)<<0 | self.GetStatus(2)<<1 | self.GetStatus(3)<<2 | self.GetStatus(4)<<3
