class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        l, r = 0, len(heights) - 1

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            if curr_area > biggest:
                biggest = curr_area
            elif heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return biggest