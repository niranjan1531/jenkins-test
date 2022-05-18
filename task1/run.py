import time
import subprocess

subprocess.run(["ls", "-l"])
subprocess.run(["docker", "ps"])
print('Start task 1')
print(time.ctime())
# using sleep() to hault the code execution
time.sleep(10)

print('End task 1')
print(time.ctime())
