
# class Solution:
#     def climbStairs(self, n):
#         a = b = 1
#         for i in range(2, n + 1):
#             a, b = b, a + b
#         return b
# class Solution:
#     def climbStairs(self,n):
#         if n==1:
#             return 1
#         if n==2:
#             return 2
#         return self.climbStairs(n-1)+self.climbStairs(n-2)
#递归
class Solution:
    def climbStairs(self,n):

        dp=[[0] for _ in range(0,n+1)]###必须n+1,因为for只能取到n，是个开区间
        dp[0]=1#到第0个台阶有一种
        dp[1]=1#到第1个台阶有一种

        for i in range(2,n+1):###必须n+1,因为for只能取到n，是个开区间
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

# ##动态规划
# class Solution:
#     def climbStairs(self,n):
#
#         dp=[[0] for _ in range(0,n+1)]###必须n+1,因为for只能取到n，是个开区间
#         dp[1]=1#到第1个台阶有一种
#         dp[2]=2#到第2个台阶有两种
#
#         for i in range(3,n+1):###必须n+1,因为for只能取到n，是个开区间
#             dp[i]=dp[i-1]+dp[i-2]
#         return dp[n]

##初始条件不一样的动态规划

a=Solution()
print(a.climbStairs(5))