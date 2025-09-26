# list2 = []
# print(type(list2))

# list1 = [1,2,3,4,5]   
# print(list1)


# ---

# list1 = [1,2,3,4,5]  
# print(list1)

# list2 = [3.7, 6.5, 3.8, 7.95 ]   
# print(list2)

# list3 = ["hello", "this", "F", "good show"]   
# print(list3)

# list4 = [True, False, True]   

# list5 = []   
# print(list5)

# print(type(list5))

# ------

# list1 = ["Fasih", 90, 5.5, [28,'Un Nabi']]
# list =[
#     [["Title Economics", "Authors: Fasih", "Intro"], ["This book is for learning economics", ""]],
#     [
#         "", 
#     """ \n"""
# ],[]]
# print(list1[3][0]) 
# print(list[0][0])
# print(type(list1))


# name = input("Please enter your name ")
# empty_list = [name]

# empty_list[0]=name
# print(empty_list)


# hetrogenous

# list1 = ["Fasih", 30, 5.5]
# allowed_host = ["my_linked.com", "fasihunnabi.com"]
# list2 = ["ali", 28, 5.7]
# print(list1 + list2)
# print("list1: ", list1)

# x = [1, 2, 3]
# y = [1, 2, 3]
# print(id(x), id(y), x is y, x==y)

# # Integers
# a = 1000
# b = 1000
# print("----------------------Integer-------------------------------")
# print(a == b)  # True - same value
# print(a is b)  # False - different objects in memory
# print("-----------------------Integer------------------------------")

# print("----------------------String-------------------------------")
# # String
# str1 = "hello"
# str2 = "hello"
# print(str1 is str2)  # True - interned strings
# print("----------------------String-------------------------------")

# print("----------------------Lists-------------------------------")
# # Lists with same content
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# print(list1 == list2)  # True - same values
# print(list1 is list2)  # False - different list objects
# print("----------------------Lists-------------------------------")

# # Same object reference
# list3 = list1
# print(list1 is list3) 
# print(id(list1) , id(list3))  

# print(id(list1) == id(list3))  


# numbers = [10, 20, 30, 40, 50]
# print(id(numbers))
# numbers[2] = 555
# print("numbers: ", numbers)
# print(id(numbers))

# b = [1,2,3,[4,5,[6,7,8,[9,10,11]]]]
# print(b[3][2][3][2])

# ------
# mylist = ['learning', 'is', 'fun', 'with', 'Fasih']
# a, b, c, d, e = mylist # the number of variables on the left must match the number of elements in the list
# my_list = [a, b, c, d, e]
# list2 = ["Fasih", 90, 5.5, 12,'Un Nabi']
# name, wieght, height, age, last_name = list2
# list3 = name, wieght
# print(wieght)
# if age > 18:
#     print (a, d, e)
# else:
#     print("you are under Age")
#     print(type(a))

# tuple1 = a,b,c,d,e
# print(tuple1)
# mylist2 = list(tuple1)
# print(mylist2)
# print(type(mylist2))
# -------
#You can access elements of list using indexing which starts from zero
# list1 = ["Fasih", 90, 5.5, [10,'Un Nabi']]
# print(list1[3])

# #accessing Nested list element
# print(list1[0][2])              #accessing third element of string at index 0
# print(list1[3][1]) 



# # negative access
# list1 = ["Fasih", 30, 5.5, [10,'Nawaz']]
# print(list1[-1][-2])                #accessing last element
# print(list1[-2])  


# ------
# list1 = ['a','b','c','d','e','f','g','h','i']
# print(list1[::-1])  # A default step of 1
# print(list1[::1])  # A step of 1
# print(list1[::2])  # A step of 2
# print(list1[::3])  # A step of 3

# list1 = ['a','b','c','d','e','f','g','h','i']

# print(list1[::3])
# print(list1[3:6])
# print(list1[2:8:-1])
# print(list1[-1:-3:-1])
# feast = ["biryani", "roti", "korma", "haleem", "dessert"]
# print(feast[::-1])
# --------------------------------

# a = [1,2,3]
# b = a + [4,5]
# x="asdgjagd"
# b = a +(x.split())
# print(b)
# # Add some elements to the beginning of an existing list using concatenation operator
# c = [0] + b
# a, b, c
#  
# ---------------------------------

# num1 = [1,2,3]
# num3 = [4, 5, 6, [7, 8]]
# num2 = num1 + num3[:3] + num3[3]
# print(num2)

