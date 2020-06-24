class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
    要求不能创建任何新的节点，只能调整树中节点指针的指向。
'''
# 首尾不成环
class Solution:
    def treeToDoublyList(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if not root.left and root.right:
            return root
        
        self.treeToDoublyList(root.left)
        left = root.left
        if left:
            while left.right:
                left = left.right
            left.right, root.left = root, left
        self.treeToDoublyList(root.right)
        right = root.right
        if right:
            while right.left:
                right = right.left
            right.left, root.right = root, right

        while root.left:
            root = root.left
        return root
# 首尾成环
    def treeToDoublyList2(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left) # 递归左子树
            if self.pre: # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else: # 记录头节点
                self.head = cur
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
        
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

pNode1 = TreeNode(4)
pNode2 = TreeNode(2)
pNode3 = TreeNode(5)
pNode4 = TreeNode(1)
pNode5 = TreeNode(3)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
# pNode3.left = pNode6
# pNode3.right = pNode7

S = Solution()
newList = S.treeToDoublyList(pNode1)
print(newList.val)
