class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap) * -1
            y =  heapq.heappop(maxHeap) * -1

            if x < y:
                y -= x
                heapq.heappush(maxHeap, -y)
            elif x > y:
                x -= y
                heapq.heappush(maxHeap, -x)
            
        return -maxHeap[0] if len(maxHeap) else 0