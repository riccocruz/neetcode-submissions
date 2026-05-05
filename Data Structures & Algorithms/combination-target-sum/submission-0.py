class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        res, cur = [], []

        def backtrack(index, total):
            if total > target:
                return
            if total == target:
                res.append(cur.copy())
                return
            
            for i in range(index, N):
                cur.append(nums[i])
                backtrack(i, total + nums[i])
                cur.pop()
            
        backtrack(0, 0)
        return res