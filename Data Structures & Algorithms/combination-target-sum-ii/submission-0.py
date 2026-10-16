"""
Just like the previous question, we want to return a subset
that add up to the target
However, we don't want to have duplicate answer and each 
element should be used at most once per subset
To make sure that each element is used at most once per 
call, we can use a hashset which contains the indice we alr
used. Or we can sort the array so that we can iterate through
without having to worry about duplicate since for each 
iteration we increase i by one 
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def dfs(i, subset, total):
            
            if(total == target):
                res.append(subset.copy())
                return

            if(i>=len(candidates) or total > target):
                return

            total += candidates[i]
            subset.append(candidates[i])

            dfs(i+1, subset, total)

            total -= candidates[i]
            subset.pop()

            while(i+1 < len(candidates) and candidates[i] == candidates[i+1]):
                i += 1

            dfs(i+1, subset, total)

        dfs(0, [], 0)
        return res





