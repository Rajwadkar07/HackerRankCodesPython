def repeatedString(s, n):    
    l = 0
    count = 0
    if len(s) == 1:
        return n
        exit
    while l<n:
        s += s
        l = len(s)
    for i in range(n):
        if "a" == s[i]:
            count += 1
    return count
