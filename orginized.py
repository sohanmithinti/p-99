import os
import shutil
path = input("Enter the name of the folder to be organized: ")
listFiles = os.listdir(path)
print(listFiles)
dest = input("Enter the name of the folder to be moved to destination: ")
filesDest = os.listdir(dest)
print(filesDest)
