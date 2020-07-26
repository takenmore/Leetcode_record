from typing import List

'''
    给定一个整数矩阵，找出最长递增路径的长度。
    对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
'''

'''
    dfs + dp + 排序
    首先对矩阵值进行排序 以确保 依赖的子问题已经被解决
    (即小值的所在的递增路径已经dfs完了 剩下只需要在它的基础上增长自身)
    之后就是正常dfs + 正常的dp 求解矩阵中每一个点的最长递增路径 求最大。
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        row, col = len(matrix), len(matrix[0])
        record = []
        for i in range(row):
            for j in range(col):
                record.append((matrix[i][j], i, j))
        record.sort()
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dp = [[1 for _ in range(col)] for j in range(row)]
        for num, i, j in record:
            for x, y in direction:
                n_y, n_x = i + y, j + x
                if 0 <= n_x < col and 0 <= n_y < row:
                    if matrix[i][j] > matrix[n_y][n_x]:
                        dp[i][j] = max(dp[i][j], 1 + dp[n_y][n_x])
        return max(sum(dp, []))


S = Solution()
print(S.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
