class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = cache[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    skip = cache[i + 1][True] if i + 1 < n else 0 
                    cache[i][True] = max(buy, skip)
                else:
                    sell = cache[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    skip = cache[i + 1][False] if i + 1 < n else 0
                    cache[i][0] = max(sell, skip)

        return cache[0][1] 

        