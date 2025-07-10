from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in prices:
            if i > buy:
               profit = max(profit, (i-buy))
            if i < buy:
                buy = i
        return profit
