'''
@description: 解码一个编码过的字符串 返回解码后的字符串
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
@param {type} 字符串
@return: 解码后的字符串
'''
    # 利用辅助栈求解
    # 遇到 [ 数字 字母 无脑进栈  遇到 ] 出栈 并处理 直到 遇到 [ 继续进栈
    # 有个地方写法有点low。。 用了第二个栈来获得正确的字符顺序。

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        times = res = ''
        str_t = []
        for i in range(len(s)):
            if s[i].isnumeric():
                times += s[i]
                continue
            elif s[i] == '[':
                stack.append('[')
                stack.append(times)
                times = ''
                continue
            elif s[i] == ']':
                while not stack[-1].isnumeric():
                    str_t.append(stack.pop())
                temp_str = ''
                while str_t:
                    temp_str += str_t.pop()
                temp_str = temp_str * int(stack.pop())
                if stack.pop() == '[':
                    stack.append(temp_str)
                str_t = []
                continue
            stack.append(s[i])
        res = res.join(stack)
        return res

S = Solution()
print(S.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))