class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        l, r = 0, len(heights) - 1

        while l < r:
            biggest = max(biggest, min(heights[l], heights[r]) * (r - l))
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return biggest