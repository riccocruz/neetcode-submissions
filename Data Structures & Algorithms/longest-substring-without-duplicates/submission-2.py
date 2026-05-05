class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        dups = set()
        l = 0
        for r, c in enumerate(s):
            while c in dups:
                dups.remove(s[l])
                l += 1
            dups.add(c)
            res = max(res, r - l + 1)
        return res
            