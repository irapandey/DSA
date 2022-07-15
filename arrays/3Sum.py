# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[1] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

def threeSum(nums):
    nums.sort()
    res = set()
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target2 = 0 - nums[i]
        j = i + 1
        right = n - 1
        while j < right:
            temp = nums[j] + nums[right]
            if temp < target2:
                j += 1
            elif temp > target2:
                right -= 1
            else:
                res.add((nums[i], nums[j], nums[right]))
                j += 1
                while j < right and nums[j] == nums[j - 1]:
                    j += 1
    return res   


nums = list(map(int, input().split()))
print(threeSum(nums))