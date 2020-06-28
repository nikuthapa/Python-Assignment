def multiple_items(a):
    m_num = 1   # m_num refers result of multiplications of numbers in the list.
    for n in a:   # a refers items.
        m_num = m_num * n
    return m_num

print(multiple_items([8, 2, 3, -1, 7]))