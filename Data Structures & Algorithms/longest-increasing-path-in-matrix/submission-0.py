"""
run a dfs from each cell and save the answers for that cell. put answer in same position in table

"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row_count, column_count = len(matrix), len(matrix[0])

        longest_from = [[0] * column_count for _ in range(row_count)]

        def find_longest_from(row, column):
            if longest_from[row][column]:
                return longest_from[row][column]
            
            best = 1
            for row_step, column_step in ((1,0), (-1,0), (0,1), (0,-1)):
                next_row, next_column = row + row_step, column + column_step
                if (
                    0 <= next_row < row_count
                    and 0 <= next_column < column_count
                    and matrix[next_row][next_column] > matrix[row][column]
                ):
                    best = max(best, 1 + find_longest_from(next_row, next_column))
            
            longest_from[row][column] = best
            return best

        return max(
            find_longest_from(row, col)
            for row in range(row_count)
            for col in range(column_count)
        )

