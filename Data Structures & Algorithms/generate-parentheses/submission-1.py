class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, cur = [], []

        def backtrack(lefts, rights):
            if lefts + rights == n * 2:
                res.append("".join(cur))
                return
            
            if rights < lefts and rights < n:
                cur.append(")")
                backtrack(lefts, rights + 1)
                cur.pop()
            if lefts < n:
                cur.append("(")
                backtrack(lefts + 1, rights)
                cur.pop()

        backtrack(0, 0)
        return res