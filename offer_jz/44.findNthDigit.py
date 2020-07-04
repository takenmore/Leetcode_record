'''
    数字以0123456789101112131415…的格式序列化到一个字符序列中。
    在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
    请写一个函数，求任意第n位对应的数字。
'''

'''
    数学题   利用位数优化时间复杂度 0-9 占10位 10-99 -180位 100-999 2700位
    然后判断所求位数位于哪个区间 以及进一步求出具体的数字 和 所在数位。
'''
class Solution:
    def findNthDigit(self, n: int) -> int:
        def countBit(n):
            if n == 1:
                return 10
            start = pow(10, n-1)
            return 9 * start * n
        digit = 1
        cur = 10
        while n > cur:
            n -= cur
            digit += 1
            cur = countBit(digit)
        num = pow(10, digit - 1) + (n) // digit
        return  int(str(num)[n % digit])


S = Solution()
print(S.findNthDigit(11))
