from typing import List
'''
    输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数.
    序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
'''

'''
    双指针。
'''
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right = 1, 2
        res = []
        while left < right:
            sumN = (left + right) * (right - left + 1) / 2
            if sumN < target:
                right += 1
            elif sumN > target:
                left += 1
            else:
                temp = []
                for i in range(left, right + 1):
                    temp.append(i)
                res.append(temp)
                left += 1
                right += 1
        return res


S = Solution()
print(S.findContinuousSequence(15))
