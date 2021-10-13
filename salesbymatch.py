import os

def sockMerchant(n, ar):
    num = []
    socks = 0
    
    #create list num with single elements
    for i in ar:
        if i not in num:
            num.append(i)
    
    #compare an element from num list with all the elements and increase the count one by one
    for i in num:
        count = 0
        for j in ar:
            if i == j:
                count += 1
            else:
                continue
            #if count is even, it is a pair
            if count % 2 == 0:
                socks += 1
    return socks
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
