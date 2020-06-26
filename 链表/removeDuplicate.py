
from typing import List

import sys
sys.path.append(".")
sys.path.append("..")
import util

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        visited = {}
        visited[head.val] = 1
        pos = head
        while pos.next:
            cur = pos.next
            if cur.val not in visited:
                visited[cur.val] = 1
                pos = pos.next
            else:
                pos.next = cur.next
        return head


h = util.buildLinkFromList([1, 2, 3, 3, 2, 1])
S = Solution()
util.printLinkList(S.removeDuplicateNodes(h))