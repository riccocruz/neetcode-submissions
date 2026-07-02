class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        res = 0
        for _ in range(k):
            res = heapq.heappop(nums)
        
        return -res