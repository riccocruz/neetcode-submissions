class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is sorted s, val is sublist
        # iterate through the array
        d = defaultdict(list)

        for s in strs:
            d[str(sorted(s))].append(s)
        
        return list(d.values())