class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 
        d = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for sub in s:
                counter[ord(sub) - ord('a')] += 1
            d[tuple(counter)].append(s)

        return list(d.values())