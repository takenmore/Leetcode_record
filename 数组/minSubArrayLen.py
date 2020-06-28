from typing import List

'''
    给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。
    如果不存在符合条件的连续子数组，返回 0。
'''
'''
    滑动窗口 + 双指针
    “进阶” 排序 + 二分查找。
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        res = n + 1
        sumNum = 0
        while right < n:
            sumNum += nums[right]
            while sumNum >= s:
                res = min(res, right - left + 1)
                sumNum -= nums[left]
                left += 1
            right += 1
        return 0 if res == n + 1 else res

S = Solution()
print(S.minSubArrayLen([2, 3, 1, 2, 4, 3], 7))