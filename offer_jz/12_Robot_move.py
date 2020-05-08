'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1]。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？

'''
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if m<=0 or n<=0 :
            return 0
        mask = [[0]*n for i in range(m)]
        def getnumsum(num):
            numsum =0
            while num > 0:
                numsum += num%10
                num = num//10
            return numsum
        def backtrace(i,j,k):
            count = 0
            if i<0 or i>=m or j>=n or j<0:
                return 0
            if getnumsum(i) + getnumsum(j)<=k and mask[i][j] == 0:
                mask[i][j]=1
                count = 1 + backtrace(i+1,j,k)+backtrace(i,j+1,k)
            return count
        count_all = backtrace(0,0,k)
        return count_all

s=Solution()
print(s.movingCount(1,2,1))
print(s.movingCount(2,3,1))