import machine
import utime
from machine import I2C

# Initialize I2C
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)  # I2C bus 0, SDA to GP0, SCL to GP1

# BMP180 sensor address
sensor_address = 0x77

while True:
    # Read temperature from the BMP180 sensor
    i2c.writeto(sensor_address, b'\x2E')  # Start temperature measurement
    utime.sleep_ms(5)  # Wait for measurement to complete
    temperature_data = i2c.readfrom(sensor_address, 2)  # Read 2 bytes
    temperature_raw = temperature_data[0] << 8 | temperature_data[1]
    temperature = temperature_raw / 10.0  # Convert raw value to temperature (in degrees Celsius)
    print(f"Temperature: {temperature:.2f}°C")
    utime.sleep(1)
