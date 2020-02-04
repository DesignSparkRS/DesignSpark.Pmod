#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Read GPS and print position, speed, and GPS time
"""

from DesignSpark.Pmod.HAT import createPmod
import time
# import webbrowser

if __name__ == '__main__':
    
    GPS = createPmod('GPS','JCA') # UART port is only avairable on JCA
    time.sleep(0.1)
    
    try:
        while True:
            """
            LINE = GPS.getGPSLine()
            print(LINE)
            time.sleep(0.5)
            """
            GPS.gpsUpdate()
            print(GPS.getGPSPosData())
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        #day,month,year,hour,minute,sec,LatDeg,LogDeg,PDOP = GPS.getGPSPosData()
        #url = "https://google.com/maps?q={},{}"
        #url = url.format(LatDeg,LogDeg)
        GPS.cleanup()
        #webbrowser.open(url)
