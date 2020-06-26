class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List


def printLinkList(LinkList: ListNode):
    while LinkList:
        print(LinkList.val, end='')
        if LinkList.next:
            print('->', end='')
        LinkList = LinkList.next
    print('')


def buildLinkFromList(nums: List):
    if not nums:
        return None
    n = len(nums)
    head = ListNode(None)
    prev = head
    for num in nums:
        temp = ListNode(num)
        prev.next = temp
        prev = prev.next
    return head.next

