class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        one_index = 1
        l, r = 0, len(numbers) - 1

        while l < r:
            curr = numbers[l] + numbers[r]
            if curr == target and l != r:
                return [l + one_index, r + one_index]
            elif curr < target:
                l += 1
            else:
                r -= 1
