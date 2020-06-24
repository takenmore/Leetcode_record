from typing import List
'''
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
    如果是则返回 true，否则返回 false。
    假设输入的数组的任意两个数字都互不相同。
'''
'''
    二叉搜索树 ： 左子树 小于 根  根 小于右子树
    后序排列 左 右 根

'''


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        root = postorder[-1]
        n = len(postorder)
        l = 0
        while l < n - 1:
            if postorder[l] > root:
                break
            l += 1
        r = l + 1
        while r < n - 1:
            if postorder[r] < root:
                return False
            r += 1
        left = True
        if l > 0:
            left = self.verifyPostorder(postorder[:l])  # 相当于0-l-1
        right = True
        if l < n - 1:
            right = self.verifyPostorder(postorder[l:n-1])  #相当于 l-n-1
        return left and right


s = Solution()
print(s.verifyPostorder([1, 2, 5, 10, 6, 9, 4, 3]))
