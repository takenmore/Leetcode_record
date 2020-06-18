from typing import List

'''
    我们从二叉树的根节点 root 开始进行深度优先搜索.
    在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。
    （如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
    如果节点只有一个子节点，那么保证该子节点为左子节点。
    给出遍历输出 S，还原树并返回其根节点 root。
'''

'''
    用栈模拟递归的过程  利用题目种给的D条短划线信息。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        n = len(S)
        if n == 0:
            return None
        pos = 0
        stack = []
        while pos < n:
            level = 0
            while pos < n and S[pos] == '-':
                level += 1
                pos += 1
            value = 0
            while pos < n and S[pos].isdigit():
                value = value * 10 + ord(S[pos]) - ord('0')
                pos += 1
            cur = TreeNode(value)
            if len(stack) == level:
                if stack:
                    stack[-1].left = cur
            else:
                stack = stack[:level]
                stack[-1].right = cur
            stack.append(cur)
        return stack[0]


s = Solution()
print(s.recoverFromPreorder("1-2--3---4-5--6---7"))
