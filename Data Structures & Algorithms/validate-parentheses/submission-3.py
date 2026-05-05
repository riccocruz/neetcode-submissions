class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []
        for i, c in enumerate(s):
            if c in '({[':
                stack.append(c)
            elif not stack and c in brackets:
                return False
            elif stack and stack[-1] != brackets[c]:
                return False
            else:
                stack.pop()
        return len(stack) == 0