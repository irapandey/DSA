def linearMINMAX(arr):
    arr_min = arr[0]
    arr_max = arr[0]
    for i in arr:
        arr_min = min(arr_min, i)
        arr_max = max(arr_max, i)
    return (arr_max, arr_min)

def tournamentMinMax(low, high,arr):
    arr_max = arr[low]
    arr_min = arr[low]

    if low == high :
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)

    elif high == low + 1:
        arr_max = max(arr[low], arr[high])
        arr_min = min(arr[low], arr[high])
        return (arr_max, arr_min)
    else:
        mid = (low + high) // 2
        arr_max1, arr_min1 = tournamentMinMax(low, mid, arr)
        arr_max2, arr_min2 = tournamentMinMax(mid+1, high, arr)

        return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    max_arr1, min_arr1 = linearMINMAX(arr)
    max_arr2, min_arr2 = tournamentMinMax(0, len(arr) - 1,arr)
    print(max_arr1, min_arr1)
    print(max_arr2, min_arr2)
