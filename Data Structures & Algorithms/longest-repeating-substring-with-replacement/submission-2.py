class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        res = 0
        for r, c in enumerate(s):
            freq[c] += 1

            while k + max(freq.values()) < r - l + 1:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res