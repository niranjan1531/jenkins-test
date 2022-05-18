import time
import subprocess
import os


subprocess.run(["ls", "-l"])
os.system('docker ps')
subprocess.call("docker ps -a", shell=True)
print('Start task 1')
print(time.ctime())
# using sleep() to hault the code execution
time.sleep(10)

print('End task 1')
print(time.ctime())
