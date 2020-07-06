from typing import List
'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

'''
'''
    位运算的应用 利用异或遍历整个数组 找到那两个不同数字的异或结果
    由于数字不同所以异或结果二进制中必有某一位为1 则以该位为界划分数组
    可以求得这两个所求数字。
'''


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        def findIndBit(nums):
            temp = nums[0]
            for i in range(1, len(nums)):
                temp ^= nums[i]
            index = 0
            while (temp & 1) != 1:
                temp = temp >> 1
                index += 1

            return index

        index = findIndBit(nums)
        a, b = None, None
        for i in range(len(nums)):
            t = nums[i] >> index
            if (t & 1) == 1:
                a = nums[i] if not a else a ^ nums[i]
            else:
                b = nums[i] if not b else b ^ nums[i]
        res = [a, b]
        return res

    def SingleOneinTriNum(self, nums: List[int]) -> int:
        '''
            在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。
            请找出那个只出现一次的数字。
        '''
        '''
            核心思路 每个出现三次的数字 其二进制上的值 出现的次数为三的倍数。
            于是 对每个二进制位1出现的情况进行统计之后 mod 3 既可以得到只出现一次的数字
            下面是LC 上大佬的有限状态机的解法：由于mod 3 只能有三种情况 所以总共只有三种状态。
            0->1->2  如果位 1 则状态转换  位 0 则状态不变。
            由于有三个状态 于是用两个数位来状态机.
            而下面的写法 相当于除了 a,b 自身的二进制0，1表达两种状态
            然后再借了对方的同样的位做状态
        '''
        a, b = 0, 0
        for i in range(len(nums)):
            a = a ^ nums[i] & ~b
            b = b ^ nums[i] & ~a
        return a

    def SingleOneinTriNum_Ord(self, nums: List[int]) -> int:
        '''
            书上的解法 
            几个小点 1 counts 是 按位递增记录 
                    而求解的时候从高位处理会简单很多 所以从后往前遍历counts
                    2 当结果时负数的时候 因为python 存储负数特殊 所以需要额外处理：
                        res if counts[31] % m == 0 else ~(res ^ 0xffffffff)
        '''
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m #可以用加法
        return res #if counts[31] % m == 0 else ~(res ^ 0xffffffff)


S = Solution()
print(S.singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))
print(S.SingleOneinTriNum_Ord([9, -1, 7, 9, 7, 9, 7]))
