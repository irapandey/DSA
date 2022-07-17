# iven a collection of Intervals, the task is to merge all of the overlapping Intervals.

# Example 1:

# Input:
# Intervals = {{1,3},{2,4},{6,8},{9,10}}
# Output: {{1, 4}, {6, 8}, {9, 10}}
# Explanation: Given intervals: [1,3],[2,4]
# [6,8],[9,10], we have only two overlapping
# intervals here,[1,3] and [2,4]. Therefore
# we will merge these two and return [1,4],
# [6,8], [9,10].
# Example 2:

# Input:
# Intervals = {{6,8},{1,9},{2,4},{4,7}}
# Output: {{1, 9}}
# Your Task:
# Complete the function overlappedInterval() that takes the list N intervals as input parameters and returns sorted list of intervals after merging.

def thirdElement(elem):
    return elem[0]

def overlap(arr):
    arr.sort(key=thirdElement)
    res = []
    res.append(arr[0])
    for i in range(1,len(arr)):
        curr = arr[i]
        top = res[-1]
        if top[1] >= curr[0]:
            res[-1] = [top[0],max(top[1],curr[1])]
        else:
            res.append(curr)
    return res
		

n = int(input())
arr = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
print(overlap(arr))