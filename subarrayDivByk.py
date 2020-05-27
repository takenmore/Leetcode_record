'''
@description: 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
@param {type} A 数组 K 除数
@return: 子数组数目
'''
'''
    前缀和+哈希表
    和简单的求和不同 由于是取余数 所以 哈希表中 存的是前缀和除K的余数
    同余定理：两个整数 a,b 若 a-b能被m整除 则 a除m 与 b除m 的余数相同
    只 - 不 +
'''
from typing import List
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        d = {}
        sumNum = count = 0
        for i in range(len(A)):
            sumNum += A[i]
            if sumNum % K == 0:
                count += 1
            if sumNum%K in d:
                count += d.get(sumNum%K, 0)
            if sumNum%K in d:
                d[sumNum%K] += 1
            else:
                d[sumNum%K] = 1
        return count

S = Solution()
print(S.subarraysDivByK([7,9,5,6,7,2], 7))