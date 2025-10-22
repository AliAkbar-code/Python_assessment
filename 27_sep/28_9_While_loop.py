# i = 1
# while i<6:
#     print(i)
#     i+=1
#     if i==2:
#         continue
# else:
#     print("End")   


# fruits = ["apple","banana","cherry","avacado"]
# for x in fruits:
#     if x.startswith("a"):
#         print("this fruit start with the  a-->",x)
#     if x.startswith("a") or x.startswith("e") or x.startswith("i") or x.startswith("o") or x.startswith("u"):
#         print("these are start with vowel letter",x)   



# fruits = ["apple","banana","cherry","avacado"]
# for x in fruits:
#     if x.startswith("a"):
#         print("this fruit start with the  a-->",x)
#     if x.startswith("a") or x.startswith("e") or x.startswith("i") or x.startswith("o") or x.startswith("u"):
#         print("these are start with vowel letter",x)



# name = "ali akbar"
# for a in name:
#     # print(a)
#     list=[name]
#     print(list)
    
# a_count = name.count("a")
# print(f"{a_count}") 
 
# name = "ali akbar"

# name = name.replace(" ", "")

# most_repeated_letter = ''
# max_count = 0


# for letter in set(name):
#     count = name.count(letter)
#     if count > max_count:
#         max_count = count
#         most_repeated_letter = letter

# print(f" Most repeated letter is '{most_repeated_letter}' (appears {max_count} times).")

# -------------------------------------------------------------------------------------------

# name = "aliakbbbbbbbbbbbbbbar"
# most_repeated=[]
# max_count=0

# for letter in set(name):
#     # print("letter------",letter)
#     count = name.count(letter)
#     # print("this is count---------------------",letter,count)
#     if count>max_count:
#         max_count= count
#         # print("max--------------",max_count)
#         # print("letter------------",letter)
#         most_repeated= letter
#         # print("most repeated-----------",most_repeated)

# print(f"the most repeated letter is {most_repeated} and the total number is {max_count}")       

# ---------------------------------------------------------------------
# num = [3,2,1]

# for x in num:
#     if x==max(num):
#      print(max(num))


# -----------------------------------------------------
# num = [35,67,34,567,234,4654,474,52,425,436,345,24,634,6]

# for x in range(len(num)):
#     # print(x)
#     for j in range(len(num)-1):
#         # print(j)
#         if num[j]>num[j+1]:
#             num[j],num[j+1]=num[j+1],num[j]

# print(num)            
# ----------------------------------------------------

# fruits = ["apple", "banana", "cherry", "avacado"]
# for x in fruits:
#   if x == "cherry":
#     continue
#   print(x)


# print("-----------------------------------")

# fruits = ["apple", "banana", "cherry", "avacado"]
# for x in fruits:
#   print(x)
#   if x == "cherry":
#     continue

# ------------------------------------------------

# for x in range(3,33,3):
#     print(x)

# user_input = int(input("enter the number "))  
# for x in range(user_input,(user_input*10)+user_input,user_input):
#     print(x)    
#  solve this with try except and again user to enter right input on number 
player_name = ["ali","fakhar","zaman","babar","azam","saim","ayub","salman","agha","rizwan"]

# user_input = int(input("Enter the player name "))


while True:
 try:
        user_input= int(input("Enter the number here "))
        index_list = user_input - 1
    # for y in range(len(player_name)-1):
        if index_list==0:
           print(player_name[index_list],"Goal Keeper")
        elif index_list <= 3:
              print(player_name[index_list],"Defender")
        elif index_list <= 6:
         print(player_name[index_list],"Mid Filed")
        elif index_list <= 9:
         print(player_name[index_list],"forward")    
        else:
         print("not in team")
        break
 except Exception as e:
   print("Invalid Input")
 