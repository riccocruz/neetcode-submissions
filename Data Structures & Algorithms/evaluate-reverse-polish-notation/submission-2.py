class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i, token in enumerate(tokens):
            if token in "/*-+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(str(int(eval(num1 + token + num2))))
            else:
                stack.append(token)
        return int(stack[0])