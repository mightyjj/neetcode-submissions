class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        curr_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, curr_min))
        self.size += 1

    def pop(self) -> None:
        self.stack = self.stack[:self.size - 1]
        self.size -= 1

    def top(self) -> int:
        return self.stack[self.size - 1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
