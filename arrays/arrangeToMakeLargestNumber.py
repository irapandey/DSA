# Given an array of numbers, arrange them in a way that yields the largest value. For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value. And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.

def largest(arr):
    if len(arr) == 1:
        return str(arr[0])
    arr = list(map(lambda x: str(x), arr))
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] > arr[j] + arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    res = "".join(arr)
    if(res == '0' * len(res)):
        return 0
    else:
        return res


arr = list(map(int, input().split()))
print(largest(arr))