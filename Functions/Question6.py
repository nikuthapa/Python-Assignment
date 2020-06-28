x = int(input("Enter start-number: "))
y = int(input("Enter end-number: "))
z = int(input("Enter value-number: "))
def check_range_ofNum (start, end, number):
    if start <= number <= end:
        print("{} is in the range ({}, {})".format(number, start, end))

    else:
        print("{} is not in the range ({}, {})".format(number, start, end))

check_range_ofNum(x, y, z)