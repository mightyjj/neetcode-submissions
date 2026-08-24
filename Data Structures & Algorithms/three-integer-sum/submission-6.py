class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            if i and num == nums[i - 1]:
                continue
            
            # if its not dupe, keep going
            l, r = i + 1, len(nums) - 1
            target = 0 - num
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum == target:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return result