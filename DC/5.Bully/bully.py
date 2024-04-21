class BullyAlgorithm:
    def __init__(self, processes):
        self.processes = processes
        self.coordinator = None

    def election(self, process_id):
        print(f"Process {process_id} initiates an election")
        higher_processes = [p for p in self.processes if p > process_id]
        if not higher_processes:
            self.coordinator = process_id
            print(f"Process {process_id} is elected as coordinator")
            self.notify_coordinator()
            return

        highest_id = max(higher_processes)
        print(f"Process {process_id} sends election message to higher processes: {higher_processes}")

        for higher_process in higher_processes:
            # Simulate message passing, here it just prints the message
            print(f"Process {process_id} sends election message to Process {higher_process}")

            # Simulate receiving reply message, here it just prints the message
            print(f"Process {higher_process} sends reply message to Process {process_id}")

            if highest_id == higher_process:
                self.coordinator = highest_id
                print(f"Process {highest_id} is elected as coordinator")
                self.notify_coordinator()
                return

    def notify_coordinator(self):
        print(f"Coordinator {self.coordinator} is notified about the election result")
        for process_id in self.processes:
            if process_id != self.coordinator:
                # Simulate message passing, here it just prints the message
                print(f"Process {self.coordinator} sends 'Co-ordinator' message to Process {process_id}")


if __name__ == "__main__":
    processes = [1, 2, 3, 4, 5]  # Example processes, each process has a unique identifier
    bully = BullyAlgorithm(processes)

    # Assume process 3 initiates an election
    bully.election(4)
