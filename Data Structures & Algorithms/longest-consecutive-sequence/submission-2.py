class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        result = 1

        if len(numset) == 0:
            return 0

        for n in numset:
            length = 1
            while (n + length) in numset:
                length += 1
                result = max(length, result)
        
        return result
            