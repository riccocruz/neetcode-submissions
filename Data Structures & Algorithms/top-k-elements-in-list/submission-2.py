class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        bucket = [[] for _ in range(len(nums))]
        for key, val in counter.items():
            bucket[val - 1].append(key)
        
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.extend(bucket[i])
            if len(res) >= k:
                return res

