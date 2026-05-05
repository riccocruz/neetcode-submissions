class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = {}, {}
        for c in s:
            a[c] = a.get(c, 0) + 1
        for c in t:
            b[c] = b.get(c, 0) + 1

        return a == b