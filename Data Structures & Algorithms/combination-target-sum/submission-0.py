class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        """
        We want to return any unique combination of elements in the 
        array to get the target
        This can include multiple amount of a same indice
        
        Idea: like the previous question, we can use a dfs function
        that iterates through each index and for each index we can 
        find all the possible combination starting at indice
        dfs()
        base case
        to add or not add
        check
        When we staring at 2, we have two options: add it to sublist
        or not. What doese the decision tree look afterward:
        we can add 2 again or we can adding another number
        """

        res = []

        def dfs(i, curr, sum):
            if (i >= len(nums) or sum > target):
                return
            
            if(sum == target):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i, curr, sum + nums[i])
            curr.pop()
            dfs(i+1, curr, sum)
        
        dfs(0, [], 0)
        return res
            



