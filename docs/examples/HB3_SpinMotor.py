#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Spin motor forwards then backwards.
Ramp speed up and then down in forward direction.
Ramp speed up and then down in reverse direction.
"""

from DesignSpark.Pmod.HAT import createPmod
import time

if __name__ == '__main__':

    motor = createPmod('HB3','JAA')

    try:
        while True:
        
            print('fwd')
            motor.forward(20)
            time.sleep(2)
            motor.stop()
            time.sleep(2)
            print('rev')
            motor.reverse(20)
            time.sleep(1)
            motor.stop()
            time.sleep(2)
            
            
            print ('ramp up fwd')
            for i in range(100):
                motor.forward(i)
                time.sleep(.1)
            
            print ('ramp down fwd')
            for i in range(100):
                motor.forward(100-i)
                time.sleep(.1)
                
            motor.stop()
            time.sleep(2)
            
            print ('ramp up rev')
            for i in range(100):
                motor.reverse(i)
                time.sleep(.1)
            
            print ('ramp down rev')
            for i in range(100):
                motor.reverse(100-i)
                time.sleep(.1)
        
    except KeyboardInterrupt:
        pass
    
    finally:
        motor.cleanup() 
    
    
    
