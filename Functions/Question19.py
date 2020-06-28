from functools import reduce

fibonacci_s = lambda x: reduce(lambda a, _: a + [a[-1] + a[-2]], range(x - 2), [0, 1])

n = int(input("Enter a number:"))

print("Fibonacci series:", fibonacci_s(n))