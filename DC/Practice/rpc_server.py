import socket
import subprocess

class Server:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((self.host,self.port))
        print("Server started...")

    def exec_process(self,command):
        try:
            process = subprocess.run(command.split(), capture_output=True,text=True)
            if process.returncode == 0:
                return process.stdout
            else:
                return "Internal server error"
        except Exception as e:
            print(e)
            return "Internal server error"
        
    def reply(self,conn,message):
        conn.sendall(message.encode())

    def handle_client(self,conn,addr):
        while True:
            try:
                data = int(conn.recv(1024).decode())
                result = None
                if data == 1:
                    result = self.exec_process("python contents_of_folder.py")
                elif data == 2:
                    result = self.exec_process("python get_file_size.py")
                elif data == 3:
                    result = self.exec_process("python get_free_space.py")
                elif data == 4:
                    result = self.exec_process("python get_video_size.py")
                elif data == 5:
                    result = self.exec_process("systeminfo")
                else:
                    result = "Invalid Option"
                self.reply(conn,result)
            except Exception as e:
                print(e)
                conn.close()
                break
    
    def run(self):
        self.server_socket.listen()
        while True:
            conn, addr = self.server_socket.accept()
            self.handle_client(conn,addr)

if __name__ == "__main__":
    server = Server("127.0.0.1",5900)
    server.run()

