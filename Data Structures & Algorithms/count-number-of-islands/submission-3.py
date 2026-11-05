class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        seen = set()
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):

            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or (row, col) in seen or grid[row][col] == "0":
                return 

            seen.add((row, col))
            for d in dir:
                dfs(row + d[1], col + d[0])


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if (i, j) not in seen:
                        res += 1
                    dfs(i, j)
                    

        return res