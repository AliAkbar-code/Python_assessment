# # sa = lambda num : num **2
# # print(sa(5) )



# # my_sum = lambda a,b,c : a+b+c
# # print(my_sum(2,9,6))


# # Even = lambda a: a%2 == 0 
# # print(Even(6))

# # func = lambda a : a[::-1]
# # print(func("hi"))

# # func2 = lambda b : len(b)
# # print(func2("ali"))


# # def add (a,b):
# #     return a + b
# # print(add(6,3))
# # def sub (a,b):
# #     return a - b
# # print(sub(6,3))
# # def mul (a,b):
# #     return a * b
# # print(mul(6,3))
# # def div (a,b):
# #     return a // b
# # print(div(6,3))

# # add = lambda a,b :a+b
# # print(add(6,3))
# # sub = lambda a,b :a-b
# # print(sub(6,3))
# # mul = lambda a,b :a*b
# # print(mul(6,3))
# # div = lambda a,b :a//b
# # print(div(6,3)) 


# # def cal(op ,a ,b):
# #     return op(a,b)


# # print(cal(lambda a,b : a+b, 8,9))

# # l = [1,2,3,4,5]

# # def sqr (x):
# #     return x **2

# # mo = map(lambda x:x**2,l)

# # l1 = list(mo)
# # print(l)
# # print(l1)

# list1  = [ "ali","akbar"]
# result = map(lambda a :"Dr "+ a.upper(), list1)
# result = list(result)
# print(result)

# cel_temp = [23,34,32,12,24]

# result1=map(lambda b : (9/5) * b +32 , cel_temp )
# result1 = list(result1)
# print(result1)

# num = [1,2,3]
# result2 = map(lambda c : "Number : " + str(c),num)
# result2=list(result2)
# print(result2)

# data = ["apple ","   Kiwi  ","Mango   "]

# result3 = map(lambda d : d.strip().capitalize(),data)
# result3 = list(result3)
# print(result3) 
# marks = [34, 45, 56, 32, 54, 76]

# result4 = map(lambda e: "Fail" if e < 40 else ("Distinction" if e > 75 else "Pass"),marks)

# result4 = list(result4)
# print(result4)


# listmy = [1, -4, 5, 7, 4, -5, 4, -5]

# final = list(filter(lambda y: y >= 0, listmy))

# print(final)

a = input("Enter the number")
print(a)
# if (a%2==0):
#     print("The number is Even")
# else:
#     print("The number is odd")