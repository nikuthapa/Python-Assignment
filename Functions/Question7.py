def calculate_num_ofString_letters (a):
    upper_case = 0
    lower_case = 0
    for x in a:
        if x.isupper():
            upper_case = upper_case + 1
        elif x.islower():
            lower_case = lower_case + 1
        else:
            pass

    print("Actual string is", a)
    print("The number of upper case letters: ", upper_case)
    print("The number of lower case letters: ", lower_case)

calculate_num_ofString_letters('"The quick Brown Fox"')