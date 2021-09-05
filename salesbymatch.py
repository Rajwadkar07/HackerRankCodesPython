def sockMerchant(n, ar):
    num = []
    cnt = 0
    for i in ar:
        if i not in num:
            num.append(i)
    for i in num:
        ind_cnt = 0
        for j in ar:
            if i == j:
                ind_cnt += 1
            else:
                pass
        if ind_cnt >= 2:
            cnt += ind_cnt//2
    return cnt
