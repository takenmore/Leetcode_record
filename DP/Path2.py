from typing import List
'''
    一个机器人位于一个 m x n 网格的左上角。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

    网格中的障碍物和空位置分别用 1 和 0 来表示。
'''
'''
    基本DP 利用滚动数组优化空间。
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(col)]
        if obstacleGrid[0][0] == 1: return 0
        dp[0] = 1
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j - 1 >= 0 and obstacleGrid[i][j - 1] == 0:
                    dp[j] += dp[j - 1]
        return dp[-1]


S = Solution()
print(S.uniquePathsWithObstacles([[0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 0, 0]]))
