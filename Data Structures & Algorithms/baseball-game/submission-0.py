class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        res = 0

        for i in range(len(operations)):
            if (operations[i] != '+' and operations[i] != 'C' and operations[i] != 'D'):
                stack.append(operations[i])
                print(stack)
            
            if operations[i] == 'D':
                stack.append(int(stack[-1]) * 2)
            if operations[i] == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
            if operations[i] == 'C':
                stack.pop()

        print(stack)
        for num in stack:
            res += int(num)
        
        return res