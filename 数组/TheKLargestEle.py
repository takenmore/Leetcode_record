from typing import List
import random

'''
    在未排序的数组中找到第 k 个最大的元素。
'''

'''
    快速选择算法 每次partition 都会返回主元的排序后的正确位置
    所以为了找到第K大个元素 只需要要求partition的结果为 n-k 即可
    随机化使其期望时间复杂度为n 否则在worse case 时间复杂度n^2
    需要细心写
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k
        if k <= 0 or k > n:
            return
        left, right = 0, n - 1
        while True:
            index = self.__partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1
            else:
                right = index - 1

    def __partition(self, nums, first, last):
        r_index = random.randint(first, last)
        nums[first], nums[r_index] = nums[r_index], nums[first]

        pivot = nums[first]
        left = first + 1
        right = last
        while left <= right:
            while left <= right and nums[left] <= pivot:
                left += 1
            while right >= left and nums[right] >= pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[right], nums[first] = nums[first], nums[right]
        return right


S = Solution()
print(S.findKthLargest([3, 2, 1, 5, 6, 4], 2))
