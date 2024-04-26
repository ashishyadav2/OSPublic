import os
file = os.path.join(os.getcwd(),"rpc_server.py")
size = os.path.getsize(file)
print(size)
