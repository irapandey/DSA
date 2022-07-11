import sys 

MIN_INT = -sys.maxsize - 1


def maxSubArray(arr):
    local_max = 0
    global_max = MIN_INT
        
    for i in range(len(arr)):
        local_max = max(arr[i], arr[i] + local_max)
        if local_max > global_max:
            global_max = local_max
                
    return global_max

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(maxSubArray(arr))