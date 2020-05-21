'''
@description: 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
@param {type} 字符串 s
@return: 最长回文子串
'''
'''
    动态规划 / 中心扩散
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for i in range(len(s))]
        ans = ""
        n = len(s)
        for l in range(n):
            for i in range(n):
                j = i+l
                if j>=n:
                    break
                if l==0:
                    dp[i][i] = 1
                elif l==1 and s[i]==s[j]:
                    dp[i][j] = 1
                else: 
                    if dp[i+1][j-1]==1 and s[i]==s[j]:
                        dp[i][j]=1
                if dp[i][j]==1 and l+1>len(ans):
                    ans=s[i:j+1]
        return ans

s = Solution()
print(s.longestPalindrome("abcba"))