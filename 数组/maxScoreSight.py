from typing import List


'''
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
返回一对观光景点能取得的最高分。
'''

'''
        拆解公式 (A[i] + i) + (A[j] - j )
        以及滚动数组的思想
'''
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n = len(A)
        res = 0
        a = A[0] + 0
        for i in range(1, n):
            if A[i] - i + a > res:
                res = A[i] - i + a
            if A[i] + i > a:
                a = A[i] + i
        return res