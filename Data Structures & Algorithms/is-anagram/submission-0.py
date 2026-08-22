class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # we can reorder the strings
        return sorted(s) == sorted(t)