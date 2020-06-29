'''
    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
    如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''
'''
    维护两个堆 一个大根堆 一个小根堆 则能够保证中位数一定出现在堆顶 取中位数的操作时间复杂度为常数
    而在添加数据的时候 则需要动态保证 堆的特征之外 还要确保小根堆里面的数据大于大根堆里的数据
    做法： 将数据先插入大根堆 然后取大根堆顶元素插入小根堆中  反之同理
'''
from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minH = []
        self.maxH = []


    def addNum(self, num: int) -> None:
        if len(self.minH) != len(self.maxH):
            heappush(self.maxH, -num)
            heappush(self.minH, -heappop(self.maxH))
        else:
            heappush(self.minH, num)
            heappush(self.maxH, -heappop(self.minH))


    def findMedian(self) -> float:
        return -self.maxH[0] if len(self.minH) != len(self.maxH) else (self.minH[0] - self.maxH[0]) / 2.0

Mid = MedianFinder()
Mid.addNum(1)
Mid.addNum(2)
print(Mid.findMedian())
Mid.addNum(3)
print(Mid.findMedian())
