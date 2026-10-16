class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque()
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                Stackt, Stacki = stack.pop() # when extracting the values in the array, it goes second then first, so even though temp is second in the array, you declare it first in the variable. 
                diff = i - Stacki
                result[Stacki] = diff
            stack.append([t, i])
            
        return result

