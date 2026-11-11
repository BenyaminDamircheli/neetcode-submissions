class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0] * (n + 1) for _ in range(m + 1)]
        paths[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                paths[i][j] += paths[i + 1][j] + paths[i][j + 1]
        
        return paths[0][0]

