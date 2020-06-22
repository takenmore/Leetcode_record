from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        top, left, right, bottom = 0, 0, cols - 1, rows - 1
        res = []
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            for j in range(top + 1, bottom + 1):
                res.append(matrix[j][right])
            if left < right and top < bottom: 
                #最内圈情况下不需要重复处理。(只有一行或一列甚至一个数 前面已经处理过了)
                for k in range(right - 1, left, -1):
                    res.append(matrix[bottom][k])
                for l in range(bottom, top, -1):
                    res.append(matrix[l][left])
            top, left, right, bottom = top + 1, left + 1, right - 1, bottom - 1
        return res


S = Solution()
print(S.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
