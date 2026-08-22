from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # naive: count freq in dic 
        counts = Counter(nums)
        # {1: 1, 2: 2, 3: 3}

        # sort by value
        sorted_counts = sorted(counts.items(), key=lambda x : x[1], reverse=True)

        res = []
        i = 0

        for value, freq in sorted_counts:
            if i == k:
                return res
            res.append(value)
            i += 1

        return res