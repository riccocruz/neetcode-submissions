class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-w for w in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)
            if one != two:
                heapq.heappush(stones, one - two)

        return abs(stones[0]) if stones else 0