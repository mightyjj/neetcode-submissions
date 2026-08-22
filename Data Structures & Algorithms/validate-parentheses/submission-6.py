class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}': '{', ']': '[', ')': '('}
        stack = []

        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif c in mapping.keys():
                if not stack or stack.pop() != mapping[c]:
                    return False
            else:
                return False
        
        return not stack