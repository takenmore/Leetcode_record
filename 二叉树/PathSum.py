class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
'''
    给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
    hasPathSum -> 判断有没有
    pathSum -> 记录下路径。
'''
'''
    两道 dfs 题 (虽然记录是利用了回溯的思想。)
'''


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val)

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        path = []
        if not root:
            return res

        def dfs(root, target):
            if not root:
                return
            target -= root.val
            path.append(root.val)
            if target == 0 and not root.left and not root.right:
                res.append(path.copy())
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()

        dfs(root, sum)
        return res


S = Solution()
root = TreeNode(5)
l_1 = TreeNode(4)
r_1 = TreeNode(8)
l_2 = TreeNode(11)
r_2_l = TreeNode(13)
r_2_r = TreeNode(4)
l_3_l = TreeNode(7)
l_3_r = TreeNode(2)
r_3_l = TreeNode(5)
r_3_r = TreeNode(2)
root.left = l_1
root.right = r_1
l_1.left = l_2
r_1.left = r_2_l
r_1.right = r_2_r
l_2.left = l_3_l
l_2.right = l_3_r
r_2_r.left = r_3_l
r_2_r.right = r_3_r
print(S.pathSum(root, 22))
