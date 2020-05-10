'''
@description: 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
@param {type} 二叉树的前序 中序数组
@return:  二叉树
'''
'''
    经典递归
'''
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index = i
                break
        root.left = self.buildTree(preorder[1:index + 1], inorder[0:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root


'''
    可用leetcode 测试。
'''