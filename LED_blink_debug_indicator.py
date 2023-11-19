import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)

while True:
    try:
        # Your code here

    except Exception as e:
        print("Error:", e)
        for _ in range(5):
            led.on()
            utime.sleep(0.2)
            led.off()
            utime.sleep(0.2)
