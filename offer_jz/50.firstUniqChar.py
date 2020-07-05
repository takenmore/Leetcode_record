'''
    在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
'''
'''
    简单哈希
'''
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        for char in s:
            if dic[char] == 1:
                return char
        return " "