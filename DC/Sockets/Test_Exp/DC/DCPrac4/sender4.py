import socket
from datetime import datetime

def send_message(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        message = input("Enter message to send: ")
        current_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]  # Extracting time up to milliseconds
        combined_message = f"{message}||{current_time}"  # Combining message and current time
        s.sendall(combined_message.encode())
        print("Message sent successfully.")

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 12348  # Port number can be any available port
    send_message(HOST, PORT)
