
from random import randint
#partition模板
def partition(nums, left, right):
    p=randint(left,right)
    pivot = nums[p]#初始化一个待比较数据
    nums[p],nums[left]=nums[left],nums[p]#多个这就好使了？
    i,j = left, right
    while(i < j):
        while(i<j and nums[j]>=pivot): #从后往前查找，直到找到一个比pivot更小的数
            j-=1
        nums[i] = nums[j] #将更小的数放入左边
        while(i<j and nums[i]<=pivot): #从前往后找，直到找到一个比pivot更大的数
            i+=1
        nums[j] = nums[i] #将更大的数放入右边
    #循环结束，i与j相等
    nums[i] = pivot #待比较数据放入最终位置
    return i #返回待比较数据最终位置



#快速排序
def quicksort(nums, left, right):
    if left < right:
        index = partition(nums, left, right) #partition返回的index用来划分区间然后分治
        quicksort(nums, left, index-1)#对左半区间递归
        quicksort(nums, index+1, right)#对右半区间递归

arr = [1,3,2,2,0]
print(arr)
quicksort(arr, 0, len(arr)-1)
print("快速排序")
print(arr)
print("----------------------------------------------")





# def topk_split(nums, k, left, right):
#     #寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
#     if (left<right):
#         index = partition(nums, left, right)
#         if index==k:
#             return
#         elif index < k:
#             topk_split(nums, k, index+1, right)
#         else:
#             topk_split(nums, k, left, index-1)
# arr=[1,3,2,2,0]
# print(arr)
# k=3
# topk_split(arr,k,0,len(arr)-1)
# print("找到k=",k,"的快速分割")
# print(arr)
# print("----------------------------------------------")
#
#
#
# #获得前k小的数
# def topk_smalls(nums, k):
#     topk_split(nums, k, 0, len(nums)-1)
#     return nums[:k]###k左边的都比k小，不管顺序
#
# arr = [1,3,2,3,0,-19]
# k = 2
# print("获得前",k,"小的数")
# print(topk_smalls(arr, k))
# print(arr)
# print("----------------------------------------------")
#
# #获得第k小的数
# def topk_small(nums, k):
#     topk_split(nums, k, 0, len(nums)-1)
#     return nums[k-1] #右边是开区间，需要-1
#
# arr = [1,3,2,3,0,-19]
# k = 3
# print("获得第",k,"小的数")
# print(topk_small(arr, k))
# print(arr)
# print("----------------------------------------------")
#
# #获得前k大的数
# def topk_larges(nums, k):
#     #parttion是按从小到大划分的，如果让index左边为前n-k个小的数，则index右边为前k个大的数
#     topk_split(nums, len(nums)-k, 0, len(nums)-1) #把k换成len(nums)-k
#     return nums[len(nums)-k:]
#
# arr = [1,3,-2,3,0,-19]
# k = 3
# print("获得前",k,"大的数")
# print(topk_larges(arr, k))
# print(arr)
# print("----------------------------------------------")
#
# #获得第k大的数
# def topk_large(nums, k):
#     #parttion是按从小到大划分的，如果让index左边为前n-k个小的数，则index右边为前k个大的数
#     topk_split(nums, len(nums)-k, 0, len(nums)-1) #把k换成len(nums)-k
#     return nums[len(nums)-k]
#
# arr = [1,3,-2,3,0,-19]
# k = 2
# print("获得第",k,"大的数")
# print(topk_large(arr, k))
# print(arr)
# print("----------------------------------------------")
#
# #只排序前k个小的数
# #获得前k小的数O(n)，进行快排O(klogk)
# def topk_sort_left(nums, k):
#     topk_split(nums, k, 0, len(nums)-1)
#     topk = nums[:k]
#     quicksort(topk, 0, len(topk)-1)
#     return topk+nums[k:] #只排序前k个数字
#
# arr = [0,0,1,3,4,5,0,7,6,7]
# k = 4
# print(arr)
# print("只排序前",k,"大的数")
# print(topk_sort_left(arr, k))
#
# print("----------------------------------------------")
#
# #只排序后k个大的数
# #获得前n-k小的数O(n)，进行快排O(klogk)
# def topk_sort_right(nums, k):
#     topk_split(nums, len(nums)-k, 0, len(nums)-1)
#     topk = nums[len(nums)-k:]
#     quicksort(topk, 0, len(topk)-1)
#     return nums[:len(nums)-k]+topk #只排序后k个数字
#
# arr = [0,0,1,3,4,5,0,-7,6,7]
# k = 4
# print(arr)
# print("只排序后",k,"大的数")
# print(topk_sort_right(arr, k))
#
# print("----------------------------------------------")



