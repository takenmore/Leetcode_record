from typing import List
'''
    二叉搜索树中的两个节点被错误地交换。

    请在不改变其结构的情况下，恢复这棵树。
'''
'''
    中序遍历  记录下错误的节点
    遍历完后交换节点。
    一定先记录
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None
        first, second = None, None

        def inorder(root):
            nonlocal pre, first, second
            if not root:
                return
            inorder(root.left)
            if not pre and root.val < pre.val:
                if not first:
                    first = pre
                second = root
            pre = root
            inorder(root.left)

        inorder(root)
        first.val, second.val = second.val, first.val
