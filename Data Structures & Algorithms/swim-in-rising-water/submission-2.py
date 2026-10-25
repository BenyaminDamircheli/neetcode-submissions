"""
(highest elevation to that cell, row, col)

max(popped value, neighbour elevation)

n = side length of the grid, there are n^2 cells
Time: (n^2log n)
Space: O(n^2)
"""

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = [[False] * n for _ in range(n)]
        seen[0][0] = True
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            time, row, col = heapq.heappop(heap)
            if row == n - 1 and col == n - 1:
                return time
            
            for row_step, col_step in directions:
                n_row, n_col = row + row_step, col + col_step
                if 0 <= n_row < n and 0 <= n_col < n and not seen[n_row][n_col]:
                    seen[n_row][n_col] = True
                    heapq.heappush(heap, (max(time, grid[n_row][n_col]), n_row, n_col))
        
        return -1
    
            










        