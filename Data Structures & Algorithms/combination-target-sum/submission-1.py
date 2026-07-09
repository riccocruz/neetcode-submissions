class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, amt, cur):
            if amt > target:
                return
            
            if amt == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                cur.append(nums[j])
                backtrack(j, amt + nums[j], cur)
                cur.pop()
        
        backtrack(0, 0, [])
        return res