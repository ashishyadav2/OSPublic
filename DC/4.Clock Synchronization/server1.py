# https://www.geeksforgeeks.org/cristians-algorithm/
import socket
from datetime import datetime
# Clock Server

# Define the IP address and port number for Server 1
SERVER1_IP = '127.0.0.1'
SERVER1_PORT = 6000

# Create a socket object
server1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port number
server1_socket.bind((SERVER1_IP, SERVER1_PORT))

# Listen for incoming connections
server1_socket.listen(1)

print("Server 1 is listening...")

# Accept incoming connection
client_socket, client_address = server1_socket.accept()
print(f"Connection from {client_address} has been established.")

# Get the current time
current_time = datetime.now()

# Send "hello" message along with current time to the client
message = f"Hello from Server 1.{current_time}"
client_socket.sendall(message.encode())

# Close the connection
client_socket.close()
server1_socket.close()
