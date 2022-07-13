# Write a function to reverse the given array

def iter_rev(arr):
    res = []
    for i in range(len(arr) -1, -1, -1):
        res.append(arr[i])
    return res

def recurr_rev(low, high, arr):
    if low >= high:
        return

    temp = arr[low]
    arr[low] = arr[high]
    arr[high] = temp

    recurr_rev(low+1, high-1, arr)
    return arr


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(arr)
    print(iter_rev(arr))
    print(recurr_rev(0, len(arr)-1, arr))
