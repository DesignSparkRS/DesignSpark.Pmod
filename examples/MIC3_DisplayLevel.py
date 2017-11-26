#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

from DesignSpark.Pmod.HAT import createPmod
import time

s = ':'
lut = [s]
for i in range(128):
    s+=':'
    lut.append(s)

if __name__ == '__main__':
    
    mic = createPmod('PmodMIC3','JBA')
    time.sleep(0.1)
    
    try:
        while True:
            int = mic.readIntegerValue()
            #print(int)
            print(lut[int>>5])
            snd = mic.readPhysicalValue()
            #print(snd)
            
            #time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        mic.cleanup()

