//input: number of courses + pairs of [a,b]
// output: one order of courses that takes every course or empty if a cycle exists
// deps form a directed graph -> topological sort (kahn's algorithm)


// graph[b] -> courses that need b, and a vector indegree[a] = count of prerequisites of a
// push every course with indegree == 0 into queue
// pop course, decrement val of indegree of each neighbor, push a neighbor when that val reaches 0
// when queue is empty return result if queue len is = numCourses, else empty vector

#include <vector>
#include <queue> 
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        vector<int> indegree(numCourses, 0);
        for (const auto& p : prerequisites) {
            graph[p[1]].push_back(p[0]);
            ++indegree[p[0]];
        }

        queue<int> ready;
        for (int c = 0; c < numCourses; ++c) 
            if (indegree[c] == 0) ready.push(c);
        
        vector<int> order;
        while (!ready.empty()) {
            int c = ready.front(); ready.pop();
            order.push_back(c);
            for (int next : graph[c]) {
                if (--indegree[next] == 0) ready.push(next);
            }
        }

        if ((int)order.size() != numCourses) return {};

        return order;
    }
};
