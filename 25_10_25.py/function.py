# def sum(a,b):
#     total = a+b
#     return total
# print(sum(10,20))

# def mylenght(x):
#     length=0
#     for i in x:
#         length+=1
#     return length
#         # print(length) 
# print(mylenght("ali"))
# print(type(mylenght("ali")))



# def greeting (a):
#     """
#     Ch sab
#     """
#     print(f"{a} Hello Oye")
# print(greeting())

# print(print.__doc__)

# def sum_of_square():
#     a=[1,2,3,4,5]
#     x=0
#     for i in a:
#         x =x+(i*i)
#     return x
#     print(x)    

# print(sum_of_square())  

# def myfunc(a) :
#     name="ali"
#     return name
# a = "Akbar"
# print("before ",a)

# x = myfunc(a)
# print("after ",x)

# pass by value 

# def func(x,y,z):
#     x = x-1
#     y = y+1
#     z = z+1
#     print(x,y,z)

# a=10
# b=20
# c=30

# pass by reference

# print(func(a,b,c))
# print(a,b,c)
    
# def func1(l2):
#     l2[2]="x"
# my_list = ["a","b","c","d"]
# print(my_list)
# func1(my_list)
# print(my_list)


def func(list2):
    l3 = list2[1:4]
    l3[0]="x"
    print("list l3 is local to the function having:  ",l3)
list1 = ["a","b","c","d"] 
print("before Calling ",list1)  

