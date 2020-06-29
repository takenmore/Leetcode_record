'''
    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
'''
from typing import List
import random
'''
    两种解法 摩尔投票法 / 快速选择 partition / 哈希
    快速选择 超时。 但渐进时间复杂度应该是一致的 且修改了数组
    摩尔投票法 ： 极限一换一，换到最后的就是众数
    哈希 ： 未写 通过记录次数。 申请了额外空间
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        times = 1
        for i in range(1, len(nums)):
            if times == 0:
                res = nums[i]
                times = 1
            else:
                times = times + 1 if nums[i] == res else times - 1
        return res

    def majorityElement_p(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 0:
            return None
        target = n >> 1
        left, right = 0, n - 1
        index = self.partition(nums, left, right)
        while index != target:
            index = self.partition(nums, index + 1, right) \
                if index < target else self.partition(nums, left, index - 1)
        return nums[index]

    def partition(self, nums, first, last):
        r_index = random.randint(first, last)
        nums[first], nums[r_index] = nums[r_index], nums[first]
        pivot = nums[first]
        pos = first
        for i in range(first + 1, last + 1):
            if nums[i] < pivot:
                pos += 1
                if pos != i:
                    nums[i], nums[pos] = nums[pos], nums[i]
        nums[first], nums[pos] = nums[pos], nums[first]
        return pos


S = Solution()
print(S.majorityElement([2, 1, 3, 3]))
