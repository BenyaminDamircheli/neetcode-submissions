from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        heap = [(0, k)]
        visit = set()
        t = 0
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            t = weight

            for next_node, next_weight in edges[node]:
                if next_node not in visit:
                    heapq.heappush(heap, (weight + next_weight, next_node))
        
        return t if len(visit) == n else -1

