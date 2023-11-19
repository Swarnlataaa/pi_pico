import machine
import utime

# Initialize UART
uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

while True:
    # Send data via UART
    uart.write("Hello, UART!\n")

    # Receive and print data from UART
    if uart.any():
        received_data = uart.read()
        print("Received:", received_data.decode("utf-8"))  # Decode received bytes to a string

    utime.sleep(1)
