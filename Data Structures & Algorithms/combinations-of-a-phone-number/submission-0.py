class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        N = len(digits)
        DMAP = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        
        res, cur = [], []

        def backtrack(i):
            if i == N:
                res.append("".join(cur))
                return
            
            for digit in DMAP[digits[i]]:
                cur.append(digit)
                backtrack(i + 1)
                cur.pop()
            
        backtrack(0)
        return res