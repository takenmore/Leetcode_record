'''
@description: 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
            k 是一个正整数，它的值小于或等于链表的长度。
            如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
@param {type}  链表 以及 k
@return: 翻转后链表
'''
'''
    哨兵结点的使用， 双指针。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, head,tail):
        prev = tail.next
        p = head
        while p != tail:
            temp = p.next
            p.next = prev
            prev = p
            p = temp
        return tail,head
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0) # 哨兵结点
        hair.next = head
        p = hair
        while head:
            tail = p
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            n = tail.next
            head,tail = self.reverse(head,tail)
            p.next = head
            tail.next = n
            p = tail
            head = tail.next
        return hair.next



