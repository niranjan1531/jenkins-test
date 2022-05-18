import time
import subprocess

subprocess.run(["ls", "-l"])
subprocess.call("docker ps -a", shell=True, stdout=output, stderr=output)
print('Start task 1')
print(time.ctime())
# using sleep() to hault the code execution
time.sleep(10)

print('End task 1')
print(time.ctime())
