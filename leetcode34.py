#在排序数组中查找元素的第一个和最后一个位置
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        if target not in nums:
            return [-1, -1]
        def search(nums,target):
            n = len(nums)
            left = 0
            right = n - 1
            # ret = []
            while left <=right:
                mid = left + (right - left) // 2
                # if nums[mid] == target:
                #     return mid
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] >=target:
                    right = mid-1
            return left
        a=search(nums,target)
        b=search(nums,target+1)
        print(a,b)
        # if a==len(nums) or nums[a]!=target:
        #     return [-1,-1]
        # else:
        return [a,b-1]
a=Solution()
print(a.searchRange([5,7,7,8,8,10],8))