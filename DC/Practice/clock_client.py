import socket
from datetime import datetime

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.connect(("127.0.0.1",7000))
t0 = datetime.now()
server_socket.sendall(bytes("REQ",encoding="utf-8"))
received_message = server_socket.recv(1024).decode()
message = received_message.split(".")[0]
T_server = received_message.split(".")[1]
t1 = datetime.now()
print(f"Message received from server {message} with {T_server}")
T_server = datetime.strptime(T_server,"%Y-%m-%d %H:%M:%S")
T_client = T_server + (t1 - t0)/2
print(f"{T_client}")
print(f"{(t1-t0)/2}")
