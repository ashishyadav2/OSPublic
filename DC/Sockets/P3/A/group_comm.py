import socket
import threading

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []

    def start_server(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"Node listening on {self.host}:{self.port}")
        while True:
            conn, addr = self.sock.accept()
            self.connections.append(conn)
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

    def handle_client(self, conn, addr):
        print(f"New connection from {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                conn.close()
                break
            print(f"Received message: {data.decode()}")
            self.broadcast(data)

    def broadcast(self, message):
        for conn in self.connections:
            conn.sendall(message)

    def connect_to_node(self, host, port):
        try:
            self.sock.connect((host, port))
            threading.Thread(target=self.receive_messages).start()
        except Exception as e:
            print(f"Failed to connect to node at {host}:{port}, Error: {e}")

    def receive_messages(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(f"Received broadcasted message: {data.decode()}")

if __name__ == "__main__":
    node1 = Node("127.0.0.1", 6000)
    node2 = Node("127.0.0.1", 6001)
    node3 = Node("127.0.0.1", 6002)


    threading.Thread(target=node1.start_server).start()
    threading.Thread(target=node2.start_server).start()
    threading.Thread(target=node3.start_server).start()

    node1.connect_to_node("127.0.0.1", 6001)
    node1.connect_to_node("127.0.0.1", 6002)

    node2.connect_to_node("127.0.0.1", 6000)
    node2.connect_to_node("127.0.0.1", 6002)

    node3.connect_to_node("127.0.0.1", 6000)
    node3.connect_to_node("127.0.0.1", 6001)

    # Send broadcast message from node 1
    node1.broadcast(b"Hello from node 1!")
