class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n values in nums
        # m is # of unique num values
        # brute force: count each freq sort from high to low -> pick top k

        counts = collections.Counter(nums)
        counts = sorted(counts.items(), key=lambda x : x[1], reverse=True)

        # {3: 3, 2: 2, 1: 1}

        res = []
        for count in counts:
            if len(res) == k:
                return res
            res.append(count[0])

        return res