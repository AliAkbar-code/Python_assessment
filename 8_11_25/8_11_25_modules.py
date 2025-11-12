# from math import *
# print(dir()) 
# # print(m.floor(0.999999999999999999999))
# # print(m.factorial(9))

# import random

# rv = random.randrange(1,10,2)
# print(rv)

# import time
# # print("ali")
# sec = time.ctime(time.time())
# print(sec)

# import datetime
# rv1 = datetime.datetime.now()
# print(rv1)

# import calendar

# rv2 = calendar.isleap(2001)
# print(rv2)

import os
cw = os.getcwd()
print(cw)
print(os.listdir(os.getcwd()))
import shutil
# os.mkdir("newdir")

# for f in os.listdir("newdir"):
#     ext=(f.split("."))
#     os.chdir(r'D:\8_11_25\newdir')

#     os.mkdir(ext[1])

import os
import shutil

base = r"D:\8_11_25\newdir"

for f in os.listdir(base):
    src = os.path.join(base, f)
    if os.path.isdir(src):
        continue  

    nam, ext = os.path.splitext(f)
    folder = ext[1:].upper() 
 
    dest_folder = os.path.join(base, folder)
    os.makedirs(dest_folder, exist_ok=True)  

    shutil.move(src, os.path.join(dest_folder, f))

print(" All files sorted by extension!") 
