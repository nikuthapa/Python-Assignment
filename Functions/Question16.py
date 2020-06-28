list3 = [1, 2, 4, 6, 7, -3, -5, -9]
square_numbers = list(map(lambda a : a ** 2, list3))
cube_numbers = list(map(lambda a : a ** 3, list3))
print("Actual list: ", list3)
print("\nList after squaring every number element in actual list:", square_numbers)
print("\nList after cube of every number element in actual list:", cube_numbers)