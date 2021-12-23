#被围绕的区域
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=len(board)
        col=len(board[0])
        def dfs(x,y):
            if board[x][y]!="O":
                return
            else:
                board[x][y]="#"#这是赋值不是判断

            for c in[[1,0],[-1,0],[0,1],[0,-1]]:#找到一个边界相连的“O”以后开始dfs，搜跟他直接相连的“O”
                nx=x+c[0]
                ny=y+c[1]
                if 0<=nx<row and 0<=ny<col :
                    dfs(nx,ny)

        for i in range(row):
            dfs(i,0)
            dfs(i,col-1)#下标减1不越界

        # for j in range(1,col-1):#从1开始到col-1结束，因为上面dfs的时候把最边界搜过了,这样子能快一点
        for j in range(col):
            dfs(0,j)
            dfs(row-1,j)

        for i in range(row):
            for j in range(col):
                # dfs(i,j)
                board[i][j]="O" if board[i][j]=="#" else "X"

        return board
a=Solution()
print(a.solve([["X","X","X"],["X","O","X"],["X","X","O"]]))