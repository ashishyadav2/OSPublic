import socket
class Client:
    def __init__(self,host=None,port=None):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        try:
            self.socket.connect((self.host,self.port))
        except ConnectionRefusedError as e:
            print(e)

    def make_request(self,message):
        self.socket.sendall(bytes(message,encoding="utf-8"))
    
    def get_response(self):
        return self.socket.recv(1024).decode()

    def close_connection(self):
        self.socket.close()

if __name__ == "__main__":
    client = Client(host="127.0.0.1",port=5900)
    while True:
        choice = input("Choice: ")
        if choice=='6':
            client.close_connection()
            break
        client.make_request(choice)
        print(client.get_response())