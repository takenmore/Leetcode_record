'''
    定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
    调用 min、push 及 pop 的时间复杂度都是 O(1)。
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minS = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minS == []:
            self.minS.append(x)
        else:
            self.minS.append(min(x, self.minS[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minS[-1]

