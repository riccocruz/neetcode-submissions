class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            distances.append((distance, [x, y]))
        
        heapq.heapify(distances)

        res = [heapq.heappop(distances)[1] for _ in range(k)]
        return res
