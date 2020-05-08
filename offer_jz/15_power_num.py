'''
@description: 实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。
@param {type} base
@return: base 的整数次方
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0.0 and n<0:
            return 0
        if n<0:
            abs_n = -n
        else:
            abs_n = n
        result = self.power_abs_r(x,abs_n)
        if n<0:
            result = 1.0/result
        return result
    def power_abs_r(self,x,n)->float:
        if n==0:
            return 1
        if n==1:
            return x
        result = self.power_abs_r(x,n>>1)  #利用右移代替除2 
        result *= result
        if n&1==1:   #利用位与运算 代替 求余
            result *=x
        return result
s=Solution()
print(s.myPow(3.5,7))