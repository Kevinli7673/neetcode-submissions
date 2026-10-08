class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        """
        idea: we want to find all the possible subset
        we want to use a dfs structure, essentially at every indice
        we have a option of adding it and not, giving us different
        subsets
        """

        res = []

        sublist = []
        def dfs(i):
            
            if i >= len(nums):
                res.append(sublist.copy())
                return

            sublist.append(nums[i])
            dfs(i+1)

            sublist.pop()
            dfs(i+1)
        
        dfs(0)
        return res
