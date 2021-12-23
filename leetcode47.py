#全排列2
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         ret=[]
#         path={}#是一个字典，字典用.values
#         def dfs(nums):
#             if len(nums)==len(path) and list(path.values())  not in ret:#list函数把数据转换成列表（广义的数组）类型
#                 ret.append(list(path.values()))
#             for i in range(len(nums)):
#                 if i not in path:
#                     path[i]=nums[i]
#                     dfs(nums)
#                     path.pop(i)
#         dfs(nums)
#         return ret

class Solution:
    def permuteUnique(self, nums) :
        ret = []
        nums.sort()
        n = len(nums)
        stage = [0] * n
        path = []

        def dfs(nums):
            if len(nums) == len(path):
                ret.append(path[:])
                # ret.append((path))
                return#return回dfs的入口，不执行下面的for循环了（一个return执行，那么直接结束该函数的执行）
            for i in range(len(nums)):
                if stage[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and stage[i - 1] == 0:#i>0因为i-1要大于0，该元素等于上一个元素，且上一个元素的stage为0说明撤销过了，用过了
                    continue
                path.append(nums[i])
                stage[i] = 1#stage=1说明该元素用过了
                dfs(nums)
                path.pop()#回溯后stage置0说明该元素没用过
                stage[i] = 0

        dfs(nums)
        return ret


a=Solution()
print(a.permuteUnique([1,1,2]))
