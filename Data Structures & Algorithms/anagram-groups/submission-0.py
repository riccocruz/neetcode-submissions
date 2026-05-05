from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sorted_anagram = ''.join(sorted(s))
            d[sorted_anagram].append(s)
        
        return d.values()