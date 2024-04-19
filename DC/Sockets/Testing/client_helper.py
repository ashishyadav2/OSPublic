import argparse
from client import Client
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="A program that is used to send requests"
        )
    parser.add_argument("ip", type=str, help="IPv4 Address of the server")
    parser.add_argument("port", type=int, help="port")
    args = parser.parse_args()
    host = args.ip
    port = args.port
    client = Client(host=host,port=port)
    while True:
        print("-------------------------------------")
        print("1. Contents of folder\n2. File size\n3. Video Size\n4. Free space\n5. System info\n6. Exit\n7. Message")
        choice = input("INPUT: ")
        if choice == '6':
            print("Disconnect from the server")
            client.close_connection()
            break
        elif choice=='7':
            choice = input("MESSAGE: ")
        client.make_request(choice)
        response = client.getReponse().decode()
        print(f'\nReponse from the server: \n{response}')
            