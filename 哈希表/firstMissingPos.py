from typing import List

'''
    给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
'''
'''
    !! 没有出现的最小正整数必然出现于[1,n] 这个区间里
    利用哈希的思想，进行原地哈希，交换后数组内存储的每个值为 下标 + 1
    如果不为 下标 +1 则第一个违反的 下标 +1 即为所求。
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


S = Solution()
print(S.firstMissingPositive([1, 2, 3, 4]))
