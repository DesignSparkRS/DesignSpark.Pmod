Pmod Information
----------------

Details of currently supported Pmods can be found below.

ACL2
""""

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/PmodACL2-oblique.jpg
   :alt: PmodACL2

The Pmod ACL2 is a 3-axis MEMS accelerometer powered by the Analog Devices ADXL362. By communicating with the chip via the SPI protocol, users may receive up to 12 bits of resolution for each axis of acceleration. Additionally, this module offers freefall detection as well as power saving features through its motion activated sleep and wake modes. 

Features:

* 3-axis MEMS accelerometer
* Up to 12 bits of resolution per axis
* User-selectable resolution
* Activity/inactivity monitoring
* Low current consumption at <2 μA at 100Hz
* Free-fall detection

AD1
"""

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/PmodAD1-oblique.jpg
   :alt: PmodAD1

The Digilent Pmod AD1 (Revision G) is a two channel 12-bit analog-to-digital converter that features Analog Devices' AD7476A. With a sampling rate of up to 1 million samples per second, this Pmod™ is capable of excelling in even the most demanding audio applications. 

Features:

* Two channel 12-bit analog-to-digital converter
* Simultaneous A/D conversion at up to one MSa per channel
* Two 2-pole Sallen-Key anti-alias filters
* Small PCB size for flexible designs 0.95 in × 0.8 in (2.4 cm × 2.0 cm)

.. note::
   Only a single channel (A1) is supported at present due to the
   way that SPI is configured.

GPS
"""

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/PmodGPS-oblique.jpg
   :alt: PmodGPS

The Pmod GPS can provide satellite-positioning accuracy to any embedded system. By communicating through UART with the GlobalTop FGPMMOPA6H GPS module, users may benefit from the 3-meter accuracy for any long term traveling. 

Features:

* Ultra-sensitive GPS module (-165 dBm)
* Add 3m 2D satellite positioning accuracy to any embedded system
* Low power consumption
* Up to 10Hz update rate
* NMEA (default) and RTCM protocols available

HB3
"""

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/PmodHB3-oblique.jpg
   :alt: PmodHB3

The Pmod HB3 utilizes a full H-Bridge circuit to allow users to drive DC motors from the system board. Two external pins are provided on the Pmod for sensor feedback on the DC motor, if desired. 

Features:

* 2A H-bridge circuit
* Drive a DC motor with operation voltage up to 12V
* Screw terminal blocks for connection to the motor
* Separate header for external motor feedback

ISNS20
""""""

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/PmodISNS20-oblique.jpg
   :alt: PmodISNS20

The Digilent Pmod ISNS20 (Revision A) is a small current sense module with a digital SPI interface. The board combines an Allegro ACS722 Hall Effect current sensor with a 12-bit analog-to-digital converter from Texas Instruments. The Pmod ISNS20 is quick, accurate, and easy to use for a variety of applications. 

Features:

* High accuracy current sensor
* Measure current with 120Hz/20kHz/80kHz jumper selections
* ±20A DC or AC input
* Accurate to within ±2%
* 12-bit ADC

KYPD
""""

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/PmodKYPD-oblique.jpg
   :alt: PmodKYPD

The Pmod KYPD is a 16-button keypad arranged in a hexidecimal format (0-F). By digitally driving a column line to a logic low level and digitally reading each of the rows, users can determine which button is currently pressed.

Features:

* 16 momentary push-buttons
* Can detect simultaneous button presses
* Isolated rows and columns

LS1
"""

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/PmodLS1-oblique.jpg
   :alt: PmodLS1

The Digilent Pmod LS1 allows users to receive signals from multiple optical sensors, such as the popular combination of an IR LED with an IR sensor used in line-following robots.

Features:

* Infrared light detector with on-board sensitivity adjustment
* Interface with up to four reflective or transmissive photo detectors
* Works with Digilent IR Proximity Sensor

MIC3
""""

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/PmodMIC3-oblique.jpg
   :alt: PmodMIC3

The Digilent Pmod MIC3 (Revision A) is small microphone module with a digital interface. With a Knowles Acoustics SPA2410LR5H-B MEMs microphone and Texas Instrument's ADCS7476 12-bit Analog-to-Digital Converter, you can capture your audio inputs with ease. 

Features:

* MEMS Microphone module with digital interface
* Transform audio inputs with 12-bit A/D converter
* Adjust incoming volume with on-board potentiometer
* Up to 1 MSPS of data

OLEDrgb
"""""""

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/PmodOLEDrgb-oblique.jpg
   :alt: PmodOLEDrgb

The Digilent Pmod OLEDrgb (Revision B) is an organic RGB LED module with a 96×64 pixel display capable of 16-bit color resolution. 

Features:

* 96×64 pixel RGB OLED screen
* 0.8“ x 0.5” graphical display
* 16-bit color resolution
* Two low-power display shutdown modes

SWT
"""

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/PmodSWT-oblique.jpg
   :alt: PmodSWT

The Pmod SWT provides users with four slide switches for up to 16 different binary logic inputs to for the attached system board.

Features:

* 4 slide switches
* Add user input to host board or project
* Static binary logic input

TC1
"""

.. image:: https://raw.githubusercontent.com/designsparkrs/DesignSpark.Pmod/master/docs/images/PmodTC1-oblique.jpg
   :alt: PmodTC1

The Digilent Pmod TC1 (Revision A) is a cold-junction thermocouple-to-digital converter module designed for a classic K-Type thermocouple wire. With Maxim Integrated's MAX31855, this module reports the measured temperature in 14-bits with 0.25°C resolution. 

Features:

* K-type thermocouple-to-digital converter
* Wide temperature range of -73°C to 482°C with provided wire
* ±2°C accuracy from -200°C to 700°C
* 14-bit with 0.25°C resolution
* Cold-junction temperature compensation

