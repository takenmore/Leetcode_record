'''
    输入链表的头 从尾到头反过来返回每个节点的值 返回形式：数组。
    思路：直接用栈。
'''
from typing import List
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        l = []
        while head:
            l.insert(0,head.val)
            head = head.next
        return l
    
node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

test = ListNode()

S = Solution()
print(S.reversePrint(node1))
print(S.reversePrint(test))
print(S.reversePrint(singleNode))