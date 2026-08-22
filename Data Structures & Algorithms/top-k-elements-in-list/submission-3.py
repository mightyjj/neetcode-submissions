from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket approach
        # put nums with same # freq in same bucket
        # sort it by bucket
        # number of buckets is the number of unique values

        counts = Counter(nums) # O(n)

        buckets = []

        for _ in range(len(nums) + 1):
            buckets.append([])

        for value, freq in counts.items():
            buckets[freq].append(value)

        res = []

        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res

        return res