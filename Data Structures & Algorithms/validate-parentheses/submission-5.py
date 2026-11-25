class Solution:
    def isValid(self, s: str) -> bool:
        paren_mapping = {
            "(" : ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        for p in s:
            if p in paren_mapping:
                stack.append(p)
                continue
            elif stack and paren_mapping[stack[-1]] == p:
                stack.pop()
            else:
                return False
            
        
        return False if stack else True
