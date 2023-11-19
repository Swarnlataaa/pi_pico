import machine
import utime

# Define the button and LED pins
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(15, machine.Pin.OUT)

# Define an interrupt handler function
def button_interrupt(pin):
    led.toggle()  # Toggle the state of the LED

# Configure an interrupt on the button pin for falling edge (button press)
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_interrupt)

while True:
    utime.sleep(1)  # Main loop can perform other tasks or sleep
