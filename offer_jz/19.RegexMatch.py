'''
@description: 请实现一个函数用来匹配包含'. '和'*'的正则表达式。
              模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
              在本题中，匹配是指字符串的所有字符匹配整个模式。
              例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
@param {str} s 待匹配字符串 p 匹配模式
@return: 匹配结果
'''
'''
    正则表达式  解法非确定有限状态机
    遇到的坑：1. python 用下标 模拟 指针 需要额外注意下标越界的情况 这题相对越界有点小麻烦
    学习的点：1. 处理可能越界情况时，使用if 越界逻辑 and 其他逻辑 能够优化代码，当越界发生 其他逻辑不会再执行
            2. 状态机的建模方式 （初步

'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s==None or p==None:
            return False
        return self.matchcore(s,p,0,0)
    def matchcore(self,s,p,s_i,p_i):
        if p_i >= len(p):
            return s_i==len(s)
        if p_i < len(p)-1 and p[p_i+1] == '*':
            if s_i<=len(s)-1 and (s[s_i]==p[p_i] or p[p_i]=='.'):  #越界判断在先 越界后 后续逻辑不执行
                return self.matchcore(s,p,s_i+1,p_i) or self.matchcore(s,p,s_i,p_i+2)
               #return self.matchcore(s,p,s_i+1,p_i+2) or \
               # self.matchcore(s,p,s_i+1,p_i) or \
               # self.matchcore(s,p,s_i,p_i+2)f   书上的翻译 但是在第一个条件在下面的测试用例 超时
            else:
                return self.matchcore(s,p,s_i,p_i+2)   
        else:
            if s_i<=len(s)-1 and (s[s_i]==p[p_i] or p[p_i]=='.'): #越界判断在先 越界后 后续逻辑不执行
                return self.matchcore(s,p,s_i+1,p_i+1)
        return False

s = Solution()
print(s.isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c"))