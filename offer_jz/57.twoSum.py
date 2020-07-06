'''
    输入一个递增排序的数组和一个数字s，
    在数组中查找两个数，使得它们的和正好是s。
    如果有多对数字的和等于s，则输出任意一对即可。
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            temp = nums[left] + nums[right]
            if temp == target:
                return [nums[left], nums[right]]
            if temp > target:
                right -= 1
            else:
                left += 1
        return []


S = Solution()
print(S.twoSum([10, 26, 30, 31, 47, 60], 40))
