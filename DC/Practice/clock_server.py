import socket
from datetime import datetime

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1",7000))
server_socket.listen(1)
print("Server is listening")
client_socket,client_addr = server_socket.accept()
print("Connection established")
current_time = datetime.now()
message = f"Hello from server.{current_time}"
client_socket.sendall(message.encode())
server_socket.close()
client_socket.close()