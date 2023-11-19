import machine
import utime

# Define the LED pin
led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.toggle()  # Toggle the state of the LED
    utime.sleep(1)  # Pause for 1 second
