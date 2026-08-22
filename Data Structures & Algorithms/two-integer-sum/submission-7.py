class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = list(enumerate(nums))
        nums_idx = sorted(nums_idx, key=lambda x : x[1])

        l, r = 0, len(nums) - 1

        while l < r:
            curr = nums_idx[l][1] + nums_idx[r][1]
            if curr == target:
                return [min(nums_idx[l][0], nums_idx[r][0]), max(nums_idx[l][0], nums_idx[r][0])]
            elif curr < target:
                l += 1
                continue
            else:
                r -= 1
                continue

        
            