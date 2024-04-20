import socket
import pickle

class Node:
    def _init_(self, id):
        self.id = id
        self.elected_leader = None
        self.nodes = []

    def send_election_message(self, target):
        print("Node", self.id, "sends election message to Node", target.id)
        # You can implement the socket communication here to send election message to target

    def send_ok_message(self, target):
        print("Node", self.id, "sends OK message to Node", target.id)
        # You can implement the socket communication here to send OK message to target

def bully_election(nodes):
    n = len(nodes)

    # Step 1: If a node detects that the leader is not responding, it starts an election
    for i in range(n):
        if nodes[i].elected_leader is None:
            for j in range(i + 1, n):
                nodes[i].send_election_message(nodes[j])

    # Step 2: If a node receives an election message, it responds with an OK message if it has a higher ID
    for i in range(n):
        if nodes[i].elected_leader is None:
            for j in range(i + 1, n):
                if nodes[i].id > nodes[j].id:
                    nodes[j].send_ok_message(nodes[i])
                else:
                    nodes[i].send_election_message(nodes[j])

    # Step 3: If a node receives an OK message, it cancels its election and sends a message to the higher ID node
    for i in range(n):
        if nodes[i].elected_leader is None:
            for j in range(i + 1, n):
                if nodes[i].id < nodes[j].id:
                    print("Node", nodes[i].id, "cancels its election.")
                    break
            else:
                nodes[i].elected_leader = nodes[i]

    # Step 4: The node with the highest ID becomes the leader
    leader = max(nodes, key=lambda x: x.id)
    print("Node", leader.id, "is elected as the leader.")

def start_server():
    # Create socket to listen for incoming connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("192.168.1.244", 5555))
    server_socket.listen(5)
    print("Server is listening...")

    nodes = []  # Store connected nodes

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established.")

        # Receive data from client
        data = client_socket.recv(1024)
        if data:
            node_id = pickle.loads(data)
            new_node = Node(node_id)
            nodes.append(new_node)
            print("Node", node_id, "connected.")

        # Perform Bully Election if all nodes have connected
        if len(nodes) == 3:

            bully_election(nodes)
            break

    # Close the server socket
    server_socket.close()

if _name_ == "_main_":
    start_server()
