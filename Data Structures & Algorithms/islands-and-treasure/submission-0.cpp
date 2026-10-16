#include <queue>

class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        queue<pair<int, int>> q;

        for (int r=0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 0) q.push({r, c});
            }
        }

        int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}; 

        // BFS
        while (!q.empty()) {
            auto [r,c] = q.front(); q.pop();
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];

                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (grid[nr][nc] != INT_MAX) continue;
                grid[nr][nc] = grid[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }
};
