def find_even_num(x):
    even_num_list = []
    for a in x:
        if a % 2 == 0:
            even_num_list.append(a)
    return even_num_list

print("List of even number elements:", find_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 16, 18]))
