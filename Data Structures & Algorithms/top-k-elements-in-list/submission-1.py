class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
    
        vals = [[] for _ in range(len(nums) + 1)]
        for key, val in count.items():
            vals[val].append(key)
        
        result = []
        for val in vals[::-1]:
            for v in val:
                result.append(v)
                if len(result) >= k:
                    return result
