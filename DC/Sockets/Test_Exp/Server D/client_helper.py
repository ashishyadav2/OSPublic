import os
import argparse
from client import Client

def format_args(args):
    return args.split(',')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="A program that is used to send requests"
        )
    parser.add_argument("--ip",type=format_args, help="IPv4 Address of the server")
    parser.add_argument("--port",type=format_args, help="port")
    args = parser.parse_args()
    hosts = args.ip
    ports = args.port
    ports = [int(port) for port in ports]
    print(list(zip(hosts,ports)))
    if len(hosts)!=len(ports):
        parser.error("Error: Number of IPs must match the number of ports.")
    try:
        client = Client(hosts=hosts,ports=ports)
    except ConnectionRefusedError:
            os._exit(-1)

    while True:
        print("-------------------------------------")
        print("1. Contents of folder\n2. File size\n3. Video Size\n4. Free space\n5. System info\n6. Exit\n7. Message")
        choice = input("INPUT: ")
        if choice == '6':
            print("Disconnect from the server")
            client.close_connection(hosts,ports)
            break
        elif choice=='7':
            choice = input("MESSAGE: ")
            
        for host, port in zip(hosts, ports):
            key = client.format_ip_port(host, port)
            client.make_request(choice, key=key)  
            response = client.getReponse(key=key).decode()  
            print(f'\nResponse from {host}:{port}: \n{response}')
            