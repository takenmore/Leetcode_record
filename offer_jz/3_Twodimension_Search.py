'''
    在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序
    每一列都按照从上到下递增的顺序排序
    输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
'''
    重点思路  从右上角开始查找而不是从左上角。
'''
from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        row = len(matrix)
        col = len(matrix[0])
        i,j = 0,col-1
        while i< row and j>=0:
            if matrix[i][j] < target:
                i = i+1
            elif matrix[i][j] > target:
                j = j-1
            else:
                return True
        return False

s=Solution()
print(s.findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))