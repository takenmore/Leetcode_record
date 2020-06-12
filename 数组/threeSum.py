from typing import List
'''
@description: 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

@param {type} 数组
@return: 所有不重复的三元组
'''
'''
    双指针 + 排序
    主要的要求在于不重复这一点 
    简单思路 ： 固定一个数后 剩余的数组部分就可以当作两数之和来做。
    利用sort之后能降低两数之和的求解时间复杂度。同时重复情况可以通过当前数和前一个数对比来排除
    注意。。python 索引小于0的情况。
    其次 双指针求解两数之和。 同样需要考虑重复情况。
    注意 left 和 right 两个指针前一个情况的区别。。

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            left, right = i + 1, n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            required = -nums[i]
            while left < right:
                if nums[left] + nums[right] < required:
                    left += 1
                elif nums[left] + nums[right] > required:
                    right -= 1
                else:
                    result = [nums[i], nums[left], nums[right]]
                    res.append(result)
                    left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res


S = Solution()
print(S.threeSum([-2, 0, 1, 1, 2]))