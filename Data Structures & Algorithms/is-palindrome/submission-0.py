class Solution:
    def isPalindrome(self, s: str) -> bool:
        working = ""

        for c in s:
            if c.isupper():
               working += c.lower()
            elif c.isalnum():
                working += c
        
        l, r = 0, len(working) - 1

        while l < r:
            if working[l] != working[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True
