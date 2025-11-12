# # threading 

import threading
import time
import os

# def clean_room():
#     print("Clean")

#     time.sleep(3)
#     print("Cleaned")

# def do_homeworks():
#     print("home works ")
#     time.sleep(3)  
#     print("home works done ")

# t1 = threading.Thread(target=clean_room)
# t2 = threading.Thread(target=do_homeworks)  

# t1.start()
# t2.start() 

# t1.join()
# t2.join()
# time.sleep(5)
# print("All task done ")


# def color(picture):
#     print(f"Color {picture}")
#     time.sleep(2)
#     print(f"printed {picture}")


# picture =["sun","sky","cloud"]

# threads=[]

# for i in picture:
#     t  = threading.Thread(target=color, args=(i,))
#     threads.append(t)
#     t.start()
# for thread in threads:
#     thread.join()

import urllib.request 
import os 
os.makedirs('download', exist_ok=True)

myurl = 'https://gist.githubusercontent.com/kiranzaman/79bac8e2ca947c7db5f25598ce85fc9d/raw/bf7c14aeaa68d644fda770896928bfa9b9b159e9/myfamily.csv'

urllib.request.urlretrieve(myurl,'download/family.csv')

print("download Done")