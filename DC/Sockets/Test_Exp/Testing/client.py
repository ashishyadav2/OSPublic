import socket

class Client:
    def __init__(self, sock=None, host=None, port=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.max_byte_size = 1024
        self.host = host
        self.port = port
        try:
            self.connect(self.host, self.port)
        except ConnectionRefusedError as e:
            pass
        
    def make_request(self,message):
        self.sock.sendall(bytes(message,encoding='utf-8'))
    
    def getReponse(self):
        response = self.sock.recv(self.max_byte_size)
        return response
    
    def connect(self,host,port):
        self.sock.connect((host,port))
                
    def close_connection(self):
        self.sock.close()
            