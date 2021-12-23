class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_prices = prices[0]
        n = len(prices)
        for i in range(n):
            # if prices[i]>min_prices:#带这一行就出问题
            min_prices = min(min_prices, prices[i])
            profit = max(profit, (prices[i] - min_prices))

        return profit
