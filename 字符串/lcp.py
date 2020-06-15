from typing import List

'''
@description: 编写一个函数来查找字符串数组中的最长公共前缀。
            如果不存在公共前缀，返回空字符串 ""。
@param {type} 字符串数组
@return: 最长公共前缀
'''
 # easy题 ，留档 目前是常人思路  待实现高级解法 字典树。
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        res = strs[0]
        for i in range(1, n):
            j = 0
            while j < len(res) and j < len(strs[i]) and strs[i][j] == res[j]:
                j += 1
            res = strs[i][0:j]
            if not res:
                return ""
        return res


S = Solution()
print(S.longestCommonPrefix(["dog", "racecar", "car"]))