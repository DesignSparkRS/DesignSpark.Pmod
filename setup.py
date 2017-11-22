# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

from setuptools import setup

setup(
    name = 'DesignSparkPmod',
    version = '0.1',
    packages = ['DesignSparkPmod'],
    install_requires = ['future','RPI.GPIO','spidev','luma.oled','luma.core'],
    license = 'MIT License',
    long_description = open('README.rst').read(),
    )
