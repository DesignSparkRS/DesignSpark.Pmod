#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Display Hello, World! in bounding box.
"""

from DesignSpark.Pmod.HAT import createPmod
from luma.core.render import canvas
from luma.oled.device import ssd1331

if __name__ == '__main__':
    try:
        oled = createPmod('OLEDrgb','JA')
        device = oled.getDevice()
        
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((16,20), "Hello, World!", fill="white")
    
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        oled.cleanup()
