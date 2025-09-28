order = input("Enter 'asc' for ascending or 'desc' for descending: ").strip().lower()

if order == 'asc':
    # Bubble sort ascending
    n = len(num)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
            j += 1
        i += 1
    print("Sorted in ascending order:", num)
elif order == 'desc':
    # Bubble sort descending
    n = len(num)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if num[j] < num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
            j += 1
        i += 1
    print("Sorted in descending order:", num)
else:
    print("Invalid input. Please enter 'asc' or 'desc'.")
num = [3,2,1]

for x in num:
    # print(x)
    if num[0]>num[1]:
        num[1]=num[0]
    if num[1]>num[2]:
        num[0]=num[2] 