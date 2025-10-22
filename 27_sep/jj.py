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
 elif rv =="8":
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

 



x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict) 

