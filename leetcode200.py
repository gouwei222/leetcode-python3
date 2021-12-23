#岛屿数量
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)#行
        col=len(grid[0])#列
        ret=0
        # print(grid[1][1])
        def dfs(x,y):
            grid[x][y]="0"
            for c in ([0,1],[0,-1],[1,0],[-1,0]):#上，下，右，左移动
                nx=x+c[0]
                ny=y+c[1]
                if 0<=nx<row and 0<=ny<col and grid[nx][ny]=="1":
                    dfs(nx,ny)

        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":#dfs完都置为0了，这里很快跳过去
                    dfs(i,j)
                    ret+=1
        return ret
a=Solution()
print(a.numIslands([["1","0"],["0","1"]]))