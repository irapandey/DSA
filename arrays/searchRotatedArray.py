def search(nums, target):
    if target not in nums:
            return -1
    else:
        return nums.index(target)

nums = list(map(int, input().split()))
target = int(input())