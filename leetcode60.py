#排列序列（第k个排列）
# class Solution:
#     def permute(self, nums,n,k):
#         ret = []
#         path = []
#
#         def dfs(li,n,k,path):
#             if n == len(path):
#                 ret.append(path[:])
#             for i in li:
#                 if i not in path:
#                     path.append(i)
#                     dfs(li,n,k)
#                     path.pop()
#
#         dfs(nums,n,k,path)
#         return ret[k-1]
# ###我这么全生成阶乘的话，不剪枝能把人算死
# a=Solution()
# print(a.permute([1,2,3,4,5],4,3))
# b=len(a.permute([1,2,3,4,5],4,3))
# print(b)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(n, k, index, path):
            if index == n:
                return
            cnt = factorial[n - 1 - index]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                path.append(i)
                used[i] = True
                dfs(n, k, index + 1, path)
                # 注意：这里要加 return，后面的数没有必要遍历去尝试了
                return

        if n == 0:
            return ""

        used = [False for _ in range(n + 1)]
        path = []
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i

        dfs(n, k, 0, path)
        return ''.join([str(num) for num in path])

a=Solution()
print(a.getPermutation(3,3))