class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        """
        For each iteration, we have to make sure don't create
        duplicate subsets. What we can do is for each recursive call
        we choose either the same indice or increase indice
        whenever we go over the target, we backtrack
        """

        res = []

        def dfs(i, subset, curr):

            if(curr == target):
                res.append(subset.copy())
                return

            if(i >= len(nums) or curr > target):
                return
        
            subset.append(nums[i])
            curr += nums[i]

            dfs(i, subset, curr)
            curr -= nums[i]
            subset.pop()

            dfs(i+1, subset, curr)

        dfs(0, [], 0)
        return res



