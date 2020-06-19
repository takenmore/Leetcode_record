from typing import List
'''
    给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。
    返回 A 的任意排列，使其相对于 B 的优势最大化。
'''
'''
    贪心算法 逻辑比较简单 但写好不容易
    首先 对两个数组都sort 令j = 0 然后遍历A， 找到A中 大于B[j] 的值 存储起来，小于的放进 remain里面(未曾采用)
    由于两个数组都是排序后的 所以 存储进visit 表的值 一定是 A中大于B[j] 的最小值 符合贪心的思想
    同样 由于sort 如果A[i] 小于 B[j] 则A[i] 一定小于 B[k](k>j) 所以后续A[i]是一定不可能被采用了 于是放进小黑屋
    最后重建 如果有大的 提取出来， 如果没有 从小黑屋里面拿
    注意 为了不影响 B 的顺序 所以B 不能原地sort 应该采用 sorted 方法。
'''


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        n = len(B)
        if n <= 1:
            return A
        A.sort()
        sortedB = sorted(B)  # 避免 影响B 的顺序
        visit = {b: [] for b in B}
        remain = []
        j = 0
        for i in range(n):
            if A[i] > sortedB[j]:
                visit[sortedB[j]].append(A[i])
                j += 1
            else:
                remain.append(A[i])

        return [visit[b].pop() if visit[b] else remain.pop() for b in B]


S = Solution()
print(S.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))

# 初始的 多倍 O(n^2)的结果  可以通过优化手段得到上面的结果
# B.sort()减少内层循环 额外空间remain 减少第二次循环
# class Solution:
#     def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
#         n = len(B)
#         if n <= 1:
#             return A
#         res = [0 for i in range(n)]
#         visit = {}
#         A.sort()
#         for i in range(n):
#             for j in range(n):
#                 if A[j] > B[i] and j not in visit:
#                     res[i] = A[j]
#                     visit[j] = 1
#                     break
#         for i in range(n):
#             if res[i] == 0:
#                 for j in range(n):
#                     if j not in visit:
#                         res[i] = A[j]
#                         visit[j] = 1
#                         break
#         return res
