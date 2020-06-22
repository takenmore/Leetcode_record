'''
    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
    假设压入栈的所有数字均不相等。
    例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，
    但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
'''
'''
    模拟过程 
    一直进栈 直到 与出栈元素相等 就进行出栈 直到与出栈元素不等 再次进栈
'''
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:
        push_stack = []
        cur = 0
        for i in range(len(pushed)):
            push_stack.append(pushed[i])
            while push_stack and push_stack[-1] == popped[cur]:
                push_stack.pop()
                cur += 1
        return not push_stack


S = Solution()
print(S.validateStackSequences([2, 1, 0], [1, 2, 0]))
