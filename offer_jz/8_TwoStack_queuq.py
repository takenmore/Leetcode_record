'''
    利用两个栈实现队列 并实现 头部删除函数和尾部插入函数
    思路 一个栈存队列 一个栈用于操作
'''
class CQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2!=[]:
            return self.stack2.pop()
        while self.stack1:
            Val = self.stack1.pop()
            self.stack2.append(Val)
        if self.stack2==[]:
            return -1
        return self.stack2.pop()