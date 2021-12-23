from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
#k是不断更新的
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]#当nums1排空的时候，返回nums2的第k小的数
                if index2 == n:
                    return nums1[index1 + k - 1]#当nums2排空的时候，返回nums1的第k小的数
                if k == 1:
                    return min(nums1[index1], nums2[index2])#k==1的时候返回两个数组中较小的

                # 正常情况
                # newIndex1 = min(index1 + k // 2 - 1, m - 1)#这个min函数是防止越界的
                # newIndex2 = min(index2 + k // 2 - 1, n - 1)
                newIndex1 = index1+k//2-1#这个min函数是防止越界的
                newIndex2 = index2+k//2-1
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:#排除nums1的左半边
                    # k -= newIndex1 - index1 + 1#更新k的值，等号右边为我们删除掉的个数
                    k=k-k//2
                    index1 = newIndex1 + 1#下标偏移

                else:#排除nums2的左半边
                    # k -= newIndex2 - index2 + 1
                    k=k-k//2
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2
a=Solution()
print(a.findMedianSortedArrays([1,2],[3,4]))

"""
  - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
  - 这里的 "/" 表示整除
  - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
  - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
  - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
  - 这样 pivot 本身最大也只能是第 k-1 小的元素
  - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
  - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
  - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
  """


