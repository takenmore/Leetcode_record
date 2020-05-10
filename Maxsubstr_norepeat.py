'''
@description: 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
@param {type} 字符串
@return: 最大子串的长度
'''
'''
    set 去重， 滑动窗口 当不满足的时候直接去掉set里面的当前字符
    逻辑： abcdabcbb  
        第一次循环： set: abcd  冲突字符:a  当前字符:a  于是相当于去掉下一次遍历的前一个字符
        第二次循环:  set:bcda   冲突字符:b  当前字符:b  同理
        ...
        直到遍历完字符串

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows = set()
        winlen = 0
        pi = -1
        for i, item in enumerate(s):
            if i != 0:
                windows.remove(s[i - 1])
            while pi < len(s) - 1 and s[pi + 1] not in windows:
                windows.add(s[pi + 1])
                pi += 1
            if len(windows) > winlen:
                winlen = len(windows)
        return winlen


s = Solution()
print(s.lengthOfLongestSubstring("abcdabcbb"))