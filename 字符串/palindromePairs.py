from typing import List
'''
    给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，
    使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
'''
'''
    枚举前缀后缀进行匹配  如果A的前缀 的 翻转是B的后缀 且 A的后缀是回文串则符合条件
    核心就是 判断下所有为回文的前后缀 然后 排除掉 然后找剩余子串的翻转是否存在。
    类似于前缀数组
    先存下所有单词的翻转然后每次找翻转的时候如果找到则记录到结果中 注意顺序
'''


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrom(word, left, right):
            sub = word[left:right + 1]
            return sub == sub[::-1]

        dic = {word[::-1]: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrom(word, j, m - 1):
                    left = dic.get(word[0:j], -1)
                    if left != -1 and left != i:
                        res.append([i, left])
                if j != 0 and isPalindrom(word, 0, j - 1):
                    right = dic.get(word[j:m], -1)
                    if right != -1 and right != i:
                        res.append([right, i])
        return res


S = Solution()
print(S.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))