class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds = whites = blues = 0

        for num in nums:
            if num == 0:
                reds += 1
            elif num == 1:
                whites += 1
            elif num == 2:
                blues += 1
        
        i = 0
        while reds > 0:
            nums[i] = 0
            i += 1
            reds -= 1
        
        while i < len(nums) and whites > 0:
            nums[i] = 1
            i += 1
            whites -= 1
        
        while i < len(nums) and blues > 0:
            nums[i] = 2
            i += 1
            blues -= 1
        
    
