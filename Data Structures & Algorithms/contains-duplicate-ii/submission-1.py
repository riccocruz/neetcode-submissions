class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dups = set()
        l = 0
        for r, num in enumerate(nums):
            if r - l > k:
                dups.remove(nums[l])
                l += 1
            if num in dups:
                return True
            dups.add(num)
        
        return False