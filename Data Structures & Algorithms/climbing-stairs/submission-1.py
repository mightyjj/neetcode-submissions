class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev, second_prev = 2, 1

        for _ in range(n - 2):
            curr = prev + second_prev
            second_prev = prev
            prev = curr
    
        return curr