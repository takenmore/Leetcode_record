from typing import List
'''
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
    返回这三个数的和。假定每组输入只存在唯一答案。
'''
'''
    和三数之和一个思路  排序 双指针 要稍微简单一点。
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        dist = abs(target - res)
        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, n - 1
            required = target - nums[i]
            while left < right:
                if nums[left] + nums[right] - required < 0:
                    if abs(nums[left] + nums[right] - required) < dist:
                        res = nums[i] + nums[left] + nums[right]
                        dist = abs(nums[left] + nums[right] - required)
                    left += 1
                elif nums[left] + nums[right] - required > 0:
                    if abs(nums[left] + nums[right] - required) < dist:
                        res = nums[i] + nums[left] + nums[right]
                        dist = abs(nums[left] + nums[right] - required)
                    right -= 1
                else:
                    return target
        return res


s = Solution()
print(s.threeSumClosest([-1, 2, 4, 3], 1))
