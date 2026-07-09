# Just like Reverse Polish notation's, base on what the element is
# We can either run the function or grab the next element to perform
# Create a stack that stores the numbers

# Read the first element, checks if its MinStack

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:

            self.stack.append(val)

            if not self.minStack:
                self.minStack.append(val)
            else:
                if val < self.minStack[-1]:
                    self.minStack.append(val)
                else:
                    self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        val = self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
