#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Key Pad
"""

from DesignSpark.Pmod.HAT import createPmod
import time

if __name__ == '__main__':
    
    KYPD = createPmod('KYPD','JA')
    time.sleep(0.1)
    
    try:
        # set default key map
        KYPD.setKeyMapDefault()
        
        # set User Key Map
        # keyMap=[['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','P']]
        # KYPD.setKeyMap(keyMap)
        
        # get keyMap
        print(KYPD.getKeyMap())
        while True:
            # print(KYPD.getColRow())
            print(KYPD.getKey())
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        KYPD.cleanup()

