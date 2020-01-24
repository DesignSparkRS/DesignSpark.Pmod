Installation
------------

This guide assumes that you are running Raspbian Stretch.

First enable SPI:

.. code-block:: console

    pi@raspberrypi:~$ sudo raspi-config

Selecting:

* Option 5 - Interfacing
* P4 - SPI
* Enable → YES

* P6 - Serial
* Would you like a login shell to be accessible over serial? → No
* Would you like the serial port hardware to be enabled? → Yes

Then exit raspi-config.

Next update the package lists:

.. code-block:: console

    pi@raspberrypi:~$ sudo apt-get update

Then install the Raspbian dependencies:

.. code-block:: console

    pi@raspberrypi:~$ sudo apt-get install python-pip python-dev libfreetype6-dev libjpeg-dev build-essential

Finally, install DesignSpark.Pmod and dependencies from PyPi:

.. code-block:: console

    pi@raspberrypi:~$ sudo pip install pyserial

.. code-block:: console

    pi@raspberrypi:~$ sudo pip install designspark.pmod
