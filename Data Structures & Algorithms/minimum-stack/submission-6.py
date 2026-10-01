class MinStack:

    def __init__(self):
        self.que = deque()
        self.minque = deque()
        self.minval = float('inf')

    def push(self, val: int) -> None:
        self.que.append(val)
        if not self.minque or val < self.minque[-1]:
            self.minque.append(val)
        else:
            self.minque.append(self.minque[-1])

    def pop(self) -> None:
        self.que.pop()
        self.minque.pop()

    def top(self) -> int:
        return self.que[-1]

    def getMin(self) -> int:
        return self.minque[-1]
