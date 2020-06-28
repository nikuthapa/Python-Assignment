list_num = [1, 2, 3, 4 ,5 ,6, 7, 8, 9, 12, 14, 19, 21, 24, 27]
even_number = list(filter(lambda a: a % 2 == 0, list_num))
odd_number = list(filter(lambda a: a % 2 != 0, list_num))
print("Actual list of integers before filter: \n", list_num)
print("\nList filtering with even numbers elements from actual list: \n", even_number)
print("\nList filtering with odd numbers elements from actual list: \n", odd_number)
