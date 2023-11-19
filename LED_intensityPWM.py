import machine
import utime

# Define the LED pin
led_pin = machine.Pin(15)
led_pwm = machine.PWM(led_pin)  # Create a PWM object

while True:
    # Increase LED intensity (fade in)
    for duty_cycle in range(0, 65535, 256):
        led_pwm.duty_u16(duty_cycle)
        utime.sleep(0.01)  # Adjust this delay for the desired fade-in speed
    
    utime.sleep(1)  # Pause at full intensity
    
    # Decrease LED intensity (fade out)
    for duty_cycle in range(65535, 0, -256):
        led_pwm.duty_u16(duty_cycle)
        utime.sleep(0.01)  # Adjust this delay for the desired fade-out speed
    
    utime.sleep(1)  # Pause at minimum intensity
