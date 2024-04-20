class Process:
    def __init__(self, pid):
        self.pid = pid
        self.waiting_for = None

    def set_waiting_for(self, target_process):
        self.waiting_for = target_process

    def initiate_probe(self):
        print(f"Process {self.pid} initiated a probe.")
        path = [self.pid]
        self.send_probe(self.pid, path)

    def send_probe(self, initiator_pid, path):
        if self.waiting_for:
            print(f"Process {self.pid} sent probe to process {self.waiting_for.pid}.")
            self.waiting_for.receive_probe(initiator_pid, list(path))  # Pass a copy of the path

    def receive_probe(self, initiator_pid, path):
        print(f"Process {self.pid} received probe from process {initiator_pid}.")
        if self.pid in path:
            if self.pid == initiator_pid:
                print(f"Deadlock detected in path: {' -> '.join(map(str, path))}")
            return
        else:
            path.append(self.pid)
            if self.waiting_for:
                self.waiting_for.send_probe(initiator_pid, path)

def main():
    print("Script started")
    # Create some example processes
    p1 = Process(1)
    p2 = Process(2)
    p3 = Process(3)
    p4 = Process(4)

    # Set up a circular wait condition
    p1.set_waiting_for(p2)
    p2.set_waiting_for(p3)
    p3.set_waiting_for(p4)
    p4.set_waiting_for(p1)  # This creates a cycle p1 -> p2 -> p3 -> p4 -> p1

    # Initiate the deadlock detection from process p1
    p1.initiate_probe()
    print("Script ended")

if __name__ == '__main__':
    main()
