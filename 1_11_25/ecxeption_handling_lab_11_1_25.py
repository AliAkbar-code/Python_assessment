# def divide(x,y):
#     try:
#         result = x / y
#         return result
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#         return None

# x=int(input("Enter the x value"))
# y=int(input("Enter the y value"))
# print(divide(x,y)) 





# def square(num):
#     try:
#         if num <=0:
#             print("number must be greater than 0")
#         else:    
#          result = num** 0.5
#          print(f"Result {result}")
#     except ValueError:
#         print(" Invalid input Please enter a positive integer or a float value.")
# # Test case
# num=float(input("Enter the number"))
# square(num)



# def calculation(num):
#     try:
#         result = num / (num - 5)
#         print (f"Result {result}")
#     except Exception as e:
#         print("An error occur")

# user_input = float(input("Enter a number "))
# calculation(user_input)



x= "hi"

assert  type(x) is int , 'number is not integar  ' 
print("bye")
