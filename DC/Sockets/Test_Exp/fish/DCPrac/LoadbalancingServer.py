import socket

def print_load(servers, processes):
    server_loads = [0] * servers
    for process in range(processes):
        next_server = process % servers
        server_loads[next_server] += 1
    for i, load in enumerate(server_loads):
        print(f"Server{i+1} has {load} Processes")

def main():
    host = "192.168.1.185"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Load Balance Server Started...")
    while True:
        conn, addr = server_socket.accept()
        print("Connection from: " + str(addr))
        data = conn.recv(1024).decode()
        servers, processes = map(int, data.split())
        print_load(servers, processes)
        conn.close()

if __name__ == "__main__":
    main()
