#两数之和
class Solution:
    def twoSum(self, nums, target: int) :
        n=len(nums)
        i,j=0,1
        while (i<j and j<=n-1):
            if nums[i]+nums[j]==target:
                return [i,j]
            else:
                i+=1
                j+=1
a=Solution()
print(a.twoSum([3,2,3],6))