'''
    给你两个二进制字符串，返回它们的和（用二进制表示）。
    输入为 非空 字符串且只包含数字 1 和 0。
    字符串如果不是 "0" ，就都不含前导零。
'''
'''
    从后向前处理  补零  进位。
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        flag = 0
        res = []
        pa = len(a) - 1
        pb = len(b) - 1
        while pa >= 0 or pb >= 0:
            if pa < 0:
                ch_a = 0
            else:
                ch_a = ord(a[pa]) - ord('0')
            if pb < 0:
                ch_b = 0
            else:
                ch_b = ord(b[pb]) - ord('0')
            res.append(str(ch_a ^ ch_b ^ flag))
            if ch_a == 1 and ch_b == 1:
                flag = 1
            elif ch_a == 0 and ch_b == 0:
                flag = 0
            pa -= 1
            pb -= 1
        if flag == 1:
            res.append('1')
        return ''.join(res[::-1])


S = Solution()
print(S.addBinary('1', '1011'))