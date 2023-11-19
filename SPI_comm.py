import machine
import utime
import ssd1306  # Import the SSD1306 library

# Initialize SPI
spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0)
oled = ssd1306.SSD1306_SPI(128, 64, spi, machine.Pin(15), machine.Pin(12), machine.Pin(13))

while True:
    # Clear the display
    oled.fill(0)
    # Display "Hello, World!" at (0, 0)
    oled.text("Hello, World!", 0, 0, 1)
    # Refresh the display
    oled.show()
    utime.sleep(2)
