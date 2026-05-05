class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        for l in range(len(s)):
            char_set = set()
            for r in range(l, len(s)):
                if s[r] in char_set:
                    break
                char_set.add(s[r])
                res = max(r - l + 1, res)
        return res