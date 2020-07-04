from typing import List
'''
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
'''
'''
    简单的dfs  升序数组 即可转为二叉搜索树的中序遍历序列
    高度平衡则说明中间数字为根节点。 如果奇数中间数字唯一，偶数则可以任取一个。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs(nums):
            n = len(nums)
            if n == 0:
                return None
            l, r = nums[0], nums[n - 1]
            m = (l + r) >> 1
            root = TreeNode(m)
            root.left = dfs(nums[:m])
            root.right = dfs(nums[m:n])
            return root

        Tree = dfs(nums)
        return Tree


S = Solution()
print(S.sortedArrayToBST([-10, -3, 0, 5, 9]))
