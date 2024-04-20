import socket
import select  # Importing the select module
from datetime import datetime

def receive_message(host, ports):
    connections = []

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen()
        print(f"Listening for connections on port {port}...")
        connections.append(s)

    print("Receiver\t\tReceived\tSender's time\tReceiver's time\t\tDifference\tBandwidth (Mbps)")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")

    while True:
        readable, _, _ = select.select(connections, [], [])
        
        for sock in readable:
            conn, addr = sock.accept()
            #print(f"Connected by {addr}")

            data = conn.recv(1024)
            if data:
                receiving_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]  # Remove microseconds
                combined_message = data.decode()
                message, sender_time = combined_message.split("||")  # Splitting message and sender's time
                sending_time = datetime.strptime(sender_time, '%H:%M:%S:%f').strftime('%H:%M:%S:%f')[:-3]  # Remove microseconds
                time_difference = (datetime.strptime(receiving_time, '%H:%M:%S:%f') - datetime.strptime(sending_time, '%H:%M:%S:%f')).total_seconds() * 1000
                if time_difference < 1:  # Ensure time difference is at least 1 millisecond
                    time_difference = 1
                
                bandwidth = len(message) / time_difference * 8 / 1e6  # Mbps

                print(f"{addr}\t{message}\t{sending_time}\t{receiving_time}\t\t{time_difference}\t\t{bandwidth:.2f}")
            else:
                print("Error: No data received.")

if __name__ == "__main__":
    HOST = 'localhost'
    PORTS = [12345, 12346, 12347, 12348]  # Different port numbers for each sender
    receive_message(HOST, PORTS)
