class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: # its <= because if nums: [1]
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid

            # [4,5,6,7,0,1,2]
            #  l r         
            #  m 
            # target = 4

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:   # right sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1