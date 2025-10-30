# list= [2,4,6,8,10]
# list1=[]
# for i in list:
#     list1.append(i*i)
# print(list1)

# list1 = [i*i for i in list]
# print(list1)

# list_name = ["ali","akbar"]
# first_letter = [i[0] for i in list_name]
# length_of_word = [len(i) for i in list_name]
# upper_case = [i.upper() for i in list_name]
# print(upper_case)
# print(length_of_word) 
# print(first_letter)


# num = [ 1,3,521,435,346,234,1,4234,534,5243]
# new_num = [ i for i in range(1 , 101) if (i % 3 == 0 and i % 5 == 0)]
# print(new_num)

# name = "beautiful name "
# new_namee = [ i for i in name if i  not in 'aeiou ']
# new_name = ["".join(new_namee)]
# print(new_namee)


# numbers = [ 10 , -2 , 5 , -7 , 10 ]
# new_number = [ i if i>0 else 0 for i in numbers]
# print(new_number)


# fruits = ["apple","banana","cherry"]
# new_fruits = [i[::-1] for i in fruits]
# print(new_fruits)

# pal = ["madam","level","noon","python","bob"]
# new_pal = [ i   for i in pal if i== i[::-1]]
# print(new_pal)

# a=[1,2,3]
# b = [2]
# new_a = [(j,i)  for i  in a for j in b]
# print(new_a)

# list = [1,2,3,4,5]

# new_dict = {i:i*i for i in list}
# print(new_dict)

# list1= range(1,11)
# new_list = { i:i**3 for i in list1 if (i**3 %4 ==0)}
# print(new_list)

dict = {"milk":120, "chocolate" :45, "bread":80}  
new_price = { i:dict[i]+dict[i]*0.25  for i in dict  }

print(new_price)