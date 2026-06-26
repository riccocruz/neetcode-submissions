class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # brute force:
        # sort the array O(nlogn)
        # while len(stones) > 1:
        #   get two heaviest and smash em
        #   then resort array O(nlogn)
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)

            if one != two:
                heapq.heappush(stones, -abs(one - two))
            
        return 0 if not stones else -stones[0]