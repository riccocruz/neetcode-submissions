class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, cur = [], []

        def backtrack(lefts, rights):
            if lefts == rights == n:
                res.append("".join(cur))

            if lefts < n:
                cur.append("(")
                backtrack(lefts + 1, rights)
                cur.pop()
            if rights < lefts:
                cur.append(")")
                backtrack(lefts, rights + 1)
                cur.pop()
            
        backtrack(0, 0)
        return res