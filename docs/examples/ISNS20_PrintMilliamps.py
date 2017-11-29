#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Read current and print out milliamps.
"""

from DesignSpark.Pmod.HAT import createPmod
import time

if __name__ == '__main__':
    
    isens = createPmod('ISNS20','JBA')
    time.sleep(0.1)
    
    try:
        while True:
            mA = isens.readMilliAmps()
            print(mA)
            time.sleep(0.8)
    except KeyboardInterrupt:
        pass
    finally:
        isens.cleanup()

