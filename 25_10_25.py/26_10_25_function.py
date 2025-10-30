import time 
# time.sleep(10)
# print("abc")
# def countdown(seconds):
#     while seconds:
#         print(f"Time left {seconds} seconds")
#         time.sleep(1)
#         # seconds-=1
#     print("time Up")
# countdown(int(input("Enter the time ")))        

# def simple_bot(message):
#     responses ={
#         "hello":"hi there",
#         "how are u":"fine",
#         "your age":"23",
#         "Your name":"ali",
#         "Bye":"Good Bye"
#     }
#     message=message.lower()


#     while True:
#         user_input = input("")








# def simple_bot(message):
#     responses = {
#         "hello": "hi there",
#         "how are u": "fine",
#         "your age": "23",
#         "your name": "ali",
#         "bye": "good bye"
#     }
    
    
#     message = message.lower()
    
    
#     return responses.get(message, "Sorry, I don't understand that.")



# while True:
#     user_input = input("Enter the user input ")
#     reply = simple_bot(user_input)
#     print("Bot:", reply)
#     if user_input.lower() == "bye":
#         break
# -----------------------------------------------------------------
# def romanToInt(s: str) -> int:
#     # Step 1: Map Roman symbols to their values
#     roman_values = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }

#     total = 0  # This will store the final result

#     # Step 2: Loop through the string
#     for i in range(len(s)):
#         # If the current value is smaller than the next one, subtract it
#         if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
#             total -= roman_values[s[i]]
#         else:
#             total += roman_values[s[i]]

#     return total


# # --- Main program ---
# if __name__ == "__main__":
#     # Take user input
#     s = input("Enter a Roman numeral (I to MMMCMXCIX): ").upper().strip()

#     # Convert and print the result
#     result = romanToInt(s)
#     print(f"The integer value of {s} is {result}.")


# def my_func(*args):
#     for i in args:
#         print(i , end=' ')
#     return i

# # my_func()
# print(my_func("ali","akbar"))        

# user_input = input("Enter something: ")

# def name(user_input):
#     for i in range(1, len(user_input) + 1):
#         print(user_input[:i])

# name(user_input)

# def make_pizza(size, *toppings):
#     if toppings:
#         print(f"\nI'm making your {size} pizza with {', '.join(toppings)}!")
#     else:
#         print(f"\nI'm making your plain {size} pizza! ")


# # Ask for pizza size (mandatory)
# size = ""
# while size not in ["S", "M", "L"]:
#     size = input("Enter pizza size (S/M/L): ").upper()

# # Ask for toppings
# toppings_input = input("Enter toppings separated by commas (or press Enter for none): ").lower()

# # Split toppings if provided
# if toppings_input:
#     toppings = [t.strip() for t in toppings_input.split(',')]
#     make_pizza(size, *toppings)
# else:
#     make_pizza(size)

def my_func(**kwargs):
    for arg in kwargs.items():
        print(arg)

        
my_func(a = "Learning", b = 'Is', c = 'dash') 


def myfunc(**kwargs):
    result = ""
    for arg in kwargs.values():
        print(arg)

myfunc(a = "Learning", b = 'Is', c = 'Fun', d ='with', e='shahbaz sharif')



def myconcat(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg + ' '
    return result

rv = myconcat(a = "Learning", b='Is', c='same dash')
print(rv)

    #  scope

    