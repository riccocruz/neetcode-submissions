class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            res.append(0)
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[-1] = j - i
                    break
            
        return res