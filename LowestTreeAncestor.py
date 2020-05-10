'''
@description: 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。  LeetCode 236
“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）."
@param {type} 树，两个结点
@return: 最近公共祖先
'''
'''
    深度优先遍历  注意一些python对象复制的坑

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(self,r,p,q):
            if r is None:
                return False
            isleft = dfs(self,r.left,p,q)
            isright = dfs(self,r.right,p,q)
            if isright and isleft:
                ans.val = r.val   #注意不能直接对象赋值。另一种方式是 self.ans = r 可以确保ans能带出去
            elif (r.val==p.val or r.val == q.val) and (isleft or isright):
                ans.val = r.val   #注意不能直接对象赋值。另一种方式是 self.ans = r 可以确保ans能带出去
            else:
                return isleft or isright or (r.val == p.val or r.val == q.val)
        ans = TreeNode(0)
        dfs(self,root,p,q)
        return ans
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
print(s.lowestCommonAncestor(root,l3,l4).val)