# numbers = [1, 2, 3, 4]

# try:
#     a, b, u = numbers
# except ValueError as e:
#     print(f"Error unpacking list: {e}")
#     # Optionally, handle the situation or assign default values
    

# ---------------------------------------------------------------
# x = 1, 2, 3 

# try:
#     print("Original tuple:", x) 
#     x = list(x)  
#     print("Converted to list:", x)  
# except TypeError as e:
#     print(f"Error: {e}")  

# -------------------------------------------------------------------------
# try:
#     list1=[1, 2, 3, 4, 5]
#     print(len(list1))
#     print(list1[len(list1)])
# except IndexError as e:
#     print(f"ERROR: {e}")


# ------------------------------------------------------------------------------


# try:
#     mylist = [27, 4.5, 'Fasih', 64, 'UnNabi', 19, 'Fasih']
#     index = mylist.index('Fasih1')  
#     print(f"Index of 'Fasih1': {index}")
# except ValueError as e:
#     print(f"Error: {e}")
# ---------------------------------------------------------------------------------

# try:
#     list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#     print(list1[10])
# except IndexError as e:
#     print(f"Error: {e}")
# ----------------------------------------------------------------------------------


# try:
#     list2 = ['learning', 'is', 'fun', 'with', 'Fasih', 'UnNabi', 'fun']
#     x = list2.remove('fun')  
#     print("After remove('fun'):", list2)
#     print("Return value of remove() is:", x) 
# except ValueError as e:
#     print(f"Error: {e} - 'fun' is not in the list")
# -------------------------------------------------------------------------------------

# try:
#     mylist = ['learning', 'is', 'fun', 'with', 'Fasih', 'Un Nabi']
#     del mylist
#     print(mylist)
# except NameError as e:
#     print(f"Error: {e}")
# ---------------------------------------------------------------------------------------


# try:
#     mylist = ['learning', 'is', 'fun', 'with', 'Fasih']
#     a, b, c, d, e = mylist # the number of variables on the left must match the number of elements in the list
#     my_list = [a, b, c, d, e]
#     list2 = ["Fasih", 90, 5.5, 28,'Un Nabi']
#     name, wieght, height, age, last_name = list2
#     list3 = name, wieght
#     print(wieght)
#     if age > 18:
#         print (a, d, e)
#     print(type(a))
# except SyntaxError as e:
#     print(f"Error: {e}")
