import machine
import utime

# Define the analog pin
analog_pin = machine.ADC(26)

while True:
    sensor_value = analog_pin.read_u16()  # Read the analog sensor value
    voltage = (sensor_value / 65535) * 3.3  # Convert to voltage (assuming 3.3V reference)
    print(f"Sensor Value: {sensor_value}, Voltage: {voltage:.2f}V")
    utime.sleep(1)
