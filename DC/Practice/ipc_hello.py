import subprocess
command = "python ipc_namaste.py"
try:
    process = subprocess.run(command.split(), capture_output=True, text=True)
    if process.returncode == 0:
        print(process.stdout)
except Exception as e:
    print(e)