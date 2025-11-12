# try:
#  1/0
#  print("this")
#  if True:
#     print("as")
# except:
#  print("Exception part")
# try:
#     far = float(input("ENter the numbeer "))
#     cel = (far - 32.0)* 5.0/9.0
#     print(cel) 
# except Exception as a:
#     print(a)       
# # print("Outside")    

# try:
#     # a=z
#     # print(f)
#     # a = a +"asd"
#     l = [1,2,3]
#     print(l[1])
# except ZeroDivisionError:
#     print("zero error ")
# except NameError:
#     print("name error ")
# except TypeError:
#     print("type error ")
# except IndexError:
#     print("index Error ")
# except ModuleNotFoundError:
#     print("module error ")                   
# else:
#     print("tata bye bye ") 
# finally:
#     print("this is finally part ")    


# import sys
# assert sys.platform !="win32",'only run on mac' 
# print("program is runing ")
import random

num = random.randint(1,10)
print(num)

try:
  user_input = int(input("Enter the user number any between 1 to 10 "))
  if user_input <=0 or user_input >10:
    print("this number is not allowed")
  elif num == user_input:
    print("you win ")
  else:
    print("you lose ")
except Exception as x:
  print(f"invalid input {x}")
