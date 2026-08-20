class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        seen = set()

        def dfs(r, l):
            if (r, l) in seen or r < 0 or r == len(grid) or l < 0 or l == len(grid[0]) or grid[r][l] == "0":
                return
            
            seen.add((r,l))
            dfs(r+1, l)
            dfs(r-1, l)
            dfs(r, l+1)
            dfs(r, l-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    dfs(r,c)
                    res += 1
        
        return res