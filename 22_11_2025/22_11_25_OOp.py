# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#         # class attribute
#         self.engine = "12V"

# my_car = Car("Tesla","Pink") 
# print(my_car.brand,my_car.model,my_car.engine)


# class Stu:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# student_name = Stu("ali",18)
# print(student_name.name,student_name.age)        
        

# class circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2   


# cr = circle(10)
# print(cr.area())     


# class Bankaccount:
#     def __init__(self,owner,Balance):
#         self.owner = owner 
#         self.Balance = Balance 
#     def deposit(self,amount):
#        self.Balance +=amount
#        return self.Balance
#     def __str__(self):
#         return f"{self.owner} has Balance: {self.Balance}"   
#     def withdraw(self,withdrawal):
#         if withdrawal >self.Balance:
#          return "insufficient Balance"
#         else:
#            self.Balance -=withdrawal
#            return f"You withdraw {withdrawal} and your remainig Balance is {self.Balance}"


# user = Bankaccount("Ali" ,10000)
# print(user)
# print(user.withdraw(50000)) 
# print(user.deposit(15000))        
        
# class Animal:
#     def speak(self):
#         return "i can speak "
        

# class Dog(Animal):
#     def meow(self):
#         print("meow meow me me moew ") 

# s1 = Dog()
# print(s1.speak())
# print(s1.meow())               

#  class Employee:
#     def __init__(self,name,salary):

#         self.name = name 
#         self.salary = salary

#     def show_salary(self):
#         return f"My name is {self.name} and my Salary is {self.salary}"

# class manager(Employee):
#     def __init__(self, name, salary,department):
#         super().__init__(name, salary)
#         self.department = department

#     def manage(self):
#      return f"I manage the {self.department} department "
    
# s2 = manager("Ali",20,"Computer science" )
# print(s2.show_salary()) 
# print(s2.manage()) 
# 
#  

# class vehicle:
#     def __init__(self,type,name , model , color):
#         self.type = type
#         self.name = name
#         self.model = model
#         self.color = color 

#     def show_details(self):
#         return f"The type is {self.type} and name is {self.name} and model is {self.model} and color is {self.color}"

# class tesla(vehicle):
#     def __init__(self, type, name, model, color,door , fule_type):
#         super().__init__(type, name, model, color)
#         self.door = door
#         self.fule_type= fule_type

    

#     def show_tesla(self):
#         return f"The type is {self.type} and model is {self.model} and color is {self.color} having {self.door} doors and fule Type is {self.fule_type}"   


# s1 = tesla("car","Tesla",2025,"red",4,"electric")
# print(s1.show_details())
# print(s1.show_tesla())



# class animal:
#     def move(self):
#         return f"You move"
#     def eat(self):
#         return f"you eat"
    
# class cat(animal):
#     def move():
#         return f"child move"

# s = cat()
# print(cat.move()) 
# # 
# # # Base class
# class Payment:
#     def process(self, amount):
#         print(f"Processing generic payment of ${amount}")


# # Subclass 1: Credit Card Payment
# class CreditCardPayment(Payment):
#     def process(self, amount):
#         print(f"Processing Credit Card payment of ${amount}...")
#         print("Verifying card details...")
#         print("Transaction approved!")


# # Subclass 2: PayPal Payment
# class PayPalPayment(Payment):
#     def process(self, amount):
#         print(f"Processing PayPal payment of ${amount}...")
#         print("Connecting to PayPal account...")
#         print("Payment successful!")


# # Subclass 3: Bank Transfer Payment
# class BankTransferPayment(Payment):
#     def process(self, amount):
#         print(f"Processing Bank Transfer of ${amount}...")
#         print("Verifying bank account details...")
#         print("Funds transferred successfully!")


# # Function that uses polymorphism
# def make_payment(payment_method: Payment, amount):
#     payment_method.process(amount)


# # ----------- Testing the system ------------

# cc = CreditCardPayment()
# paypal = PayPalPayment()
# bank = BankTransferPayment()

# make_payment(cc, 500)
# print()
# make_payment(paypal, 250)
# print()
# make_payment(bank, 1000)
       



# class PetrolEngine:
#     def start_engine(self):
#         return "Petrol engine started with a roar!"
# class ElectricEngine:
#     def start_engine(self):
#         return "Electric engine started silently!"

# class car:
#     def __init__(self, engine):
#         self.engine = engine

#     def start(self):
#         return self.engine.start_engine()
    
# petrol_car = car(PetrolEngine())
# print(petrol_car.start())
# electric_car = car(ElectricEngine())
# print(electric_car.start()) 


class book:
    def __init__(self,title , pages ):
        self.title = title
        self.pages = pages

    def __sub__(self,others):
        return self.pages - others.pages

book1 = book("harry",900) 
book2 = book("harry",90)

tp = book1 - book2
print(tp) 
