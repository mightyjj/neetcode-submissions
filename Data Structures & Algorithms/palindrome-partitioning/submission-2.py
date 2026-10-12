class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
            
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if s[i:j+1] == sub[::-1]:
                    part.append(sub)
                    dfs(j + 1)
                    part.pop()
                
        dfs(0)

        return res