# --------------------------------------------

# repeating
# name = ['Fasih', 'Aqsa', 'Sana']
# a = name * 3
# print(a)

# # adding element
# mylist = ['advacned python', 'machine learning', 2, 5, 7]
# # Let us change the second element of this list
# mylist[1] = 'my addition'

# print(mylist)

# --------------------------------------

# mylist = ['data science', 'machine learning', 2, 5, 7]
# mylist[0:2] = ['english', 'urdu','hi'] # Note we are replacing two elements with two elements
# print(mylist)


# # append-----------------------------------
# list1 = [2, 4, 6, 8]
# list1.append(4.631)
# print(list1) 
# list1.append('hello')
# print(list1)  


# list1 = [2, 4, 6, 8]
# team2 = [
#     ["Babar", "Rizwan", "Shahee"],
#     [45, 34, 17]
# ]

# player_names_list = ["Babar", "Rizwan", "Shaheen"]
# player_score_list = [45, 34, 17]
# team3 = []
# team3.append(player_names_list)
# team3.append(player_score_list)
# print(team3[0][2])
# team3[0].append("Salman")
# team3[0].insert(5, "Fakhar Zaman")
# team3[1].append(56)
# team3[1].append(33)

# print(team3)
# list1.append([4.631, 'hello'])
# print(list1)



# extend---------------------------------------

# fruits = ['apple', 'banana', 'cherry']
# vegs = ['potato', 'tomato', 'radish']
# fruits.extend(vegs)
# fruits

# insert-----------------------------------

# myfamily = ["Shifa", 'Abdul Ahad', 'Aaraiz']
# myfamily.insert(2,['Irfan','Kashif'])
# print(myfamily)

# Pop------------------------------

# list1 = ['learning', 'is', 'fun', 'with', 'Fasih', 'Un Nabi']
# print("Original list: ", list1)
# x  = list1.pop()
# print("\nAfter pop(): ", list1)
# print("Element popped is: ", x)

# remove---------------------------------------

# list2 = ['learning', 'is', 'fun', 'with', 'Fasih', 'Un Nabi', 'fun']
# print("\nOriginal list: ", list2)
# #list2[2].remove()
# x = list2.remove('fun')

# print("After remove('fun'): ", list2)
# print("Return value of remove() is: ", x)

# del----------------------------------------

# list3 = [1,2,3,[53, 41, 99, 12], 8,9]
# print("\nOriginal list", list3)
# del list3[3]
# print("After del list1[3] the list becomes", list3)

# list convert----------------------------------

# str1 = 'Learning is fun'    #this is a string
# print(type(str1))
# print("Original string: ", str1, "and its type is:  ", type(str1))
# l1 = list(str1)
# l2 = str1.split()
# print(l2)
# print("l1: ", l1, "and its type is:  ", type(l1))

# deep and shallow copy--------------------------------

# list1 = [1, 2, 3, 4]
# list2 = list1

# # Both variables point to same memory object, so have the same ID
# print('ID of Old List:', id(list1))
# print('ID of New List:', id(list2))

# list1 = [1, 2, 3, 4]
# list2 = list1[:]

# # Both variables point to different memory objects, so have the different ID
# print('ID of Old List:', id(list1))
# print('ID of New List:', id(list2))

# import copy
# list1 = [1, 2, 3, 4]
# list2 = copy.copy(list1)

# # Both variables point to different memory objects, so have different ID
# print('ID of Old List:', id(list1))
# print('ID of New List:', id(list2))

# import copy
# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_list = copy.deepcopy(old_list)
# [23, 44, 66]
# [25, 46, 66]
# # Both variables point to different memory object, having their own object elements
# print('ID of Old List:', id(old_list))
# print('ID of New List:', id(new_list))

# # sorting a list-------------------------------------------
# list_num = [3, 8, 1, 6, 0, 8, 4]
# print("Original numbers list: ", list_num)

# list_num.sort()
# print("Ascending Sort: ", list_num)

# list_num.sort(reverse=True)
# print("Descending Sort: ", list_num)

# # sorting custom-----------------------------------------------

# list1 = ['ccc', 'aaaaa', 'd', 'bb']
# list1.sort()
# print(list1)

# list2 = ['ccc', 'aaaaa', 'd', 'bb']
# list2.sort(key=len)
# print(list2)


# compare----------------------------------

x = 'hello'
y = 'helllo'
print (x is y) # is operator is checking the memory address (ID) of two strings
print (x == y)