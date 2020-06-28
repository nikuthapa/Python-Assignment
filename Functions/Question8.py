def take_list_uniqueEle (a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b


print("The unique elements from the list is", take_list_uniqueEle([1, 2, 3, 3, 3, 3, 4, 5]))