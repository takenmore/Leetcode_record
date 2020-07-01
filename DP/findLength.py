from typing import List
'''
    给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
'''
'''
    解法 dp  状态  当前数字是否能够与上个数字组成最长子数组 (子串)
            状态转移  dp[i][j] = dp[i-1][j-1] + 1 if A[i] == B[j] else 0
            0 代表当前字符不在最长公共子数组(串)内
            随后记录下这个二维表的最大值即为所求的最长长度。
            ans 为这个最长子数组。
            方法记录最长子数组末尾的的那个index 然后倒退最大长度。
'''


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        lA, lB = len(A), len(B)
        dp = [[0 for i in range(lA + 1)] for _ in range(lB + 1)]
        res = 0
        index = 0
        for i in range(1, lA + 1):
            for j in range(1, lB + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    index = i
                    res = max(dp[i][j], res)
        ans = A[index - res:index]
        print(ans)
        return res


S = Solution()
print(S.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7, 8, 7]))
