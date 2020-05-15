'''
@description: 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
@param {type} 整数数组，整数
@return: 和为整数的连续子数组个数
'''
'''
    比较容易想到的解法：BF 优化： 固定左边界，移动右边界 求和，若相等则count+1 否则移动右边界 时间代价 O(n^2) 空间代价 O(1)
    但是这样时间代价过高 于是 以空间换时间
    1. 前缀和数组 和BF 优化一样 只不过将 每次移动右边界的和记录下来，且 pre[i] = pre[i-1] + nums[i]
       则 题目可以转换为求有多少个 Sum(nums[i:j])s = pre[i]-pre[j-1]=k  而这么做记录了中间过程 但对时间还没有帮助
       依旧是 O(n^2) 空间 O(n)
    2. 前缀和 + hashMap(利用python的字典)  核心还在 求有多少个 但是如果遍历前缀和数组查找 是O(n)的额外时间开销 
        于是可以利用 HashMap 来存储  方便快速的查找。
    PS python 中 字典 与 Java的HashMap 类似， 但python {} 使用的是开放寻址法 处理冲突 Java 是链接法
        python 容易序列化  但删除麻烦 内存浪费？ Java 动态分配 删除容易 但 访问类似链式 不易序列化？

'''

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        sumNum = count = 0
        if nums == []:
            return count
        for i in range(len(nums)):
            sumNum += nums[i]
            if sumNum == k:
                count +=1
            if sumNum-k in d:
                count += d[sumNum-k]
            if sumNum in d:
                d[sumNum] += 1
            else:
                d[sumNum] = 1
        return count


s = Solution()
print(s.subarraySum([28,54,7,-70,22,65,-6],100))
