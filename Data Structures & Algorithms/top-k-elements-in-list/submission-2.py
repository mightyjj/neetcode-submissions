from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # use min heap
        counts = Counter(nums)
        heap = []
        res = []

        # {1: 1, 2: 2, 3: 3}

        for value, freq in counts.items():
            heapq.heappush(heap, (freq, value))
            if len(heap) > k:
                heapq.heappop(heap)

        for freq, value in heap:
            res.append(value)

        return res

        
        