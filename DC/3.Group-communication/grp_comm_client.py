import socket
import sys

def send_message(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.sendall(message.encode())
        data = s.recv(1024)
    print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py server_ip port message")
        sys.exit(1)
    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    message = sys.argv[3]
    send_message(server_ip, port, message)