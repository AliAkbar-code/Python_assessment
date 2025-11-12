
# def divide(a,b):

#     return(a/b)

# a = int(input("Enter the first number "))
# b = int(input("Enter the second number "))
# print(divide(a,b))



# def con(a, b):
#     return(a + b)

# a = (1,2,3,4)
# b = (5,6,7,8)

# print(con(a,b))


def con(a, b):
    return(a + b)

a = 56
b = 98

print(con(a,b))
str = "Mary had a little lamb little lamb, little lamb Mary had a lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
passkey = "little"
def far(str,passkey):

    # words = []

    words = str.split()
    print(words) 

    l = []

    for i in words:
        if(i == passkey):
            l = words.count(i) 
            print(l)  
    print("Total Count:",l)

far(str , passkey)



