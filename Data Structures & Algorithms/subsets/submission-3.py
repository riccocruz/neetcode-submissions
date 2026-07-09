class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, cur):
            res.append(cur.copy())
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()
        backtrack(0, [])
        return res