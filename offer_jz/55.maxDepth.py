class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
maxDepth
输入一棵二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        nLeft = self.maxDepth(root.left)
        nRight = self.maxDepth(root.right)
        return nLeft + 1 if nLeft>nRight else nRight + 1

    def isBalanced(self, root:TreeNode) -> int:
        '''
            验证一棵二叉树是否是平衡二叉树
        '''
        '''
            后序遍历节省多余判断。aa
        '''
        def dfs(root):
            if not root:return 0
            left = dfs(root.left)
            if left == -1:return -1
            right = dfs(root.right)
            if right == -1:return -1
            return max(left,right) +1 if abs(left - right)<=1 else -1
        
        return dfs(root) != -1
