class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = defaultdict(list)
        for s in strs:
            # turn s into a counter.
            # if tupled counter is foudn in res, add to key's value
            counter = [0] * 26
            for letter in s:
                counter[ord(letter) - ord('a')] += 1

            counters[tuple(counter)].append(s)

        return list(counters.values())