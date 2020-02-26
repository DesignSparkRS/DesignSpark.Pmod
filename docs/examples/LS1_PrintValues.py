#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Read Sensor status
"""

from DesignSpark.Pmod.HAT import createPmod
import time

if __name__ == '__main__':
    
    LS1 = createPmod('LS1','JAA')
    time.sleep(0.1)
    
    try:
        while True:
            print(LS1.GetAllStatus())
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        LS1.cleanup()

