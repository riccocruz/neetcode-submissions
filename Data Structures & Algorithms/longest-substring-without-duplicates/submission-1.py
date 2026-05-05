class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        # sliding window
        char_set = set()
        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            res = max(r - l + 1, res)
            char_set.add(s[r])
        return res