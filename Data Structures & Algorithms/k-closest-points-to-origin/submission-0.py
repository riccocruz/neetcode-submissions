class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        heapq.heapify(closest)
        for x, y in points:
            heapq.heappush(closest, [-math.sqrt(x**2 + y**2), [x, y]])
            if len(closest) > k:
                heapq.heappop(closest)
        return [coords[1] for coords in closest]
