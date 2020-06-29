from typing import List
'''
    输入整数数组 arr ，找出其中最小的 k 个数。
    例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
'''
'''
    依旧可以通过快速选择求解 问题是要求读入了所有数据之后才求解 离线
    通过堆求解是在线的算法 虽然渐进时间复杂度不如快速选择 但适合更多的场景
    默认python 提供的heapq 方法里面的heapify (堆排序) 是小根堆 取负值转换构建大根堆
    C++ 可以直接用优先队列 priority_queue
'''
import heapq

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k <= 0 or len(arr) < k:
            return []

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans



S = Solution()
print(S.getLeastNumbers([0, 0, 1, 2, 4, 2, 2, 3, 1, 4], 8))
