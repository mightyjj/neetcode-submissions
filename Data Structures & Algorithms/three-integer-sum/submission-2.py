class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # check dupes
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # assign pointers
            l = i + 1
            r = len(nums) - 1

            # iterate
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skips dupes
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif curr < 0:
                    l += 1
                else:
                    r -= 1
        return res