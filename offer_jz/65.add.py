'''
    写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
'''
'''
    位运算  进位表达： a&b<<1  非进位和: a^b
    python 数据存储为补码形式
    为了处理负数 ： 需要与0xffffffff 相与 获得一个32位无符号整数
    如果补码 大与 0x7fffffff（最大的正数补码） 则需要取反。
'''


class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)