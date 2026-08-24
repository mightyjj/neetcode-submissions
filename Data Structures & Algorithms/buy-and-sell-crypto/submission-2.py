class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = 0
        l = 0 

        while l < len(prices):
            bought = prices[l]
            r = l + 1
            while r < len(prices):
                sold = prices[r]
                high = max(high, sold - bought)
                r += 1
            l += 1
    
        return high