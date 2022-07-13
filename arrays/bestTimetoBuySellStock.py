def maxProfit(prices):
    l = 0
    r = 1
    max_p = 0
        
    while r < len(prices):
        currP = prices[r] - prices[l]
        if prices[l] < prices[r]:
            max_p = max(currP, max_p)
        else:
            l = r
            r += 1
    return max_p

prices = list(map(int,input().split()))
print(maxProfit(prices))