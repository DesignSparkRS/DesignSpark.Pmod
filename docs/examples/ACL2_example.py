#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Read current and print out milliamps.
"""

from DesignSpark.Pmod.HAT import createPmod
import time

if __name__ == '__main__':
    
    ACL2 = createPmod('ACL2','JB')
    time.sleep(0.1)
    
    # print(hex(ACL2.getDeviceID())) # Device test. 0xAD will be expected.
    # ACL2.setRange(ACL2.SENSOR_RANGE_8G) # default setting: +/- 4G
    # maxz = 0

    try:
        while True:
            x,y,z,t = ACL2.getXYZT()
            print(x,y,z,t)
            time.sleep(0.8)
            # if maxz < z:
            #     maxz = z
    except KeyboardInterrupt:
        pass
    finally:
        ACL2.cleanup()
        # print(maxz)
