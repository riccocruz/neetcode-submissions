class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        window = deque()

        for i, num in enumerate(nums):
            window.append(num)
            heapq.heappush(heap, (-num, i))
            if i < k - 1:
                continue

            curmax = num
            while heap[0][1] < i - k + 1:
                heapq.heappop(heap)

            popped_num, index = heap[0]
            curmax = max(curmax, -popped_num)
            window.popleft()

            res.append(curmax)
        return res