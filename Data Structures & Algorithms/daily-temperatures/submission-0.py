

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for i, k in enumerate(temperatures):
            if stack:
                while stack and stack[-1][1] < k:
                    val = stack.pop()
                    res[val[0]] = i - val[0]
            stack.append((i,k))

        return res