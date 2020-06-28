a = input("Enter string value to check:")
s_num = lambda a: a.replace('.', '', 1).isdigit()
s_num1 = lambda a: s_num(a[1:]) if a[0] == '-' else s_num(a)
print(" Get Result:", s_num1(a))
