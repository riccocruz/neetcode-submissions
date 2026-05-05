class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        cur = []

        def helper(index):
            res.append(cur.copy())

            for i in range(index, N):
                cur.append(nums[i])
                helper(i + 1)
                cur.pop()
        
        helper(0)
        return res