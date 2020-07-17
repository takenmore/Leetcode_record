from typing import List
'''
    给定一个无向图graph，当这个图为二分图时返回true。

    如果我们能将一个图的节点集合分割成两个独立的子集A和B，
    并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。

    graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。
    每个节点都是一个在0到graph.length-1之间的整数。
    这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。

'''

'''
    dfs + 颜色标记
    从头开始dfs遍历 如果遇到无标记的点则标记 然后遍历它的邻居 
    有标记则检验其邻居是否和它标记一样如果一样则不是二分图。

'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        GREEN, RED = 1, 2
        color = [0 for i in range(n)]
        valid = True
        
        def dfs(node, c):
            nonlocal valid
            color[node] = c
            cur = (GREEN if c == RED else RED)
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    dfs(neighbor, cur)
                    if not valid:
                        return
                elif color[neighbor] != cur:
                    valid = False
                    return

        for i in range(n):
            if color[i] == 0:
                dfs(i,RED)
                if not valid:
                    break
        return valid




S = Solution()
print(S.isBipartite([[1,3], [0,2], [1,3], [0,2]]))
