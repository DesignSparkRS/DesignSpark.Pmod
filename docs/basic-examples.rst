Basic Examples
==============

AD1
---

12-bit analog-to-digital converter.

Print volts out to the terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Read ADC channel A1, print the voltage measured out to the
terminal, sleep for 0.8s and repeat.

.. literalinclude:: examples/AD1_PrintVolts.py

.. admonition:: Requirements

   * PmodAD1 module connected to port JBA
   * A voltage source connected to ADC channel A1

HB3
---

2A H-bridge circuit for DC motor drive up to 12V.

Spin motor
^^^^^^^^^^

This example:

1. Spins the motor forwards for 20 seconds
2. Commands the motor to stop and pauses for 2 seconds
3. Spins the motor in reverse for 20 seconds
4. Commands the motor to stop and pauses for 2 seconds
5. Ramps up the speed across 100 steps in the forward direction
6. Ramps down the speed across 100 steps in the forward direction
7. Ramps up speed across 100 steps in the reverse direction
8. Ramps down the speed across 100 steps in the reverse direction
9. Loops back to (1)

.. literalinclude:: examples/HB3_SpinMotor.py

.. admonition:: Requirements

   * PmodHB3 module connected to port JAA
   * DC motor
   * Motor power supply

ISNS20
------

±20A DC or AC input, high accuracy current sensor. 

Print milliamps out to the terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Read the current sense module, print the milliamps out to the
terminal, sleep for 0.8s and repeat.

.. literalinclude:: examples/ISNS20_PrintMilliamps.py

.. admonition:: Requirements

   * PmodISNS20 module connected to port JBA
   * Suitable current source, e.g. a power supply and load

MIC3
----

Knowles Acoustics SPA2410LR5H-B MEMs microphone and Texas Instrument’s ADCS7476
12-bit Analog-to-Digital Converter.

Display mic level
^^^^^^^^^^^^^^^^^

Print a continous sound level reading out to the terminal.

.. literalinclude:: examples/MIC3_DisplayLevel.py

.. admonition:: Requirements

   * PmodMIC3 module connected to port JBA

OLEDrgb
-------

Organic RGB LED module with a 96×64 pixel display capable of 16-bit color
resolution.

Display text in a bounding box
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Display the text "Hello, World!" in a bounding box.

.. literalinclude:: examples/OLEDrgb_TextBox.py

Luma.Core & Luma.OLED API:
:py:class:`luma.core.render.canvas`,
:py:class:`luma.oled.device.ssd1331`.

.. admonition:: Requirements

   * PmodOLEDrgb connected to port JA

PmodTC1
-------

A cold-junction thermocouple-to-digital converter module designed for a classic
K-Type thermocouple wire. Features a temperature range of -73°C to 482°C with
provided wire.

Print celsius out to the terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Print the celsius reading out to the terminal, sleep for 0.8s and repeat.

.. literalinclude:: examples/TC1_PrintCelsius.py

.. admonition:: Requirements

   * PmodTC1 module connected to port JBA

PmodACL2
-------

A 3-axis MEMS accelerometer module. Features the Analog Devices ADXL362 device 
with Measurement ranges ±2g, ±4g, ±8g. Up to 12-bit resolution on each axis.

Print axis out to the terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Print the axis reading out to the terminal, sleep for 0.5s and repeat.

.. literalinclude:: examples/ACL2_PrintValues.py

.. admonition:: Requirements

   * PmodACL2 module connected to port JB

PmodGPS
-------

A GlobalTop FGPMMOPA6H GPS antenna module to receive position data from GPS satellites.

Print date, time, and location out to the terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Print the date, time, and location reading out to the terminal, sleep for 0.5s and repeat.

.. literalinclude:: examples/GPS_PrintValues.py

.. admonition:: Requirements

   * PmodGPS module connected to port JCA
   * View of the sky or external antenna connected to the module
   * ...takes time to obtain a fix and get the data

PmodSWT
-------

Four slides switches for up to 16x different binary logic inputs.

Print switches out to the terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Read the four switches and print out to the terminal, sleep for 0.5s and repeat.

.. literalinclude:: examples/SWT_PrintValues.py

.. admonition:: Requirements

   * PmodSWT module connected to port JAA

PmodLS1
-------

A line follower robot interface system board.

Print received signals from optical sensor out to the terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Print the signals from multiple optical sensors out to the terminal, sleep for 0.5s and repeat.

.. literalinclude:: examples/LS1_PrintValues.py

.. admonition:: Requirements

   * PmodLS1 module connected to port JAA

PmodKYPD
--------

A 16-button keypad.

Print character out to the terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Print the key presses out to the terminal, sleep for 0.5s and repeat.

.. literalinclude:: examples/KYPD_PrintValue.py

.. admonition:: Requirements

   * PmodKYPD module connected to port JA
