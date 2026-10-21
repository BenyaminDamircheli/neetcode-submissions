class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = deque([node])
            visit.add(node)
            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
        
        components = 0
        for node in range(n):
            if node not in visit:
                bfs(node)
                components += 1
        
        return components

