'''
@description: 给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 
              'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。
@param {type} 字符串
@return: 最长符合条件的子字符串
'''
'''
    状态压缩 + 位运算 + hash + 前缀和  
    奇偶校验的题 -- 异或运算  相同为0 不同为1 
    状态压缩 利用二进制 用一个二进制数来表示 只有二元状态 但是有很大的数量实体的状态情况
    例如 100个路灯，有亮有灭 如何记录状态 简单的想法 数组 但是如果是1000000 个路灯 数组可能会超内存
    这时用 二进制数来表达这个状态就会节约大量内存。 
    位运算 因为利用了状态压缩 所以 想知道状态的情况 利用位运算会快很多
    前缀和 连续子字符串 子数组 子。。。 考虑 前缀和 + hashmap/hashtable
    这题的前缀和 存储的是 元音字母出现次数的某种状态 出现最早的字符串index
    若该状态再次 出现 说明符合题目条件 而最早能够确保最长。
'''
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel = {'a':1,'e':2,'i':4,'o':8,'u':16}   # bitmask 状态压缩
        state = Longest = 0
        pre = {0:-1}   # -1的原因是 index 从0开始，当0状态第二次出现 时 当前index-(-1) =子字符串长度
        for i in range(len(s)):
            if s[i] in vowel.keys():
                state ^= vowel[s[i]]
                if state not in pre:
                    pre[state] = i
            Longest = max(Longest,i-pre[state])
        return Longest


s = Solution()
print(s.findTheLongestSubstring('bcbcbc'))