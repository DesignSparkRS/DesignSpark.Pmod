#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Print the celsius reading out.
"""

from DesignSpark.Pmod.HAT import createPmod
import time

if __name__ == '__main__':
    
    therm = createPmod('PmodTC1','JBA')
    time.sleep(0.1)
    
    try:
        while True:
            cel = therm.readCelcius()
            print(cel)
            #intn = therm.readInternal()
            #print(intn)
            time.sleep(0.8)
    except KeyboardInterrupt:
        pass
    finally:
        therm.cleanup()

