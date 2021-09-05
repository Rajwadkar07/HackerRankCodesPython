def jumpingOnClouds(c):
    j = 0
    for i in range(len(c)):
        k = 0
        try:
            if c[k+2] == 1 or c[k+1] == 0:
                c = c[k+1::]
            elif c[k+2] == 0:
                c = c[k+2::]
            j += 1
        except:
            pass
    return j
