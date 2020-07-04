from typing import List

'''
    在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
    你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
    给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
'''

'''
    基本的DP题 但是应该注意空间的优化 如果能够原地应该原地 O(1)
'''
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[0 for i in range(col)] for j in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    continue
                if i == 0 or j == 0:
                    dp[i][j] = grid[i][j] + (dp[i - 1][j]
                                             if j == 0 else dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        print(dp)
        return dp[row - 1][col - 1]


S = Solution()
print(S.maxValue([[1, 2, 5], [3, 2, 1]]))
