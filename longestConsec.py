'''
@description:
    给定一个未排序的整数数组，找出最长连续序列的长度。
    要求算法的时间复杂度为 O(n)。
@param {type} nums 未排序数组
@return: 最长连续序列的长度
'''
'''
    利用set去重 + 哈希 来优化 暴力解法  得到不严谨的O(n)解法
'''
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                cur_num = num
                cur_len = 1
                while cur_num+1 in num_set:
                    cur_num += 1
                    cur_len += 1
                res = max(cur_len, res)
        return res

# 并查集写法 但是 没过最长的测试用例 超时。。。
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         union = {}
#         res = 0
#         for num in nums:
#             if num not in union:
#                 union[num] = num
#         def find(x):
#             if x in union:
#                 return find(x+1)
#             else:
#                 return x
#         for i in range(len(nums)):
#             cur_len = find(nums[i])
#             res = max(res, cur_len - nums[i])
#         return res

S = Solution()
print(S.longestConsecutive([0, -1]))
