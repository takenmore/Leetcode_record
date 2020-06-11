'''
    LRU缓存实现
    要求O(1)时间复杂度
    思路 快速读写： Hashmap  记录最近最少使用的项：双向链表
    记录的方法：当get或put对应项时 将对应数据项 移到链表尾部，put时容量不够了 将链表头部移除
    即为链表头部代表 最近最少使用 尾部代表最近一次使用
    原本准备用deque 双向队列实现，但是涉及到remove操作 时间复杂度O(n)
    于是只能参照题解 利用双向链表
'''
class LinkedNode:
    '''
        双向链表结点定义
    '''
    def __init__(self, key=None, val=None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    '''
    @description: LRU缓存简易实现
    获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
    写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。
    当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
    '''
    def __init__(self, capacity: int):
        self.record = {}
        self.capacity = capacity
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_tail(self, key: int):
        '''
        @description: 移动某节点到链表尾部
        @param {type} key 节点Key
        @return: None
        '''
        node = self.record[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.record:
            self.move_to_tail(key)
            return self.record[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        curr = LinkedNode(key, value)
        if key not in self.record:
            if len(self.record) == self.capacity:
                self.record.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            curr.next = self.tail
            curr.prev = self.tail.prev
            self.tail.prev.next = curr
            self.tail.prev = curr
            self.record[key] = curr
        else:
            self.record[key].val = value
            self.move_to_tail(key)

cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))
cache.put(3,3)
cache.get(2)
cache.put(4,4)
print(cache.record)
cache.get(1)
cache.get(3)
cache.get(4)