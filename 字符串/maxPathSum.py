# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
    给定一个非空二叉树，返回其最大路径和。
    本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
'''
'''
    dfs  需要好好体会
    最大路径和可能为
    左子树最大路径和
    右子树最大路径和
    或 包含左子树部分节点且跨过根节点 再包含右子树部分节点。 (包含根节点的最大路径)

    注意 与0比较大小，如果子树最大路径和为负值 则不采用 避免影响含根路径和的结果
    内层嵌套函数想要更改外层函数的变量 可以通过声明 nonlocal
'''
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')  #res = float('-inf')

        def maxSum(TreeNode):
            #nonlocal res
            if not TreeNode:
                return 0
            LeftGain = max(maxSum(TreeNode.left), 0)  #左子树最大路径和
            RightGain = max(maxSum(TreeNode.right), 0)  #右子树最大路径和

            NewPathSum = TreeNode.val + LeftGain + RightGain

            self.res = max(self.res, NewPathSum)   # res = max(res,NewPathSum)

            return TreeNode.val + max(LeftGain, RightGain)
        maxSum(root)
        return self.res