class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        word1_len, word2_len = len(word1), len(word2)

        res = []
        while i < word1_len and j < word2_len:
            res.append(word1[i])
            res.append(word2[j])

            i += 1
            j += 1
        
        res.extend(list(word1[i:]))
        res.extend(list(word2[j:]))

        return "".join(res)
