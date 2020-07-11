from typing import List

'''
给定一个整数数组 nums，按要求返回一个新数组 counts.
数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
'''

'''
    分治归并思想的应用 与 剑指 51 逆序对解法一模一样 难
    注意 使用索引数组 保持原本数组元素关系。仅更新索引数组。
        与逆序对不同的是 逆序对在前有序数组元素归并时计算逆序对的个数
                            也可以在后有序数组归并时计算逆序对个数
        而本题 仅适用 前有序数组归并时计算逆序对个数。
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [0]
        indexs = [i for i in range(n)]
        res = [0 for i in range(n)]
        temp = [None for _ in range(n)]
        self.mergeSort(nums, 0, n - 1, temp, indexs, res)
        return res

    def mergeSort(self, nums, left, right, temp, indexs, res):
        if left == right:
            return
        mid = left + (right - left) // 2
        self.mergeSort(nums, left, mid, temp, indexs, res)
        self.mergeSort(nums, mid + 1, right, temp, indexs, res)
        if nums[indexs[mid]] <= nums[indexs[mid + 1]]:
            return
        self.__sort(nums, left, mid, right, temp, indexs, res)

    def __sort(self, nums, left, mid, right, temp, index, res):
        for i in range(left, right + 1):
            temp[i] = index[i]
        l, r = left, mid + 1
        for i in range(left, right + 1):
            if l > mid:
                index[i] = temp[r]
                r += 1
            elif r > right:
                index[i] = temp[l]
                l += 1
                res[index[i]] += (right - mid)
            elif nums[temp[l]] <= nums[temp[r]]:
                index[i] = temp[l]
                l += 1
                res[index[i]] += r - mid - 1
            else:
                index[i] = temp[r]
                r += 1


S = Solution()
print(S.countSmaller([5, 2, 6, 1]))
