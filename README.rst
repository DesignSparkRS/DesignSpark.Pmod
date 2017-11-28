DesignSpark.Pmod
---------------- 

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/DesignSpark_Pmod_Library.jpg
   :alt: logo

Python library to support using Pmods with a Raspberry Pi via the DesignSpark Pmod HAT.

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/Pmod_HAT.jpg
   :alt: HAT

Features include:

* Simple interfaces for supported Pmods
* Checking that Pmod and port capabilities match
* Checking for port usage conflicts
* Usage examples

Supported Pmods
---------------

The following Pmods are currently supported:

* PmodAD1 12-bit ADC
* PmodHB3 2A H-bridge driver
* PmodISNS20 20A Current Sensor
* PmodMIC3 MEMS Microphone Module
* PmodOLEDrgb 96x64 RGB OLED Display :sup:`1`
* PmodTC1 K Type Thermocouple Module with Wire

:sup:`1` *Builds on the excellent luma.oled and luma.core libraries from Richard Hull and contributors.*

Installation
------------

DesignSpark.Pmod can be installed from PyPi using pip. See the documentation for details.


Documentation
-------------

Installation and API documentation, along with examples, can be found at:

http://designsparkpmod.readthedocs.io
