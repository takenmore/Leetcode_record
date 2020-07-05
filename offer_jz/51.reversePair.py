'''
    在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
    输入一个数组，求出这个数组中的逆序对的总数。
'''

from typing import List


class Solution:
    def reversePair(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        temp = [0] * n
        return self.mergeSort(nums, 0, n - 1, temp)

    def mergeSort(self, nums, left, right, temp):
        if left == right:
            return 0
        mid = left + (right - left) // 2
        left_pair = self.mergeSort(nums, left, mid, temp)
        right_pair = self.mergeSort(nums, mid + 1, right, temp)

        if (nums[mid] <= nums[mid + 1]):
            return left_pair + right_pair

        cross_pair = self.merge(nums, left, mid, right, temp)
        return left_pair + right_pair + cross_pair

    def merge(self, nums, left, mid, right, temp):
        for i in range(left, right + 1):
            temp[i] = nums[i]
        i, j = left, mid + 1
        count = 0
        for k in range(left, right + 1):
            if i > mid:
                nums[k] = temp[j]
                j += 1
            elif j > right:
                nums[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                nums[k] = temp[i]
                i += 1
            else:
                nums[k] = temp[j]
                j += 1
                count += (mid - i + 1)
        return count


S = Solution()
print(S.reversePair([7, 5, 6, 4]))
