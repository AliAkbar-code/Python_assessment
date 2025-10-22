# list = []
# print(list)

# list1 = [1,2,3,4,5]
# print(type(list1))
# list2 = [1.2,2.2,3.3,4.4]
# print(type(list2))
# list3=["hello","hi","happy"]
# print(type(list3))
# list4=[True,False,True]
# print(type(list4))

# listF = [ 1,1.3,"hello",True,[12,4.5,"hi"]]
# print(listF)

# list = [


#     ["Title:Python",["Author:","Me"],"intro"], # 0 index
# # 1 index
#     [
#         "What is Python?\nPython is a popular programming language. It was created by Guido van Rossum, and released in 1991.\n","It is used for:\nweb development (server-side)\nsoftware development\nmathematics\nsystem scripting.\n"
#          ,"What can Python do?\nPython can be used on a server to create web applications.\nPython can be used alongside software to create workflows.\nPython can connect to database systems. It can also read and modify files.\nPython can be used to handle big data and perform complex mathematics.\nPython can be used for rapid prototyping, or for production-ready software development.\n"],
# # 2 index
#         [
#             "Why Python?\nPython works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).\nPython has a simple syntax similar to the English language.\nPython has syntax that allows developers to write programs with fewer lines than some other programming languages.\nPython runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.\nPython can be treated in a procedural way, an object-oriented way or a functional way.\n"
#          ,"Good to know\nThe most recent major version of Python is Python 3, which we shall be using in this tutorial.In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files"
#          ,"Python Syntax compared to other programming languages\nPython was designed for readability, and has some similarities to the English language with influence from mathematics.\nPython uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.\nPython relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose."]

#    ]

# print(list[0][1][1])

# x=[1,2,3,4]
# y=[1,2,3,4,5]

# print(x is y)
# print(x==y)
# print(id(x),id(y))
# x=y
# print(x==y)
# print(x is y)
# print(x)
# print(id(x),id(y))


# list =["Ali",24,60]
# a,b,c=list

# list1=a,b,c
# print(type(list1))
# print(a,b,c)
# print(f"""
# Name:{a}\nAge:{b}\nWeight:{c}
# """)
# print(list1)


# list=["Ali",24,60,["Akbar","Nothing"]]

# # print(list,list[1],list[3][1])
# print(f"""
# Full Name is: {list[0]} {list[3][0]}
# """)
# print(list)


# names=["Ali","Ahmad","Umair","Faz","Abdullah","Hamid"]

# user_name=input("Enter the your name ")
# position = names.index(user_name)+1
# print("your Position is ",names.index(user_name))

# print(f"""
# Your Position is {position}
# """)

# list1=["a","b","c","d","e","f","g"]
# print(list1[0:len(list1):2])
# print(list1[3:5],list1[3])
# print(f"""
# {list1[3][4][0][5]}
# """)

# print(list1[::-1])

# list1=["a","b","c","d","e","f","g"]

# print(list1[2:6:-1])

# dish=["hi","hello","you","we"]
# print(dish)
# dish1=dish[::-1]
# print(dish1)

# all_dish=dish+dish1
# print(all_dish)



# list1=["Python","Computer","Math"]
# list1[0:1]=["Isl","Urdu","Eng","chem"]
# print(list1)

# list1[2]=["Ai"]
# print(list1)


dish="['hi', 'hello', 'you', 'we', 8, 7, 6]".replace("[","").replace("]","")
print(dish)
new_var=dish.replace("'","")
new_var=new_var.split(", ")
print(new_var)
print(type(new_var))

