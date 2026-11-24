class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, nums[i] + i)
            
            l = r + 1
            r = furthest
            steps += 1
        
        return steps