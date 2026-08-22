class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums = list(enumerate(nums))
        index_nums.sort(key=lambda x : x[1])

        l, r = 0, len(nums) - 1

        while l < r:
            curr = index_nums[l][1] + index_nums[r][1]
            if curr == target:
                return [min(index_nums[l][0], index_nums[r][0]), max(index_nums[l][0], index_nums[r][0])]
            elif curr < target:
                l += 1
                continue
            else:
                r -= 1
                continue
    
