import os
import subprocess
print(os.getcwd())
print(os.listdir())
subprocess.run("dir", shell=True)