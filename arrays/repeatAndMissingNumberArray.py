# You are given a read only array of n integers from 1 to n.

# Each integer appears exactly once except A which appears twice and B which is missing.

# Return A and B.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Note that in your output A should precede B.

# Example:

# Input:[3 1 2 5 3] 

# Output:[3, 4] 

# A = 3, B = 4
from collections import defaultdict

def repeatedNumber(A):
        A = list(A)
        n = len(A)
        temp = defaultdict(lambda : 0)
        for i in A:
            temp[i] += 1
        for i in range(0, n+1):
            if temp[i] == 2:
                twice = i
            if temp[i] == 0:
                missing = i
        return(twice, missing)

A = list(map(int, input().split()))
print(repeatedNumber(A))