import socket
import threading

class Client:
    def __init__(self, hosts=None, ports=None):
        self.max_byte_size = 1024
        self.client_connections = {}
        self.create_client_connections(hosts,ports)
        
    def make_request(self,message,key):
        self.client_connections[key]['socket'].sendall(bytes(message,encoding='utf-8'))
    
    def getReponse(self,key):
        response = self.client_connections[key]['socket'].recv(self.max_byte_size)
        return response
    
    def create_client_connections(self,hosts,ports):
        for i in range(len(hosts)):
            client_connection = threading.Thread(target=self.connect,args=(hosts[i],ports[i]))
            client_connection.start()
            key = self.format_ip_port(hosts[i],ports[i])
            self.client_connections[key] = {'thread': client_connection, 'socket': None}
        
    def connect(self, host, port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        key = self.format_ip_port(host, port)
        self.client_connections[key]['socket'] = client_socket
                
    def close_connection(self,hosts,ports):
        for host,port in zip(hosts,ports):
            key = self.format_ip_port(host,port)
            self.client_connections[key]['thread'].join()
            self.client_connections[key]['socket'].close()
            
    def get_clients(self):
        return self.client_connections
    
    def format_ip_port(self,host,port):
        return f'{host}:{port}'