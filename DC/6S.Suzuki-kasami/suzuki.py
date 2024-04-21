import random
import threading
import time

class SuzukiKasami:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.requests = [False] * num_processes
        self.permissions = [False] * num_processes
        self.token_holders = [False] * num_processes
        self.current_process = -1
        self.token_holder = -1
        self.token_mutex = threading.Lock()

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

        # Pass token to the next process
        self.token_mutex.acquire()
        next_process = (process_id + 1) % self.num_processes
        self.token_holders[process_id] = False
        self.token_holders[next_process] = True
        self.token_holder = next_process
        self.token_mutex.release()

    def simulate(self, process_id):
        while True:
            if self.token_holders[process_id]:
                self.request(process_id)
                print(f"Process {process_id} entered critical section")
                time.sleep(random.uniform(1, 3))  # Simulate work in critical section
                self.release(process_id)
                print(f"Process {process_id} left critical section")
                time.sleep(1)  # Simulate some delay before requesting again

if __name__ == "__main__":
    num_processes = 5
    suzuki_kasami = SuzukiKasami(num_processes)

    # Initialize token holder
    initial_token_holder = random.randint(0, num_processes - 1)
    suzuki_kasami.token_holders[initial_token_holder] = True
    suzuki_kasami.token_holder = initial_token_holder

    # Simulate processes
    threads = []
    for i in range(num_processes):
        thread = threading.Thread(target=suzuki_kasami.simulate, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
