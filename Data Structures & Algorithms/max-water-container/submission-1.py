class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_vol = 0

        while l < r:
            curr_vol = (r - l) * min(heights[l], heights[r])
            # check if this is max
            max_vol = max(max_vol, curr_vol)

            # l bar is lower, move it
            if min(heights[l], heights[r]) == heights[l]:
                l += 1
            else:
                r -= 1
        return max_vol
            

