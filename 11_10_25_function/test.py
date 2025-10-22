# n = 1
# r =1
# while (n<=3):
#     r =r *n
#     print(r ,":", n)

#     # print("hi")
#     n+=1
# # print("Go Go")  

# list = ["ali","akbar"]
# # i = 0
# # while (i < len(list)):
# #     print(list[i])
# #     i +=1
# # print("Tata Bye Bye Gya")   
# for i in list:
#     print(i)
# print("Tata Bye Bye Khatam")    
# n= 10
# a = 0
# b =1
# if a>b:
#     print("empty")
# elif a ==1:
#     print('GOod')

# for i in range(1,n):
#     j = a+b
#     print(j)
#     a = b  
#     b = j 

# n=10
# # while(n>0):
#     if (n%2 == 0):
#         print("Even")


# a= range(10)

# for i in range(0,10):
#     print(i) 

# friends = ["ali","akbar","sana","Wajeeha"]

# for j ,u in enumerate(friends):
#     print(j,u) 

# # num = [1,2,3,4,5,6,7]  
# # num1 = [] 
# # for x in num:
# #     if x % 2 ==0:
# #         print("not prime")
# #     else:
# #         print("prime")    
# # num1.append(num)    

# for i in range(-4 , 5):
#     print(i) 


# friends = ["ali","akbar","sana","Wajeeha"]
# for j in friends:
#     print(j)    


# pl = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
# i = 0
# rating = pl[0]
# while(i < len(pl) and rating >= 6):
#     print(rating)
#     i = i + 1 
#     rating = pl[i]


# squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
# ns = []
# i = 0
# while(i < len(squares) and squares[i] == 'orange'):
#     ns.append(squares[i])
#     i = i + 1
# print (ns)



# print("table of six")
# for i in range (1,11):
#     print("6","x",i,"=",6*i)



# Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]

# k,i=[],0

# while i <len(Animals):
#     j= Animals[i]
#     if (len(j)==7):
#      k.append(j)
#     i+=1
# print(k)      



# l = [1,2,3,4,5]
# l.insert(3,l.pop(1))
# print(l)


# num = [2,3,7,9,4,6]

# for i in range(len(num)):
#       mi = i

#       for j in range(i+1, len(num)):
#         if num[j]<num[mi]:
#             mi = j
#         num[i],num[mi]=num[mi],num[i]
# print(num)   




# list = ["bread","Egg","tea"]
# list1 = [100,200,300]

# j = sum(list1)
# print(j)
# tax = j*0.16

# total = j+tax


# for i in range(len(list)):
#     print(f"{list},{list1}")


# print(f"names of item {list}") 
# print(f"price of item {list1}")

# print(f"total Amount is {total}")



# grocery_names = ["Apple", "Banana", "Carrot", "Milk", "Bread"]
# grocery_prices = [144, 343, 234, 456, 7234]

# total_cost = sum(grocery_prices)
# tax = total_cost * 0.16
# total_with_tax = total_cost + tax

# print("----- Grocery Receipt -----")
# print("---------------------------")
# print(f"Total Bill:  {total_cost}")
# print(f"Total tax:  {tax}")
# print(f"Total with Tax: {total_with_tax}")

# discount = 0  # Initialize discount

# if total_with_tax >= 7000:
#     discount = total_with_tax * 0.05
#     total_after_dis = total_with_tax - discount
#     print(f"After discount, your total amount is {total_after_dis:.2f}")
# else:
#     print("No discount applied.")

# print("---------------------------")
# print("Thank you for shopping with us!")


balance = 10000
pin1 = 1234

while True:
    pin = int(input("Enter the PIN: "))
    if pin == pin1:
        print("Incorrect Pn Try again. ")
    else:
        print("")
        
    
    amount = float(input("Enter the amount to withdraw "))

    if amount <= 0:
        print("Please enter an amount greater than zer")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print(f"Withdrawal successful You withdrew ${amount}")

    choice = input("Do you want to withdraw again (yes/no): ")
    if choice == 'no':
        print(f"\nRemaining balance {balance}")
        print("Thank you for using the ATM!")
        break
    
