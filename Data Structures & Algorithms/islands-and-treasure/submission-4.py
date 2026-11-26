class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()

        def add_cell(row, col):
            if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visit and grid[row][col] != -1:
                visit.add((row, col))
                queue.append((row, col))
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    visit.add((row, col))
                    queue.append((row, col))
        
        steps = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = steps
                add_cell(row + 1, col)
                add_cell(row - 1, col)
                add_cell(row, col + 1)
                add_cell(row, col - 1)
            steps +=1 
                


