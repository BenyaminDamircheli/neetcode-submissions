class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row_count, column_count = len(heights), len(heights[0])
        heap = [[0, 0, 0]]
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            diff, r, c = heapq.heappop(heap)

            if (r, c) in visit:
                continue

            visit.add((r, c))

            if (r, c) == (row_count - 1, column_count - 1):
                return diff

            for d_row, d_column in directions:
                new_row, new_column = r + d_row, c + d_column

                if (
                    new_row < 0
                    or new_column < 0
                    or new_row >= row_count
                    or new_column >= column_count
                    or (new_row, new_column) in visit
                ):
                    continue

                new_diff = max(diff, abs(heights[r][c] - heights[new_row][new_column]))
                heapq.heappush(heap, [new_diff, new_row, new_column])
        
        return 0