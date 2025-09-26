help(tuple)

a,b,c,d = 1,2,3,3

x = a,b,c,d
type(x)

t1 = (1, 2, 3, 4, 5) 
t1 = 1, 2, 3, 4, 5
print("t1: ", t1)

t2 = (2.3, 5.6, 1.8)  
print("t2: ", t2)

t3 = ('hello', 'this', 'F', 'good show') 
print("t3: ", t3)

t4 = (True, False, True)    
print("t4: ", t4)


print("Type of t4 is: ", type(t4))



t5 = ()
print("t5: ", t5)

t6 = (25,)       
print("\nt6: ", t6)
print(type(t6))

t1 = ("FASIH", 30, 5.5, (10,'Nawaz'))
print(t1)



t1 = (1, "Hello", [8, 'OK', 6], (1, 2, 'BYE'), 5.5)
print("t1: ", t1)
print("Type of t1 is: ", type(t1))
print(t1[2][1])

t1 = ("FASIH", 30, 5.5)
print("t1: ", t1)

numbers = (2, 3, 1)
a = (2, 3, 1)
b = (2, 3, 1)
id(a), id(b), a is b, a == b

numbers = list(numbers)
type(numbers)

numbers = (10, 20, 30)
numbers[2] = 15    # this will generate an error

numbers = (10, 20, 30)
numbers = (1, 2, 3)  # A tupple can be reassigned
numbers

t1 = (1, "Hello", [8, 'OK', 6], (1, 2, 'BYE'), 5.5)
t1[2][1] = 'Not OK'         # will work fine
t1

type(t1[2])

t1[2] = 'FASIH'

# Like Lists, Tuples allow duplicate elements
names = ('FASIH', 'Aqsa', 'Sana', 'FASIH', 'Wajeeha')
print(names)

a = (1,2,3,(4,5),(6,7,8,9),10,11)
b = (1,2,3,(4,5,(6,7,8,(9,10,11))))
a, b

t1 = ('learning', 'is', 'fun', 'with', 'FASIH')
a, b, c, d, e = t1 # the number of variables on the left must match the length of tuple
print (a, c, e)
print(type(a))

t1 = a,b,c,d,e
print(t1)
print(type(t1))

t1 = ("FASIH", 30, 5.5, (10,'Nawaz'))

print(t1[2])       
print(t1[3])      

print(t1[0][2])              
print(t1[3][1][7])            
print(t1[2])

t1 = ("FASIH", 30, 5.5, (10,'Nawaz'))
print(t1[-1])                #accessing last element
print(t1[-2])                #accessing second last element

help(t1.index)

mytuple = (27, 4.5, 'FASIH', 64, 'Nawaz', 19, 'aqsa')
print("\nmytuple: ", mytuple)
print("mytuple.index(3): ", mytuple.index('FASIH'))  

t1 = ('a','b','c','d','e','f','g','h','i')
t1

t1[::]

t1[3:]

t1[:4]

t1[2:5]

t1[:-2]

t1[-1]

t1

# Slicing by using strides
print(t1[::])  # A default step of 1
print(t1[::1])  # A step of 1
print(t1[::2])  # A step of 2
print(t1[::3])  # A step of 3

print(t1[::-1]) # Take 1 step back each time
print(t1[5:1:-1]) # Take 1 step back each time
print(t1[2:10:-1])
print(t1[::-2]) # Take 2 steps back

t1 = (1, 2, 3, 4, 5, 6, 7)

a = (1,2,3)
b = a + (4,5)
c = (0,) + b
a, b, c

food_items1 = ('fruits', 'bread', 'veggies')
food_items2 = ('meat', 'spices', 'burger')
food = food_items1 + food_items2
print(food)

# You can concatenate two heterogeneous tuples
t1 = (5, 3.4, 'hello')
t2 = (31, 9.7, 'bye')
t3 = t1 + t2
print(t3)

num1 = (1,2,3)
num2 = num1 + (4, 5, 6, (7, 8))
print (num2)

name = ('FASIH', 'Nawaz', 'Hrm')
a = name * 3
print(a) 

#tuple of 100 K's
buf = ('K',)
newbuf = buf * 100
print(newbuf)
type(newbuf)

myfamily = ("Nawaz", 'AHMED', 'ALI')
print("\n myfamily tuple: ", myfamily)
myfamily.insert(2,'FASIH') # will generate an error as tuple object has no attribute 'insert'


tuple1 = ('learning', 'is', 'fun', 'with', 'FASIH', 'Nawaz')

tuple1 = (1, 2, 3, 'FASIH')
del tuple1
print(tuple1)



str1 = 'Learning is fun'    #this is a string

print("Original string: ", str1, "and its type is:  ", type(str1))
t1 = tuple(str1)
print("t1: ", t1, "and its type is:  ", type(t1))



str1 = ""
help(str1.split)

str1 = 'Learning is fun'    #this is a string
print(str1.split(' '))
t1 = tuple(str1.split(' ')) # The split() method returns a list, which you can typecast to a tuple
print(t1)
print(type(t1))

str2 = "Advanced Python is GR8 Course"    #this is a string
t2 = tuple(str2.split('c'))
print(t2)
print(type(t2))

str = "" # not a good thing to do 
help(str.join)

t1 = ('This', 'is', 'getting', 'more', 'and', 'more', 'interesting')
t1

str2 = ' '.join(t1)
str2, type(str2)

delimiter = " # "
str3 = delimiter.join(t1)
print(str3)
print(type(str3))



t1 = (3, 8, 1, 6, 0, 8, 4,6)
rv = t1.index(6)
print(rv)

t1 = (3, 8, 1, 6, 8, 0, 8, 4)
rv = t1.count(8)
print(rv)

t1 = (3, 18, 1, 6, 0, 8, 4)
print("length of list: ", len(t1))
print("max element in list: ", max(t1))
print("min element in list: ",min(t1))
print("Sum of element in list: ",sum(t1))

t1 = (3, 8, 1, 6, 0, 8, 4)
rv1 = 9 in t1 
print(rv1)

rv2 = 9 not in t1
print(rv2)


t2 = ("XYZ", "ABC", "MNO", "FASIH")
rv3 = "FASIH" in t2
print(rv3)

rv3 = "FASIH" in t2
print(rv3)



str2 = 'hello'
print(id(str1), id(str2))

print (str1 is str2)  
print (str1 == str2)  



t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(id(t1), id(t2))

print (t1 is t2)   
print (t1 == t2)   




t1 = (3, 8, 1, 6, 0, 8, 4)

print("Original Tuple = ", t1)


list1 = sorted(t1)
list2 = sorted(t1, reverse=True)

print("Ascending Sort: ", list1)
print("Descending Sort: ", list2)





t1 = ("XYZ", "ABC", "MNO", "FASIH")
print("Original Tuple: ", t1)

list1 = sorted(t1)
list2 = sorted(t1, reverse=True)

print("Ascending Sort: ", list1)
print("Descending Sort: ", list2)



t1 = ('ccc', 'aaaa', 'd', 'bb')
sorted(t1)


t1 = ('ccc', 'aaaa', 'd', 'bb')
sorted(t1, key=len,reverse=True)

def last(s):
    return s[-1]

t1 = ('abcz', 'xyza', 'bas', 'FASIH')
rv = sorted(t1, key=last)
print(rv)
print(t1)

tupe1 = (11,23,9)
min(tupe1)

 