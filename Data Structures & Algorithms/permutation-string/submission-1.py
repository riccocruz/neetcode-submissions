class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for i in range(len(s1)):
            count1[s1[i]] += 1
        
        for i in range(len(s2)):
            count2[s2[i]] += 1
            
            if i < len(s1) - 1:
                continue
            
            if count1 == count2:
                return True
            
            count2[s2[i - len(s1) + 1]] -= 1
            if count2[s2[i - len(s1) + 1]] == 0:
                del count2[s2[i - len(s1) + 1]]

        return False
