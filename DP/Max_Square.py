'''
    在0 和 1 的矩阵中 找到只包含 1 的最大正方形 并返回面积
'''
'''
    思路 dp  状态转移方程为 若矩阵值为1 则dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1 为0 则dp[i][j]=0
    将每个1的位置 均当作左下角 然后判断它的 左上 左 上方位置的值，其对应的边长即为 这个三个位置的边长最小值 +1
    时间 O(mn) 空间 O(mn)  原地应该可以 O(1)
    坑 ：由于初始化dp 数组为全0 所以不能依照 当作右下角的方式来写 包含了未处理的0 结果出错。
        如果允许原地处理 则应该可以以当作右下角的方式写
'''
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        maxsides = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    dp[i][j] == 0
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j],
                                       dp[i - 1][j - 1]) + 1
                    maxsides = max(dp[i][j], maxsides)
        ans = maxsides * maxsides
        return ans


s = Solution()
print(
    s.maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
                     ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
