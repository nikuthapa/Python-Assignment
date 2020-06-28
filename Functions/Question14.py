def sort_list_dict (d_list):
    d_list.sort(key= lambda a: a['Id'])
    return d_list

d_list = [{'Id': 'S1', 'Subject': 'Math', 'Marks': 80}, {'Id': 'K1', 'Subject': 'Science', 'Marks': 90},
          {'Id': 'A1', 'Subject': 'Computer', 'Marks': 85}, {'Id': 'L1', 'Subject': 'Nepali', 'Marks': 70}]
print("List of dictionaries before sorting: \n", d_list)
print("\nList of dictionaries after sorting: \n", sort_list_dict(d_list))
