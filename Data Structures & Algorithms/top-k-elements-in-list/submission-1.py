from collections import Counter
# count then sort and then pick top k
# min heap if > k pop keep heap (removes lowest every time)
# buckets group numbers by freq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        # {1: 1, 2: 2, 3: 3}
        # {3: 3, 2: 2, 1: 1}

        res = []

        sorted_counts = sorted(counts.items(), key=lambda x : x[1], reverse=True)

        for value, freq in sorted_counts:
            if k == 0:
                return res
            
            res.append(value)
            k -= 1

        return res
