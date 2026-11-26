from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        minutes = 0
        fresh = 0

        def add_cell(row, col):
            nonlocal fresh
            if (0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1 and (row, col) not in visit):
                visit.add((row, col))
                q.append((row, col))
                fresh -= 1
            
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    visit.add((row, col))
                    q.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1
                

        while fresh > 0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()
                add_cell(row + 1, col)
                add_cell(row - 1, col)
                add_cell(row, col + 1)
                add_cell(row, col - 1)
            minutes += 1
        
        return minutes if fresh == 0 else -1
        



            









        