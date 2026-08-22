# heap, minheap
# push value freq onto the heap
# if length heap > k pop min value O(log k)

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        # {1: 1, 2: 2, 3:3}

        heap = []

        for value, freq in counts.items():
            heapq.heappush(heap, (freq, value))
            if len(heap) > k:
                heapq.heappop(heap) # O(log k)
            
        res = []

        for freq, value in heap:
            res.append(value)

        return res
        