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
        "Country": "Pakistan"
        }

}

def update_first_name(new_value):
    sign_up_dict["personal_info"]["first_Name"] = new_value

def update_last_name(new_value):
    sign_up_dict["personal_info"]["Last_Name"] = new_value

def update_Email(new_value):
    sign_up_dict["personal_info"]["Email"] = new_value
def update_Password(new_value):
    sign_up_dict["personal_info"]["Password"] = new_value    
def update_Age(new_value):
    sign_up_dict["personal_info"]["Age"] = new_value    
def update_Phone_Number(new_value):
    sign_up_dict["Contact_info"]["Phone_Number"] = new_value    

def update_Phone_Country_Code(new_value):
    sign_up_dict["Contact_info"]["Phone_Country_Code"] = new_value

def update_address(new_value):
    sign_up_dict["address_info"]["address"] = new_value 

def update_City(new_value):
    sign_up_dict["Contact_info"]["City"] = new_value
def update_State(new_value):
    sign_up_dict["Contact_info"]["State"] = new_value
def update_Zip_Code(new_value):
    sign_up_dict["Contact_info"]["Zip-Code"] = new_value

def update_Country(new_value):
    sign_up_dict["Contact_info"]["Country"] = new_value        

def main_menu():
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


 
while True:
    main_menu()

    rv = input("Enter the Options ")
    if rv == "13":
        print("Exit Program ")
    
    elif rv == "1":
        new_value = input("Enter the New value ")
        update_first_name(new_value)
    elif rv =="2":
        new_value = input("Enter the New value ")
        update_last_name(new_value)
    elif rv =="3":
        new_value = input("Enter the New value ")
        update_Email(new_value)
    elif rv =="4":
        new_value = input("Enter the New value ")
        update_Password(new_value)

    elif rv =="5":
        new_value = input("Enter the New value ")
        update_Age(new_value)

    elif rv =="6":
        new_value = input("Enter the New value ")
        update_Phone_Number(new_value)
    elif rv =="7":
        new_value = input("Enter the New value ")
        update_Phone_Country_Code(new_value)
    elif rv =="8":
        new_value = input("Enter the New value ")
        update_address(new_value)
    elif rv =="9":
        new_value = input("Enter the New value ")
        update_City(new_value)

    elif rv =="10":
        new_value = input("Enter the New value ")
        update_State(new_value)

    elif rv =="11":
        new_value = input("Enter the New value ")
        update_Zip_Code(new_value)
    elif rv =="12":
        new_value = input("Enter the New value ")
        update_Country(new_value)
    elif rv == "13":
        break
    
    print(sign_up_dict)                                  
    


# sign_up_dict = {
#     "personal_info": {    
#         "first_Name": "Ali",
#         "Last_Name": "Akbar",
#         "Email": "ali@gmail.com",
#         "Password": 2389478923,
#         "Age": 23
#     },
#     "Contact_info": {
#         "Phone_Number": "03123456789",
#         "Phone_Country_Code": "+92"
#     },
#     "address_info": {
#         "Address": "Lahore Cantt",
#         "City": "Lahore",
#         "State": "Pakistan",
#         "Zip_Code": 8234,
#         "Country": "Pakistan",
#         "terms and condition": True
#     }
# }

# # Update functions
# def update_first_name(new_value):
#     sign_up_dict["personal_info"]["first_Name"] = new_value

# def update_last_name(new_value):
#     sign_up_dict["personal_info"]["Last_Name"] = new_value

# def update_Email(new_value):
#     sign_up_dict["personal_info"]["Email"] = new_value

# def update_Password(new_value):
#     sign_up_dict["personal_info"]["Password"] = new_value

# def update_Age(new_value):
#     sign_up_dict["personal_info"]["Age"] = int(new_value)

# def update_Phone_Number(new_value):
#     sign_up_dict["Contact_info"]["Phone_Number"] = new_value

# def update_Phone_Country_Code(new_value):
#     sign_up_dict["Contact_info"]["Phone_Country_Code"] = new_value

# def update_address(new_value):
#     sign_up_dict["address_info"]["Address"] = new_value

# def update_City(new_value):
#     sign_up_dict["address_info"]["City"] = new_value

# def update_State(new_value):
#     sign_up_dict["address_info"]["State"] = new_value

# def update_Zip_Code(new_value):
#     sign_up_dict["address_info"]["Zip_Code"] = int(new_value)

# def update_Country(new_value):
#     sign_up_dict["address_info"]["Country"] = new_value

# # Menu function
# def main_menu():
#     print("\nMain Menu - You can select multiple options separated by commas (e.g., 1,2,3)")
#     print("1: First Name")
#     print("2: Last Name")
#     print("3: Email")
#     print("4: Password")
#     print("5: Age")
#     print("6: Phone Number")
#     print("7: Phone Country Code")
#     print("8: Address")
#     print("9: City")
#     print("10: State")
#     print("11: Zip Code")
#     print("12: Country")
#     print("13: Exit")

# # Option to function mapping
# option_functions = {
#     "1": ("First Name", update_first_name),
#     "2": ("Last Name", update_last_name),
#     "3": ("Email", update_Email),
#     "4": ("Password", update_Password),
#     "5": ("Age", update_Age),
#     "6": ("Phone Number", update_Phone_Number),
#     "7": ("Phone Country Code", update_Phone_Country_Code),
#     "8": ("Address", update_address),
#     "9": ("City", update_City),
#     "10": ("State", update_State),
#     "11": ("Zip Code", update_Zip_Code),
#     "12": ("Country", update_Country)
# }

# # Main loop
# while True:
#     main_menu()
#     options = input("Enter option numbers (comma-separated): ").split(",")

#     if "13" in options:
#         print("Exiting program.")
#         break

#     for choice in options:
#         choice = choice.strip()
#         if choice in option_functions:
#             field_name, func = option_functions[choice]
#             new_value = input(f"Enter new value for {field_name}: ")
#             func(new_value)
#         else:
#             print(f"Invalid option: {choice}")

#     print("\nUpdated Info:")
#     print(sign_up_dict)
