# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
@description: 输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。
@param {type} 链表  所求的倒数节点值
@return: 倒数节点
'''
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        fast, slow = head, head
        for i in range(k):
            if fast.next:
                fast = fast.next
            else:
                return None
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow