from typing import List

'''
    给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
'''

'''
    辅助栈 ， 栈内记录index  当遇到'(' 无脑进栈
    遇到')' 先出栈(进行一次匹配)
    如果栈空说明 匹配失败 则将当前index放入栈中存储 当作最后匹配失败的右括号的下标 (也就是新的成功子串的开始点)
    如果栈不空 则当前index - 栈顶元素 则是当前匹配成功子串的长度 记录并保留更大值。
'''

'''
    DP 解法 分两种情况分析。 dp 记录以i结尾的最长有效括号长度。
    一 ： 当前状态是以 '()' 结尾 说明最后有效。
    则 dp[i] = dp[i-2] + 2
    二 ： 当前状态是以'))' 结尾 说明最后无效 情况则比较难懂
    首先 如果 i-1 为更长有效子串的部分 则 i-dp[i-1] 之前一个字符一定是 (
    即 s[i-dp[i-1] - 1] = '('
    则 当前的dp值应该为 dp[i-1] + 2 然后 还需要加上 i - dp[i-1] - 2前的有效子串长度
    所以有 dp[i] = dp[i-1] + 2 + dp[i-dp[i-1] - 2]
    三： 当前状态 是以 '('结尾 则构不成有效括号 直接赋0
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    temp = i - stack[-1]
                    res = max(temp, res)
        return res

    def longestValidParentheses_dp(self, s: str) -> int:
        res = 0
        dp = [0] * len(s)
        for i in range(1, len(s)): #从1开始 dp[0] 一定为0 无论是'('还是')'
            if s[i] == '(':
                continue
            else:
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                else:
                    if i - dp[i-1] >0 and s[i-dp[i-1]-1] == '(':
                        pre = dp[i-dp[i-1] - 2] if i-dp[i-1]-2 >=0 else 0
                        dp[i] = dp[i-1] + 2 + pre
                res = max(res, dp[i])
        return res




S = Solution()
print(S.longestValidParentheses_dp(")"))
    