class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        # dp[i] represents the length of the LIS ending at index i
        dp = [1] * n
        
        # For each position, look at all previous positions
        for i in range(1, n):
            for j in range(i):
                # If current number is greater than previous number,
                # we can potentially extend the subsequence
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Return the maximum value in dp array
        return max(dp)