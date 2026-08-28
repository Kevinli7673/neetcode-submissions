"""
we're given position and speed of each car
And we're trying to find how many fleets are in this one lane highway (a group of car reacing the destination at the same time - this can do done with a simple y = mx + b) 
We have a stack that adds (position, speed). And we pop if the speed is the same is the new tuple we're adding has a bigger position
then we return the len of the stack
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        times = []

        for i in range(len(position)):
            t = (target - position[i]) / speed[i]
            times.append((position[i], t))
        
        times.sort()

        for val in times:
            if stack:
                while stack and stack[-1] <= val[1]:
                    stack.pop()

            stack.append(val[1])
        
        return len(stack)