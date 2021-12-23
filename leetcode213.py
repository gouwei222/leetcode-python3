#打家劫舍2
from typing import List
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [[0] for _ in range(n)]
#         # print(dp)
#         def robrange(start,end):
#             # dp=[0]*n不能放这里，要放外面，要不然dp[i-1]=0 eg:dp[3-1],此问题已解决，放哪里无所谓，反正会被后面的dp填入值顶掉
#             dp[0]=nums[start]
#             dp[1]=max((nums[start],nums[start+1]))#输入只有两个的时候，没有nums[1+1]这个下标的索引，只有Nums[0]和nums[1]，所以n=2的时候特判了
#             for i in range(start+2,end+1):##为啥end+1,start+2可能会大于end+1，单步执行发现问题杵在这里。不对，当二者相等的时候，就return了，并且最后调用的那个n-1,n-2把可能超出去的两种情况都特判了
# ###其实end+1或者end无所谓，取决于开区间闭区间，最后调robrange的时候的参数
#                 dp[i]=max(dp[i-1],dp[i-2]+nums[i])#n=3的时候，nums没有下标3，是不是这个状态方程有问题？？？，不是，而是初始化的时候dp不应该从0，1开始，而是从start开始
# #并且后面调函数的时候，给进来的n-1,n-2不会让这个nums的下标超出的
#                 # dp[i]=dp[i-1]
#                 # dp[i+1]=max(dp[i],dp[i-1]+nums[i])
#
#             # dp1=dp[:]
#             return dp[end]
#         # dp[0] = nums[0]#不是0，是nums[0]
#         # dp[1] = max(nums[0], nums[1])
#
#         # for i in range(2, n):##i可以取到n
#         #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
#         # if n == 0:
#         #     return 0
#         if n == 1:
#             return nums[0]
#         if n==2:
#             return  max(nums[0],nums[1])
#         if n==3:
#             # return max(max(nums[0],nums[1]),nums[2])
#             return max(nums[0],nums[1],nums[2])
#         elif n>3:
#             return max(robrange(0,n-2),robrange(1,n-1))
#NO1.为啥会超出索引啊，因为nums没有下标为4的时候，而且dp的下标也只到3，而n是4。绝对不会超出的，调函数的时候不管写n还是写lenth都限定了

#
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def robRange(start: int, end: int) -> int:
#             first = nums[start]
#             second = max(nums[start], nums[start + 1])
#             for i in range(start + 2, end + 1):
#                 first, second = second, max(first + nums[i], second)
#             return second
#
#         length = len(nums)
#         if length == 1:
#             return nums[0]
#         elif length == 2:
#             return max(nums[0], nums[1])
#         else:
#             return max(robRange(0, length - 2), robRange(1, length - 1))
# 标准答案



# class Solution:
#     def rob(self, nums: List[int]) -> int:
#
#         n=len(nums)
#         nums1=nums[0:n-1]
#         nums2=nums[1:n]
#         print(nums1,nums2)
#         if n == 0:
#             return 0
#         if n == 1:
#             return nums[0]
#         if n == 2:
#             return max(nums[0], nums[1])
#         def makerob(li):
#             lenth=len(li)
#             dp=[0]*lenth
#             dp[0]=li[0]
#             dp[1]=max(li[0],li[1])
#             for i in range (2,lenth):
#                 dp[i]=max(dp[i-1],dp[i-2]+li[i])
#             # lenth=len(nums)
#             # dp=[0]*lenth
#             # dp[0]=nums[0]
#             # dp[1]=max(nums[0],nums[1])
#             # for i in range (2,lenth):
#             #     dp[i]=max(dp[i-1],dp[i-2]+nums[i])
#
#             return dp[lenth-1]
#         return max(makerob(nums1),makerob(nums2))
##自己的答案，好使，上面
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#
#         n=len(nums)
#         dp = [[0] for _ in range(n)]
#         # print(dp)
#
#         dp[0] = nums[0]#不是0，是nums[0]
#         dp[1] = max(nums[0], nums[1])
#         for i in range(2, n):##i可以取到n
#             dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
#         return dp[n]
#     def robrange(self,nums):
#
#         n=len(nums)
#         self.nums1=nums[0:n-2]#这里都有问题了
#         self.nums2=nums[1:n-1]
#         print(self.nums1,self.nums2)
#         if n == 0:
#             return 0
#         if n == 1:
#             return nums[0]
#         if n==2:
#             return max(nums[0],nums[1])
#         if n==3:
#             return max(nums[0],nums[1],nums[2])#这一句纯属多此一举
#         else:
#             return max(self.rob(self.nums1),self.rob(self.nums2))
#自己写的，但是本地和提交的答案不一样了。。。

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         lenth = len(nums)
#         # dp=[0]*lenth
#         if lenth == 0:
#             return 0
#         if lenth == 1:
#             return nums[0]
#         if lenth == 2:
#             return max(nums[0], nums[1])
#
#         def robrange(nums,start, end):
#             # lenth=len(nums)
#             dp = [0] *(lenth)
#             dp[start] = nums[start]
#             dp[start+1] = max(nums[start], nums[start + 1])
#             #初始化下标给start跟start+1，而不是0跟1
#             for i in range(start + 2, end+1):
#             # for i in range(start+2,end):
#                 dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
#             return dp[end]#两次调函数的过程中end下标不一样的，不是返回倒数第一个下标，而是返回end下标
#             # return dp[end-1]
#
#
#         return max(robrange(nums,0, lenth - 2), robrange(nums,1, lenth - 1))

#       # return max(robrange(nums, 0, lenth - 1), robrange(nums, 1, lenth))

#第一种的最新改型

a=Solution()
print(a.rob([2,3,2]))
#[200,3,140,20,10]出现350的原因是两次robRange递归的时候，第二次的dp[n-2]+nums[i]的dp[n-2]用了第一次递归的值，没清空
#用dp[]有一个问题，就是返回值两次递归的时候下标其实不一样，而用first跟second就避免了这个问题，反正没下标，把递归中迭代的最后一个返回就成