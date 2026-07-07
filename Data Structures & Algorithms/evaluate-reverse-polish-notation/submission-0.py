# Idea: For loop for each element in array
# Add to another array
# When we reach a operator, save two varaible that are equal the pop and do the 
# operator and add it back to the stack

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = "*-+/"

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()

                if i == "-":
                    stack.append(int(b-a))
                if i == "/":
                    stack.append(int(b/a))
                if i == "+":
                    stack.append(int(b+a))
                if i == "*":
                    stack.append(int(a*b))
        

        return stack[0]