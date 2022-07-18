def asciiCal(string):
    ans1 = 1
    ans2 = 0
    for i in string:
        ans1 *= ord(i)
        ans2 += ord(i)
    return ans1, ans2

def groupAnagram(strs):
    hashmap = {}
    ans = []

    for i in strs:
        ordVal = asciiCal(i)
        if ordVal in hashmap:
            hashmap[ordVal].append(i)
        else:
            hashmap[ordVal] = [i]
    for j in hashmap.values():
        ans.append(j)
    return ans

strs = list(input().split())
print(groupAnagram(strs))