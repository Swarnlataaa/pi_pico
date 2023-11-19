import machine

# Define the button pin
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if not button.value():  # Check if the button is pressed (LOW)
        print("Button pressed!")
