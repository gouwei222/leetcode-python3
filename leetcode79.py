#单词搜索
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        def dfs(x,y,index):
            if index==len(word)-1:
                return True
            board[x][y]="#"
            for c in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx=x+c[0]
                ny=y+c[1]
                if 0<=nx<row and 0<=ny<col and board[nx][ny]==word[index+1] and dfs(nx,ny,index+1):#在这里递归的
                    return True
            board[x][y]=word[index]#这一句还不能省,搜不到的时候要把str填回#的位置
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0] and dfs(i,j,0):
                    return True
        return False
a=Solution()
print(a.exist([["C","A","A"],["A","A","A"],["B","C","D"]],
"AAB"))