import machine
import utime
import struct

# Define the I2C bus
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=100000)  # I2C bus 0, SDA to GP0, SCL to GP1

# BME280 sensor address
sensor_address = 0x76  # Change to 0x77 if your sensor's address is different

# Read sensor data
i2c.writeto(sensor_address, b'\x88')  # Start reading data from the pressure sensor
data = i2c.readfrom(sensor_address, 6)

# Unpack the data
raw_data = struct.unpack('<hhh', data)

# Extract temperature, pressure, and humidity values
temperature = raw_data[0] / 100
pressure = raw_data[1] / 25600
humidity = raw_data[2] / 1024

print(f"Temperature: {temperature}°C")
print(f"Pressure: {pressure} hPa")
print(f"Humidity: {humidity}%")
