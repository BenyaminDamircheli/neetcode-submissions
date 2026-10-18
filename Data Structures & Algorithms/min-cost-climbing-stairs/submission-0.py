class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [0] * (n + 1)

        for i in range(2, n + 1):
            cache[i] = min(cache[i - 1] + cost[i - 1], cache[i - 2] + cost[i - 2])
        
        return cache[n]
