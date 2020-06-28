def maximum_num(x, y, z):
    tuple3 = (x, y, z)
    return max(tuple3)

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
z = int(input("Enter third number:"))
print("Maximum number: ", maximum_num(x, y, z))

              # OR


def maximum_num (x, y, z):
    if (x >= y) and (x >= z):
        return x
    elif (y >= z) and (y >=x ):
        return y
    else:
        return z
print("The maximum number is", maximum_num(3, 6, 1))