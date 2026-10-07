class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap) * -1
            y = heapq.heappop(max_heap) * -1
            if x < y:
                y -= x
                heapq.heappush(max_heap, -y)
            elif y < x:
                x -= y
                heapq.heappush(max_heap, -x)
            else:
                continue
        
        return -max_heap[0] if max_heap else 0