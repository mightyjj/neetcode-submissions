class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        second_prev, prev = 1, 2

        for i in range(3, n + 1):
            curr = prev + second_prev
            second_prev, prev = prev, curr
        
        return curr