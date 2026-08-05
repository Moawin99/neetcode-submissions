class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = len(prices)
        max_right = [0] * lp

        max_right[-1] = prices[-1]
        for i in range(lp-1, -1, -1):
            p = prices[i]
            if i < lp -1:
                max_right[i] = max(max_right[i + 1], p)
        
        profit = 0
        for i, p in enumerate(prices):
            if prices[i] < max_right[i]:
                profit = max(profit, max_right[i] - p)
        return profit

