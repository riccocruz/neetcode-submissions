class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []

        def backtrack(i):
            if len(cur) == len(nums):
                res.append(cur.copy())
            
            for j in range(len(nums)):
                if nums[j] not in cur:
                    cur.append(nums[j])
                    backtrack(j + 1)
                    cur.pop()
        backtrack(0)
        return res

