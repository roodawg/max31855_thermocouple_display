# Raspberry Pi Thermocouple Display

A Python project for reading K-type thermocouple temperatures using a MAX31855 amplifier and displaying the data on an SSD1306 OLED screen.

## Features

- Real-time temperature monitoring in Fahrenheit
- Timestamp display with date and time
- Error handling for thermocouple faults
- 5-second update intervals
- Clean OLED display interface

## Hardware Requirements

- Raspberry Pi 5 (or compatible)
- Adafruit MAX31855 Thermocouple Amplifier
- K-type Thermocouple
- 0.96" SSD1306 OLED Display (I2C)
- Jumper wires

## Wiring Diagram

### MAX31855 Thermocouple Amplifier (SPI)
| MAX31855 Pin | Raspberry Pi Pin | GPIO |
|--------------|------------------|------|
| VIN          | Pin 1            | 3.3V |
| 3Vo          | Not connected    | -    |
| GND          | Pin 6            | GND  |
| DO           | Pin 35           | GPIO19 |
| CS           | Pin 24           | GPIO8  |
| CLK          | Pin 12           | GPIO18 |

### SSD1306 OLED Display (I2C)
| OLED Pin | Raspberry Pi Pin | GPIO |
|----------|------------------|------|
| VCC      | Pin 17           | 3.3V |
| GND      | Pin 20           | GND  |
| SDA      | Pin 3            | GPIO2 |
| SCL      | Pin 5            | GPIO3 |

**Note:** Connect your K-type thermocouple to the T+ and T- terminals on the MAX31855 board.

## Software Setup

1. **Enable I2C and SPI interfaces:**
   ```bash
   sudo raspi-config
   ```
   - Navigate to "Interfacing Options" → "I2C" → "Yes"
   - Navigate to "Interfacing Options" → "SPI" → "Yes"
   - Reboot when prompted

2. **Install required Python libraries:**
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install adafruit-circuitpython-max31855
   pip3 install adafruit-circuitpython-ssd1306
   pip3 install pillow
   ```

3. **Verify I2C connection:**
   ```bash
   sudo i2cdetect -y 1
   ```
   Your OLED should appear at address 0x3C or 0x3D.

## Usage

1. **Make the script executable:**
   ```bash
   chmod +x thermocouple_display.py
   ```

2. **Run the application:**
   ```bash
   python3 thermocouple_display.py
   ```

3. **Stop the application:**
   Press `Ctrl+C` to exit gracefully.

## Display Information

The OLED screen shows:
- **Temperature** in Fahrenheit (large font)
- **Current time** (HH:MM:SS)
- **Current date** (MM/DD/YYYY)
- **Error messages** for thermocouple faults

## Troubleshooting

### Permission Errors
Add your user to the SPI group:
```bash
sudo usermod -a -G spi $USER
```
Then log out and back in.

### OLED Not Displaying
- Check I2C connections
- Verify I2C is enabled in raspi-config
- Run `sudo i2cdetect -y 1` to confirm device detection

### Erratic Temperature Readings
- Ensure secure thermocouple connections to T+ and T- terminals
- Check for loose jumper wire connections
- Verify thermocouple is not damaged

## Error Codes

| Display | Meaning |
|---------|---------|
| TC Open | Thermocouple not connected or broken |
| TC Short | Thermocouple short circuit |
| TC Error | General thermocouple error |

## License

This project is open source and available under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
