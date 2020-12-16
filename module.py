import os
import shutil
x = os.path.exists("data.txt")
print(x)
y = os.path.splitext("module.txt")
print(y)
z = os.listdir()
print(z)
source = "c-99"
destination = "c-99.txt"
shutil.move(source, destination)
