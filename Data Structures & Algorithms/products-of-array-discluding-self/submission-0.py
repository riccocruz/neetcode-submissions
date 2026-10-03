class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive solution
        forward = [1 for _ in range(len(nums))]
        for i in range(len(nums) - 1):
            forward[i + 1] = nums[i] * forward[i]
        
        res = [1 for _ in range(len(nums))]
        for i in range(len(nums) - 1, 0, -1):
            res[i - 1] = nums[i] * res[i]
        
        return [x * y for x, y in zip(forward, res)]