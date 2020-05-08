'''
   给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储一位数字。 
   
'''
'''
    思路 逐位相加 用flag 标记进位 不等长情况时 在一个整数结束后 后续根据进位 处理另外的整数 均结束时 判断进位是否为1 
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        ans = ListNode(0)
        temp = ans
        while l1!=None or l2 != None:
            x = l1.val if l1 else 0  #不等长情况 
            y = l2.val if l2 else 0
            if x + y + flag >= 10:
                temp.next = ListNode((x+y+flag)%10)
                flag = 1
            else:
                temp.next = ListNode(x+y+flag)
                flag = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            temp = temp.next
        if flag != 0:
            temp.next =ListNode(1)
        return ans.next