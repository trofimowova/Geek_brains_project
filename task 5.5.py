with open("numnum", 'r') as m_s:
    a = m_s.read()
    print(a)
    b = a.split()
    print(b)
    sum = 0
    for  x in range(len(b)):
        sum = sum + int(b[x])
    print(sum)

    