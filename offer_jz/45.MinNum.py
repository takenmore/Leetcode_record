from typing import List


'''
    输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
'''

'''
    技巧  定义新的比较规则。 先数字转字符串 然后串接后进行比较。
'''
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        def compare(a, b):
            return 1 if a + b > b + a else -1

        nums = sorted([str(i) for i in nums], key=cmp_to_key(compare))

        return ''.join(nums)


S = Solution()
print(S.minNumber([10,2]))
