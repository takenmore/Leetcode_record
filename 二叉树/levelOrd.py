'''
@description: 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
@param {type} Tree
@return: 层次遍历结果
'''
import collections
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
    队列实现的层次遍历
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = collections.deque([])
        queue.append(root)
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if level:
                res.append(level)
        return res

s= Solution()
root = TreeNode(3)
l1 = TreeNode(5)
l2 = TreeNode(1)
l3 = TreeNode(6)
l4 = TreeNode(2)
l5 = TreeNode(0)
l6 = TreeNode(8)
l7 = TreeNode(7)
l8 = TreeNode(4)
root.left = l1
root.right = l2
l1.left = l3
l1.right = l4
l2.left = l5
l2.right = l6
l4.left = l7
l4.right = l8
print(s.levelOrder(root))
