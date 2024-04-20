class RoundRobinLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def get_next_server(self):
        # Get the next server in a round-robin fashion
        next_server = self.servers[self.current_index]
        # Move to the next server index
        self.current_index = (self.current_index + 1) % len(self.servers)
        return next_server

# Example usage
servers = ["Server1", "Server2", "Server3", "Server4"]
load_balancer = RoundRobinLoadBalancer(servers)

# Simulate 10 requests
for i in range(10):
    next_server = load_balancer.get_next_server()
    print(f"Request {i+1} routed to {next_server}")
