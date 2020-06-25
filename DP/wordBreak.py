from typing import List

'''
    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
    拆分时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。

'''

'''
    基本DP的应用
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_d = {}
        for _,word in enumerate(wordDict):
            word_d[word] = 1
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_d:
                    dp[i] = True
        return dp[n]


S = Solution()
print(S.wordBreak("leetcode", ["leet", "code"]))
