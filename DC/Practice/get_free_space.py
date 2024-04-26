import math
import psutil
partitions = psutil.disk_partitions()
for i in range(len(partitions)):
    mountpoint = partitions[i].mountpoint
    disk_usage = psutil.disk_usage(mountpoint)
    total = math.trunc(disk_usage.total/pow(1024,3))
    free = math.trunc(disk_usage.free/pow(1024,3))
    print(f"Total: {total}\nFree: {free}\nUsed: {total-free}")
    print("=================================================")  