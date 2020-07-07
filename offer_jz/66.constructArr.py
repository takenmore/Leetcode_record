from typing import List

'''
    给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
    其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。
    不能使用除法。
'''
'''
    构造表格 表格遍历做乘法
    分为上三角和下三角构造。
'''
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b = [1] * len(a)
        temp = 1
        for i in range(1, len(a) - 1):
            b[i] = b[i - 1] * a[i - 1]
        for i in range(len(a) - 2, -1, -1):
            temp *= a[i+1]
            b[i] *= temp
        return b
