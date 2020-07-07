'''
    0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。
    求出这个圆圈里剩下的最后一个数字。
'''
'''
    迭代求解  
    迭代公式：f = 0 if n==1 else f = [f(n-1,m) + m] % n
'''


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n < 1 or m < 1: return -1
        res = 0
        for i in range(2, n):
            res = (res + m) % i
        return res
