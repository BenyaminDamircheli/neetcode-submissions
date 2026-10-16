class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")":"(", "]":"[", "}":"{"}
        stack = deque()

        for p in s:
            if p not in Map:
                stack.append(p)
                continue
            if not stack or Map[p] != stack[-1]:
                return False
            stack.pop()
        
        return not stack

       
        
        
        