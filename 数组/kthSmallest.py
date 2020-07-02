from typing import List


'''
    给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
    请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
'''

'''
    解法一： 将二维压缩成为一维 排序 求解 时间复杂度高 sum(matrix,[])
    解法二： 二分查找 二分查找应用条件：有序
    这题是部分有序 所以不能直接用值作比较
    而观察Matrix 可得 小于特定值的元素一定出现在Matrix的左上部分
    于是题目要求则是找到 使得分割矩阵后左上部分仅含k 个元素的一个特定值。
    依据Matrix 特定可以走Z字求解特定值条件下 左上元素的数量。 然后依据这个判断做二分
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def helper(mid):
            # 计算 小于 mid 的有效元素个数
            i, j = n - 1, 0
            nums = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    nums += i + 1
                    j += 1
                else:
                    i -= 1
            return nums

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) >> 1
            if helper(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left


S = Solution()
print(S.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))