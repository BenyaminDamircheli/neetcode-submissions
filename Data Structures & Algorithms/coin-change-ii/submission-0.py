"""
ways = [0] * (amount + 1)
loop through coins, then loop through amounts
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (amount + 1)
        ways[0] = 1

        for coin in coins:
            for a in range(coin, amount + 1):
                ways[a] += ways[a - coin]
        
        return ways[amount]