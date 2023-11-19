import machine

# Define the LED pin
led = machine.Pin(15, machine.Pin.OUT)

# Define a timer object
timer = machine.Timer()

# Define a timer callback function
def timer_callback(timer):
    led.toggle()  # Toggle the state of the LED

# Configure the timer to trigger the callback every 1 second (1000 ms)
timer.init(period=1000, mode=machine.Timer.PERIODIC, callback=timer_callback)

while True:
    # Main loop can perform other tasks while the timer handles LED toggling
    pass
