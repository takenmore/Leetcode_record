'''
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m]。
请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

'''
'''
    贪心解法 数学上 尽量剪3 乘积最大
'''
import math
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n<=3:
            return n-1
        a = n//3
        if (n - a*3) == 1:
            a -= 1
        b =(n-a*3)//2
        return int(math.pow(3,a)*math.pow(2,b))

'''
    dp 题解
'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]  # dp[0] dp[1]其实没用
        dp[2] = 1  # 初始化
        res = -1
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
        return dp[n]

s=Solution()
print(s.cuttingRope(8))