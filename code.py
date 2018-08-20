import subprocess

x = subprocess.getoutput("date")
print(x)

y = subprocess.getoutput("cal")
print(y)