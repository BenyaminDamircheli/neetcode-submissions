class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sorted_nums = sorted(numbers)
        l, r = 0, len(sorted_nums) - 1
        
        while l < r:
            curr_sum = sorted_nums[l] + sorted_nums[r]

            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l+1, r+1]
        
            
            