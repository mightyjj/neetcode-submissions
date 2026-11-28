class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)

        if sum_nums % 2:
            return False
        
        target = sum_nums // 2
        dp = set()
        dp.add(0)

        for num in nums:
            dp_copy = dp.copy()
            for t in dp:
                if t + num == target:
                    return True
                dp_copy.add(t + num)
            
            dp = dp_copy
        
        return False
