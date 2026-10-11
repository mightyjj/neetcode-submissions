from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points:
            distance = sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(minHeap, (distance, point))

        res = []

        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res