# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return False
        temp = []
        res = []
        def findpath(r, cur):
            cur += r.val
            temp.append(r.val)
            isleaf = not r.left and not r.right
            if cur == target and isleaf:
                res.append(list(temp))
            if r.left:
                findpath(r.left, cur)
            if r.right:
                findpath(r.right, cur)
            temp.pop()

        findpath(root, 0)
        return res


pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5

S = Solution()
print(S.pathSum(pNode1, 22))