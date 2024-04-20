class LamportClock:
    def __init__(self):
        self.clock = 0

    def tick(self):
        self.clock += 1

    def update(self, received_time):
        self.clock = max(self.clock, received_time) + 1

    def get_time(self):
        return self.clock

class Process:
    def __init__(self, process_id, clock):
        self.process_id = process_id
        self.clock = clock

    def send_request(self, receiver):
        self.clock.tick()
        message_time = self.clock.get_time()
        print(f"Process {self.process_id} sends REQUEST message to Process {receiver.process_id} at time:", message_time)
        receiver.receive_request(message_time)

    def receive_request(self, received_time):
        self.clock.update(received_time)
        self.clock.tick()
        message_time = self.clock.get_time()
        print(f"Process {self.process_id} receives REQUEST message at time:", message_time)
        # Simulate replying immediately
        self.send_reply()

    def send_reply(self):
        self.clock.tick()
        message_time = self.clock.get_time()
        print(f"Process {self.process_id} sends REPLY message at time:", message_time)

    def receive_reply(self, received_time):
        self.clock.update(received_time)
        message_time = self.clock.get_time()
        print(f"Process {self.process_id} receives REPLY message at time:", message_time)

    def send_release(self, receiver):
        self.clock.tick()
        message_time = self.clock.get_time()
        print(f"Process {self.process_id} sends RELEASE message to Process {receiver.process_id} at time:", message_time)
        receiver.receive_release(message_time)

    def receive_release(self, received_time):
        self.clock.update(received_time)
        message_time = self.clock.get_time()
        print(f"Process {self.process_id} receives RELEASE message at time:", message_time)

# Example usage
if __name__ == "__main__":
    # Initialize clocks for processes
    clock1 = LamportClock()
    clock2 = LamportClock()
    clock3 = LamportClock()

    # Initialize processes
    process1 = Process(1, clock1)
    process2 = Process(2, clock2)
    process3 = Process(3, clock3)

    # Process 1 sends a request to Process 2
    process1.send_request(process2)

    # Process 2 sends a request to Process 3
    process2.send_request(process3)

    # Process 3 sends a release to Process 1
    process3.send_release(process1)
