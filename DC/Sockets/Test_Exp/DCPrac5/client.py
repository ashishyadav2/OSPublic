import socket
import pickle

def send_id(id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.1.244", 5555))
    client_socket.send(pickle.dumps(id))
    client_socket.close()

if __name__ == "__main__":
    node_id = int(input("Enter Node ID: "))
    send_id(node_id)
