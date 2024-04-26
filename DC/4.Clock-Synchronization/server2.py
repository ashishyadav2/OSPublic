# https://www.geeksforgeeks.org/cristians-algorithm/
import socket
from datetime import datetime
# Client

# Define the IP address and port number for Server 1
SERVER1_IP = '127.0.0.1'
SERVER1_PORT = 6000

# Create a socket object
server2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to Server 1
server2_socket.connect((SERVER1_IP, SERVER1_PORT))

server2_socket.sendall(bytes("REQ",encoding="utf-8"))
# Time at which time the request was made
t0 = datetime.now()

# Receive message from Server 1
received_message = server2_socket.recv(1024).decode()

# Contains hello message
messaage = received_message.split(".")[0]

# Contains time from the server
T_server = received_message.split(".")[1]

# Time at which message was received
t1 = datetime.now()

# converting time received from server to compatible time format
T_server = datetime.strptime(T_server, "%Y-%m-%d %H:%M:%S")

# Display the received message along with the time it was received
print(f"Received message from Server 1: '{messaage}' at time: {t1}")

# formula
'''
T_client = T_server + (t1 - t0) / 2
'''
T_client = T_server + (t1 - t0)/2

print(f"T0: {t0}")
print(f"T1: {t1}")
print(f"Client Time: {T_client}")

# Close the connection
server2_socket.close()
