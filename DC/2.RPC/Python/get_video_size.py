import os
file_path = os.path.join(os.getcwd(),'client.py')
file_size = os.path.getsize(file_path)
print(f'{file_size} KB')