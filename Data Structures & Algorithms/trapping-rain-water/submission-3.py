class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        left_max, right_max = height[l], height[r]

        while l < r:

            if left_max < right_max:
                area += left_max - height[l]
                l += 1
                left_max = max(left_max, height[l])
            else:
                area += right_max - height[r]
                r -= 1
                right_max = max(right_max, height[r])
        
        return area
