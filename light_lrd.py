import machine
import utime

# Define the LDR pin
ldr_pin = machine.ADC(26)  # Use GP26 as the ADC pin

while True:
    ldr_value = ldr_pin.read_u16()  # Read the analog sensor value
    voltage = (ldr_value / 65535) * 3.3  # Convert to voltage (assuming 3.3V reference)
    print(f"LDR Value: {ldr_value}, Voltage: {voltage:.2f}V")
    utime.sleep(1)
