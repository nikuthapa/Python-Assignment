def factorial_of_num(x):
    f = 1
    if x < 0:
        print("There is no factorial for negative numbers.")

    elif x == 0 and x == 1:
        print("The factorial of 0 is 1")

    else:
        for i in range(1, x + 1):
            f = f * i
        print("The factorial of", x, "is", f)

x = int(input("Enter a number: "))
factorial_of_num(x)