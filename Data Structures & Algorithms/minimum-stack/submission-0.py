class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp = []

        mini = self.top()
        while len(self.stack) > 0:
            top = self.stack.pop()
            mini = min(mini, top)
            temp.append(top)
        temp.reverse()
        self.stack = temp 
        return mini
