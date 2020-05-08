'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径。
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
'''
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        row = len(board)
        col = len(board[0])
        Mask = [[0]* col for i in range(row)] #view 数组 作为一个访问的mask
        def haspath(r,c,l):
            if l == len(word):
                return True
            Path = False
            if 0<=r<row and 0<=c<col and board[r][c]==word[l] and Mask[r][c] != 1:
                l = l + 1
                Mask[r][c] = 1
                Path = haspath(r,c-1,l) or haspath(r-1,c,l) or haspath(r+1,c,l) or haspath(r,c+1,l)
                if Path != True:
                    l = l-1
                    Mask[r][c]=0
                return Path
        for i in range(row):
            for j in range(col):
                if haspath(i,j,0):
                    return True
        return False

s=Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))