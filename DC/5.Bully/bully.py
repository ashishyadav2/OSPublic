class Process:
    def __init__(self, pid):
        self.pid = pid
        self.coordinator = None
        self.processes = []

    def send_election_message(self, dest_pid):
        print(f"Process {self.pid} sends election message to Process {dest_pid}")

    def send_coordinate_message(self, dest_pid):
        print(f"Process {self.pid} sends coordinate message to Process {dest_pid}")

    def start_election(self):
        print(f"Process {self.pid} starts election")
        higher_pids = [p for p in self.processes if p.pid > self.pid]
        if not higher_pids:
            self.coordinator = self
            for p in self.processes:
                if p != self:
                    p.send_coordinate_message(self.pid)
            print(f"Process {self.pid} becomes the coordinator")
        else:
            highest_pid = max(higher_pids, key=lambda p: p.pid)
            highest_pid.send_election_message(self.pid)

    def receive_election_message(self, sender_pid):
        print(f"Process {self.pid} receives election message from Process {sender_pid}")
        self.start_election()

    def receive_coordinate_message(self, sender_pid):
        print(f"Process {self.pid} receives coordinate message from Process {sender_pid}")
        self.coordinator = self.processes[sender_pid - 1]
        print(f"Process {self.pid} acknowledges Process {sender_pid} as coordinator")

# Create processes
num_processes = 5
processes = [Process(i + 1) for i in range(num_processes)]

# Set up processes' references to each other
for i, process in enumerate(processes):
    process.processes = processes[:i] + processes[i + 1:]

# Simulate a process initiating an election
process_to_start_election = processes[0]
process_to_start_election.start_election()

# Simulate other processes receiving the election message
for process in processes[1:]:
    process.receive_election_message(process_to_start_election.pid)

# Simulate the coordinator sending the coordinate message to other processes
coordinator = process_to_start_election.coordinator
if coordinator != process_to_start_election:
    for process in processes:
        if process != coordinator and coordinator is not None:
            process.receive_coordinate_message(coordinator.pid)
