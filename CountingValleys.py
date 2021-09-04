cnt = 0
    valley = 0
    for i in path:
        if i == "U":
            if cnt == -1:
                valley += 1
            cnt += 1
        elif i == "D":
            cnt -= 1
    return valley
