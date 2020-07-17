from typing import List
'''
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
    如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
'''
'''
    基本二分查找。
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        left, right = 0, n - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return left


S = Solution()
print(S.searchInsert([1, 3, 5, 6], 5))
