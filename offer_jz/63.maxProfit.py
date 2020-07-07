'''
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
'''
from typing import List

'''
    单调栈的应用 递增栈 保证栈底为最小值。
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        stack = []
        stack.append(prices[0])
        res = 0
        for i in range(1, len(prices)):
            while stack and stack[-1] > prices[i]:
                cur = stack.pop()
            if stack:
                res = max(prices[i] - stack[0], res)
            stack.append(prices[i])
        return res


S = Solution()
print(S.maxProfit([7, 6, 4, 3, 1]))
