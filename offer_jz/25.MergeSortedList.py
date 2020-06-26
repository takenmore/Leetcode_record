import sys
sys.path.append('.')
sys.path.append('..')
import util


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
    输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
'''


class Solution:
    def MergeSortedList(self, phead1, phead2):
        if not phead1:
            return phead2
        if not phead2:
            return phead1
        pMergeHead = None
        if phead1.val < phead2.val:
            pMergeHead = phead1
            pMergeHead.next = self.MergeSortedList(phead1.next, phead2)
        else:
            pMergeHead = phead2
            pMergeHead.next = self.MergeSortedList(phead1, phead2.next)
        return pMergeHead


List1 = ListNode(1)
l_2 = ListNode(3)
l_3 = ListNode(5)
List1.next = l_2
l_2.next = l_3
List2 = ListNode(2)
l_4 = ListNode(3)
l_5 = ListNode(6)
List2.next = l_4
l_4.next = l_5

s = Solution()
util.printLinkList(List1)
util.printLinkList(List2)

util.printLinkList(s.MergeSortedList(List1, List2))
