'''
    请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
'''
'''
    哈希表 + 双指针 
    记录左右出现同一字符的index 然后相减
    也可用DP来解 本质一样
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, left = {}, 0, -1
        for right in range(len(s)):
            if s[right] in dic:
                left = max(dic[s[right]], left)  # 更新左指针 i
            dic[s[right]] = right  # 哈希表记录
            res = max(res, right - left)  # 更新结果
        return res

    def lengthOfLongestSubstring_dp(self, s: str) -> int:
        dic, cur, res = {}, 0, 0
        for i in range(len(s)):
            j = dic.get(s[i], -1)
            dic[s[i]] = i
            cur = cur + 1 if cur < i - j else i - j
            res = max(cur, res)
        return res


s = Solution()
print(s.lengthOfLongestSubstring_dp("abcdabcbb"))
