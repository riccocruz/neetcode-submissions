class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        n1, n2 = 2, 3
        for i in range(3, n):
            temp = n2
            n2 = n1 + n2
            n1 = temp
        return n2