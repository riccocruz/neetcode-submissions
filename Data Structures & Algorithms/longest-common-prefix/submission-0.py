class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # find string with least amt of chars
        min_len = min([len(s) for s in strs])

        # iterate each index for min_len. check
        # at each index that they are all equal to strs[0][index]
        for i in range(min_len):
            for s in strs[1:]:
                if s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res