import socket
import threading
import time

class Server(threading.Thread):
    def __init__(self, port):
        super(Server, self).__init__()
        self.port = port
        self.token = True  # Server initially holds the token
        self.requesting = False
        self.token_available = threading.Event()

    def request_cs(self):
        self.requesting = True
        print(f"Server on port {self.port} requesting critical section")

    def receive_request(self):
        return not self.requesting

    def enter_cs(self):
        print(f"Server on port {self.port} entering critical section")
        time.sleep(1)
        print(f"Server on port {self.port} exiting critical section")

    def release_cs(self):
        self.requesting = False

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', self.port))
        server_socket.listen(5)

        print(f"Server on port {self.port} listening for connections...")

        while True:
            connection, address = server_socket.accept()
            if self.receive_request():
                connection.send("Granted".encode())
                if self.requesting and self.token:
                    self.token = False
                    self.enter_cs()
                    self.release_cs()
                    self.token = True
            else:
                connection.send("Denied".encode())
            connection.close()

def main():
    ports = [5000, 5001, 5002]
    servers = [Server(port) for port in ports]

    for server in servers:
        server.start()

    for server in servers:
        server.join()

if __name__ == "__main__":
    main()
