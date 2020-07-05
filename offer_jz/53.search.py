from typing import List
'''
    统计一个数字在排序数组中出现的次数。
'''
'''
    两轮二分查找 
    二分查找三种形式： 下面是最常用的一种
    其他两种： 
    起始left = 0 right = len(nums)  终止 left==right 左查 right=mid 右查 left=mid+1
    起始left = 0 right = len(nums)-1 终止 left+1 == right 左查right=mid 右查 left=mid

'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(tar):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= tar:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        return helper(target) - helper(target - 1)


S = Solution()
print(S.search([5, 7, 7, 8, 8, 10], 8))
