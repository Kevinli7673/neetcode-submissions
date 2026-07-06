# Edge case: Check if its even

# Brute force: 
# For each char in string
# If the char is a opening, check theres no closing different right next to it

# Effiecent solution
# Add left side bracket to array
# when we hit a right bracket
# check the top of the array, and if its true pop

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        openChars = "({["
        closedChars = "]})"

        if len(s) % 2 != 0 or s[0] in closedChars:
            return False

        for c in s:
            if c in openChars:
                stack.append(c)
            elif c in closedChars:
                if c == ']':
                    if stack and stack[-1] == "[":
                        stack.pop()
                        continue
                    else:
                        return False
                if c == '}':
                    if stack and stack[-1] == "{":
                        stack.pop()
                        continue
                if c == ')':
                    if stack and stack[-1] == "(":
                        stack.pop()
                        continue
        
        return len(stack) == 0
        