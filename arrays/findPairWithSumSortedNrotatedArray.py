# Given an array that is sorted and then rotated around an unknown point. Find if the array has a pair with a given sum ‘x’. It may be assumed that all elements in the array are distinct.

# Examples : 

# Input: arr[] = {11, 15, 6, 8, 9, 10}, x = 16
# Output: true
# There is a pair (6, 10) with sum 16

# Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 35
# Output: true
# There is a pair (26, 9) with sum 35

# Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 45
# Output: false
# There is no pair with sum 45.

def pairNsum(arr,x):
    for i in arr:
        temp = abs(x-i)
        if temp in arr:
            return(i,temp)
    return False
        

arr = list(map(int, input().split()))
x = int(input())
print(pairNsum(arr, x))