class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # add keys to their respective values in array
        freq = [[] for _ in range(len(nums))]
        for key, val in count.items():
            freq[val - 1].append(key)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            res.extend(freq[i])
            if len(res) == k:
                return res
        
