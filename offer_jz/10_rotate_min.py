'''
@description: 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
              输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
              例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
@param {type} 旋转数组
@return: 最小数字
'''
from typing import List
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if numbers == []:
            return -1
        p_h,p_t = 0,len(numbers)-1
        mid = p_h+(p_t-p_h)//2 #
        while p_t>p_h:
            mid = p_h+(p_t-p_h)//2
            if numbers[p_t]<numbers[mid]:
                p_h = mid + 1
            elif numbers[p_h]>numbers[mid]:
                p_t = mid
            else:
                p_t -= 1
        return numbers[p_t]

Test = Solution()
print(Test.minArray([3, 4, 5, 1, 2]))
print(Test.minArray([1, 2, 3, 4, 5]))
print(Test.minArray([1, 1, 1, 0, 1]))
print(Test.minArray([1, 0, 1, 1, 1]))
print(Test.minArray([]))
print(Test.minArray([1]))