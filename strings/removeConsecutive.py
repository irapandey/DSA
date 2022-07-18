def removeCons(S):
    res = S[0]
    last = S[0]
    for i in S:
        if i != last:
            res += i
            last = i
    # print(res)
    return res

S = str(input())
print(removeCons(S))