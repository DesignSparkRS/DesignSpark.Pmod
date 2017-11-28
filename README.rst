DesignSpark.Pmod
---------------- 

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/DesignSpark_Pmod_Library.jpg
   :alt: logo

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/Pmod_HAT.jpg
   :alt: HAT

**Python library to support using Pmods with a Raspberry Pi and the DesignSpark Pmod HAT.**

Features include:

* Simple interfaces for supported Pmods
* Checking that Pmod and port capabilities match
* Checking for port usage conflicts
* Usage examples

Supported Pmods
---------------

The following Pmods are currently supported:

* `PmodAD1 <https://uk.rs-online.com/web/p/processor-microcontroller-development-kits/1346443/>`_ 12-bit ADC
* `PmodHB3 <https://uk.rs-online.com/web/p/processor-microcontroller-development-kits/1346445/>`_ 2A H-bridge driver
* `PmodISNS20 <https://uk.rs-online.com/web/p/processor-microcontroller-development-kits/1368069/>`_ 20A Current Sensor
* `PmodMIC3 <https://uk.rs-online.com/web/p/processor-microcontroller-development-kits/1346475/>`_ MEMS Microphone Module
* `PmodOLEDrgb <https://uk.rs-online.com/web/p/processor-microcontroller-development-kits/1346481/>`_ 96x64 RGB OLED Display :sup:`1`
* `PmodTC1 <https://uk.rs-online.com/web/p/processor-microcontroller-development-kits/1346476/>`_ K Type Thermocouple Module with Wire

:sup:`1` *Builds on the excellent luma.oled and luma.core libraries from Richard Hull and contributors.*

Installation
------------

DesignSpark.Pmod can be installed from PyPi using pip. See the documentation for details.


Documentation
-------------

Installation and API documentation, along with examples, can be found at:

http://designspark-pmod.readthedocs.io

For Pmod HAT documentation, including the reference manual and schematic, see:

https://reference.digilentinc.com/reference/add-ons/pmod-hat/start
