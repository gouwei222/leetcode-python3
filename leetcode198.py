#打家劫舍
from  typing import List
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         left,right=0,0
#         n=len(nums)
#         ret=0
#         path=0
#         for i in range(n+1):
#             left=i
#             for j in range(2,n-i):
#                 right=left+j
#                 path=max(path,nums[left]+nums[right])
#         ret=max(ret,path)
#         return ret
####我这套代码，只能打劫两家，局限在这里


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] for _ in range(n)]
        print(dp)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp[0] = nums[0]#不是0，是nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):##i可以取到n
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n-1]
#为啥会超出索引啊，因为nums没有下标为4的时候，而且dp的下标也只到3，而n是4

a=Solution()
print(a.rob([1,2,3,1]))
