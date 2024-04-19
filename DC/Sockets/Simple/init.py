import numpy as np
import copy
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                description="A program that is used to send requests"
            )
    parser.add_argument("--nodes",type=int, help="Number of nodes")
    args = parser.parse_args()
    nodes = args.nodes
    
    if not nodes:
        parser.error("Please enter number of nodes")
        
    nodes_list = [f'Server_{chr(i+65)}' for i in range(nodes)]
    hmap = {node: list() for node in nodes_list}
    
    start_range = 5000
    end_range = start_range+1500
    
    for key in hmap:
        port_numbers = list(map(int,np.linspace(start_range,end_range,nodes)))
        hmap[key].extend(port_numbers)
        start_range = end_range+500
        end_range += 1500
        
    hmap_copy = copy.deepcopy(hmap)
    d =  {node: list() for node in nodes_list}
    seen = set()
    for key in hmap:
        while True:
            for k in d:
                if key==k:
                    continue
                choice = np.random.choice(hmap[k])
                if choice not in seen and len(d[key])<nodes-1:
                    seen.add(choice)
                    hmap[k].remove(choice)
                    d[key].append(choice)
            if len(d[key])==nodes-1:
                break
            
    with open("all_ins.txt",'w') as f:
        for key in hmap_copy:
            data = f"\n{key}"
            for port in hmap_copy[key]:
                data = f"{data}\n{port}"
            data = f"{data}\n"
            f.write(data)
            
    with open("all_config.txt",'w') as f:
        for key in d:
            data = f"\n{key}"
            for port in d[key]:
                data = f"{data}\n{port}"
            data = f"{data}\n"
            f.write(data)
    
    
        
        