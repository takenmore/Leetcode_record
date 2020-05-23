'''
@description: 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
@param {type} 两个字符串
@return: 最小子串
'''
'''
    滑动窗口 思路：逐步扩张窗口 直到 包含T所有字符时， 开始缩小窗口，直到不满足包含T所有字符 则为待选子串
    坑点： 包含所有字符意思是 不去重的所有字符 也就是说 子串的各字符统计计数 要大于等于 T中各字符统计计数
          而不是T中的每个字符均存在于子串中。
    应对坑点： 采用两个字典分别记录 T的各字符统计计数 以及 判断的子串的各字符统计计数
'''
from collections import defaultdict
class Solution:
    def check(self,s,t):
        for k,v in t.items():
            if s[k] < v:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        head = 0
        tail = -1
        MinLength = len(s)
        ans = ''
        t_d = {}
        for i in range(len(t)):
            if t[i] in t_d:
                t_d[t[i]]+=1
            else:
                t_d[t[i]] = 1
        s_d = defaultdict(int)
        while tail < len(s):
            if self.check(s_d,t_d):
                if (tail - head + 1) <= MinLength:
                    MinLength = tail-head +1
                    ans = s[head:tail+1]
                s_d[s[head]] -= 1
                head += 1
            else:
                tail += 1
                if tail < len(s):
                    s_d[s[tail]] += 1
        return ans

s = Solution()
print(s.minWindow("acbbaca","aba"))
