class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        candidates.sort()

        res, cur = [], []

        def backtrack(index, total):
            if total > target:
                return
            if total == target:
                res.append(cur.copy())

            for i in range(index, N):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                cur.pop()
        
        backtrack(0, 0)
        return res