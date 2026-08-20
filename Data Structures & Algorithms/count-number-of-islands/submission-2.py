"""
lets try bfs now
we want to use a double end queue to allow us to store future point we can travel
if we can travel to another (if its a one), add it to the front of the queue
and we run dfs until we run out of queue
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        seen = set()

        def bfs(r, c):
            while queue:
                r,c = queue.pop()
                if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in seen or grid[r][c] == "0":
                    continue
                
                seen.add((r,c))
                queue.appendleft((r+1,c))
                queue.appendleft((r-1,c))
                queue.appendleft((r,c+1))
                queue.appendleft((r,c-1))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    print(r,c)
                    queue.append((r,c))
                    bfs(r,c)
                    res += 1

        return res