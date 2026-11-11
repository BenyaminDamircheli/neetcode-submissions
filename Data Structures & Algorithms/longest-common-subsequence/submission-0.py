"""
- A table that represents one row per prefix length of text1 and one column for prefix length of text2
    - (n * m)
    - Holds the length of the longest common subsequences for that prefix
- row = 0 and col = 0 should be set to zero.

- When the characters are equal, the cell's value should be the left diagonal cell + 1
- When chars are not equal, then its max of the cell to the left and the cell to the right
- Answer is the bottom right cell which contains the answer for the full string 
n = len of text1
m = len of text2

Time: O(m * n)
Space: O(m * n) => (m+1)(n + 1)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row_count = len(text1) + 1
        column_count = len(text2) + 1

        lengths = [[0] * column_count for _ in range(row_count)] 


        for i in range(1, row_count):
            for j in range(1, column_count):
                if text1[i - 1] == text2[j - 1]:
                    lengths[i][j] = lengths[i - 1][j -1] + 1
                else:
                    lengths[i][j] = max(lengths[i - 1][j], lengths[i][j-1])
        
        return lengths[-1][-1]

