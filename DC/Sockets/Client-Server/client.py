import socket

class Client:
    def __init__(self, host=None, port=None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        
        try:
            self.connect(self.host, self.port)
        except ConnectionRefusedError as e:
            print(e)
            
    def make_request(self,message):
        self.sock.sendall(bytes(message,encoding='utf-8'))
    
    def getReponse(self):
        response = self.sock.recv(1024)
        return response
    
    def connect(self,host,port):
        self.sock.connect((host,port))
                
    def close_connection(self):
        self.sock.close()
            
            
if __name__ == "__main__":
    client = Client(host='127.0.0.1',port=9000)
    
    while True:
        print("-------------------------------------")
        print("1. Contents of folder")
        print("2. File size")
        print("3. Video Size")
        print("4. Free space")
        print("5. System info")
        print("6. Exit")
        choice = input("INPUT: ")
        
        if choice == '6':
            print("Disconnect from the server")
            client.close_connection()
            break
        
        client.make_request(choice)
        
        response = client.getReponse().decode()
        print("Reponse from the server: ")
        print(response)