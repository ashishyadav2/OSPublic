from threading import Thread, Lock
import time

class LamportMutex:
    def __init__(self, process_id, num_processes):
        self.process_id = process_id
        self.num_processes = num_processes
        self.clock = 1
        self.requesting_cs = False
        self.reply_received = [False] * num_processes
        self.cs_mutex = Lock()
        self.request_mutex = Lock()

    def request_critical_section(self):
        self.request_mutex.acquire()
        self.clock += 1
        self.requesting_cs = True
        request_time = self.clock
        self.request_mutex.release()

        for process in range(self.num_processes):
            if process != self.process_id:
                # Send request to all other processes
                self.send_request(process, request_time)

        # Wait until all replies are received
        while not all(self.reply_received):
            time.sleep(0.1)

        self.enter_critical_section()

    def enter_critical_section(self):
        self.cs_mutex.acquire()
        print(f"Process {self.process_id} enters the critical section.")
        time.sleep(1)  # Simulating some work in the critical section
        print(f"Process {self.process_id} exits the critical section.")
        self.cs_mutex.release()

        # Reset requesting flag and clear reply received array
        self.requesting_cs = False
        self.reply_received = [False] * self.num_processes

    def send_request(self, dest_process, request_time):
        # Simulate sending a request to dest_process
        time.sleep(0.1)
        print(f"Process {self.process_id} sends request with timestamp {request_time} to Process {dest_process}.")
        self.receive_request_reply(dest_process)

    def receive_request_reply(self, sender_process):
        self.reply_received[sender_process] = True

        # Simulate sending a reply back to the sender
        time.sleep(0.1)
        print(f"Process {self.process_id} sends reply to Process {sender_process}.")

    def simulate(self):
        self.request_critical_section()


if __name__ == "__main__":
    num_processes = 3
    processes = []

    for i in range(num_processes):
        process = LamportMutex(i, num_processes)
        processes.append(process)
        thread = Thread(target=process.simulate)
        thread.start()

    for process in processes:
        thread.join()
