from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        sell = 0
        for i in range(len(prices)):
            sell = prices[i]
            if sell - buy == 0:
                continue
            if sell - buy > 0:
               profit = max(profit, (sell-buy))
            if sell - buy < 0:
                buy = prices[i]
        return profit
