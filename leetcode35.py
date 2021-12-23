#搜索插入位置，二分查找
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        left=0
        right=n-1
        while left<=right:##如果这不带等号，最后返回left和right是一样的，并且right=mid不-1
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1##这块开始写成+1了。。。
        return left
a=Solution()
print(a.searchInsert([1,3,5,6],2))