import numpy as np
import subprocess
import os
import glob
directory = os.listdir('/Users/kansei.ishikawa/Desktop/kabu/')
#print(directory)
data = glob.glob("*")
file = open("da_c.txt", "w")
a = np.array([])
for i in range(0,len(data)):
    
    if data[i] == "check.py"\
       or data[i] == "download.py"\
       or data[i] == "da_c.txt":
        continue
    else:
        path = "/Users/kansei.ishikawa/Desktop/kabu/" + data[i] + "/*.csv"
        check = glob.glob(path)
        
        if len(check) == 0:
            a = np.append(a, int(data[i]))
a = np.sort(a)

for i in range(0,len(a)):
    file.write(str(a[i]) + "\n")
file.write(str(len(a)) + "\n")
