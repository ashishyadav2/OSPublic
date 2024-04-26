import socket

def print_load(server_loads):
    for i, load in enumerate(server_loads):
        print("Load Balancing using Round Robin")
        print(f"Server{i+1} has {load} Processes")

def main():
    host = "127.0.0.1"
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Load Balance Server Started...")
    initial_servers = 3 # Number of servers
    server_loads = [0] * initial_servers
    current_server = 0

    while True:
        conn, addr = server_socket.accept()
        print("Connection from: " + str(addr))
        data = conn.recv(1024).decode()
        # Split the received data into number of servers and processes
        servers, processes = map(int, data.split())
        # Distribute processes using round-robin
        
        for _ in range(processes):
            server_loads[current_server % initial_servers] += 1
            current_server += 1
        print_load(server_loads)
        conn.close()

if __name__ == "__main__":
    main()