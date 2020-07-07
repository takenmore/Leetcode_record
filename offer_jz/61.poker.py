'''
    从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
    2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
    数组长度为5
    取值大小不大于13，不小于0
'''
from typing import List

'''
    数学建模题 两种解法：
    1 排序 计算0的个数 然后观察gap 如果gap< 0的个数 且没有重复 则可以构成顺子 
    2 排序 计算0的个数 用最大 - 除0之外的最小值 如果结果小于5 则可以构成顺子(事先需要判断有无重复)
'''
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        numsOfZero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                numsOfZero += 1
            else:
                break
        for i in range(numsOfZero, len(nums)):
            if nums[i] == nums[numsOfZero] + i - numsOfZero:
                continue
            else:
                dura = nums[i] - nums[i - 1] - 1
                if dura > numsOfZero or dura < 0:
                    return False
        return True

    def isStraight_T(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort() # 数组排序
        for i in range(4):
            if nums[i] == 0: joker += 1 # 统计大小王数量
            elif nums[i] == nums[i + 1]: return False # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5 # 最大牌 - 最小牌 < 5 则可构成顺子




S = Solution()
print(S.isStraight([11, 8, 12, 8, 10]))
