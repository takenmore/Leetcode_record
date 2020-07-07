from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        res = []
        for i in range(k):
            while deque and nums[i] > deque[-1]:
                deque.pop()
            deque.append(nums[i])
        res.append(deque[0])
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and nums[i] > deque[-1]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res


nums = [-7, -8, 7, 5, 7, 1, 6, 0]
k = 4
S = Solution()
print(S.maxSlidingWindow(nums, k))

'''
请定义一个队列并实现函数 max_value 得到队列里的最大值.
要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
'''
import queue
class MaxQueue:

    def __init__(self):
        self.deque = collections.deque()
        self.queue = queue.Queue()


    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1


    def push_back(self, value: int) -> None:
        while self.deque and value > self.deque[-1]:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        res = self.queue.get()
        if res == self.deque[0]:
            self.deque.popleft()
        return res