class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        present = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in present:
                present.remove(s[l])
                l += 1
            
            present.add(s[r])
            res = max(res, r - l + 1)

        return res
