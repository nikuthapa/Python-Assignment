
def str_made (p):
    if len(p)<2:
        return ''

    return p[0:2] + p[-2:]

print(str_made('Python'))
print(str_made('Py'))
print(str_made('w'))

