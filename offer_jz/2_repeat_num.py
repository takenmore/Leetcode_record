'''
    找出数组中重复的数字 长度为n的数组
    所有数字都在0~n-1的范围内，数组中某些数字重复 
    存在多个重复的可能性 求任意一个
'''
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if nums:
            for i in range(len(nums)):
                while nums[i] != i:
                    m = nums[i]
                    if (m != nums[m]):
                        nums[i], nums[m] = nums[m], nums[i]
                    else:
                        return m
        return -1

    '''
        找出所有的重复数字
    '''

    def duplicate2(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return False
        for i in numbers:
            if i < 0 or i > len(numbers) - 1:
                return False
        repeatedNums = []
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    repeatedNums.append(numbers[i])
                    break
                else:
                    index = numbers[i]
                    numbers[i], numbers[index] = numbers[index], numbers[i]
        return repeatedNums


s = Solution()
l = [2, 3, 1, 0, 2, 5, 3]
print(s.duplicate2(l))