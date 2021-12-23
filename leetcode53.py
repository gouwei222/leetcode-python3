class Solution:
    def maxSubArray(self, nums) -> int:
        # if nums is None:
        #     return 0
        n=len(nums)
        res=nums[0]
        tmp=0
        for i in range(n):
            tmp=max(nums[i],tmp+nums[i])
            res=max(tmp,res)
        return res
a=Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))