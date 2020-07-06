'''
    reverseWords:
    输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
    为简单起见，标点符号和普通字母一样处理。
    例如输入字符串"I am a student. "，则输出"student. a am I"。
'''
'''
    reverseLeftWords
    字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
    请定义一个函数实现字符串左旋转操作的功能。
    比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"
'''
'''
    py 赖皮
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

S = Solution()
print(S.reverseWords("  the sky is blue"))
