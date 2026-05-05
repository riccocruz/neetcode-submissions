class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []

        def backtrack(i):
            res.append(cur.copy())

            for j in range(i, len(nums)):
                cur.append(nums[j])
                backtrack(j + 1)
                cur.pop()
        backtrack(0)
        return res