'''
    给一个整数 求解其二进制表示中1的个数 例如 9 -> 1001 则返回 2
'''
'''
    通过位与运算求解
    tips： 把一个整数减去1后 与原来的整数做位与运算，得到的结果
    相当于整数的二进制表示中最右一位的1变成0 
    右移循环判断也可。
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count +=1
            n &= n-1
        return count

s = Solution()
print(s.hammingWeight(9))