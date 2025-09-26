# import platform
# import os
# import sys

# print("=== Basic OS Info ===")
# print(f"Platform Identifier: {sys.platform}")
# print(f"System: {platform.system()}")
# print(f"Node Name (Hostname): {platform.node()}")
# print(f"Release: {platform.release()}")
# print(f"Version: {platform.version()}")
# print(f"Machine: {platform.machine()}")
# print(f"Processor: {platform.processor()}")

# print("\n=== More Detailed Info ===")
# print(f"Platform: {platform.platform()}")
# print(f"Architecture: {platform.architecture()}")

# # If available, use uname for even more info
# try:
#     print("\n=== Uname Info ===")
#     uname_info = os.uname()
#     print(f"Sysname: {uname_info.sysname}")
#     print(f"Nodename: {uname_info.nodename}")
#     print(f"Release: {uname_info.release}")
#     print(f"Version: {uname_info.version}")
#     print(f"Machine: {uname_info.machine}")
# except AttributeError:
#     print("\nos.uname() not available on this OS (usually only on Unix-like systems).") 

# 2 list exception handling----------------------------------------------------------------
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


# tuple exception handling------------------------------------------------------------------




# numbers = (10, 20, 30)

# try:
    
#     numbers[2] = 15
# except TypeError as e:
#     print(f"Error: {e} - Tuples are immutable, cannot modify an element.")

#     t1 = (1, "Hello", [8, 'OK', 6], (1, 2, 'BYE'), 5.5)

# try:
#     t1[2] = 'FASIH' 
# except TypeError as e:
#     print(f"Error: {e} - Tuples are immutable.")

# t1 = ("FASIH", 30, 5.5, (10, 'Nawaz'))


# try:
#     print(t1[2])  
# except IndexError as e:
#     print(f"Error: {e} - Index out of range.")

# # Accessing the element at index 3 (Valid, nested tuple)
# try:
#     print(t1[3])  # Expected output: (10, 'Nawaz')
# except IndexError as e:
#     print(f"Error: {e} - Index out of range.")

# try:
#     print(t1[5]) 
# except IndexError as e:
#     print(f"Error: {e} - Index out of range.")


# try:
#     print(t1[3][2])  
# except IndexError as e:
#     print(f"Error: {e} - Index out of range.")


# try:
#     print(t1[0][10])  
# except IndexError as e:
#     print(f"Error: {e} - Index out of range.")



# myfamily = ("Nawaz", 'AHMED', 'ALI')
# print("\nOriginal tuple:", myfamily)

# try:
#     temp_list = list(myfamily)      
#     temp_list.insert(2, 'FASIH')     
#     myfamily = tuple(temp_list)      
#     print("Modified tuple:", myfamily)
# except Exception as e:
#     print(f"Unexpected error: {e}")

