x = input("Enter string:")
y = input("Enter letter from x value or any other letters: ")
begin_char = lambda a: True if a.startswith(y) else False
print(begin_char(x))
