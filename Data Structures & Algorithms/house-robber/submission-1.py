class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return max(nums)
        
        n1, n2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = n2
            n2 = max(n2, n1 + nums[i])
            n1 = temp
        
        return max(n1, n2)