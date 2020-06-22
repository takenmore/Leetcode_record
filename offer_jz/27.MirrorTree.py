class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
'''
    请完成一个函数，输入一个二叉树，该函数输出它的镜像。
'''
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        if root.left:
            root.left = self.mirrorTree(root.left)
        if root.right:
            root.right = self.mirrorTree(root.right)
        return root
        