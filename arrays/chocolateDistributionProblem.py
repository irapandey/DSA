# Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

# Each student gets one packet.
# The difference between the number of chocolates in the packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.

def minChocolate(arr,m):
    arr.sort()
    if(len(arr) < m):
        return -1
    res = 10000000
    for i in range(len(arr)-m):
        temp = abs(arr[i] - arr[i+m-1])
        res = min(res, temp)
    return res
        


arr = list(map(int, input().split()))
# arr = [12, 4,  7,  9,  2,  23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = int(input())
# m = 7
print(minChocolate(arr,m))