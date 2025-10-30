def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    first = 1
    second = 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second


while True:
    n = int(input("Enter number of steps: "))
    print("Number of distinct ways to climb:", climbStairs(n))

    choice = input("Do you want to try again? (y/n): ").lower()
    if choice == 'n':
        break
