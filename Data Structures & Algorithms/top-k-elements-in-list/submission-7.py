class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force count freq, sort highest to lowest, pick top k
        counts = collections.Counter(nums)
        # {1: 1, 2: 2, 3: 3}

        # sort it
        counts = sorted(counts.items(), key=lambda x : x[1], reverse=True)

        # due to sorted it converts to a list
        res = []
        for i in range(k):
            res.append(counts[i][0])

        return res