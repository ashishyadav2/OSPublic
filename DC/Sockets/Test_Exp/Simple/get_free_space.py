import math
import psutil
partitions = psutil.disk_partitions(all=True)
for i in range(len(partitions)):
    mountpoint = partitions[i].mountpoint
    disk_usage = psutil.disk_usage(mountpoint)
    total_space = math.trunc(disk_usage.total/(pow(1024,3)))
    free_space = math.trunc(disk_usage.free/(pow(1024,3)))
    print('===================================')
    print(f'Total space: {total_space}GB\nFree Space: {free_space}GB\nUsed Space: {total_space-free_space}GB')
    

