'''
    给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。
'''
'''
    动态规划 和 剑指里面的正则匹配类似的逻辑 但要简单一些(但jz书是递归 
    遇到 字符相同或 ? 则直接模式和字符都依据之前的结果进行一次转移
    遇到* 则依据 字符的前一次的状态或模式的前一个状态进行转移。
    (模式前一次就相当于把*去除没使用，字符前一次 则是继续使用*匹配了)
    由于要使用dp[i-1][j-1] 前一次的结果进行转移 所以递归基需要先定义
    空字符串 与 空模式自然是匹配的，空模式和任意字符串不匹配
    而复杂一点的是空字符串只和所有的*号匹配 所以前导任意*号都匹配只到不是*号。
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for i in range(m + 1)] for j in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):   #前导均为* 则更新为True 否则False
            if p[i - 1] == '*':
                dp[i][0] = True
            else:
                break
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[j - 1] == p[i - 1] or p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    continue
        return dp[-1][-1]



S = Solution()
print(S.isMatch("aab", "c*a*b"))
