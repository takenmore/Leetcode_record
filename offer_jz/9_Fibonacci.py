'''
@description: 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。f(n) = f(n-1)+f(n-2) f(0)=0 f(1)=1
@param {type} num:int
@return: 第n项值
'''
class Solution_f:
    from functools import lru_cache
    @lru_cache(maxsize=128)
    def fib(self, n: int) -> int:
        temp = [0,1]
        if n<=1:
            return temp[n]
        f_1,f_2 = 0,1
        for i in range(2,n+1):
            num = f_1 + f_2
            f_1 = f_2
            f_2 = num
        return num

'''
    青蛙跳台阶  一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
'''
class Solution:
    def numWays(self, n: int) -> int:
        temp =[1,1,2]
        if n<=2:
            return temp[n]
        f_1,f_2=1,2
        for i in range(3,n+1):
            num = f_1 + f_2
            f_1 = f_2
            f_2 = num
        return num