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

