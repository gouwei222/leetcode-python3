#合并两个有序数组
from typing import List
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         if m==0 and n==1:
#             return nums2
#         if m==1 and n==0:
#             return nums1
#
#         for _ in range (m):
#             nums1.pop()
#         for key,value in enumerate(nums2):
#             nums1.append(value)
#             # print(value)
#         nums1.sort()
#         # nums1[m:]=nums2#这一行
#         # nums1.sort()
#         return nums1
    ###自己乱写的
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted=[]
        p,q=0,0
        while p<m or q<n:
            if p==m:
                sorted.append(nums2[q])
                q+=1
            elif q==n:
                sorted.append((nums1[p]))
                p+=1
            elif nums1[p]<nums2[q]:##循环的时候先执行后面两个，等一个超出上界了只给另一个+
                sorted.append(nums1[p])
                p+=1
            else:#改成else就可以
                sorted.append(nums2[q])
                q+=1

        # nums1=sorted[:]
        nums1[:]=sorted
        return nums1


a=Solution()
print(a.merge([1,2,3,0,0,0],3,[2,5,6],3))
