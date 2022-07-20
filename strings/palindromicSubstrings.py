# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


def pal_sub(s):
    def fromMiddle(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return (r - l)//2

    ans = 0
    for i in range(len(s)):
        ans += fromMiddle(i, i) + fromMiddle(i, i + 1)
    return ans
s = str(input())
print(pal_sub(s))