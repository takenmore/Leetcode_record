class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


'''
    输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
    B是A的子结构， 即 A中有出现和B相同的结构和节点值。
'''


class Solution:
    def isSubStructure(self, Root1, Root2):
        def dfs(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return dfs(A.left, B.left) and dfs(A.right, B.right)

        if not Root1 and not Root2:
            return True
        if not Root1 or not Root2:
            return False
        return dfs(Root1, Root2) or self.isSubStructure(
            Root1.left, Root2) or self.isSubStructure(Root1.right, Root2)
