class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = float('inf')
        profit = 0
        currentprofit = 0
        for i in range(len(prices)):
            if prices[i]<current and not currentprofit:
                current = prices[i]
            elif prices[i]-current>currentprofit:
                currentprofit = prices[i]-current
            else:
                profit+=currentprofit
                current = prices[i]
                currentprofit = 0
        return profit+currentprofit
    
        
