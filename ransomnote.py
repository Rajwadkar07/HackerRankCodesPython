def checkMagazine(a, n):
    t = a
    r = []
    flag = 0
    for i in n:
        if i in t:
            r.append(i)
            t.remove(i)
    if n == r:
        print("Yes")
    else:
        print("No")
