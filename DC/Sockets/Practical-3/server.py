import socket
import subprocess
import threading
from client import Client

class Server:
    def __init__(self, host, ports):
        self.host = host
        self.ports = ports
        self.max_bytes_size = 1024
        self.server_threads = []  
        self.clients_obj = None
        self.client_connections = None
        self.all_connections = []
        self.create_connections()
        self.create_server_threads(host,ports)
        print("Server started...")

    def create_server_threads(self,host,ports):
        for port in ports:
            server_thread = threading.Thread(target=self.run,args=(host,port))
            server_thread.start()
            self.server_threads.append(server_thread)
        
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
        host_port = conn.getsockname()
        print(f"[{host_port}]: Connected")
        while True:
            try:
                data = conn.recv(self.max_bytes_size)
                if not data:
                    print(f"[{host_port}]: Disconnected")
                    self.send_to_all(host_port,1)
                    conn.close()
                    break
                try:
                    client_msg = int(chr(int.from_bytes(data, byteorder="big")))
                    if client_msg is not None:
                        self.send_to_all(host_port,0)                        
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
                print(f"[{host_port}]: {client_msg}")
                
            except BlockingIOError:
                pass
            except ConnectionResetError:
                print(f"[{host_port}] Node: Failed!")
                conn.close()
                break
            except Exception as e:
                print(f"Error handling client: {e}")
                conn.close()
                break

    def run(self,host,port):
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_socket.bind((host,port))
        server_socket.listen()
        while True:
            try:
                conn, addr = server_socket.accept()
                threading.Thread(target=self.handle_client,args=(conn,addr)).start()
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
        hosts = []
        ports = []
        res = set([self.format_ip_port(ip,port) for ip,port in self.read_config_file()])
        res2 = set([self.format_ip_port(self.host,port) for port in self.ports])
        res.difference_update(res2)
        for elem in list(res):
            hosts.append(elem.split(":")[0])
            ports.append(int(elem.split(":")[1]))
        clnt = Client(hosts=hosts,ports=ports)
        self.client_connections = clnt.get_clients()
        self.clients_obj = clnt
        self.all_connections = [self.format_ip_port(i,j) for i,j in list(zip(hosts,ports))]
            
    def send_to_all(self,addr,flag=0):
        if flag == 0:
            msg = f"{addr}----->{self.host}"
        else:
            msg = f"{addr}--X-->{self.host}"  
                      
        for key in self.all_connections:
            self.clients_obj.make_request(msg,key=key)

    def format_ip_port(self,host,port):
        return f"{host}:{port}"
    
if __name__ == "__main__":
    host = "127.0.0.1"
    with open("in.txt",'r') as f:
        ports = f.read().split("\n")
    ports = list(map(int,ports))
    server = Server(host, ports)
