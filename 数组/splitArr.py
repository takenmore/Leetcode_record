from typing import List

'''
    给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。
    设计一个算法使得这 m 个分割出来的子数组各自和的最大值最小。
'''

'''
    变换思路的二分查找  (值域二分查找) (如果存在负数可能应该DP解。)
    由题意可知  这个值的可行范围在 [max(nums), sum(nums)]内
    二分过程中模拟对数组划分的过程 贪心的认为中值是 所求 然后模拟划分之后得到子数组个数
    如果个数过大  则说明中值小了 应该加大  个数少了 则说明中值大了 应该减小。
    一旦个数符合之后， 二分实际上会一直缩小可行值范围 直到只剩一个值。left == right
    不一定对：
    (一 非负 才能得到正确的可行域
     二 非负 才能“严格有序”
        这里的有序的含义是 由于数组内元素非负，所以确保在模拟划分时 连续子数组和是一直递增的。
        且模拟划分出的子数组时 分的越多 子数组各自和的最大值越小。)
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if not nums:
            return 0
        if len(nums) == m:
            return max(nums)
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) >> 1
            temp = 0
            cnt = 1
            for num in nums:
                if temp + num > mid:
                    temp = num
                    cnt += 1
                else:
                    temp += num
            if cnt > m:
                low = mid + 1
            else:
                high = mid
        return low
    def splitArray_dp(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[10**18] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)
        
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sub[i] - sub[k]))
        
        return dp[n][m]


S = Solution()
print(S.splitArray([7, 2, 5, 10, 8], 2))
