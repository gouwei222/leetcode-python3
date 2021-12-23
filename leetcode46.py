#全排列

# class Solution:
#
#     def permute(self, nums) :
#         # nonlocal n=len(nums)
#         self.ret=[]
#         self.path=[]
#         self.dfs(nums)
#         return self.ret
#     def dfs(self,nums):
#         if len(nums)==len(self.path):
#             self.ret.append(self.path[:])
#         for i in nums:
#             if i not in self.path:
#                 self.path.append(i)
#                 self.dfs(nums)
#                 self.path.pop()


class Solution:
    def permute(self, nums):
        ret = []
        path = []

        def dfs(li):
            if len(li) == len(path):
                ret.append(path[:])
            for i in li:
                if i not in path:
                    path.append(i)
                    dfs(li)
                    path.pop()

        dfs(nums)
        return ret

a=Solution()
print(a.permute([1,2,3]))

