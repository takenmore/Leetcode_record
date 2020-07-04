from typing import List
'''
@description: 给定一个数字，我们按照如下规则把它翻译为字符串：
0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
@param {type} 数字
@return: 翻译方法的种数
'''

'''
    基本DP 书中的解法是从末尾递归。
    当然可以利用滚动数组对空间进行优化 但(没必要)
'''
class Solution:
    def translateNum(self, num: int) -> int:
        str_num = str(num)
        dp = [1, 1]
        for i in range(2, len(str_num) + 1):
            if '10' <= str_num[i - 2:i] <= '25':
                dp.append(dp[i - 1] + dp[i - 2])
            else:
                dp.append(dp[i - 1])
        return dp[len(str_num)]


S = Solution()
print(S.translateNum(26))
