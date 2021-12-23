#螺旋矩阵
from typing import List
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # bottom=len(matrix)
        # right=len(matrix[0])
        # ret=[]
        # top,left=0,0
        # while top<bottom and left<right:#开区间还是闭区间，得用开区间
        #     for i in range(left,right):
        #         ret.append(matrix[top][i])
        #     top+=1
        #     for i in range(top,bottom):
        #         ret.append(matrix[i][right-1])
        #     right-=1
        #     #
        #     if left<right and top<bottom:
        #         for i in range(right-1,left-1,-1):#上下界跟顺序，倒序的，-1取不到，因此取到0
        #             ret.append(matrix[bottom-1][i])#索引最底下一行就是bottom-1
        #         bottom-=1
        #         for i in range(bottom-1,top-1,-1):#上下界跟顺序
        #             ret.append(matrix[i][left])
        #         left+=1
        # return ret
        #


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1  ##这里是索引
        ret = []
        if matrix is None:
            return ret
        while True:
            for i in range(left, right + 1):  # 加1才能取到
                ret.append(matrix[top][i])
            top = top + 1  # 这几个都在for循环外
            # top+=1
            if top > bottom:
                break
            for i in range(top, bottom + 1):
                ret.append(matrix[i][right])
            right = right - 1
            if right < left:
                break
            for i in range(right, left - 1, -1):  # left要-1才能取到left，右边是开区间
                ret.append(matrix[bottom][i])
            bottom = bottom - 1
            if bottom < top:
                break
            for i in range(bottom, top - 1, -1):
                ret.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ret


a=Solution()
print(a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))