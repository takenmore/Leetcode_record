from typing import List

'''
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
在处理标点符号和大小写之前，你得先把它断成词语。
当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，
设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

'''

'''
    动态规划
    类似于双指针窗口的动态规划，用字典里面最长的元素长度作为窗口大小，然后进行滑窗匹配
    状态转移  当不匹配时 dp[i] = dp[i-1] + 1 匹配时 dp[i] = min(dp[i],dp[j])
    注意 不能直接 dp[i] = dp[j] 因为一个窗口内可能出现多次匹配的情况。要取最小。
'''
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        if n == 0:
            return 0
        if len(dictionary) <= 0:
            return n
        maxlen = 0
        for i in range(len(dictionary)):
            maxlen = max(maxlen, len(dictionary[i]))
        dp = [0 for i in range(n + 1)]
        dictionary = set(dictionary)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(max(0, i - maxlen), i):
                if sentence[j:i] in dictionary:
                    dp[i] = min(dp[j],dp[i])
        print(dp)
        return dp[n]


S = Solution()
print(
    S.respace(["looked","just","like","her","brother"], "jesslookedjustliketimherbrother"))
