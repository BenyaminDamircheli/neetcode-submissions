"""
1. Scan the grid once: count fresh fruits, que up every rotten fruits position.
2. spread rot wave by wave: pop every current fruit in teh queue
3. track minutes elapsed, and no fresh fruit remain as neighbours or the queue is empty.
4. return -1 if fresh fruit remains after stopping
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        rotten: deque[tuple[int, int]] = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count +=1 
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while rotten and fresh_count > 0:

            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 
                        fresh_count -= 1
                        rotten.append((nr, nc)) 
            
            minutes += 1

        
        return minutes if fresh_count == 0 else -1
            









        