import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxInf = -math.inf
        for i in range(len(prices) - 1):
            for p in prices[i+1:]:
                maxInf = max(maxInf, p - prices[i])
        if maxInf < 0:
            return 0
        return maxInf
        