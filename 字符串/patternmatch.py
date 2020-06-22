'''
        你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。
        例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），
        该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。
        编写一个方法判断value字符串是否匹配pattern字符串。
'''

'''
        暴力匹配 带一点数学上的优化   la * ca + lb * cb = len(value)
        转变思路
        枚举长度固定的字符串 然后滑动匹配。
'''
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        n = len(value)
        count_a = sum(1 for ch in pattern if ch == 'a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)
        if not pattern:
            return value == ""
        if not value:
            return count_b == 0
        for i in range(n // count_a + 1):
            rest = n - i * count_a
            if (count_b == 0 and rest == 0) or rest % count_b == 0:
                j = 0 if count_b == 0 else rest // count_b
                pos = 0
                res = True
                subA, subB = None, None
                for s in pattern:
                    if s == 'a':
                        temp = value[pos:pos + i]
                        if not subA:
                            subA = temp
                        else:
                            if subA != temp:
                                res = False
                                break
                        pos += i
                    else:
                        temp = value[pos:pos + j]
                        if not subB:
                            subB = temp
                        else:
                            if subB != temp:
                                res = False
                                break
                        pos += j
                if res and subA != subB:
                    return True
        return False


S = Solution()
print(S.patternMatching('bbbbbbbbbbbbbbabbbbb', 'ppppppppppppppjsftcleifftfthiehjiheyqkhjfkyfckbtwbelfcgihlrfkrwireflijkjyppppg'))


