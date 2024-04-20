import socket
import time

class BakeryClient:
    def __init__(self):
        self.host = '192.168.1.195'
        self.port = 9999

    def request_lock(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(b"lock")
            response = s.recv(1024).decode('utf-8')
            if response == 'locked':
                print("Lock acquired.")
                print("Entered in Critical Section")
                
            else:
                print("Failed to acquire lock.")

    def release_lock(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(b"unlock")
            print("Exited from Critical Section")
            print("Lock released.")

if __name__ == "__main__":
    client = BakeryClient()
    client.request_lock()
    # Critical Section
    time.sleep(2)  # Simulating some work in critical section
    client.release_lock()
