class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def search(row, col, index):
            if index == len(word):
                return True
            if not (0 <= row < rows and 0 <= col < cols):
                return False
            if board[row][col] != word[index]:
                return False
            
            letter = board[row][col]
            board[row][col] = "#"

            found = (
                search(row + 1, col, index + 1)
                or search(row - 1, col, index + 1)
                or search(row, col + 1, index + 1)
                or search(row, col - 1, index + 1)
            )

            board[row][col] = letter

            return found
        
        for row in range(rows):
            for col in range(cols):
                if search(row, col, 0):
                    return True
        
        return False


