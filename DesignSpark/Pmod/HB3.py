# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Interface for PmodHB3 module.
"""

import RPi.GPIO as gpio

CAP = 'GPIO'
PHY = '1x6'
    
STOPPED = 0
FORWARD = 1
REVERSE = -1

class PmodHB3:

    def __init__(self, DSPMod6):
        
        self.port = DSPMod6
        
        self.dir = self.port.pin1
        self.en = self.port.pin2
        self.sA = self.port.pin3
        self.sB = self.port.pin4
        
        gpio.setmode(gpio.BCM)
        gpio.setup(self.dir, gpio.OUT)
        gpio.output(self.dir, gpio.LOW)
        gpio.setup(self.en, gpio.OUT)
        
        gpio.setup(self.sA, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(self.sB, gpio.IN, pull_up_down=gpio.PUD_UP)
        
        self.enable = gpio.PWM(self.en,100)
        self.enable.stop()
        
        self.direction = STOPPED 
        
    def forward(self,duty):
        if self.direction == STOPPED or self.direction == FORWARD:
            gpio.output(self.dir, gpio.HIGH)
            self.enable.start(0)
            
        else:
            self.enable.ChangeDutyCycle(0)
            self.enable.stop()
            gpio.output(self.dir, gpio.HIGH)
            self.enable.start(0)
            
        self.enable.ChangeDutyCycle(duty)    
        self.direction = FORWARD
            
    def reverse(self,duty):
        if self.direction == STOPPED or self.direction == REVERSE:
            gpio.output(self.dir, gpio.LOW)
            self.enable.start(0)
            
        else:
            self.enable.ChangeDutyCycle(0)
            self.enable.stop()
            gpio.output(self.dir, gpio.LOW)
            self.enable.start(0)
            
        self.enable.ChangeDutyCycle(duty)    
        self.direction = REVERSE
        
    def stop(self):
        self.enable.ChangeDutyCycle(0)
        self.enable.stop()
        self.direction = STOPPED
        
    def changeFrequency(self,freq):
        self.enable.ChangeFrequency(freq)
        
    def cleanup(self):
        gpio.cleanup();
        
