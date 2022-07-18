from collections import Counter

def printDuplicate(s):
    temp = Counter(s)
    for k,v in temp.items():
        if v > 1:
            print(k)

    return 0

s = str(input())
print(printDuplicate(s))
