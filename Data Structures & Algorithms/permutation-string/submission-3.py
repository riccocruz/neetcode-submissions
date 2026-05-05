class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        s2_cur = Counter()

        for i, c in enumerate(s2):
            s2_cur[c] += 1
            if i < len(s1) - 1:
                continue

            if s2_cur == s1_count:
                return True

            s2_cur[s2[i - len(s1) + 1]] -= 1
            if s2_cur[s2[i - len(s1) + 1]] == 0:
                del s2_cur[s2[i - len(s1) + 1]]

        return False

