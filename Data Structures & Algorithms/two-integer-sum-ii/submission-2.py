class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for index, val in enumerate(numbers):
            if target - val in seen:
                return sorted([index + 1, seen[target - val] + 1])
            else:
                seen[val] = index
        