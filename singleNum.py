'''
@description: 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
@param {type} 数组
@return: 只出现一次的元素
'''
'''
    异或运算 ^  1^0 = 1 1^1 = 0 0^0 = 0 0^1=1 不同为1 相同为0 数字异或则先转二进制在计算。
    a^b^a = a 也就是说对一个数进行两次相同的异或操作 返回的还是这个数  
    汉明距离：对两个字符串进行异或运算后 并统计结果中 1的个数 这个数就是汉明距离
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = nums[0]
        for i in range(1, len(nums)):
            a = a ^ nums[i]
        return a


s = Solution()
print(s.singleNumber([5, 1, 1, 2, 2]))
