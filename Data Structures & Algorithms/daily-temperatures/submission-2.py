class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temps))]

        for i, t in enumerate(temps):
            while stack and t > temps[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res
