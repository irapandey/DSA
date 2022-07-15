# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.

def kLargestElement(nums, k):
    nums.sort()
    return nums[::-1][k-1]

nums = list(map(int, input().split()))
k = int(input())
print(kLargestElement(nums, k))