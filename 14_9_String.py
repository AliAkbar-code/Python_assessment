# # str1 = "Fash"

# # print(id(str1))

# # str1="LearningAdvanceProgramming"

# # # print(id(str1))
# # print(str1[-2:])
# # print(str1[:2])
# # print(str1[-2:-1])
# # print(str1[2:-1])

# # tem = float(23.5)
# # # print(len(tem))
# # temp2 = int(34)
# # # print(len(temp2))
# # temp3 = "hi"
# # print(len(temp3))

# # str1="LearningAdvanceProgramming"

# # print(str1[19:len(str1)])
# # print(str1.index('o'))


# str1="0123456"
 
# # print(str1[::])
# # print(str1[::1])
# # print(str1[::2])
# # print(str1[::3])
# # print(str1[0:4:2])
# # print(str1[0:len(str1):])

# print(str1[5:1:-1])
# print(str1[1:5:-1])
 
# str1 ="my name is ali"
# str2 ="What is your name "
# str3 ="this is full string", str1 + str2
# print(str3)
# first_name =input("Enter your firs name ")
# last_name = input("Enter Your last name ")
# full_name = first_name + " "+ last_name

# name='2.5'
# print(name*5)

# name= "ali akbar"
# print(name.lower())
# print(name.upper())
# print(name.capitalize())

# name1 ="ali"
# name2 ="Ali"
# print(name1.capitalize()==name2)
# print(name1.capitalize() is name2)
# print(name1.translate())

# name1="ali"
# user_name=input("Enter the username ")

# full_name = (name1.capitalize()) + (user_name.capitalize())
# print(full_name)

# print(help(type))


# name = " Ali "
# name2=name.strip()
# name2=name.lstrip()
# name2=name.rstrip()
# print(name2)
# import random
# first_name =input("enter the first name ")
# last_name = input("Enter the last name ")
# user_name = input("Enter the username ")
# random_num = random.randint(1000, 9999)
# Email = input("Enter the email ")
# user_name = (user_name + "_" (random_num)) .split(sep='_')
# first_name1 = first_name.strip().capitalize()
# last_name2 = last_name.strip().capitalize()

# full_name2 = first_name1 + last_name2
# print("First Name",first_name1)
# print("Last Name",last_name2)
# print("This is Full name", (full_name2.capitalize().strip()))
# print(f"this is username, {user_name.lower()}_{random_num}")
# print("This is the email",Email)
# print(f"is Email Valid --{'@' in Email }" )


# first_name = "Ali"
# last_name = "Akbar"
# full_name=(first_name+last_name).strip().lower()
# saved_username = full_name + "_1233"
# saved_email = "ali12@gmail.com"

# first_name = (input("enter the first name ")).strip()
# last_name = (input("Enter the last name ")).strip()
# user_name = (input("Enter the username ")).strip()
# email= (input("Enter the email ")).strip()
# email2 = email.split(sep='@')
# x=email2[1]
# print(email2)
# print(''.join(email2))

# saved_username2 = saved_username.split(sep='_')
# y=saved_username2[0]

# print(saved_username2)
# check_username = y == full_name
# print(check_username)

# rv = saved_username.startswith('aliakbar')
# print(rv)
# check_service_provider = (x == saved_email.split(sep='@')[1])
# print(check_service_provider," the service provider is ",x)

# split in one line 

# how = "this is how ".split()
# print(how)
# how ='&'.join(how)
# # how1 = how.split()
# print(how)

# find string lenghth and also the 

# str1 = "PythonProgramm"

# mid_point= len(str1)//2

# print(str1.find('r',7))
# print(str1.find('r',0 ,mid_point))
# # print(str1.find('r',mid_point))


# str1 = "hey World"
# replaced_string = str1.replace("a","z")
# print(replaced_string)
# print("str1".replace("e","z"))

raw = " Buy AAPL   $150.0  USD  2323-10-15"

cleaned = raw.strip()

print(cleaned)

no_dollar = cleaned.replace("$","")
print(no_dollar)

parts = no_dollar.split()
print(parts)

Information=f"Action:{parts[0]},symbol:{parts[1]}, Amount:{parts[2]},Currency:{parts[3]},Date:{parts[4]}"
print(Information)