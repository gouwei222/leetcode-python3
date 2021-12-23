#组合总数2
#要先sort，这样后面的候选集和都是第一个的真子集
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        size=len(candidates)
        res=[]
        path=[]
        def dfs(candidates,begin,size,path,res,target):
            if target<0:
                return
            if target==0:
                res.append(path)
                return
            for i in range (begin,size):
                residue=target-candidates[i]
                if residue<0:
                    break#大剪枝，target小于0表示搜索下去无意义，则剪枝
                if i>begin and candidates[i]==candidates[i-1]:
                    continue#小剪枝，前面出现过可能会重复的
                # path.append(candidates[i])
                dfs(candidates,i+1,size,path+[candidates[i]],res,target-candidates[i])
                # dfs(i+1,path,target-candidates[i])
                # path.pop()#不pop就解答错误
                #这里用path.append()和path+candidate[i]还不一样，前者需要pop，可以都跑一下看看
                #如果用path+,那么pop的话会报错说空列表没法pop，因为path是空的，相加后的结果在新的列表里
        if size==0:
            return []
        dfs(candidates,0,size,path,res,target)
        return res


# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         size=len(candidates)
#         res=[]
#         path=[]
#         def dfs(candidates,begin,size,path,res,target):
#             if target<0:
#                 return
#             if target==0:
#                 res.append(path[:])
#                 return
#             for i in range (begin,size):
#                 residue=target-candidates[i]
#                 if residue<0:
#                     break#大剪枝，target小于0表示搜索下去无意义，则剪枝
#                 if i>begin and candidates[i]==candidates[i-1]:
#                     continue#小剪枝，同一层中i和i-1对应的candidate相同则剪枝
#                 path.append(candidates[i])
#                 dfs(candidates,i,size,path+[candidates[i]],res,target-candidates[i])
#                 path.pop()#不pop就解答错误
#         if size==0:
#             return []
#         dfs(candidates,0,size,path,res,target)
#         return res
###有问题，这种代码每个candidate输出了多次，跟39的做法一样了


a=Solution()
print(a.combinationSum2([10,1,2,7,6,1,5],8))
