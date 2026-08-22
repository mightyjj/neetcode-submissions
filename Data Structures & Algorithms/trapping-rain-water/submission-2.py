class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force: iterate through update max l and max right for each i
        if not height:
            return 0

        maxL = [0] * len(height)
        maxR = [0] * len(height)

        for i in range(1, len(height)):
            maxL[i] = max(maxL[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], height[i + 1])
        
        # go through and recompute
        res = 0
        for i in range(len(height)):
            calc = min(maxL[i], maxR[i]) - height[i]
            if calc > 0:
                res += calc
        
        return res