import machine
import onewire
import ds18x20
import utime

# Initialize the OneWire bus and DS18B20 sensor
ow = onewire.OneWire(machine.Pin(4))
temp_sensor = ds18x20.DS18X20(ow)

# Scan for DS18B20 devices
roms = temp_sensor.scan()

while True:
    # Request temperature conversion for all sensors
    temp_sensor.convert_temp()
    utime.sleep_ms(750)

    for rom in roms:
        temperature = temp_sensor.read_temp(rom)
        print("Sensor", rom, "Temperature:", temperature, "°C")

    utime.sleep(5)  # Read and print temperature every 5 seconds
