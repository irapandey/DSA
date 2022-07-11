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