import os

def jumpingOnClouds(c):
    steps = 0
    i = 0
    while i<len(c):
        #throws list index error for the last iteration
        try: 
            #first priority is step over 2 elements
            if c[i+2] == 0:
                steps += 1
                i += 2
                continue
        except:
            break
        #else increase step over 1 elements
        steps += 1
        i += 1
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
