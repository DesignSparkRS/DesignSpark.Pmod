# -*- coding: utf-8 -*-
# Copyright (c) 2019 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Interface for Pmod_SWT
"""

import RPi.GPIO as GPIO
CAP = 'GPIO'
PHY = '1x6'

class PmodSWT:
    def __init__(self,DSPmod6):
        # GPIO setup
        self.port = DSPmod6
        self.SWT1 = self.port.pin1
        self.SWT2 = self.port.pin2
        self.SWT3 = self.port.pin3
        self.SWT4 = self.port.pin4
        GPIO.setmode(GPIO.BCM)  #
        GPIO.setup(self.SWT1,GPIO.IN)   #
        GPIO.setup(self.SWT2,GPIO.IN)   #
        GPIO.setup(self.SWT3,GPIO.IN)   #
        GPIO.setup(self.SWT4,GPIO.IN)   #

    def cleanup(self):
        GPIO.cleanup()

    def GetSwitchPin(self,SW):
        # returns phisical GPIO Pin assignment
        if SW == 1:
            return self.SWT1
        elif SW == 2:
            return self.SWT2
        elif SW == 3:
            return self.SWT3
        elif SW == 4:
            return self.SWT4
        else:
            return None
    def GetStatus(self,SW):
        # returns switch status
        switchPin = self.GetSwitchPin(SW)
        return GPIO.input(switchPin)
    def AllOn(self):
        # returns "True" if all pins are ON
        return GPIO.input(GetSwitchPin(1)) and GPIO.input(GetSwitchPin(2)) and GPIO.input(GetSwitchPin(3)) and GPIO.input(GetSwitchPin(4))
    def AllOff(self):
        # returns "True" if all pins are OFF
        return (not GPIO.input(GetSwitchPin(1))) and (not GPIO.input(GetSwitchPin(2))) and (not GPIO.input(GetSwitchPin(3))) and (not GPIO.input(GetSwitchPin(4)))
