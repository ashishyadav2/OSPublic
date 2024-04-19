import socket
import subprocess
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        print(f"Listening on port {port}")

    def reply(self, conn, response):
        conn.sendall(response.encode())

    def exec_process(self, command):
        try:
            process = subprocess.run(command.split(), capture_output=True, text=True)
            if process.returncode == 0:
                return process.stdout
            else:
                return "Cannot process your request! :("
        except Exception as e:
            print(e)
            return "Internal server error"

    def handle_client(self, conn, addr):
        while True:
            try:
                data = conn.recv(1024)
                client_msg = int(data.decode())
                print(f'{addr}: {client_msg}')
                if client_msg == 1:
                    response = self.exec_process("python contents_of_folder.py")
                elif client_msg == 2:
                    response = self.exec_process("python get_file_size.py")
                elif client_msg == 3:
                    response = self.exec_process("python get_video_size.py")
                elif client_msg == 4:
                    response = self.exec_process("python get_free_space.py")
                elif client_msg == 5:
                    response = self.exec_process("cpuinfo")
                else:
                    response = "Invalid option"
                self.reply(conn, response)
                
            except Exception as e:
                print(e)
                print("Closing connection with client")
                conn.close()
                break

    def run(self):
        self.server_socket.listen()
        while True:
            conn, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    hosts = ["127.0.0.1", "127.0.0.1", "127.0.0.1"]
    ports = [19000, 19500, 19800]
    servers = []
    for i in range(3):
        server = Server(hosts[i], ports[i])
        servers.append(server)
        threading.Thread(target=server.run).start()
