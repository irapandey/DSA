from collections import defaultdict

def charReplacement(s,k):
    count = defaultdict(int)

    max_len = 0
    start = 0

    max_freq = 0
    for end in range(len(s)):
        ch = s[end]
        count[ch] += 1

        max_freq = max(max_freq, count[ch])
        # if the window is invalid
        while end - start + 1 > k + max_freq:
            start_ch = s[start]
            count[start_ch] -= 1
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len
s = str(input())
k = int(input())
print(charReplacement(s,k))