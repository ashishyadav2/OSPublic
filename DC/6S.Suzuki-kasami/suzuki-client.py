import socket

def request_critical_section(port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', port))
    client_socket.send("Request".encode())
    response = client_socket.recv(1024).decode()
    client_socket.close()
    return response

def main():
    ports = [5000, 5001, 5002]

    for port in ports:
        response = request_critical_section(port)
        print(f"Process on port {port}: {response} access to critical section")

if __name__ == "__main__":
    main()
