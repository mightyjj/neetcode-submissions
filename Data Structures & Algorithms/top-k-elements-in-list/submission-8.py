from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            
        ordered_nums = sorted(counts, key=counts.get, reverse=True)
        res = ordered_nums[:k]
        return res
                
            