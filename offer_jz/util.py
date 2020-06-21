class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printLinkList(LinkList: ListNode):
    while LinkList:
        print(LinkList.val, end='')
        if LinkList.next:
            print('->', end='')
        LinkList = LinkList.next
    print('')