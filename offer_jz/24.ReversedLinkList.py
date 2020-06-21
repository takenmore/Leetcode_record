class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
'''
    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
'''
import util
class Solution:
    def reverseLinkList(self, pHead):
        pReverseHead = None
        pNode = pHead
        pPrev = None
        while pNode:
            pNext = pNode.next
            if not pNext:
                pReverseHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext

        return pReverseHead


s = Solution()
pHead = ListNode(1)
p_1 = ListNode(2)
p_2 = ListNode(3)
p_3 = ListNode(4)
p_4 = ListNode(5)
pHead.next = p_1
p_1.next = p_2
p_2.next = p_3
p_3.next = p_4

util.printLinkList(pHead)
util.printLinkList(s.reverseLinkList(pHead))