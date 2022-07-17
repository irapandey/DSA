# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

def valid(s):
    temp = [1]
    for i in s:
        if i == "(" or i == "{" or i == "[":
            temp.append(i)
        elif i == ")":
            if temp[-1] == "(":
                temp.pop(-1)
            else:
                return False
        elif i == "}":
            if temp[-1] == "{":
                temp.pop(-1)
            else:
                return False
        elif i == "]":
            if temp[-1] == "[":
                temp.pop(-1)
            else:
                return False
    if temp != [1]:
        return False
    return True

s = str(input())
print(valid(s))