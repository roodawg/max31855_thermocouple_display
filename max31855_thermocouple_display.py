#!/usr/bin/env python3
"""
Raspberry Pi 5 Thermocouple Display
Reads K-type thermocouple via MAX31855 and displays on SSD1306 OLED
Updates every 5 seconds with temperature, timestamp, and units
"""

import time
import board
import digitalio
import busio
from datetime import datetime
import adafruit_max31855
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# SPI setup for MAX31855
spi = busio.SPI(board.D18, MOSI=board.D19, MISO=board.D19)  # SCK, MOSI, MISO
cs = digitalio.DigitalInOut(board.D8)  # Chip select
max31855 = adafruit_max31855.MAX31855(spi, cs)

# Hardware I2C setup for SSD1306
i2c = board.I2C()  # Hardware I2C on GPIO2 (SDA) and GPIO3 (SCL)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear display
oled.fill(0)
oled.show()

# Create blank image for drawing
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Try to load a font, fall back to default if not available
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
except:
    font = ImageFont.load_default()
    font_large = ImageFont.load_default()

def display_temperature(temp_f, timestamp):
    """Display temperature and timestamp on OLED"""
    # Clear the image
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    
    # Display temperature (large font)
    temp_text = f"{temp_f:.1f}°F"
    draw.text((10, 10), temp_text, font=font_large, fill=255)
    
    # Display "Temperature" label
    draw.text((10, 30), "Temperature", font=font, fill=255)
    
    # Display timestamp
    time_text = timestamp.strftime("%H:%M:%S")
    draw.text((10, 45), time_text, font=font, fill=255)
    
    # Display date
    date_text = timestamp.strftime("%m/%d/%Y")
    draw.text((10, 55), date_text, font=font, fill=255)
    
    # Display the image on OLED
    oled.image(image)
    oled.show()

def display_error(error_msg):
    """Display error message on OLED"""
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    draw.text((5, 20), "ERROR:", font=font_large, fill=255)
    draw.text((5, 40), error_msg, font=font, fill=255)
    oled.image(image)
    oled.show()

def main():
    """Main loop"""
    print("Starting thermocouple display...")
    print("Press Ctrl+C to exit")
    
    try:
        while True:
            try:
                # Read temperature from MAX31855
                temp_c = max31855.temperature
                temp_f = temp_c * 9/5 + 32  # Convert to Fahrenheit
                
                # Get current timestamp
                timestamp = datetime.now()
                
                # Display on OLED
                display_temperature(temp_f, timestamp)
                
                # Print to console for debugging
                print(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} - Temperature: {temp_f:.1f}°F ({temp_c:.1f}°C)")
                
                # Wait 5 seconds before next reading
                time.sleep(5)
                
            except RuntimeError as e:
                # Handle MAX31855 errors (like disconnected thermocouple)
                error_msg = str(e)
                print(f"Sensor error: {error_msg}")
                
                if "open circuit" in error_msg.lower():
                    display_error("TC Open")
                elif "short" in error_msg.lower():
                    display_error("TC Short")
                else:
                    display_error("TC Error")
                
                time.sleep(5)
                
    except KeyboardInterrupt:
        print("\nExiting...")
        # Clear display before exit
        oled.fill(0)
        oled.show()

if __name__ == "__main__":
    main()
