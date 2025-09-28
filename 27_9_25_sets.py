# s1 = {1,2,3,4,5}
# print(type(s1))
# s2 = {1,2,3,4,5}

# print(s1==s2, s1 is s2)

# print(type(s2))

# s2 = set(['ali','akbar','ali','ahmad','farhan','farhan','awais'])

# print(type(s2))

# print(s2)

# s3= {True,False,True,False}
# print(s3)

# s4=set({})
# print(type(s4))

# s5={"Ali",3,("ali",5)}
# print(s5)

# s6={"Ali",3,["ali",5]}
# print(s6)

# try:
#     s7 = {"akbar", 5, {"ali", 9}}
#     print(s7)
# except Exception as e:
#     print(f"An Error occured: {e}")
    
# myset = set(['ali','akbar'])
# print(len(myset))
# a,b = myset
# new = {a,b}
# print(type(new))
# print(a,b)
# # -------------------------------------------
# myset = set(['ali','akbar'])
# for i in myset:
#     print(i ,end=' ')

# mysett = set(['ali','akbar'])

# rv = "ali" in mysett

# print(rv)
# ------------------------------------------------
# myset = set()
# # myset.add("ahmad")
# myset.add((8,9))
# # print(myset)
# myset.update([99,78])
# print(myset)

# -----------------------------------------------

# str1 = 'Hi i am ali'
# s1 = set(str1.split('a'))
# print(s1)

# str2 =' '.join(str1)
# print(str2)


# ---------------------------------------------------

# num_set = set([1,2,3,4,5,6,7,8,5,4,3])
# rc = 9 in num_set
# print(rc)
# rc = 9 not in num_set
# print(rc)
# print("length ", len(num_set))
# print("max ", max(num_set))
# print("min ", min(num_set))
# print("sum", sum(num_set))


# s1 = {'ali','akbar','ahmad','abdullah','farhan'}
# s2 = {'faz','waqas','wahid','saad','ali'}
# print(s1)
# print(s2)
# s3 = s1 | s2 
# print(s3)

# s4 = s1 & s2
# print(s4)

# s5 = s1.difference(s2)
# print(s5)

# s6 = s1.symmetric_difference(s2)
# print(s6)

# rc1 = {2,3,4, 6, (5,6)}
# rc2 = {2,3,4,(6, 7),(55,"777")}

# rc3 = rc1 - rc2
# print(rc3)

# rc4 = rc1.symmetric_difference(rc2)
# print(rc4)

# rc5 = s1.issuperset(s2)
# print(rc5)

# rc6 = s2.issubset(s1)
# print(rc6)


# -------------------------------------------------------------

# if 2==2:
#     print("equal")
# else:
#     print("your number is not equal to")



# try:
#     x = input("Enter the number ")
#     if x % 2 ==0:
#         print("the number is even")
#     else:
#         print("the number is odd ")
# except Exception as e:
#     print("Enter the number only")            


  
# x = input("Enter the number ")

# y = x.isnumeric()
 
# if y == True:
#     print()
#     if y % 2 ==0:
#         print("the number is even ")
#     else:
#         print("the number is odd")    
# else:
#     print()


# x = input("Enter the number: ")


# if x.isnumeric():
#     num = int(x)  
#     if num % 2 == 0:
#         print("The number is even.")
#     else:
#         print("The number is odd.")
# else:
#     print("The input is not a valid number.")


#  ---------------------------------------------------------   


# x= 49

# if x%3==0 and x%7==0:print("the number is divided by 3 and 7")
   
# elif x%3==0 :print("the number is divided by 3 ")
        
# elif x%7==0:print("the number is divisible by 7")  
             
# else:print("the number is not divided by 3 and 7")


# str = "asgdj"
# set = {1,2,3}
# tuple = (1,3,4)

# if str:
#     print(True)
# else:
#     print(False)

# if set:
#     print(True)
# else:
#     print(False)
            
# if tuple:
#     print(True)
# else:
#     print(False) 
"""
num =int(input("enter the your marks "))

if num<50:
    print("You are Fail ")
elif num<=60:
    print("your grade D")
elif num<=70:
    print("your grade C")  
elif num<=80:
    print("your grade B")
elif num<=90:
    print("your grade A")
elif num<=100:
    print("your grade A+") 
"""

 
# age = 12
# print( 'adult' if age>18 else 'child')
# email= "aliakbar@gmail.com"
# print("valid" if '@' in "aliakbar@gmail.com" else 'invalid')


# a=330
# b=330
# print("A" if a>b else print"=" if a==b else print"B"end=)

# if a>b:
#     print("A")
# else:
#     if a==b:
#         print("is equal")
#     else:
#         print("B")        

# num = 4
# i=1
# while i<=10:
#   print(num , "x" , i , "=" ,num*i)
#   i += 1


# j =1
# while j<6:
#   print(j)
#   j+=1
#   if j == 10:
#     break
  

# ------------------------------------
i=1
while i<6:
  print(i)
  i+=1
else:
     print("loop End")