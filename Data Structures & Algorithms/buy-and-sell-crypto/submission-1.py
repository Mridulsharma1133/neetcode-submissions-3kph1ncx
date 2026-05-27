import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        i = 0
        while(i < len(prices) - 1):
            max_value = max(prices[i + 1: ])
            curr_profit = max_value - prices[i]
            max_profit = max(curr_profit, max_profit)
            i  += 1

        if max_profit<0:
            return 0
        
        else:
            return max_profit
        