class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0

        for price in prices:
            if price > lowest:
                profit = max(profit, price - lowest)
            else:
                lowest = price
        return profit

            