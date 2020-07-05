'''
    我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
'''
'''
    三指针 + 动态规划
    利用指针以及额外的数组 申请额外的空间来优化一定的时间
'''


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        a, b, c = 0, 0, 0
        index = 1
        while index < n:
            n_2, n_3, n_5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            cur = min(n_2, n_3, n_5)
            if cur == n_2: a += 1
            if cur == n_3: b += 1
            if cur == n_5: c += 1
            dp[index] = cur
            index += 1
        print(dp)
        return dp[-1]


S = Solution()
print(S.nthUglyNumber(10))
