'''
@description: 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
@param {type} 柱状图数组
@return: 最大面积
'''
'''
    单调栈
    单调栈的含义：栈内元素 保持递增关系或者递减关系 本题为 递增关系
    如果新的元素比栈顶元素打 入栈 否则出栈 直到栈顶元素比新元素小
    如此保证栈内递增，且出栈时 栈顶元素 为出栈元素之前的第一个比它小的元素 而 新元素为第一个比它大的元素。
    本题 即利用这两个边界求解出 每个柱子对应完全容纳该柱子的矩形的宽度 高度为柱子高度
    而对所有这样的矩形面积 求最大值 即为 题目所求。
'''
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        res = max((right[i] - left[i] - 1) * heights[i]
                  for i in range(n)) if n > 0 else 0
        return res


s = Solution()
print(s.largestRectangleArea([8, 4, 3, 5, 7, 6, 2, 1]))
