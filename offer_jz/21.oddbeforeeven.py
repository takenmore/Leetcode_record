from typing import List
'''
@description: 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
            使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
@param {type} 整数数组
@return: 调整数据顺序的数组
'''


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 1:
            return nums
        left, right = 0, n - 1
        while left < right:
            while nums[left] & 1 == 1 and left < right:
                left += 1
            while nums[right] & 1 == 0 and left < right:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums


S = Solution()
print(S.exchange([1, 5, 4, 7, 3, 5]))
