import os
file_path = os.path.join(os.getcwd(),'python.ipynb')
file_size = os.path.getsize(file_path)
print(f'{file_size} KB')