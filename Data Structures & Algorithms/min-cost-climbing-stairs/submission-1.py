class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)

        if N == 2:
            return min(cost)
        
        n1, n2 = cost[0], cost[1]

        for i in range(2, N):
            temp = n2
            n2 = cost[i] + min(n1, n2)
            n1 = temp

        return min(n1, n2)