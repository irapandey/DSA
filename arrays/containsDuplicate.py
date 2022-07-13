# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

from collections import defaultdict

def containsDuplicate(arr):
    res = defaultdict(lambda: 0)
    for i in arr:
        if res[i] == 1:
            return True
        res[i] = 1
            
    return False

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(containsDuplicate(arr))