"""
the time for a given path is the highest cell on the path, the answer is the path with the path whose highest cell is the lowest

you can reach a given cell at time max(time to reach its neighbor, grid[cell]) -> cost of a given path is the highest cell on that path

min heap that stores (time, row, col)
for each new neighbour that you have not seen, push max(time, grid[neighbor]) and we mark the neighbor as seen at push time.
    - this works because heap pops come at non-increasing time values, so the first push to a cell already carries it's smallest value.

Answer: the first time the bottom-right cell is popped, it's time value is the answer.
"""
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]

        while heap:
            time, row, col = heapq.heappop(heap)
            if row == n - 1 and col == n - 1:
                return time
            
            for d_row, d_col in directions:
                next_row, next_col = row + d_row, col + d_col
                if 0 <= next_row < n and 0 <= next_col < n and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    heapq.heappush(heap, (max(time, grid[next_row][next_col]),next_row, next_col))

        return -1 









        