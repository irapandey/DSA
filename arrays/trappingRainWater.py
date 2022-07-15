# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 
def trap(h):
    if h == []:
        return 0
    ans = 0
    n = len(h)
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]
    left[0] = h[0]
    for i in range(1, n):
        left[i] = max(left[i-1], h[i])
    right[n-1] = h[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(h[i], right[i+1])
    for i in range(1, n-1):
        ans += min(left[i], right[i]) - h[i]
    return ans

h = list(map(int, input().split()))
print(trap)