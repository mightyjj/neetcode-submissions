class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def backtrack(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                sub = s[i:j + 1]
                if sub == sub[::-1]:
                    part.append(sub)
                    backtrack(j + 1)
                    part.pop()
            
        backtrack(0)
        return res


                
                