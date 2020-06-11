from typing import List
'''
@description:  根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。
如果之后都不会升高，请在该位置用 0 来代替。
给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

@param {type} 气温列表 
@return: 等待多久温度才会升高的列表。
'''
'''
    单调栈的一种应用，利用递减栈来求解
    注意 栈中应存列表的下标 而不是元素！
'''

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        n = len(T)
        res = [0 for _ in range(n)]
        stack.append(0)
        for i in range(1, n):
            while stack and T[i] > T[stack[-1]]:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res


S = Solution()
print(S.dailyTemperatures([73,74,75,71,69,72,76,73]))

