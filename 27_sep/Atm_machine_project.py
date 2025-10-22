

name = input("enter the name ")
Id = int(input("enter the id "))

pin = int(input("enter the 4 digits Pin "))
amount = int(input("Enter the starting amount "))

accounts = [
    [name , Id , pin , amount]
]


print(f"Your Account Created Successfully ")
print(f" Your Id {Id} Name {name} your Pin {pin} Your Amount {amount}")


# login system 

login = False
user = None

login_id = int(input("enter the id "))
Usr_pin = int(input("enter your pin here "))

if  login_id == accounts[0][1]  and   Usr_pin ==  accounts[0][2]:
    login = True
    print("Login success ")
else:
  
   print("not ")


print("\nATM Menu")
print("1.Check Balance")
print("2.Cash Withdraw")


option = input("enter the choice ")

if option == "1":
    print(f"Your Account Balance is {accounts[0][3]}")

elif option =="2":
 withdraw_amount = int(input("Enter the amount "))

 if withdraw_amount <= accounts[0][3]:
    accounts[0][3] -= withdraw_amount
    print(f"Your remainig blance is {accounts[0][3]} is withdraw ")
 else:
    print("Insufficent Amount")    
elif option == "3":
 reciver_id = int(input("Enter the reciver id here "))
 transfer_amount = int(input("Enter the amount "))
 if transfer_amount <= accounts[0][3]:
    accounts[0][3]-=transfer_amount
    print(f"the amount ")

else:
   print("bilkul khtm")



   