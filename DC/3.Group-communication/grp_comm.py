import socket

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    print(f"Server running on port {port}...")
    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        handle_client(conn, addr)

def handle_client(conn, addr):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received message from {addr}: {data.decode()}")
            conn.sendall(b"Message received")

if __name__ == "__main__":
    start_server(8002) # Change port number if needed