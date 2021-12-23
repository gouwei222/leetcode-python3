#组合总和
# class Solution:
#     def combinationSum(self, candidates, target) :
#         def dfs(candidates,begin,size,path,res,target):
#             if target<0:
#                 return
#             if target==0:
#                 res.append(path)
#                 return
#             for i in range(begin,size):##前后都要限定，要不然会重复#没这个begin会重复，i传参给def dfs的begin，begin再传参给for i in range的begin
#                 dfs(candidates,i,size,path+[candidates[i]],res,target-candidates[i])#path是个list，后面的candidates也要加[]弄成数组
#         size=len(candidates)
#         if size==0:
#             return []
#         path=[]
#         res=[]
#         dfs(candidates,0,size,path,res,target)
#         return res
####剪枝后
class Solution:
    def combinationSum(self, candidates, target) :
        def dfs(candidates,begin,size,path,res,target):
            if target<0:
                return
            if target==0:
                res.append(path)
                return
            for i in range(begin,size):##前后都要限定，要不然会重复#没这个begin会重复，i传参给def dfs的begin，begin再传参给for i in range的begin
                residue=target-candidates[i]
                if residue<0:
                    # continue
                    break#跳出这一层的所有循环
                dfs(candidates,i,size,path+[candidates[i]],res,target-candidates[i])#path是个list，后面的candidates也要加[]弄成数组
        candidates.sort()
        size=len(candidates)
        if size==0:
            return []
        path=[]
        res=[]
        dfs(candidates,0,size,path,res,target)
        return res




a=Solution()
print(a.combinationSum([2,3,6,7],7))