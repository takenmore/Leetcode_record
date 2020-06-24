class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


'''
    请实现 copyRandomList 函数，复制一个复杂链表。
    在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
    还有一个 random 指针指向链表中的任意节点或者 null。

    复制链表需要复制 val ， next ，random三项
'''

#  利用哈希表降低时间复杂度
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}

        def getCloneNode(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    visited[node] = Node(node.val, None, None)
                    return visited[node]

        if not head:
            return head
        prev_node = head
        clone_node = Node(prev_node.val, None, None)
        visited[prev_node] = clone_node
        while prev_node:
            clone_node.random = getCloneNode(prev_node.random)
            clone_node.next = getCloneNode(prev_node.next)

            prev_node = prev_node.next
            clone_node = clone_node.next
        return visited[head]

