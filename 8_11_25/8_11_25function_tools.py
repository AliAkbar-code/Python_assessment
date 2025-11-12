# from functools import reduce

# num= [1,23,4,4,5,4,3]
# rv = reduce(lambda x,y : x+y ,num)
# print(rv) 
# from functools import reduce

num1 = [-10, -20, -93, -4]
num = [-10, -20, -93, -4]

# min_rv = reduce(lambda x, y: x if x < y else y, num)
# max_rv1 = reduce(lambda x, y: x if x > y else y, num)

# print(f"The minimum value using reduce is: {min_rv}")
# print(f"The maximum value using reduce is: {max_rv1}")




t1 = ["asc","jhasdb","hdja","jasdgd"]
# rv = sorted(t1, key=lambda x: x[-1])
# print(rv)


# l = [(1,2),(3,4),(8,7),(2,5)]

# sot = sorted(l,key= lambda x: x[0])
# print(sot)

l1 = zip(num,t1,num1)
print(list(l1))