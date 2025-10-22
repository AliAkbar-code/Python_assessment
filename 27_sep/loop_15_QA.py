# # Q1.
# num = int(input("Enter a number: "))
# limit = int(input("Enter the limit: "))
# print(f"Multiples of {num} up to {limit}:")
# for i in range(num, limit+1, num):
#     print(i)

# # # Q2. 
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operator = input("Enter the operator (+, -, *, /): ")
# if operator == "+":
#     print(f"{num1} + {num2} = {num1 + num2}")
# elif operator == "-":
#     print(f"{num1} - {num2} = {num1 - num2}")
# elif operator == "*":
#     print(f"{num1} * {num2} = {num1 * num2}")
# elif operator == "/":
#     if num2 != 0:
#         print(f"{num1} / {num2} = {num1 / num2}")
#     else:
#         print("Error Division by zero")
# else:
#     print("Invalid operator")

# # # Q3.
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range "))
# for i in range(end, start-1, -1):
#     print(i)

# # Q4. 
# patients = "hi i am ali"
# names = patients.split()
# for name in names:
#     print(name)

# # Q4.
# patients = "hi i am ali akbar "
# names = patients.split()
# for name in names:
#     for j in name:
#         print(j, end=" ")
#     print()

# # Q5. 
# num = int(input("Enter a number for table: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# # Q6. 
# for i in range(1, 6):
#     print("* " * i)

# # # Q7.
# num = int(input("Enter a number to check if it's prime: "))
# if num <= 1:
#     print("Not a Prime Number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")

# # Q8. 
str = input("Enter a string to reverse: ")
rst = ""
for i in str:
    rst = i + rst
print( rst)

# # Q9. 
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# # Q10. 
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print(f"{len(words)} words")
# # Q11. 
# size = int(input("Enter the size of the square: "))
# for i in range(size):
#     if i == 0 or i == size - 1:
#         print("*" * size)
#     else:
#         print("*" + " " * (size-2 ) + "*")

# # Q12. 
# num = input("Enter a number to check if it's a palindrome: ")
# if num == num[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# # Q13. 
# num = input("Enter a number to find the sum of digits ")
# total = sum(int(digit) for digit in num)
# # print(digit)
# print(f"Sum of digits: {total}")

# # Q14.
# num = int(input("Enter a number "))
# rev_num = 0
# while num > 0:
#     digit = num % 10
#     rev_num = rev_num * 10 + digit
#     num //= 10
# print(f"Reversed number {rev_num}")

# # Q15.
# numbers = list(map(int, input("Enter a list of numbers separated by space ").split()))
# # numbers = list(int(input("Enter the number ")).split())
# numbers = list(set(numbers))  
# numbers.sort()
# print(f"Second largest number: {numbers[-2]}")
