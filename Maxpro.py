'''
@description: 给你一个整数数组 nums ，
        请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
@param {type} 数组
@return: 最大子数组乘积
'''

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max = nums[0]
        Min = nums[0]
        res = 0
        for i in range(1,len(nums)):
            tma = Max
            tmi = Min
            Max = max(tma*nums[i],max(tmi*nums[i],nums[i]))
            Min = min(tmi*nums[i],min(tma*nums[i],nums[i]))
            res = max(Max,res)
        return res


s=Solution()
print(s.maxProduct([1,5,0]))