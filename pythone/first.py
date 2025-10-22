"""
input("my name is ali")
no_of_instructor = "Ali Akbar"
no_of_instructor
type(no_of_instructor)
a,b,c = 2,5,3.2

print( 'a=' ,a, 'b', b, 'c=', c)

 
y=6
print(id(x) , id(y)) 
print(dir())
newvar= 20

print(dir())
del y

print(y)
name = [0,1,4]
print(id(name))
print(name)
name[2] = 20
print(name)
print(id(name))



a= 3.30
b = 1.10 + 2.20
print(b)
c=(a==b)
print(a,b,c)
print (c)

a =4//2
b= 4//2.0
print(a,b)
print(type(a), type(b))

x= 21
y = float(x)
print(type(y),y)

a = 5
print(a)

z= bool(a)
print(type(z),z)

num = 396

t= str(num)
name = "Ali Akbar"
print("my name is " ,{name}, type(t),t)


x=90
x+=5
print (x)


x=8
y=10
print(x>y or x<y )
print not(x<y)
print(x>y)
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)


x=True
y=False
print(x and y, x or y,not x, not y)

num =3
print(2>3 and 4<5 or not(num<0 and True))



x=3
y=0
print((x<=6) or (y!=0) or (x/y))

x=10
y=4
print(~x)
"""
age = input("enter your age")
your_age = int(age)
current_age = 2025

print("your age is",current_age - your_age)