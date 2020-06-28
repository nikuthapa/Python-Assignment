def ar_func (x):
    return lambda a: a * x

n = int(input("Enter a number:"))
out_come = ar_func(n)
print("Result of 2 multiplied with given number =", out_come(2))