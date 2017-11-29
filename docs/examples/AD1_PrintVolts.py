#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Read ADC channel A1 and print volts out.
"""

from DesignSpark.Pmod.HAT import createPmod
import time

if __name__ == '__main__':
    adc = createPmod('AD1','JBA')
    time.sleep(0.1)
    
    try:
        while True:
            volts = adc.readA1Volts()
            print(volts)
            #val = adc.readA1()
            #print(val)
            time.sleep(0.8)
    except KeyboardInterrupt:
        pass
    finally:
        adc.cleanup()
