
class Bully:
    def __init__(self,processes):
        self.processed = processes
        self.co_ordinator = None
    
    def election(self,process_id):
        print(f"Process {process_id} starts an election")

        higher_processes = [p for p in self.processed if p>process_id]
        if not higher_processes:
            self.co_ordinator = process_id
            print(f"Process {process_id} is elected as a co ordinator")
            self.notify()
            return 
        
        print(f"Process {process_id} will send election message to {higher_processes}")

        highest_id = max(higher_processes)
        for hi_processes in higher_processes:
            print(f"Process {process_id} sends election message to Process {hi_processes}")
            print(f"Process {hi_processes} reply to Process {process_id}")
            if highest_id==hi_processes:
                print(f"{highest_id} is elected as a co ordinator")
                self.co_ordinator = highest_id
                self.notify()
                return
    def notify(self):
        for proc in self.processed:
            if proc!=self.co_ordinator and proc>0:
                print(f"{self.co_ordinator} sends 'co-ordinator' message to {proc}")
if __name__ == "__main__":
    processes = [1,2,3,4,5,6,7]
    bully = Bully(processes)
    bully.election(4)