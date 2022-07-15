# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

def pro(nums, i):
    res = 1
    for j in range(len(nums)):
        if i != j:
            # print(nums[j])
            res *= nums[j]
        # print(res)
    return res
            
def productExceptSelf(nums):
    if 0 in nums:
        total = 0
        ans = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(0)
            else:
                ans.append(pro(nums, i))
        return ans
    else:
        total = 1
        ans = []
        for i in nums:
            total *= i
        for i in nums:
            ans.append(total//i)
        return ans
nums = list(map(int, input().split()))
print(productExceptSelf(nums))