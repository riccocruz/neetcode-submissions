class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # get tuple[] of distances, key = distance, v = [x, y]
        # heapify that
        # get the k closest

        distances = [(x**2 + y**2, [x, y]) for x, y in points]
        heapq.heapify(distances)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(distances)[1])

        return res