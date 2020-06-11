'''
@description: 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
@param {type} 字符串
@return: 是否为回文字符串
'''
'''
    回文字符串 判定 + 额外条件处理
    实际上 如果删除后是回文字符串 意味着 s[head+1:tail] 或 s[head:tail-1] 两个子字符串一定是回文字符串 
'''


class Solution:
    def helper(self, s, h, t):
        while h < t:
            if s[h] == s[t]:
                h += 1
                t -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1
        while head < tail:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
            else:
                return self.helper(s, head, tail - 1) or self.helper(
                    s, head + 1, tail)
        return True


s = Solution()
print(s.validPalindrome('bddb'))