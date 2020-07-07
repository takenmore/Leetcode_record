'''
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
'''
from typing import List
'''
    首先 忽略概率的问题 可以直接讨论点数出现的次数
    然后 二维DP  dp[i][j] 在有i个骰子之后 点数j出现的次数。
    状态转移方程： dp[i][j] = dp[i-1][j-1] + dp[i-1][j-2]+...+dp[i-1][j-6]
    然后滚动数组优化。
    最后 将次数除以所有可能6^n得到概率。
'''


class Solution:
    def twoSum(self, n: int) -> List[float]:
        dp = [0 for _ in range(6 * n + 1)]
        g_MaxPoint = 6
        for i in range(1, g_MaxPoint + 1):
            dp[i] = 1
        for i in range(2, n + 1):
            for j in range(6 * i, -1, -1):
                dp[j] = 0
                for k in range(6, 0, -1):
                    if j - k < 0:
                        continue
                    dp[j] += dp[j - k]
        for i in range(len(dp)):
            dp[i] /= pow(g_MaxPoint, n)
        return dp[n:]


S = Solution()
print(S.twoSum(3))
