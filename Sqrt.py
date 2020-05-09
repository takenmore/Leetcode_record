'''
@description: 实现 int sqrt(int x) 函数。
              计算并返回 x 的平方根，其中 x 是非负整数。结果只保留整数的部分，小数部分将被舍去。
@param {type}  x
@return: x的平方根
'''
'''
    基本二分查找法
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        left ,right,ans = 0,x,-1
        while left<=right:
            mid = (left+right) //2
            if mid * mid<=x:
                left = mid + 1 
                ans = mid
            else:
                right = mid - 1
        return ans

s = Solution()
print(s.mySqrt(16))
