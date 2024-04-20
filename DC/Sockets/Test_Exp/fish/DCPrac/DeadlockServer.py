import socket
import threading

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode()
        print("Received message:", data)
        # Process the message as needed for deadlock detection
    except Exception as e:
        print("Error handling client:", e)
    finally:
        client_socket.close()

def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('192.168.1.185', 12345))
        server_socket.listen(5)

        print("Server started. Waiting for connections...")

        while True:
            client_socket, addr = server_socket.accept()
            print("Client connected:", addr[0])
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
