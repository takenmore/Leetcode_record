'''
    替换字符串中的空格
'''
'''
    python 。。。懂？
    书中思路 双指针 后往前
'''
class Solution:
    def replaceSpace(self, s: str) -> str:
        c = []
        for i in s:
            if i == ' ':
                c.append('%20')
            else:
                c.append(i)
        return "".join(c)
    # 参考解法 双指针
    def replaceSpace3(self, s):
        if not isinstance(s,str) or len(s) <= 0 or s == None:
            return ""
        spaceNum = 0
        for i in s:
            if i == " ":
                spaceNum += 1
        newStrLen = len(s) + spaceNum * 2
        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
        while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew-2:indexOfNew+1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return "".join(newStr)
