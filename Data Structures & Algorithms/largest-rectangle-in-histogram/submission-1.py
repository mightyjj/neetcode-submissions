class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # height, idx
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                h, idx = stack.pop()
                w = i - idx
                a = h * w
                max_area = max(max_area, a)
                start = idx
            
            stack.append((height, start))
        
        while stack:
            h, idx = stack.pop()
            w = len(heights) - idx
            a = h * w
            max_area = max(max_area, a)

        return max_area