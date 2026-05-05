class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        one = 2
        two = 3
        for i in range(4, n+1):
            temp = two
            two = one + two
            one = temp
        return two
