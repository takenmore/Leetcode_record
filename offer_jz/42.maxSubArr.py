from typing import List
'''
    输入一个整型数组，数组里有正数也有负数。
    数组中的一个或连续多个整数组成一个子数组。
    求所有连续子数组的和的最大值。
'''
'''
    dp思想 
    pre_sum 代表当前index 下连续子数组的和的最大值
    如果之前的pre_sum 的和的最大值 <= 0 意味着对当前index 连续和无贡献 直接舍弃
    否则 进行累加
    然后 和 之前的连续子数组 最大值 进行比较 保留更大的一项。
    或者 用dp 一维数组版本  申请了O(n) 空间(如果不允许原地修改的话) 可能更好理解
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        pre_sum = nums[0]
        for i in range(1, n):
            pre_sum = nums[i] if pre_sum <= 0 else pre_sum + nums[i]
            res = max(res, pre_sum)
        return res

    def maxSubArray2(self, nums):
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0] # 初始状态
        for i in range(1, n):
            dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
        return max(dp)


S = Solution()
print(S.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
