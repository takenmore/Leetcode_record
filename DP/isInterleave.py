'''
    给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
'''

'''
    二维dp
    dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, t = len(s1), len(s2), len(s3)
        if (m + n) != t:
            return False
        dp = [False for i in range(m + 1)]
        dp[0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                idx = i + j - 1
                if i > 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[idx]
                if j > 0:
                    dp[j] |= dp[j-1] and s2[j - 1] == s3[idx]
        return dp[-1]


S = Solution()
print(S.isInterleave("a", "", "a"))