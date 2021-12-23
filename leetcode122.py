# class Solution:
#     def maxProfit(self, prices):
#         tmp=0
#         n=len(prices)
#         for i in range(1,n):#要弄个下届为1，要不i-1出问题 price[0]-price[-1],第一个元素减去倒数第一个元素
#             if prices[i]>prices[i-1]:
#                 tmp=tmp+prices[i]-prices[i-1]
#         return tmp
# ###这是个贪心算法

class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        dp = [[[0,0],[0,0] ]for _ in range(length)]
        dp[0][0] = -prices[0]#0是持有，该状态表示第一天持有，需要减去第一天股价
        dp[0][1] = 0#1是不持有，该状态表示第一天不持有
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i]) #当天持有，前一天如果不持有，那么当天为前一天减去当天股价；前一天
            #如果持有，那么当天等于前一天# ，#注意这里是和121. 买卖股票的最佳时机唯一不同的地方
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])#当天不持有，前一天如果不持有，那么当天等于前一天；前一天如果持有，
            #那么当天等于前一天加当天股价
        return dp[-1][1] #-1就是最后一天，1是不持有

a=Solution()
print(a.maxProfit([7,1,6,3,5,4]))