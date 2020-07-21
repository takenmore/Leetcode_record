from typing import List

'''
    给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树.
'''

'''
    递归 / 动态规划
    每次选择一个节点作为根节点，在这个节点之前的作为左子树，之后的作为右子树
    然后一次搭配构建成一颗二叉搜索树。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(start, end):
            ans = []
            if start > end:
                return [None]
            for i in range(start, end+1):
                left = generate(start, i-1)
                right = generate(i+1, end)

                for l in left:
                    for r in right:
                        cur = TreeNode(i, l, r)
                        ans.append(cur)
            return ans
        return generate(1, n) if n else []


S = Solution()
print(S.generateTrees(3))
