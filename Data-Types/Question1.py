def count_num_char(str):  # str for string.
    dict = {}  #dict for dictionaries
    for x in str:
        keys = dict.keys()
        if x in keys:
            dict[x] += 1
        else:
            dict[x] = 1

    return dict

print(count_num_char('google.com'))