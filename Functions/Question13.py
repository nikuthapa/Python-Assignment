def sort_list_tup (data_list):
    data_list.sort(key= lambda a: a[1])
    return data_list

data_list = [('Apple', 50), ('Mango', 23), ('Biscuits', 45), ('Orange', 15), ('Pineapple', 33) ]
print("List of tuples before sorting: \n", data_list)
print("\nList of tuples after sorting: \n", sort_list_tup(data_list))
