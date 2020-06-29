'''
输入一个字符串，打印出该字符串中字符的所有排列。
'''
from typing import List
'''
    回溯法  固定一个字符 求解其他字符。
'''

class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s:
            return None
        temp = list(s)
        res = []

        def dfs(x):
            if x == len(s) - 1:
                res.append("".join(temp))
                return
            dic = set()
            for i in range(x, len(s)):
                if temp[i] in dic:
                    continue
                dic.add(temp[i])
                temp[i], temp[x] = temp[x], temp[i]
                dfs(x + 1)
                temp[i], temp[x] = temp[x], temp[i]
        dfs(0)
        return res

S = Solution()
print(S.permutation("abcde"))
