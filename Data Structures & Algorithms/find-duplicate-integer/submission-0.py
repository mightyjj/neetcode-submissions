class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
         myDict = {}

         for num in nums:
            if num in myDict:
                return num
            else:
                myDict[num] = 1
                