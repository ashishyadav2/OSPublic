import subprocess
command = "python namaste.py"
try:
    process = subprocess.run(command.split(), capture_output=True, text=True)
    if process.returncode == 0:
        print(process.stdout)
    else:
        print("Cannot process your request! :(")
        
except Exception as e:
    print(e)