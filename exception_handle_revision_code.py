
mylist = [5, 33, 21]
print(mylist[8])



far = float(input("Enter Fahrenheit Temprature: "))
cel = (far - 32.0) * 5.0/9.0
print (cel)


try:
    far = float(input("Enter Fahrenheit Temprature: "))
    cel = (far - 32.0) * 5.0/9.0
    print (cel)

# This block will exectue the program without any crash    
except:
    print("An error occurred")
    

print("GR8 going")


try:
    z = 45 / 0
    print(z)
    a = 34 + 'hello'
    

except:
    print("An error occurred")


z= 5
b = int(input("enter"))
a = z
try:
    z = a / b
    calate_salary(b)
    print(z)
   #a = 34 + 'hello'
    
except Exception as error:
    print("Exception occured: ", error)
print(b)
    



try:
    list1 = [1, 5, 9]
    print("List Elements are: ", list1)
    #5/0

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
except TypeError:
    print("TypeError Occurred and Handled")
except IndexError:
    print("IndexError Occurred and Handled")
else:           
    print("This will execute if try clause does not raise an exception")

try:
    list1 = [1, 5, 9]
    print("List Elements are: ", list1)
    #5/0

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
except TypeError:
    print("TypeError Occurred and Handled")
except IndexError:
    print("IndexError Occurred and Handled")
else:           
    print("This will execute if try clause does not raise an exception")
finally:
    print("This will always be executed")




age = -1
#age = 5
if age < 0:
    raise Exception("x should not be negative. The value of age was {}".format(age))
print("Program continues as age is positive")


age = -1
#age = 5
if age < 0:
    raise Exception("My name is fasih")
print("Program continues as age is positive")


x = "hello"
#x = 5fasih
if not type(x) is int:
  raise TypeError("Only integers are allowed")
print("Program continues as x is a number")



# Example 1:
age = -1
age = -5
assert age > 0 , 'age should be positive'
print("Program continues as age is positive")

#Example 2: 
x = "hello"
#x = 5
assert type(x) is int, 'x must be integer'
print("Program continues as x is a number")









