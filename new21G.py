'''
@description: 爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字.
抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。
当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？
@param {type} N 最大分数  K 可行分数上限 W 分数集合[1,W]
@return: 结果小于N的概率
'''
'''
    动态规划的一道题 看了题解才会
    每个分数出现的概率为1/W，而终止抽取的最大分数为K-1 而可获得的最大分数为 K-1+W
    dp[x] 代表已经有的分数为x时 最终分数不超过N的概率
    从边界分数开始分析 在拥有了K-1分数时 只能再抽最后一张 此时不超过N的概率为 1/W*(N-K+1)
    dp[K-1]=1/W*(N-K+1)=1/W*(dp[K]+dp[K+1]+...+dp[K+W-1])
    所以初步的状态转移方程为 dp[x] = (dp[x+1]+...dp[x+W])/W   0<=x<K
    优化 dp[x]-dp[x+1] = (dp[x+1]-dp[x+W+1])/W  0<=x<K-1
    整理 dp[x] = (1+1/W)dp[x+1]-1/W*dp[x+W+1]
    最终从上至下 求解到dp[0]即为所求 意思是当已经有了的分数为0时 最终分数不超过N的概率
'''
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        dp[K - 1] = float(min((N - K + 1), W) / W)
        for i in range(K - 2, -1, -1):
            dp[i] = (1 + 1 / W) * dp[i + 1] - dp[i + W + 1] / W
        return dp[0]

S = Solution()
print(S.new21Game(21, 17, 10))
