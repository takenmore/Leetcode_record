class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
    请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def check(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        return check(root.left, root.right)
