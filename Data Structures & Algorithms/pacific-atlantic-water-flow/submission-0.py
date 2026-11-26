class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit_pac = set()
        visit_atl = set()

        def bfs(source, visit):
            q = deque(source)
            while q:
                row, col = q.popleft()
                visit.add((row, col))
                for dr, dc in DIRECTIONS:
                    new_row, new_col = row + dr, col + dc
                    if (
                        0 <= new_row < ROWS
                        and 0 <= new_col < COLS
                        and (new_row, new_col) not in visit
                        and heights[new_row][new_col] >= heights[row][col]
                    ):
                        q.append((new_row, new_col))
       
        pacific = []
        atlantic = []

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS -1))

        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))
        
        bfs(pacific, visit_pac)
        bfs(atlantic, visit_atl)

        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in visit_pac and (row, col) in visit_atl:
                    res.append([row, col])

        return res
        
