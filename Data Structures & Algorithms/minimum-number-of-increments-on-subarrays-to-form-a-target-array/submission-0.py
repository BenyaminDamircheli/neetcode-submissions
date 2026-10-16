"""
every operation adds 1 to a contiguous range, so increments between neighbors only matter.
greedy approach??

an operation that covers index i either starts with i or also covers i-1, so index i needs target[i] - target[i - 1] new operations if target[i] is greater than target[i-1]
if target[i] <= target[i - 1], then the operation can stop before i
treat the value before index 0 as 0 so target[0] operations start at index 0


"""

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = 0
        previous = 0 
        for value in target:
            if value > previous:
                operations += value - previous
            previous = value
        
        return operations
        