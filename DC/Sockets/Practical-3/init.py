import numpy as np
import copy
import argparse
if __name__ == "__main__":
    file_path = 'start.txt'
    with open(file_path,'r') as f:
        nodes_list = f.read().split('\n')
        nodes_list = [line for line in nodes_list if len(line)>1]
    nodes = len(nodes_list)
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
    new_dict = {}
    i=0    
    to_write = ''
    for key in d:
        keys = list(d.keys())
        keys.remove(key)
        port_list = d[key]
        in_ports = ''.join([f'{str(port)}\n' for port in hmap_copy[key]])
        to_write += f'{key} (config.txt)\n'
        for ind,port in enumerate(port_list):
            to_write+=f'{keys[ind]}:{port}\n'

        to_write+='\n'
        to_write+=f'{key} (in.txt)\n'
        to_write+=in_ports
        i+=1
        to_write+='\n\n'
    
    with open('init_file.txt','w') as f:
        f.write(to_write)
