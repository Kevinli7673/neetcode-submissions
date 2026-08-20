"""
BFS
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        seen = set()
        queue = deque()
        res = 0

        def bfs(r, c):
            count = 0
            while queue:
                r,c = queue.pop()
                if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in seen:
                    continue
                
                seen.add((r,c))
                count += 1
                queue.appendleft((r+1,c))
                queue.appendleft((r-1,c))
                queue.appendleft((r,c+1))
                queue.appendleft((r,c-1))
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    queue.append((r,c))
                    res = max(res, bfs(r,c))
        
        return res