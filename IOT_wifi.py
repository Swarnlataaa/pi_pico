import machine
import network
import socket

# Set up UART for communication with the ESP8266
uart = machine.UART(0, baudrate=115200, tx=machine.Pin(0), rx=machine.Pin(1))

# Connect to Wi-Fi network
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("your-ssid", "your-password")  # Replace with your Wi-Fi SSID and password

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's IP address and port
server_ip = "your-server-ip"
server_port = 80  # Replace with your server's IP and port

# Connect to the server
s.connect((server_ip, server_port))

# Send data to the server
data = "Hello, IoT World!"
s.send(data.encode())

# Receive and print the server's response
response = s.recv(1024)
print("Server Response:", response.decode())

# Close the socket
s.close()
