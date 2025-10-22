main_dict = {
    "user1":{
        "name":"ali",
        "id":1,
        "pincode":1111,
        "balance":5000,
        "transaction":[]
    },
    "user2":{
        "name":"ahmad",
        "id":2,
        "pincode":2222,
        "balance":6000,
        "transaction":[]
    },
    "user3":{
        "name":"waqas",
        "id":3,
        "pincode":3333,
        "balance":7000,
        "transaction":[]
    },
    "user4":{
        "name":"awais",
        "id":4,
        "pincode":4444,
        "balance":8000,
        "transaction":[]
    }, 
}

print("/////////////////Main Menu/////////////////")
# while True:
print("1: Create transfer")
print("2: Change Pincode ")
print("3: Cash Withdraw ")
print("4: Check Withdraw/Transfer History ")
print("5: Check Balance ")
print("6: When did you last used Your Atm ")
print("7: Exit Atm Machine ")

choice = input("Enter what you want ")
