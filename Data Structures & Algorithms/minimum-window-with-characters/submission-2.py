class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tcount = Counter(t)
        # smallest window, i, r
        smallest_window = [float('inf'), 0, 0]
        l = 0
        scount = Counter()
        for r, c in enumerate(s):

            if c in tcount:
                scount[c] = scount.get(c, 0) + 1
            
            while all(scount[c] >= tcount[c] for c in tcount):
                if r - l < smallest_window[0]:
                    smallest_window = [r - l + 1, l, r + 1]
                if s[l] in scount:
                    scount[s[l]] -= 1
                l += 1

        return s[smallest_window[1] : smallest_window[2]]