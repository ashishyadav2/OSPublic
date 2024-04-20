import socket
import subprocess
from client import Client

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.max_bytes_size = 1024
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.setblocking(False)
        # self.sock.bind((host, port))
        # self.sock.listen()
        self.connections = {}
        # self.create_connections()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.server_socket.bind(('0.0.0.0', self.port))
        print("Server started...")

    def reply(self, conn, response):
        if not isinstance(response, bytes):
            response = bytes(response, encoding="utf-8")
        conn.sendall(response)

    def exec_process(self, command: str):
        try:
            process = subprocess.run(
                command.split(" "), capture_output=True, text=False
            )
            if process.returncode == 0:
                return process.stdout
            else:
                return "Cannot process your request! :("
        except Exception as e:
            print(e)
            return "Internal server error"

    def handle_client(self, conn, addr):
        print(f"[{addr[0]}]: Connected")
        while True:
            try:
                data = conn.recv(self.max_bytes_size)
                self.send_to_all(addr,0)
                if not data:
                    print(f"[{addr[0]}]: Disconnected")
                    self.send_to_all(addr,1)
                    conn.close()
                    break
                try:
                    client_msg = int(chr(int.from_bytes(data, byteorder="big")))
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
                    client_msg = data.decode()
                    response = f"Your MSG: {client_msg}\n"
                    self.reply(conn, response)
                print(f"[{addr[0]}]: {client_msg}")
                
            except BlockingIOError:
                pass
            except ConnectionResetError:
                print(f"[{addr[0]}] Node: Failed!")
                conn.close()
                break
            except Exception as e:
                print(f"Error handling client: {e}")
                conn.close()
                break

    def run(self):
        while True:
            try:
                conn, addr = self.sock.accept()
                self.handle_client(conn, addr)
            except BlockingIOError:
                pass
            except Exception as e:
                print(f"Error accepting connection: {e}")

    def read_config_file(self):
        ip_and_ports = []
        with open("config.txt", "r") as f:
            config_file = f.read()
        for ip_port in config_file.split('\n'):
            ip = ip_port.split(":")[0]
            port = ip_port.split(":")[1]
            ip_and_ports.append((ip,int(port)))
        return ip_and_ports

    def create_connections(self):
        for ip,port in self.read_config_file():
            x = f"{ip}:{port}"
            y = f"{self.host}:{self.port}"
            if x==y:
                continue
            clnt = Client(host=ip,port=port)
            key = (ip,port)
            if key not in self.connections:
                self.connections[key] = clnt
            
    def send_to_all(self,addr,flag=0):
        if flag == 0:
            msg = f"{addr[0]}----->{self.host}"
        else:
            msg = f"{addr[0]}--X-->{self.host}"  
                      
        for key in self.connections.keys():
            self.connections[key].make_request(msg)


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 9000
    server = Server(host, port)
    server.run()
