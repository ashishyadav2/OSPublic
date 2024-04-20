import random

class SuzukiKasami:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.requests = [False] * num_processes
        self.permissions = [False] * num_processes
        self.current_process = -1

    def request(self, process_id):
        self.requests[process_id] = True
        self.update_permissions(process_id)

    def update_permissions(self, process_id):
        while True:
            if self.requests[process_id] and not self.permissions[process_id]:
                for i in range(self.num_processes):
                    if i == process_id:
                        continue
                    if self.requests[i] and self.permissions[i]:
                        self.requests[process_id] = False
                        break
                else:
                    self.permissions[process_id] = True
                    self.current_process = process_id
                    break

    def release(self, process_id):
        self.requests[process_id] = False
        self.permissions[process_id] = False
        self.current_process = -1

# Example usage
num_processes = 5
suzuki_kasami = SuzukiKasami(num_processes)

# Simulate process requests and releases
for _ in range(10):
    process_id = random.randint(0, num_processes - 1)
    suzuki_kasami.request(process_id)
    print(f"Process {process_id} entered critical section")

    # Simulate some work in the critical section
    import time
    time.sleep(random.uniform(1, 3))

    suzuki_kasami.release(process_id)
    print(f"Process {process_id} left critical section")