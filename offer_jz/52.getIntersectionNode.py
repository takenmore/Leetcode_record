class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
    输入两个链表，找出它们的第一个公共节点。
'''
'''
    持续遍历知道相遇 
    还有一种方法是可以利用快慢指针 先求两个链表的长度 然后求差。
    快指针先走差的步数 然后一起前进。
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1