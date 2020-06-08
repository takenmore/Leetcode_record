from typing import List
'''
@description: 给定一个由表示变量之间关系的字符串方程组成的数组，
每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。
在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名
@param {type} 等式方程集合
@return: 方程集合 正确 或 错误

'''

'''
    基本的并查集使用 难度不高
    下面的解法 空间复杂度可以优化 哈希表完全可以不用使用 通过将字母转换为数字的方法。
    先处理完所有等式 再处理不等式。
'''

class Solution:
    def find(self, x, table):
        if table[x] == x:
            return x
        return self.find(table[x], table)

    def equationsPossible(self, equations: List[str]) -> bool:
        Id = 0
        var2id = {}
        id2var = []
        res = True
        for equation in equations:
            if equation[0] not in var2id:
                var2id[equation[0]] = Id
                id2var.append(Id)
                Id += 1
            if equation[3] not in var2id:
                var2id[equation[3]] = Id
                id2var.append(Id)
                Id += 1
        for equation in equations:
            if equation[1] == '=':
                var = id2var[var2id[equation[3]]]
                des = id2var[var2id[equation[0]]]
                for i in range(Id):
                    if id2var[i] == var:
                        id2var[i] = des
        for equation in equations:
            if equation[1] == '!':
                if self.find(id2var[var2id[equation[0]]],
                             id2var) == self.find(id2var[var2id[equation[3]]],
                                                  id2var):
                    res = False
        return res


S = Solution()
print(
    S.equationsPossible(
        ["b!=g", "k!=e", "c==k", "c==b", "d!=i", "d==k", "k!=c"]))
