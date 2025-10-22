# this_dic = {
#     1: "Ali",
#     "name":"Akbar",
#     "age": 23,
#     "age":63,
#     "pass":True,
#     "subject":["Maths","Eng","urdu","pak Study"]
# }
# print(this_dic["name"])
# print(this_dic["subject"][1])
# print(len(this_dic))

# dic = dict(name = "ali", age=34, country = "pakistan")
# print(dic["country"])
# # p = this_dic.get("subject")
# # print(p)
# p = dic.keys()
# print(p)

# car = {
#     "brand":"Honda",
#     "price":32748,
#     "year":2001
# }
# x = car.keys()
# print(x)

# car["color"]= "white"
# print(x)
# y = car.values()
# print(y)

# car["color"] = "black"
# print(y)

# z = car.items()
# print(z)

# car["color"]= "red"
# print(z)

# if "Honda" in y:
#     print(f"yes brand exists")
#     print(f"the year of the car is",car["year"])
       
# car.update({"color":"pink"})
# print(z)



# a = {"type":"fruit" , "name": "Cherry"}
# b= a.get("type") =="berry"
# print(b)

# remove

# car = {
#     "brand":"Honda",
#     "price":32748,
#     "year":2001
# }
# car["color"]="red"
# print(car)

# x=car.pop("brand")
# print(x)
# print(car)
# y=car.popitem()
# print(car)
# del car["price"]
# print(car)
# car.clear()
# print(car) 

# loop

# car = {
#     "brand":"Honda",
#     "price":32748,
#     "year":2001
# }
# car["color"]="red"
# for x ,y in car.items():
#     print(x,y)

# AttributeError

# for y in x:
#     print(y.value()) 


# car2 = car
# car2 = car.copy()
# car["color"]="pink"
# print("car 2 ",car2)
# print("car 1 ",car)   


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# for i in myfamily.values():
#     print(i,["name"],["year"])


# for i , j in myfamily.items():
#     print(i)
#     for y in j:
#         print(y + )
# j = 1

# for i in myfamily.values():

#     print(j ,i["name"],i["year"])
#     j+=1

# this is the dict so i want to when user want to change the number than take input from user and than change in the code , now tell  me how i can achieve this 
sign_up_dict ={
    "personal_info":{    
        "first_Name": "Ali",
        "Last_Name": "Akbar",
        "Email": "ali@gmail.com",
        "Password": 2389478923,
        "Age":23
        },

    "Contact_info": {
        "Phone_Number": "03123456789",
        "Phone_Country_Code": +92
        },

    "address_info":{
        "Address": "Lahore Cantt",
        "City": "Lahore",
        "State": "Pakistan",
        "Zip_Code": 8234,
        "Country": "Pakistan",
        "terms and condition":True
        }

} 
# without funtions 
# print(sign_up_dict.keys())

# x = sign_up_dict.keys()
# # print(x)
# print(sign_up_dict["personal_info"].keys())

# change = input("what u want to change ")
# new_value = input("Enter the New value ")

# sign_up_dict["personal_info"].update({change:new_value})
# if "Phone_Number" in sign_up_dict.keys():
    # print(sign_up_dict)
# print(sign_up_dict["personal_info"])
for x,y  in sign_up_dict.items():
    print(x)

    for j in y:
        print(j)
while True:
    print("Main Menu")
    print("1: First Name ")
    print("2: Last Name ")
    print("3: Email ")
    print("4: Password ")
    print("5: Age ")
    print("6: Phone Number ")
    print("7: Phone_Country_Code ")
    print("8: Address")
    print("9: City ")
    print("10: State ")
    print("11: Zip_Code ")
    print("12: Country")
    print("13: Exist")

    rv = input("Enter the Option ")
    if rv == "1":
        new_value = input("Enter the New value ")
        sign_up_dict["personal_info"].update({"First_Name":new_value})
    elif rv =="2":
        new_value = input("Enter the New value ")
        sign_up_dict["personal_info"].update({"Last_Name":new_value})
    elif rv =="3":
        new_value = input("Enter the New value ")
        sign_up_dict["personal_info"].update({"Email":new_value})
    elif rv =="4":
        new_value = input("Enter the New value ")
        sign_up_dict["personal_info"].update({"Password":new_value})

    elif rv =="5":
        new_value = input("Enter the New value ")
        sign_up_dict["personal_info"].update({"Age":new_value})

    elif rv =="6":
        new_value = input("Enter the New value ")
        sign_up_dict["Contact_info"].update({"Phone_Number":new_value}) 
    elif rv =="7":
        new_value = input("Enter the New value ")
        sign_up_dict["Contact_info"].update({"Phone_Country_Code":new_value})
    elif rv =="8":
        new_value = input("Enter the New value ")
        sign_up_dict["address_info"].update({"address":new_value})
    elif rv =="9":
        new_value = input("Enter the New value ")
        sign_up_dict["address_info"].update({"City":new_value})

    elif rv =="10":
        new_value = input("Enter the New value ")
        sign_up_dict["address_info"].update({"State":new_value})

    elif rv =="11":
        new_value = input("Enter the New value ")
        sign_up_dict["address_info"].update({"Zip-Code":new_value})
    elif rv =="12":
        new_value = input("Enter the New value ")
        sign_up_dict["address_info"].update({"Country":new_value})
    elif rv == "13":
        break
    
    print(sign_up_dict)                                  
    
