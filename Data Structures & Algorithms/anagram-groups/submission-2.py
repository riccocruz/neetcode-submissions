class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is the tuple of the Counter(s)
        d = defaultdict(list)

        # iterate through array, adding each s to their
        # respective anagram key
        for s in strs:
            counter = [0] * 26
            for letter in s:
                counter[ord(letter) - ord('a')] += 1
            d[tuple(counter)].append(s)
        
        return list(d.values())
