# max31855_thermocouple_display
Reads K-type thermocouple via MAX31855 and displays on OLED

### Hardware Connections to a Raspiberry Pi 5
MAX31855 Thermocouple Amplifier (SPI)

**VIN** → Pi Pin 1 (3.3V)

**3Vo** → Leave unconnected

**GND** → Pi Pin 6 (Ground)

**DO** → Pi Pin 35 (GPIO19)

**CS** → Pi Pin 24 (GPIO8)

**CLK** → Pi Pin 12 (GPIO18)

### SSD1306 OLED Display (Hardware I2C) - Already Connected

**VCC** → Pi Pin 17 (3.3V)

**GND** → Pi Pin 20 (Ground)

**SDA** → Pi Pin 3 (GPIO2)

**SCL** → Pi Pin 5 (GPIO3) 
