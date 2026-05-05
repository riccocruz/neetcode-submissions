class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] + nums[j] == target:
        #             return [j, i]
        sums = {}
        for i, num in enumerate(nums):
            if target - num in sums:
                return [sums[target - num], i]
            sums[num] = i
