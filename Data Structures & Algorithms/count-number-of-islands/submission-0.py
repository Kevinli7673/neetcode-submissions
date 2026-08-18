"""
Idea: We iterate over each sub array and iterate each element in each of the subarray
    Check in all directions if theres another one, else, add to amt of island
While a 1 is touch another 1, we'll consider that a single island
However, the 1 can be touching from all directions
Time complexity: O(n^2)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if (r,c) in visited or r == rows or c == cols or c < 0 or r < 0 or grid[r][c] == "0":
                return
            
            visited.add((r, c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    res += 1
                    dfs(r, c)

        return res