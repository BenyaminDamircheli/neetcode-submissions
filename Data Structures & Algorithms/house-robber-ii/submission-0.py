class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums:List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        cache = [0] * len(nums)
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cache[i] = max(cache[i - 1], cache[i - 2] + nums[i])
        
        return cache[len(nums) - 1]
