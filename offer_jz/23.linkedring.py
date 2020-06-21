class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
    一个链表中包含环，请找出该链表的环的入口结点。
'''


class Solution:
    def MeetNode(self, Linklist):
        if not Linklist:
            return None
        pSlow = Linklist.next
        if not pSlow:
            return None
        pFast = pSlow.next
        while pSlow != None and pFast != None:
            if pFast == pSlow:
                return pFast
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next
        return None

    def EntryNode(self, Linklist):
        meetNode = self.MeetNode(Linklist)
        if not meetNode:
            return None
        RingNodeNum = 1
        pNode = meetNode
        while pNode.next != meetNode:
            pNode = pNode.next
            RingNodeNum += 1
        pNode = Linklist
        for _ in range(RingNodeNum):
            pNode = pNode.next
        pSlow = Linklist
        while pSlow != pNode:
            pSlow = pSlow.next
            pNode = pNode.next

        return pNode


head = ListNode(1)
p_1 = ListNode(2)
p_2 = ListNode(3)
p_3 = ListNode(4)
p_4 = ListNode(5)
head.next = p_1
p_1.next = p_2
p_2.next = p_3
p_3.next = p_4
p_4.next = p_2
S = Solution()
print(S.EntryNode(head).val)
