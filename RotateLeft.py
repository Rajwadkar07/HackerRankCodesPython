def rotLeft(a, d):
    for i in range(d):
        temp = a[0]
        a.remove(temp)
        a.append(temp)
    return a
