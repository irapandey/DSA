# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

def next(nums):
    end = len(nums)-1
    while end > 0 and nums[end] <= nums[end-1]:
        end -= 1
    
    if end > 0:
        pointer = len(nums)-1
        while nums[pointer] <= nums[end-1]:
            pointer -= 1
        
        nums[end-1], nums[pointer] = nums[pointer], nums[end-1]
        
    nums[end:] = reversed(nums[end:])

nums = list(map(int, input().split()))
print(next(nums))