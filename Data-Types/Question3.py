def get_change_char(str):
    character = str[0]
    str = str.replace(character, '$')
    str = character + str[1:]

    return str

print(get_change_char('restart'))