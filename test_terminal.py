import subprocess

test1 = subprocess.run(["ls", "-l"], capture_output=True, text=True)
test2 = subprocess.run(["echo", "hola"], capture_output=True, text=True)
print(test2.stdout)