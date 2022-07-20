# Given a string str of length N, you have to find number of palindromic subsequence (need not necessarily be distinct) which could be formed from the string str.
# Note: You have to return the answer module 109+7;
 

# Example 1:

# Input: 
# Str = "abcd"
# Output: 
# 4
# Explanation:
# palindromic subsequence are : "a" ,"b", "c" ,"d"
 

# Example 2:

# Input: 
# Str = "aab"
# Output: 
# 4
# Explanation:
# palindromic subsequence are :"a", "a", "b", "aa"
 
def countPs(s):
    mod = 10 ** 9 + 7
    n = len(s)
    memo = [[0 for i in range(n+2)]for j in range(n+2)]
    
    for i in range(n):
        memo[i][i] = 1
        
    for l in range(2, n+1):
        for i in range(n):
            k = l + i - 1
            if k < n:
                if s[i] == s[k]:
                    memo[i][k] = memo[i][k-1] + memo[i+1][k] + 1
                else:
                    memo[i][k] = memo[i][k-1] + memo[i+1][k] - memo[i+1][k-1]
    return memo[0][n-1] % mod

s = str(input())
print(countPs(s))
