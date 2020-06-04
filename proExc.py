'''
@description: 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
@param {type} 数组
@return: 除自身外其他元素的乘积的数组
'''
'''
    前缀积  后缀积 + 排除自身 index
    利用滚动数组的思想 节约空间复杂度 降至O(1)
'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pro, bac = 1, 1
        res = [1] * n
        for i in range(n):
            res[i] *= pro
            pro *= nums[i]
            res[n - 1 - i] *= bac
            bac *= nums[n - 1 - i]
        return res


S = Solution()
print(S.productExceptSelf([5, 8, 9, 10]))
