import os

def repeatedString(s, n):
    count = 0
    #calculate number of a in input string
    for i in s:
        if i == "a":
            count += 1
    l = len(s)
    #multiplier to get desired length of string
    multiplier = n // l
    #remainder of partial string to be added
    remainder = n % l
    #number of a when reminder is 0
    final = count * multiplier
    #if remainder is more than 0 and the remaining substring contains a, add 1 to final
    if remainder!=0:
        for i in range(remainder):
            if s[i] == "a":
                final += 1
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
