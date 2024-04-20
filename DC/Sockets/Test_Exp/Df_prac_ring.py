import threading
import time
import random
import queue  # Import the queue module

class Node(threading.Thread):
    def __init__(self, node_id, total_nodes, message_queue):
        super().__init__()
        self.node_id = node_id
        self.total_nodes = total_nodes
        self.next_node_id = (node_id + 1) % total_nodes
        self.elected_leader = None
        self.is_active = True
        self.has_elected = False
        self.message_queue = message_queue

    def run(self):
        while True:
            if self.is_active:
                if not self.has_elected:
                    self.start_election()
                else:
                    break
            time.sleep(1)

    def start_election(self):
        message = self.message_queue.get()  # Get next message from the queue
        destination_id, leader_id = message
        self.send_election_message(destination_id, leader_id)

    def send_election_message(self, destination_id, leader_id):
        print(f"Node {self.node_id}: Sending election message to Node {destination_id} for leader {leader_id}")
        time.sleep(1)
        if destination_id == self.node_id:
            self.elected_leader = leader_id
            self.has_elected = True
            print(f"Node {self.node_id}: Elected leader {leader_id}")
        else:
            self.message_queue.put((self.next_node_id, leader_id))  # Put the next message in the queue
            self.next_node_id = (self.next_node_id + 1) % self.total_nodes

    def stop_node(self):
        self.is_active = False

def main():
    total_nodes = 3  # Changed to 3 nodes
    message_queue = queue.Queue()  # Create a message queue

    # Define message passing sequence
    message_queue.put((1, 0))  # Node 0 will send message to Node 1
    message_queue.put((2, 1))  # Node 1 will send message to Node 2
    message_queue.put((0, 2))  # Node 2 will send message to Node 0

    nodes = []

    for i in range(total_nodes):
        node = Node(i, total_nodes, message_queue)
        nodes.append(node)

    # Start the nodes
    for node in nodes:
        node.start()

    # Simulate failure of random nodes
    time.sleep(5)
    failed_node = random.randint(0, total_nodes - 1)
    nodes[failed_node].stop_node()
    print(f"Node {failed_node} has failed.")

    # Wait for all nodes to finish
    for node in nodes:
        node.join()

    # Print elected leader
    elected_leader = nodes[0].elected_leader  # Node with highest priority will be first in the list
    print(f"Elected Leader: Node {elected_leader}")

if __name__ == "__main__":
    main()
