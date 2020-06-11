'''
@description: 现在你总共有 n 门课需要选，记为 0 到 n-1。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。
@param {type} 课程数量 n  二维课程先修数组 pre
@return: 课程安排顺序
'''
'''
    拓扑排序： 对于任何有向图而言，拓扑排序为其结点的一个线性排序(排序不唯一)，其满足若存在边从u指向v 则排序中u一定在v前面
    拓扑排序 解决 有向图的依赖解析问题  当且仅当 有向图为 有向无环图DAG 时 才存在拓扑排序 
    实现 BFS + 条件（每次只有入度为0的结点入队 入队后更新入度数组） 此题 O(n+e) n为点数 e为先修边数  DFS也可
    核心 维护一个所有结点的入度数组  注意最后判断是否存在拓扑排序 存在应该结束时 结果中包含所有结点
'''
from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        degree = [0 for i in range(numCourses)]
        res = []
        for i in range(len(prerequisites)):
            degree[prerequisites[i][0]] += 1
        out = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                out.append(i)
        while out:
            curr = out.pop()
            res.append(curr)
            for i in range(len(prerequisites)):
                if prerequisites[i][1] == curr:
                    degree[prerequisites[i][0]] -= 1
                    if degree[prerequisites[i][0]] == 0:
                        out.append(prerequisites[i][0])
        return res if len(res) == numCourses else []


s = Solution()
print(s.findOrder(3, [[1, 0], [1, 2], [0, 1]]))
