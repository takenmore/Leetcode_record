'''
@description: 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。返回删除后的链表的头节点.
@param {type} 头节点 ，值
@return: 删除后链表
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            head = head.next
        else:
            temp = head
            while temp.next and temp.next.val != val:
                temp = temp.next
            if temp.next: 
                temp.next = temp.next.next
        return head


'''
    利用Leetcode测试。
'''

'''
    剑指的要求是 给定的是节点指针，要求在O(1)删除该节点
    。。解法
'''
class Solution:
    def deleteNode(self, head:ListNode, val:ListNode):
        if head is None or val is None:
            return None
        if val.next is not None:  # 待删除节点不是尾节点
            tmp = val.next
            val.val = tmp.val
            val.next = tmp.next
        elif head == val:  # 待删除节点只有一个节点，此节点为头节点
            head = None
        else:
            cur = head    # 待删除节点为尾节点
            while cur.next != val:
                cur = cur.next
            cur.next = None
        return head