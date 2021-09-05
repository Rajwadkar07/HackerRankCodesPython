def hourglassSum(arr):
    sum = []
    l = 0
    for i in arr:
        l = l + len(i)
    try:
        for i in range(l):
            sum.append(arr[i][0] + arr[i][1] + arr[i][2] + arr[i+1][1] + arr[i+2][0] + arr[i+2][1] + arr[i+2][2])
            sum.append(arr[i][1] + arr[i][2] + arr[i][3] + arr[i+1][2] + arr[i+2][1] + arr[i+2][2] + arr[i+2][3])
            sum.append(arr[i][2] + arr[i][3] + arr[i][4] + arr[i+1][3] + arr[i+2][2] + arr[i+2][3] + arr[i+2][4])
            sum.append(arr[i][3] + arr[i][4] + arr[i][5] + arr[i+1][4] + arr[i+2][3] + arr[i+2][4] + arr[i+2][5])
    except:
        pass
    max = 0
    for i in sum:
        if i>max:
            max = i
    return max
