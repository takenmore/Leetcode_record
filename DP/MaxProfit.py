'''
    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
'''

from typing import List
'''
    多状态的DP 有点不熟
    涉及到三种状态的转移  sell  buy  cold 在最后一次操作的最大收益
    其中 cold 实际是可以优化的 因为最后为冷冻期并不影响收益 cold[i] = sell[i-1]
        buy 也不产生收益 实际是记录了这次是否值得买入 是前缀的最大收益
        sell 收益的主要记录 依赖于buy 当前的最大收益
    转移方程： buy[i] = max(cold[i-1]-prices[i], buy[i-1])
             sell[i] = max(buy[i-1]+prices[i], sell[i-1])
             cold[i] = sell[i-1]
    空间上因为每次状态只与前一次有关，还可以利用滚动数组的思想 利用三个变量代替数组。
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        sell = [0 for i in range(n)]
        buy = [0 for i in range(n)]
        buy[0] = -prices[0]
        for i in range(1, n):
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
            if i >= 2:
                buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
            else:
                buy[i] = max(0 - prices[i], buy[i - 1])
        print(buy)
        return sell[-1]


S = Solution()
print(S.maxProfit([1, 2, 3, 0, 3, 0, 8]))
